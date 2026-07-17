#!/usr/bin/env python3
"""extract_frame.py — 抽影片第一/最後幀存 PNG，給 img2video 續接當參考圖。

概念源自 Emily2040/seedance-2.0 的 scripts/extract_last_frame.py（MIT License,
Copyright (c) 2026 Iamemily2050）；此為精簡獨立改寫，僅保留本 skill 需要的核心。
用途：多鏡頭續接時抽上一段末幀 → 下一段 img2video 的輸入（見 SKILL.md 續接紀律）。

依賴：ffmpeg（系統指令）。stdlib only。

用法:
  extract_frame.py --last  <video> [-o out.png]   # 最後一幀（預設）
  extract_frame.py --first <video> [-o out.png]   # 第一幀
  extract_frame.py --self-test                    # 端到端自測（合成 2 秒測試片）
"""
import argparse
import os
import subprocess
import sys
import tempfile


def _run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        sys.exit("ffmpeg not found — install it first (apt/brew install ffmpeg)")
    if r.returncode != 0:
        sys.exit(f"ffmpeg failed (rc={r.returncode}): {r.stderr.strip()[:300]}")
    return r


def extract(video, out, which="last"):
    if not os.path.isfile(video):
        sys.exit(f"input not found: {video}")
    # 信任邊界：out 只接受本地 .png 路徑（-y 會覆寫；不接受 ffmpeg 協定型輸出）。
    # abspath 正規化讓 "http://host/x.png" 之類變成本地相對路徑，ffmpeg 不會做協定解讀。
    out = os.path.abspath(out)
    if not out.endswith(".png"):
        sys.exit(f"output must be a local .png path: {out}")
    if not os.path.isdir(os.path.dirname(out)):
        sys.exit(f"output directory does not exist: {os.path.dirname(out)}")
    if which == "last":
        # 全解碼影像流 + -update 1 每幀覆寫同一輸出 → 最終內容 = 真正的最後一幀。
        # 刻意不用 -sseof 檔尾 seek：容器音軌比影像長時（AI 生成片常見）seek 會落在
        # 影像流結束之後、零幀輸出。目標檔都是 ≤15s 短片，全解碼成本可忽略。
        # 不可加 -frames:v 1（那會變成第一幀）。
        cmd = ["ffmpeg", "-y", "-i", video, "-map", "0:v:0",
               "-update", "1", "-q:v", "2", out]
    else:
        cmd = ["ffmpeg", "-y", "-i", video, "-frames:v", "1", "-q:v", "2", out]
    _run(cmd)
    if not (os.path.isfile(out) and os.path.getsize(out) > 0):
        sys.exit(f"extraction produced no output: {out}")
    print(f"✅ {which} frame → {out} ({os.path.getsize(out)} bytes)")
    return out


def self_test():
    with tempfile.TemporaryDirectory() as td:
        vid = os.path.join(td, "t.mp4")
        # lavfi 合成 2 秒漸變測試片（無需任何輸入素材）
        # 30fps：確保「seek 後第一幀 ≠ 最後一幀」的回歸能被抓到（10fps 曾遮蔽此 bug）
        _run(["ffmpeg", "-y", "-f", "lavfi", "-i",
              "testsrc=duration=2:size=320x240:rate=30", vid])
        for which in ("first", "last"):
            out = os.path.join(td, f"{which}.png")
            extract(vid, out, which)
            assert os.path.getsize(out) > 1000, f"{which} frame too small"
        # ground-truth 斷言：抽出的「最後一幀」必須與影片真實末幀像素級一致
        # （framemd5 統一 rgb24；此斷言能抓到 -frames:v 1 型「seek 後第一幀」回歸）
        def _md5s(path):
            r = _run(["ffmpeg", "-i", path, "-map", "0:v:0", "-pix_fmt", "rgb24", "-f", "framemd5", "-"])
            return [l.split(",")[-1].strip() for l in r.stdout.splitlines()
                    if l and not l.startswith("#")]
        ref = _md5s(vid)              # 每一幀的 md5，取最後一筆 = 真實末幀
        got = _md5s(os.path.join(td, "last.png"))
        assert got[-1] == ref[-1], f"last-frame mismatch: got {got[-1][:12]} != true-final {ref[-1][:12]}"
        assert got[-1] != ref[0], "sanity: last frame equals first frame"
        # 音尾回歸：音軌（4s）比影像（2s）長的容器，末幀抽取仍須成功且像素一致
        # （-sseof 型實作在這裡會零幀輸出）
        av = os.path.join(td, "av.mp4")
        _run(["ffmpeg", "-y", "-f", "lavfi", "-i",
              "testsrc=duration=2:size=320x240:rate=30",
              "-f", "lavfi", "-i", "sine=frequency=440:duration=4",
              "-c:v", "libx264", "-c:a", "aac", av])
        out_av = os.path.join(td, "av_last.png")
        extract(av, out_av, "last")
        ref_av = _md5s(av); got_av = _md5s(out_av)
        assert got_av[-1] == ref_av[-1], "audio-tail last-frame mismatch"
    print("✅ self-test passed")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--last", action="store_true", help="最後一幀（預設）")
    g.add_argument("--first", action="store_true", help="第一幀")
    g.add_argument("--self-test", action="store_true", dest="selftest")
    ap.add_argument("video", nargs="?", help="輸入影片路徑")
    ap.add_argument("-o", "--out", help="輸出 PNG 路徑（預設 <video>.<which>.png）")
    a = ap.parse_args()
    if a.selftest:
        return self_test()
    if not a.video:
        ap.error("需要輸入影片路徑（或 --self-test）")
    which = "first" if a.first else "last"
    out = a.out or f"{os.path.splitext(a.video)[0]}.{which}.png"
    extract(a.video, out, which)


if __name__ == "__main__":
    main()
