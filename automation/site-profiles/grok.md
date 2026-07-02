# Site Profile: Grok Imagine (xAI)

**URL:** `https://grok.com/imagine`（也在 X app 內；API `docs.x.ai`）
**驗證狀態:** ⚠️ 部分驗證 2026-07-02（自動化路徑 = 內部 endpoint + statsig 擷取腳本，非 UI 點擊；UI 座標待實機補）
**平台類型:** 多功能（生圖 + 生影片，一站式）
**Stack:** Next.js / React SPA；受 **Cloudflare + `x-statsig-id`** 反自動化保護（純 HTTP 打不進，必須走已登入瀏覽器 context）

> ⚠️ 這份 profile 的自動化交付路徑跟 flow / oiioii / kling **不同**：Grok 不是用 `computer.left_click` 逐格點 UI，而是用 **Playwright `connect_over_cdp` 接管使用者已登入的 Chrome**，在該 context 內直接打 xAI 內部 REST endpoint（`ctx.request` / `page.evaluate`）。這樣呼叫會繼承活的 CF cookie + 活的 `x-statsig-id` + 真 TLS 指紋，才過得了反機器人層。腳本見 **[`../grok_batch.py`](../grok_batch.py)**。
>
> ⚠️ **ToS / quota：** 自動化驅動的是使用者**自己**登入的 grok.com session，**消耗使用者本人的 Grok 額度**，受 Grok 服務條款約束，且 Grok 改 API/DOM 時腳本會壞。用內部未公開 endpoint 有隨時失效的風險。

---

## 1. 整體 UI 地圖

```
┌─ grok.com / imagine ───────────────────────────────────┐
│ 頂部：帳號頭像（確認已登入）｜ 模式切換                  │
│ 中央：prompt 輸入框 + 生成類型（Image / Video）          │
│ 生成後：一次回多格（圖預設 6 格），影片格可下載 mp4      │
└────────────────────────────────────────────────────────┘
```

**關鍵：** 互動式 UI 走一般 chat/imagine 流程；**批次自動化不碰 UI**，改打內部 `/rest/**` endpoint（見 §2 自動化路徑）。UI 只用來（a）讓使用者登入、（b）觸發一次帶 `x-statsig-id` 的 `/rest/**` 請求好讓腳本擷取該 header。

---

## 2. 主流程 Phase-by-phase

### Phase 0 — 登入狀態（紅線，使用者親自）

- URL: `https://grok.com/imagine`
- 確認已登入 indicator：右上帳號頭像；未登入 → **停下請使用者自己登入**（絕不代輸入密碼）。
- Chrome 必須以 `--remote-debugging-port` 啟動且是使用者真實登入的 profile。本機配方：pinchtab 啟動器 `~/.pinchtab/flow-windows-chrome.sh <port>`（WSL→Windows 原生 Chrome，mirrored localhost 直連；預設 9224），或 Windows Chrome `--remote-debugging-port=9222`。就緒判斷必 grep `webSocketDebuggerUrl`（光 HTTP 200 不夠——`grok_batch.py` 的 `probe_cdp()` 已內建此檢查）。

### Phase 1 — 互動式（給使用者 / Claude-in-Chrome 手動）

1. `navigate` `https://grok.com/imagine`
2. 選 Image 或 Video；圖預設一次回 6 格。
3. 貼 prompt（心法見 [../../references/grok.md](../../references/grok.md)），送出前完整預覽給使用者確認。
4. 影片：設 aspect / length（~1–15s）/ resolution（≤720p），送出 → 等生成 → 格內下載 mp4。

### Phase 2 — 批次自動化（CDP + statsig 擷取，`grok_batch.py`）

**這是本 skill 對 Grok 新增的 REAL 自動化路徑。** 一支 clip = 一個 create→statsig→poll→download 週期：

