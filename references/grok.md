# Grok Imagine (xAI) — 圖 + 影片一站式

xAI 的生成式影像/影片產品，掛在 **Grok**（grok.com / X app 內）與 **xAI API**（`docs.x.ai`）。**一個工具同時做圖與影片**：text-to-image、image editing（自然語言改圖）、多圖合成、text-to-video、image-to-video。

> **本 skill 的定位（保守接入）：** 這裡只提供 **Grok 的 prompt 寫法與選用判斷**。Grok 在本 skill **沒有**像 Flow / pinchtab 那樣接好的瀏覽器自動化交付路徑——產圖 / 產片請使用者自己在 Grok app 或 xAI API 上跑。寫 prompt 的心法比照 [kling.md](kling.md) / [seedance.md](seedance.md)：先讀本檔，別憑記憶硬編。規格更新很快，數字一律以 `docs.x.ai` 與當下 app UI 為準。

## 什麼時候選 Grok
- **要圖也要影片、想在同一個工具一條龍**（先生圖 → 同一張直接轉影片）。
- **快速比稿**：圖預設一次回 **6 張**（可設到 10），挑構圖 / 光線 / 角度 / 表情很快。
- **社群短片、產品 teaser、生活感片段**——約 1–15 秒短形式正中守備範圍。
- ⚠️ **音訊別當預設賣點**：部分 Grok app / Imagine 輸出可能含聲音，但**官方 API 文件目前未保證可控音訊、對白、歌聲或 lip-sync**。需要帶聲、對嘴請以當下 UI/API 實測為準，別預期穩定可控。

## 什麼時候別選 Grok（改用別的）
- **要 1080p / 4K**：Grok 影片目前**封頂 720p**。要高解析走 [kling.md](kling.md)（4K）或 [veo.md](veo.md)。
- **複雜多主體、多動作同框**：易出 artifact / 動態不一致；Grok 在**簡單動作**最穩。複雜編排走 Kling 多鏡。
- **長敘事**：單段約 1–15s，長片靠 **Extend from Frame**（從上一段末幀延伸、保持動態與光線連續）接續，但不如原生多鏡順。

## 模式（Modes）
| 模式 | 取向 | 用途 |
|---|---|---|
| **Normal** | 平衡、寫實、專業安全 | 行銷片、教學、通用（預設首選） |
| **Fun** | 誇張、俏皮、幽默 | 迷因、輕鬆社群 |
| **Custom** | 精準控制 | 要自己調參數時 |
| **Spicy** | 大膽 / 較少守門（含部分 NSFW） | ⚠️ 仍有審核上限，過度露骨會被模糊 / 擋下；品牌 / 商用帳號別用 |

## 圖片 prompt
**結構：** `主體 + 場景 + 風格 + 光線 + 氛圍 + 比例`

- **自然語言改圖**：可直接「把背景換成黃昏」「移除路人」這樣口語下指令，多回合 refine。
- **多圖合成**：一次 edit 裡丟多張參考圖組合。
- 一次回 6 張（可設張數 / 比例 / 解析度）→ 先挑再 refine，定稿再轉影片。

**範例：**
```
一隻橘貓側臥在窗台 (主體)，午後陽光斜射的木質書房 (場景)，溫暖底片質感 (風格)，
柔和逆光、塵埃微粒在光束中浮動 (光線)，慵懶寧靜 (氛圍)，3:4 直幅 (比例)
```

## 影片 prompt（Grok Imagine Video 1.5 = 現行產線）
- **能力：** text-to-video + image-to-video，輸出 **480p / 720p（上限 720p）**，單段約 **1–15s**。
- **音訊（不保證）：** 部分輸出可能含聲音，但**官方 API 文件未保證可控音訊 / 對白 / 歌聲 / lip-sync**；要帶聲以當下 UI/API 實測為準。
- **接長：** Extend from Frame——從前段末幀續生，保持動態 / 光線連續。

**結構：** `主體 + 動作 + 運鏡 + 動態細節 + 氛圍 + 長度`

**範例（i2v，只描述動作不重述畫面）：**
```
她緩緩轉向鏡頭、微笑，髮絲隨動作被光帶起；鏡頭輕微 push-in；
柔和窗光；溫柔懷舊；約 8 秒。
```
**i2v 黃金法則（同 Kling）：** 別重述圖裡已有的東西，**只寫動作與演變**。

## 取用方式
- **Grok app / grok.com**：登入後在 Imagine 介面跑（互動最快）。
- **xAI API**：`docs.x.ai` 的 image / video generation endpoint（可設輸出張數、比例、解析度、回應格式）。第三方亦有代跑（Replicate `xai/grok-imagine-video` 等）。

## 批次自動化（瀏覽器自動化交付路徑）
> 2026-07-02 新增。先前本檔標「不含自動化交付路徑」，現已補上 **REAL 批次自動化後端**。

- **腳本：** [`../automation/grok_batch.py`](../automation/grok_batch.py)｜**站別 profile：** [`../automation/site-profiles/grok.md`](../automation/site-profiles/grok.md)
- **手法：** Playwright `connect_over_cdp` 接管使用者**已登入**的 Chrome，在該 context 內直接打 xAI **內部 REST endpoint**（`/rest/media/post/create` → 現場**擷取活的 `x-statsig-id`** → 頁內 `fetch('/rest/app-chat/conversations/new')` 帶 `videoGen` → 輪詢 `/rest/media/post/get` 取 `mediaUrl` → 下載 mp4）。跑在真登入瀏覽器 context 才能繼承活的 CF cookie + statsig + 真 TLS 指紋，**純 HTTP/curl 會被 Cloudflare + statsig 擋**。
- **CDP 探測：** `--cdp-port` / `--cdp-url` / `$PINCHTAB_CDP_URL` / `$CHROME_CDP_URL`，省略則試 `:9222`（本機 WSL→Windows Chrome 走 pinchtab 啟動器，見 `reference_flow_wsl_windows_chrome_cdp`）。
- ⚠️ **ToS / quota caveat：** 驅動的是使用者**本人**登入的 grok.com session，**消耗其 Grok 額度**，受 **Grok 服務條款**約束；且用的是**內部未公開 endpoint**，Grok 改 API/DOM 即失效。批次前跟使用者確認額度，不代按大 `--count`。

## 連結
- xAI 官方 — Imagine 總覽：https://docs.x.ai/developers/model-capabilities/imagine
- xAI 官方 — 影片生成：https://docs.x.ai/developers/model-capabilities/video/generation
- Grok Imagine Video 1.5 指南（imagine.art）：https://www.imagine.art/blogs/xai-grok-imagine-video-1-5-guide
- 能力總整理（GenAIntel）：https://www.genaintel.com/guides/grok-xai-video-generation-capabilities-2026
- 圖 + 影片教學（PixVerse）：https://pixverse.ai/en/blog/grok-imagine-video-generation-capabilities-2026

---
*規格與模式更新頻繁（Imagine 1.0 = 2026-02 釋出；Video 1.5 為現行產線）。寫 prompt 前以 `docs.x.ai` 與 app 當下 UI 為準。本檔提供 prompt / 選用心法；批次自動化交付路徑已補（見上「批次自動化」段 → `automation/grok_batch.py` + `automation/site-profiles/grok.md`，走內部 endpoint + statsig 擷取，注意 ToS/quota）。*
