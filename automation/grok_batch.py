# -*- coding: utf-8 -*-
"""
grok_batch.py - Grok Imagine batch video generator (browser-automation backend).

Provenance:
  vendored+adapted from 阿軒 Sora去水印下載器 grok_batch.py
  (2026-07-02 intake-audit GREEN-for-this-file).
  Grok automation drives the user's OWN logged-in grok.com session — consumes
  their quota, subject to Grok ToS, may break on Grok API/DOM drift.

How it works (faithful to the source):
  Every API call goes through a REAL, already-running, logged-in Chrome via
  Playwright's `connect_over_cdp` + `ctx.request` / `page.evaluate`. Running the
  calls INSIDE the live browser context makes them inherit live Cloudflare
  cookies + the live `x-statsig-id` header + the real TLS fingerprint, which is
  what lets them past grok.com's anti-bot layer (plain HTTP cannot).

  Per clip: (1) POST /rest/media/post/create -> post_id;
            (2) capture live x-statsig-id by routing **/rest/** on a grok.com page;
            (3) in-page fetch POST /rest/app-chat/conversations/new (videoGen);
            (4) poll /rest/media/post/get for mediaUrl;
            (5) download the mp4 via ctx.request.get.

Security:
  No credentials live in this file. It attaches to an already-running Chrome that
  the USER launched and logged into (see automation/site-profiles/grok.md and the
  WSL->Windows Chrome CDP note). Only connect to a Chrome you started yourself.

CDP discovery (this machine's pattern — WSL -> Windows Chrome over mirrored
localhost; see reference_flow_wsl_windows_chrome_cdp / the pinchtab launcher
~/.pinchtab/flow-windows-chrome.sh which exposes a --remote-debugging-port):
  precedence  --cdp-url  >  --cdp-port  >  $PINCHTAB_CDP_URL  >  $CHROME_CDP_URL
              >  http://localhost:9222 (last-resort default)
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import os
import sys
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlparse
from uuid import uuid4

POLL_MAX_DEFAULT = 70
POLL_SLEEP_DEFAULT = 3

# Trust boundaries (security): only ever inject into / download from grok/x.ai
# origins, and only attach to a loopback CDP unless the user opts into remote.
_GROK_HOSTS = ("grok.com",)          # in-page fetch origin (exact host or subdomain)
_MEDIA_HOSTS = ("grok.com", "x.ai")  # allowed download CDN roots (exact or subdomain)


def _host_of(u: str | None) -> str:
    try:
        return (urlparse(u or "").hostname or "").lower()
    except Exception:
        return ""


def _host_matches(host: str, roots: tuple[str, ...]) -> bool:
    return bool(host) and any(host == r or host.endswith("." + r) for r in roots)


_GROK_PAGE_HOSTS = ("grok.com", "www.grok.com")  # in-page fetch is relative → EXACT host only


def _is_grok_page(u: str | None) -> bool:
    """True only if the URL's HOSTNAME is EXACTLY grok.com / www.grok.com.
    The injected fetch is relative ('/rest/...'), so it resolves against the
    page's own origin — a *.grok.com subdomain (or grok.com.evil.tld) would
    receive the prompt. Exact-match only; the /rest API lives on grok.com."""
    return _host_of(u) in _GROK_PAGE_HOSTS


def _is_loopback(host: str) -> bool:
    """True for localhost or a loopback IP. Parse the IP properly — a string
    prefix check like host.startswith('127.') would wrongly accept the hostname
    '127.evil.com', which can resolve to a remote CDP endpoint."""
    if host == "localhost":
        return True
    try:
        return ipaddress.ip_address(host.strip("[]")).is_loopback
    except ValueError:
        return False


def _cdp_host_ok(url: str, allow_remote: bool) -> bool:
    """Attach only to a loopback CDP endpoint unless --allow-remote-cdp is given.
    A remote CDP endpoint can fully drive the user's logged-in session."""
    return allow_remote or _is_loopback(_host_of(url))


def probe_cdp(base_url: str, timeout: float = 3.0) -> bool:
    """True only if the CDP endpoint is live AND exposes webSocketDebuggerUrl.

    HTTP 200 alone is not enough — an unrelated Chrome (e.g. the Desktop /
    Claude-in-Chrome one on :9222) can answer 200 but not be attachable, or a
    stray server can 404. We require the debugger websocket to be advertised.
    Runs only at call time (no network at import).
    """
    url = base_url.rstrip("/") + "/json/version"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            if r.status != 200:
                return False
            body = r.read().decode("utf-8", "ignore")
        return "webSocketDebuggerUrl" in body
    except Exception:
        return False