| 步 | 動作 | 端點 / 手法 |
|---|---|---|
| 1 | 建立 post | `ctx.request.post` → `POST grok.com/rest/media/post/create`（`mediaType=MEDIA_POST_TYPE_VIDEO`）→ 取 `post_id` |
| 2 | 擷取活的 `x-statsig-id` | 在 grok.com page 上 `page.route("**/rest/**", …)`，讀 request header 的 `x-statsig-id`，reload 觸發一次即得 |
| 3 | 觸發影片生成 | `page.evaluate` 在頁內 `fetch('/rest/app-chat/conversations/new', …)`，body 帶 `toolOverrides.videoGen=true` + `videoGenModelConfig`（parentPostId / aspectRatio / videoLength / resolutionName），header 帶擷到的 statsig |
| 4 | 輪詢結果 | `POST grok.com/rest/media/post/get`（帶 `post_id`）直到 `post.mediaUrl` 出現（預設 70 次 × 3s）|
| 5 | 下載 | `ctx.request.get(mediaUrl, referer=…/imagine/post/{post_id})` → 寫檔 mp4 |

**跑法：**
```bash
python3 automation/grok_batch.py \
  --prompt "法國爸爸煮菜燒焦了" \
  --count 3 --aspect 9:16 --length 6 --resolution 480p \
  --out-dir ./grok_downloads \
  --cdp-port 9224          # 或 --cdp-url http://localhost:9224 / 設 $PINCHTAB_CDP_URL；省略則試 :9222
```

**安全護欄（腳本內建，codex review 加固）：**
- CDP 端點**預設只接 loopback**（localhost/127.x）；非 loopback host 直接拒（`--allow-remote-cdp` 才放行）——遠端 CDP 可完全操控你的登入 session。
- 注入 prompt 前用 **hostname 精確比對** grok.com（非子字串），並在導頁後 re-verify origin；`grok.com.evil.tld` 這種不會命中。
- 下載只允許 **grok.com / x.ai CDN** host，`mediaUrl` 指向他站直接拒。

**陷阱：**
- ❌ 純 `requests` / curl 打這些 endpoint → 被 Cloudflare / statsig 擋。**必須**在已登入瀏覽器 context 內跑。
- ⚠️ `x-statsig-id` 是動態的、每次 session 不同，**必現場擷取**，不能寫死。
- ⚠️ 這些是 xAI **內部未公開** endpoint，Grok 一改就壞（見 §10 版本紀錄，壞了先重抓 DOM/endpoint）。

---

## 3. 付費結構速查

| 階段 / 功能 | 成本 | 驗證 |
|---|---|---|
| 生成一段影片 | 消耗使用者 Grok 訂閱額度（依 X Premium / SuperGrok 方案）| ⏳ 依當下方案 |
| 解析度上限 | **720p**（要 1080p/4K 改 Kling/Veo）| ✅ 文件 |
| 單段長度 | ~1–15s | ✅ 文件 |

> 自動化不改變計費——跑幾支就扣幾支的額度。批次前跟使用者確認額度夠。

---

## 4. Click 策略備註

- **本 profile 主要不靠 click**：自動化走 endpoint，不點 UI。以下僅供互動式 fallback。
- ref 穩定度：中（React SPA，改版頻繁）
- 座標系：以當下 UI 為準，改版快，別記死
- Selected state 視覺：以實機截圖為準（⏳ 待補）
- 送出前一律把 prompt 預覽給使用者確認（安全紅線）

---

## 5. 常見 toast / modal 速查

| Toast / Modal | 意義 | 對策 |
|---|---|---|
| create HTTP != 200 | statsig/CF 擋或未登入 | 確認 Chrome 是真登入 profile；重抓 statsig |
| conversations/new HTTP != 200 | statsig 過期 / videoGen 參數變 | reload 頁面重抓 statsig；對照 §2 endpoint 是否改版 |
| poll TIMEOUT | 生成過慢 / 佇列塞 | 加大 `--poll-max`；或稍後重跑該 clip |
| Spicy 內容被模糊/擋 | 審核上限 | 品牌/商用別用 Spicy；換詞 |

---

## 6. 快速決策樹