def resolve_cdp_url(cli_url: str | None, cli_port: int | None,
                    allow_remote: bool = False) -> str | None:
    """Resolve the Chrome CDP base URL (portable — no Windows wmic).

    Precedence: --cdp-url > --cdp-port > $PINCHTAB_CDP_URL > $CHROME_CDP_URL
                > http://localhost:9222 (last-resort default).
    SECURITY: a CDP endpoint fully drives the attached (logged-in) browser, so
    non-loopback hosts are REJECTED unless allow_remote (--allow-remote-cdp).
    An explicit --cdp-url / --cdp-port is returned even if the probe fails
    (with a warning); env / default candidates must actually probe live.
    """
    def _reject_remote(url: str, src: str) -> bool:
        if not _cdp_host_ok(url, allow_remote):
            print(f"REFUSED: {src} points at non-loopback host {_host_of(url)!r}; "
                  f"a remote CDP can hijack your logged-in session. Pass --allow-remote-cdp "
                  f"only if you fully trust that endpoint.")
            return True
        return False

    if cli_url:
        if _reject_remote(cli_url, "--cdp-url"):
            return None
        if not probe_cdp(cli_url):
            print(f"WARN: --cdp-url {cli_url} did not advertise a debugger websocket; trying anyway.")
        return cli_url

    if cli_port:
        url = f"http://localhost:{cli_port}"
        if not probe_cdp(url):
            print(f"WARN: --cdp-port {cli_port} did not advertise a debugger websocket; trying anyway.")
        return url

    candidates: list[str] = []
    for env_key in ("PINCHTAB_CDP_URL", "CHROME_CDP_URL"):
        val = os.environ.get(env_key, "").strip()
        if val:
            candidates.append((env_key, val))
    candidates.append(("default", "http://localhost:9222"))  # last-resort default

    for src, url in candidates:
        if not _cdp_host_ok(url, allow_remote):
            print(f"SKIP: {src} host {_host_of(url)!r} is non-loopback (use --allow-remote-cdp to allow).")
            continue
        if probe_cdp(url):
            return url
    return None