```
要用 Grok 產什麼？
├── 只要 prompt / 選型建議 → 讀 references/grok.md，不碰自動化
├── 互動式手動產 1-2 支 → Phase 1（使用者或 Claude-in-Chrome 點 UI）
├── 批次多支影片（≤720p 短片）→ Phase 2 grok_batch.py（CDP + statsig）
└── 要 1080p/4K / 複雜多鏡 / 長敘事 → 別用 Grok，改 kling.md / veo.md
```

---

## 7. Workspace / 檔案保存機制

- 生成結果掛在使用者 grok.com 帳號的 post（`/imagine/post/{post_id}`）。
- `grok_batch.py` 直接把 mp4 抓到本機 `--out-dir`（預設 `$GROK_DOWNLOAD_DIR` 或 `./grok_downloads`），檔名 `grok_{idx}_{post8}_{ts}.mp4`。
- 下載走 `ctx.request.get`（瀏覽器 context），繼承登入 session，不需另外處理下載權限。

---

## 8. 未驗證但值得注意的行為

- ⏳ UI 座標 / selected state 視覺（互動式 fallback 用）——待實機截圖補。
- ⏳ `modelName`（腳本沿用來源的 `grok-3`）是否隨 Grok 版本要調——現行 Video 1.5 產線，改版時對照 `docs.x.ai`。
- ⏳ 音訊：部分輸出可能含聲音，但官方 API 未保證可控音訊/對白/lip-sync；以實測為準。
- ⏳ 併發上限 / rate limit（目前腳本逐支序列跑，clip 間 `--inter-clip-sleep` 秒）。

---

## 9. ⚡ Chain Speed Optimization (必填)

> Grok 的 chain = 批次多支影片。**本站不走 UI click，chain 直接映射到 `grok_batch.py` 的迴圈**：一支 clip = 一個 create→statsig→poll→download 週期，天然就是最省的批次形態（無 screenshot、無逐格 UI 操作）。

### 通用最佳 SOP（本站專屬）

**前置（1 次）：** 確認 Chrome CDP 就緒（`probe_cdp` 驗 `webSocketDebuggerUrl`）+ 使用者已登入 grok.com。

**每 clip（腳本自動，無 UI call）：**
```
1. POST /rest/media/post/create      → post_id
2. route **/rest/** 擷取 x-statsig-id （首支 reload 觸發；同 session 可重用頁面）
3. evaluate fetch conversations/new  → 觸發 videoGen
4. poll /rest/media/post/get         → mediaUrl
5. ctx.request.get(mediaUrl)         → 存 mp4
```

**禁忌：**
- ❌ 用 `computer.left_click` / screenshot 逐格操作——本站不需要，純 endpoint 更快更省 token。
- ❌ 純 HTTP（requests/curl）打 endpoint——會被 CF/statsig 擋，白費。
- ❌ 寫死 `x-statsig-id`——動態值，必現場抓。
- ❌ 一次開超大 `--count` 沒跟使用者確認額度——會燒 quota。

**驗證點：** 腳本每支印 `create OK / statsig OK / conversations/new HTTP 200 / found at poll N / OK N MB`，結尾印 `success/fail/total`。看 log 即知，不需 screenshot。

**並行 / Series 替代 chain？** 目前序列跑（clip 間 `--inter-clip-sleep`）。同 session 可重用同一 grok.com 頁面重抓 statsig，省去每支開新頁。

**預期效能：** N 支 ≈ N × (生成時間 + 下載)，主要瓶頸在 Grok 端算圖，非本地 call。

---

## 10. 版本與更新紀錄

- **2026-07-02（初版）：** 新增 `automation/grok_batch.py`（vendored+adapted from 阿軒 Sora去水印下載器 grok_batch.py，intake-audit GREEN-for-this-file）。自動化路徑 = Playwright `connect_over_cdp` 接已登入 Chrome + 內部 `/rest/**` endpoint + `x-statsig-id` 現場擷取。CDP 探測改成 `--cdp-port/--cdp-url/$PINCHTAB_CDP_URL/$CHROME_CDP_URL/:9222`（原版 Windows `wmic` 拿掉）。UI 座標 ⏳ 待實機補。