def generate_one(ctx, idx: int, cfg: argparse.Namespace, out_dir: Path) -> str | None:
    """One full generate cycle using the live Chrome browser context."""
    req_id = lambda: str(uuid4())

    # Step 1: create post
    cr = ctx.request.post(
        "https://grok.com/rest/media/post/create",
        data={"mediaType": "MEDIA_POST_TYPE_VIDEO", "prompt": cfg.prompt},
        headers={"content-type": "application/json", "x-xai-request-id": req_id()},
        timeout=30000,
    )
    if cr.status != 200:
        print(f"  FAIL create HTTP {cr.status}: {cr.text()[:200]}")
        return None
    post_id = ((cr.json().get("post") or {}).get("id") or "").strip()
    if not post_id:
        print(f"  FAIL no post_id: {cr.text()[:200]}")
        return None
    print(f"  create OK -> post_id={post_id[:8]}...")

    # Step 2: get live x-statsig-id + conversations/new via Chrome page inject.
    # Reuse only a page whose HOSTNAME is grok.com (substring match is unsafe:
    # grok.com.evil.tld would let the in-page fetch POST the prompt to an
    # attacker origin). Otherwise open a fresh page and navigate to grok.com.
    grok_pg = next((p for p in ctx.pages if _is_grok_page(p.url)), None)
    if grok_pg is None:
        grok_pg = ctx.new_page()

    live_statsig: list[str] = []

    def on_route(route):
        sid = route.request.headers.get("x-statsig-id") or ""
        if sid and not live_statsig:
            live_statsig.append(sid)
        route.continue_()

    grok_pg.route("**/rest/**", on_route)
    try:
        if not _is_grok_page(grok_pg.url):
            grok_pg.goto("https://grok.com/imagine", timeout=15000, wait_until="domcontentloaded")
        else:
            grok_pg.reload(timeout=20000, wait_until="domcontentloaded")
        grok_pg.wait_for_timeout(2500)
    except Exception:
        grok_pg.wait_for_timeout(2000)
    try:
        grok_pg.unroute("**/rest/**", on_route)
    except Exception:
        pass

    # Re-verify origin AFTER navigation before injecting the prompt fetch — a
    # redirect could have landed us off grok.com.
    if not _is_grok_page(grok_pg.url):
        print(f"  ABORT: page origin is not grok.com ({grok_pg.url!r}); refusing to inject prompt.")
        return None

    statsig_id = live_statsig[0] if live_statsig else ""
    print(f"  statsig={'OK' if statsig_id else 'MISSING'}")

    chat_body = {
        "temporary": True, "modelName": "grok-3",
        "message": f"{cfg.prompt} --mode=custom",
        "toolOverrides": {"videoGen": True}, "enableSideBySide": True,
        "responseMetadata": {"experiments": [], "modelConfigOverride": {"modelMap": {
            "videoGenModelConfig": {
                "parentPostId": post_id, "aspectRatio": cfg.aspect,
                "videoLength": cfg.length, "isVideoEdit": False, "resolutionName": cfg.resolution,
            }
        }}}
    }
    body_json = json.dumps(chat_body, ensure_ascii=False)
    hdrs_obj = json.dumps({
        "content-type": "application/json", "accept": "text/event-stream",
        "x-xai-request-id": req_id(),
        **({"x-statsig-id": statsig_id} if statsig_id else {}),
    })
    js = f"""
(async () => {{
  try {{
    const r = await fetch('/rest/app-chat/conversations/new', {{
      method: 'POST', headers: {hdrs_obj}, body: {json.dumps(body_json)},
    }});
    let text = '';
    try {{
      const reader = r.body.getReader();
      for (let i = 0; i < 6; i++) {{
        const {{done, value}} = await reader.read();
        if (done) break;
        text += new TextDecoder().decode(value);
        if (text.length > 500) break;
      }}
      reader.cancel();
    }} catch(e) {{}}
    return {{status: r.status, text: text.substring(0, 300)}};
  }} catch(e) {{ return {{status: -1, text: String(e)}}; }}
}})()
"""
    result = grok_pg.evaluate(js)
    status = result.get("status", -1)
    print(f"  conversations/new -> HTTP {status}")
    if status != 200:
        print(f"  body: {result.get('text','')[:200]}")
        return None

    # Step 3: poll
    media_url = ""
    print(f"  polling...", end="", flush=True)
    for pi in range(cfg.poll_max):
        time.sleep(cfg.poll_sleep)
        pr = ctx.request.post(
            "https://grok.com/rest/media/post/get",
            data={"id": post_id},
            headers={"content-type": "application/json", "x-xai-request-id": req_id()},
            timeout=15000,
        )
        if pr.status == 200:
            media_url = ((pr.json().get("post") or {}).get("mediaUrl") or "").strip()
            if media_url:
                print(f" found at poll {pi+1}")
                break
            print(".", end="", flush=True)
        else:
            print(f"[{pr.status}]", end="", flush=True)
    else:
        print(f" TIMEOUT after {cfg.poll_max * cfg.poll_sleep}s")

    if not media_url:
        return None

    # Step 4: download via Chrome context.
    # Only download from a grok/x.ai CDN — mediaUrl comes from grok's API, but
    # guard against it pointing the authenticated context request at an
    # arbitrary third-party host.
    if not _host_matches(_host_of(media_url), _MEDIA_HOSTS):
        print(f"  REFUSED download: mediaUrl host {_host_of(media_url)!r} is not a grok/x.ai CDN.")
        return None
    fname = f"grok_{idx:02d}_{post_id[:8]}_{int(time.time())}.mp4"
    save_path = out_dir / fname
    print(f"  downloading -> {fname}")
    dl = ctx.request.get(
        media_url,
        headers={"referer": f"https://grok.com/imagine/post/{post_id}"},
        timeout=120000,
    )
    if dl.status != 200:
        print(f"  FAIL download HTTP {dl.status}")
        return None
    save_path.write_bytes(dl.body())
    size_mb = round(save_path.stat().st_size / 1024 / 1024, 1)
    print(f"  OK {size_mb} MB -> {save_path.name}")
    return str(save_path)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="grok_batch.py",
        description="Grok Imagine batch video generator via a live logged-in Chrome (CDP). "
                    "Drives the user's OWN grok.com session — consumes quota, subject to Grok ToS.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--prompt", required=True, help="Video prompt (required).")
    p.add_argument("--count", type=int, default=1,
                   help="Number of clips to generate in the batch.")
    p.add_argument("--aspect", default="9:16", help="Aspect ratio, e.g. 9:16 / 16:9 / 1:1.")
    p.add_argument("--length", type=int, default=6, help="Clip length in seconds (~1-15).")
    p.add_argument("--resolution", default="480p", choices=["480p", "720p"],
                   help="Output resolution (Grok video caps at 720p).")
    p.add_argument("--out-dir", default=None,
                   help="Directory to save mp4s (default: $GROK_DOWNLOAD_DIR or ./grok_downloads).")
    p.add_argument("--cdp-url", default=None,
                   help="Full Chrome CDP base URL, e.g. http://localhost:9224.")
    p.add_argument("--cdp-port", type=int, default=None,
                   help="Chrome CDP port on localhost (shorthand for --cdp-url http://localhost:PORT).")
    p.add_argument("--allow-remote-cdp", action="store_true",
                   help="Allow attaching to a NON-loopback CDP host (dangerous: a remote CDP can "
                        "drive your logged-in session). Off by default.")
    p.add_argument("--poll-max", type=int, default=POLL_MAX_DEFAULT,
                   help="Max poll attempts for the mediaUrl.")
    p.add_argument("--poll-sleep", type=int, default=POLL_SLEEP_DEFAULT,
                   help="Seconds between poll attempts.")
    p.add_argument("--inter-clip-sleep", type=int, default=5,
                   help="Seconds to wait between clips in a batch.")
    return p


def main() -> None:
    parser = build_parser()
    cfg = parser.parse_args()

    # Input validation (fail fast with a clear message).
    if cfg.count < 1:
        parser.error("--count must be >= 1")
    if not (1 <= cfg.length <= 60):
        parser.error("--length must be in 1..60 seconds")
    if cfg.poll_max < 1 or cfg.poll_sleep < 0 or cfg.inter_clip_sleep < 0:
        parser.error("--poll-max must be >= 1; --poll-sleep / --inter-clip-sleep must be >= 0")

    # Import playwright lazily so `--help` (and AST/import checks) work without it.
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: playwright is not installed. Install with: pip install playwright")
        sys.exit(2)

    out_dir = Path(cfg.out_dir) if cfg.out_dir else Path(
        os.environ.get("GROK_DOWNLOAD_DIR", "") or "./grok_downloads"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    cdp_url = resolve_cdp_url(cfg.cdp_url, cfg.cdp_port, allow_remote=cfg.allow_remote_cdp)
    if not cdp_url:
        print("ERROR: no reachable Chrome CDP endpoint found.")
        print("  Start a logged-in Chrome with --remote-debugging-port (e.g. the pinchtab")
        print("  launcher ~/.pinchtab/flow-windows-chrome.sh <port>, or Windows Chrome with")
        print("  --remote-debugging-port=9222), then pass --cdp-port / --cdp-url or set")
        print("  $PINCHTAB_CDP_URL / $CHROME_CDP_URL. See automation/site-profiles/grok.md.")
        sys.exit(1)

    print(f"Chrome CDP: {cdp_url}")
    print(f"=== Grok batch: {cfg.count} clip(s) ===")
    print(f"Prompt: {cfg.prompt}")
    print(f"Resolution: {cfg.resolution}  Length: {cfg.length}s  Aspect: {cfg.aspect}")
    print(f"Save to: {out_dir}")
    print()

    success = 0
    fail = 0

    with sync_playwright() as pw:
        browser = pw.chromium.connect_over_cdp(cdp_url)
        ctx = browser.contexts[0] if browser.contexts else None
        if not ctx:
            print("ERROR: no Chrome context found (is a window open?)")
            browser.close()
            sys.exit(1)

        for i in range(1, cfg.count + 1):
            print(f"[Round {i}/{cfg.count}]")
            result = generate_one(ctx, i, cfg, out_dir)
            if result:
                success += 1
            else:
                fail += 1
            if i < cfg.count:
                print(f"  waiting {cfg.inter_clip_sleep}s...")
                time.sleep(cfg.inter_clip_sleep)
            print()

        browser.close()

    print(f"=== Done: {success} OK / {fail} failed / {cfg.count} total ===")
    print(f"Videos in: {out_dir}")


if __name__ == "__main__":
    main()
