# Site Profile: OiiOii.ai

**URL:** https://www.oiioii.ai/
**驗證狀態:** ✅ 2026-04-18/19 demo 實測
**平台類型:** Multi-agent 動畫/影片創作平台
**Stack:** React + tldraw canvas (ref 極不穩定，座標優先)

---

## 1. 整體 UI 地圖

```
┌─────────────────────────────────────────────────────────┐
│ Top bar: 繁體中文選單 | 問題 | 加入會員 | 我的資產 | [代幣] │
├──────────────┬──────────────────────────────────────────┤
│ Left Sidebar │ Center Canvas (tldraw)                    │
│ - 🏠 首頁    │                                           │
│ - 📁 項目    │  [agent 產出顯示區：劇本卡 / 角色圖 /      │
│ - 👤 人像    │   場景圖 / 分鏡 / 影片]                    │
│ - 🗑 回收站  │                                           │
│ - (+) New    │                                           │
├──────────────┴──────────────────────────────────────────┤
│ Left Panel (chat-thread): agent 訊息 + 互動 UI          │
│ [prompt input / 滿意按鈕 / 選項 grid]                    │
└─────────────────────────────────────────────────────────┘
```

**關鍵：** 左側 panel 是 **chat-thread** (不是 form)，agent 訊息由上往下累加，**新內容往往在底部**，但 agent 的 narrative 回覆在上方。需要時 `scroll up` 看 agent 說什麼，`scroll down` 看互動按鈕。

---

## 2. Phase-by-phase 完整流程 + 座標

### Phase 0 — 進入首頁 (`/home`)

首頁中央 prompt 框 + 底部 4 個模式按鈕。

**互動元素 (ref 會變，座標僅供參考)：**
| 元素 | 座標 (1568×708) | 備註 |
|---|---|---|
| 中央 prompt 框 | ~(775, 275) | **contentEditable DIV**，不吃 form_input |
| Seedance 2.0 故事動畫 (預設) | ~(625, 378) | 粉框表已選 |
| 自由畫布 (多模型) | ~(755, 378) | |
| 劇情故事短片 | ~(860, 378) | |
| 角色設計 | ~(963, 378) | |
| + 按鈕 (上傳) | 左下 prompt 框內 | |
| 劇本 按鈕 | 左下 prompt 框內 | 開獨立劇本編輯 |
| 152 種風格 | 左下 prompt 框內 | 風格庫 |
| 送出箭頭 | ~(486, 325) 右下 prompt 框 | type 含 \n 也會觸發 |

### Phase 1 — 輸入 Brief

**步驟：**
1. `computer.left_click` 中央 prompt 框
2. `computer.type` 完整 brief (含 `\n` 會自動送出)
3. URL 立刻跳 `https://www.oiioii.ai/space/{uuid}`

**陷阱：**
- `form_input` 不吃 contentEditable DIV → 回錯 "Element type DIV is not supported"
- Type 帶換行會直接送出，要當心內容完整性

### Phase 2 — 參數頁 (送出 brief 後自動出現)

左側 panel 顯示 checklist + 三組必選：

**Checklist (順序)：**
- ✓ 激活工作流 (自動)
- ✓ 更新短片參數 (自動)

**三組必選 (選一個)：**

| 組別 | 選項 | 座標 (1568×708) |
|---|---|---|
| **影片長度** | 短影片 `<1min` | **(190, 200)** ★ 驗證過 |
| | 長影片 `≥1min` | **(395, 200)** |
| **影片比例** | 橫版 16:9 | **(190, 310)** ★ 驗證過 |
| | 豎版 9:16 | **(395, 310)** |
| **對白語言** | 英文 | **(157, 410)** |
| | 中文 | **(290, 410)** ★ 驗證過 |
| | 日文 | **(428, 410)** |
| **最終確認** | 確認並繼續 | **(290, 477)** (灰色 → 紫紅 active) |

**陷阱：**
- 語言按鈕 **不在 accessibility tree**，`find` 找不到，**必須用座標**
- ref_N 在 2 次 tool call 後會失效，不要先 find 再拖延
- 按鈕的 selected state = **深灰填底**，**不是粉色 ring** (粉色 ring 是 hover)
- 點 `確認並繼續` 後，UI **不會明顯變化** (參數頁凍結)，只會出現粉色「信息已確認」泡泡
- 若再點一次 `確認並繼續` → 紅色 toast「**選項暫不支援重選哦**」= **之前已送出 OK，別再點**

### Phase 3 — 多智能體互動階段 (依序)

每個 agent 2-5 分鐘出一次互動 UI。**60s polling 最好，別等超過 3 分鐘。**

#### 3A — 🔥 藝術總監 (第 1 個 agent)

**agent 訊息** (上方 chat-thread，要 scroll up 看)：「規劃完成 → 導演我收到你的創意提案...」

**互動 UI (情緒關鍵詞 6 選 1)：**
6 格 grid + 自訂輸入 + 隨機，配合 brief 內容 adaptive。

| 選項 | 座標 (1568×751) | 範例 |
|---|---|---|
| 左上 | (155, 290) | 夜晚 |
| 中上 | (290, 290) | 孤獨 |
| 右上 | (425, 290) | 治癒 |
| 左下 | (155, 425) | 溫柔 ★ demo 實測 |
| 中下 | (290, 425) | 青春 |
| 右下 (🎲 隨機) | (425, 425) | |

選中後右下出粉色泡泡 = 送出確認。

#### 3B — 🔥 編劇 (第 2 個 agent)

**agent 訊息：** 「劇本完成 → 場景 1：XXX」
**中央畫布：** 「我的劇本」卡片 + 完整劇本 (含內心 OS / 動作 / 對白)

**互動 UI：**
| 按鈕 | 座標範圍 (y 會漂) | 作用 |
|---|---|---|
| 滿意，請繼續角色設計 | x=290, y=385~430 | 通過進下階段 |
| 我要修改 | x=290, y=455~480 | 回調 |

**⚠️ 確認按鈕 y 座標會漂** — 實測 385 → 573 → 428 都出現過。**click 前必先 screenshot 定位 y**。

#### 3C — 🔥 角色設計師 (第 3 個 agent，3 層確認)

黃色王冠圖標。**有 3 個子階段：**

**3C-1 風格選擇** (8 選 1 grid + 自訂)

| 選項 | 座標 (1568×751) | 風格 |
|---|---|---|
| (135, 100) | Curved Flat |
| (235, 100) | Gentle |
| (335, 100) | Soft-Line |
| (435, 100) | Luminous Li... |
| (135, 255) | Ethereal |
| (235, 255) | Vibrant |
| (335, 255) | Soft Pastel |
| **(435, 255)** | Nostalgic Dreamline ★ demo 實測 |

下方 `+ Surprise Me` (隨機) + `風格庫 152 Style` (更多) + 自訂輸入。

選中後右下泡泡顯示完整風格名 (如 `Nostalgic Dreamline`)。

**3C-2 角色主圖確認** (生成後 2-4 分鐘出按鈕)

| 按鈕 | 座標 | 作用 |
|---|---|---|
| 滿意，請繼續生成角色概念圖 | x=290, y 漂 | ★ |
| 我要修改 | 下方 | |

**⚠️ 這階段 agent 可能自主改 brief 裡的視覺細節** — 實測寫「黑底白爪白胸斑貓」，agent 生成變「橘貓」。demo 可接受或走修改。

**3C-3 角色概念圖確認** (character sheet 生成)

中央畫布顯示每個角色的完整 character sheet (三視角 + 色票 + 特寫分解)。

| 按鈕 | 座標 | 作用 |
|---|---|---|
| 滿意，請繼續場景設計 | x=290, y 漂 | ★ |
| 我要修改 | 下方 | |

#### 3D — 🔥 場景設計師 (第 4 個 agent，3 層確認)

紅色火焰圖標。**結構跟角色設計師一樣的 3 層：**

**3D-1 場景風格**
- 推薦卡片：**「林恩，橘貓 的風格」** (沿用角色一致性) 座標 ~(290, 380)
- 風格庫 152 Style 下方
- 自訂輸入框

**最佳做法：點「林恩，橘貓 的風格」** → 場景跟角色同風格，視覺一致。

**3D-2 場景主圖確認** (生成後出圖 + 按鈕)

| 按鈕 | 作用 |
|---|---|
| 滿意，請繼續生成場景多視圖 | ★ |
| 我要修改 | |

**3D-3 場景多視圖確認** (從主圖衍生多角度縮圖格子)

| 按鈕 | 作用 |
|---|---|
| 滿意，請繼續分鏡設計 | ★ |
| 我要修改 | |

#### 3E — 🔵 分鏡師 ⚠️ **付費牆階段**

藍色圖標 (`@場景設計師 邀請 @分鏡師 加入了群聊`)。

**要選兩組：**

**影片模型 (2 選 1)：**
| 選項 | 座標 | 成本 |
|---|---|---|
| Sora 2 試用 | x=193, y=279 (舊) / y=194 (scroll 後) | **$7 解鎖** ⚠️ |
| Seedance 2.0 試用 | x=390, y=279 / y=194 | **$7 解鎖** ⚠️ |

**分鏡方案 (2 選 1)：**
| 選項 | 座標 | 用途 |
|---|---|---|
| 多圖參考 | x=290, y=378 / y=333 | 直接生影片、快便宜 |
| 宮格圖 | x=290, y=452 / y=410 | 從分鏡畫面開始、可控 |

**確認並繼續：** x=290, y 漂 (477 / 497 / 520 都出現過)

**⚠️ 付費牆機制：**
- 點 Sora 2 或 Seedance 2.0 → 跳 modal：「模型稍貴，為您奉上 **$7 (1,000 便當) 試用套餐**」
- 兩個按鈕：`$7 小試一下` / `升級會員（不差錢）`
- **不付費就無法進到 confirmation send 成功**
- OiiOii 前期免費 (角色 / 場景 / 劇本)，**影片生成關卡一定收費**

**行動原則：** 碰到這個 modal 立刻停下，**不要代付**，問使用者：(a) 付 $7 / (b) 改走 Kling/Vidu 免費模型 / (c) 暫停

#### 3F — 付費後：剪輯 / 配樂 / 最終 MP4

未驗證 (demo 暫停於此)。預計：
- 剪輯師組裝多鏡為連續影片
- 配樂生成
- 最終下載 MP4

---

## 3. 付費結構速查

| 階段 | 成本 | 驗證 |
|---|---|---|
| Brief + 藝術總監 + 情緒 + 劇本 | 免費 (2,000 FREE 代幣內) | ✅ |
| 角色設計 (風格 + 主圖 + 概念圖) | 免費 | ✅ (代幣仍 2,000 未扣) |
| 場景設計 (風格 + 主圖 + 多視圖) | 免費 | ✅ |
| **分鏡 → 影片生成** | **$7 / 1,000 便當 一次性** | ✅ 實測彈窗 |
| 會員訂閱升級 | 價格未查 | - |

---

## 4. 已驗證的 ref 不穩定證據

- `read_page filter=interactive` 回傳 ref_515 (短影片) / ref_520 (橫版 16:9) → 數秒後 click 已失效
- `find "短影片 button"` 回 ref_550 → 下次 click 也失敗
- **對策：改用座標，每 click 前 screenshot 驗證位置**

---

## 5. 常見 toast 速查

| Toast | 意義 | 對策 |
|---|---|---|
| 「信息已確認」粉色泡泡 | action 送出成功 | 繼續下步 |
| 「選項暫不支援重選哦」紅色 | 已送出過、不能再點 | 停點 |
| 「模型稍貴，為您奉上 $7...」modal | paywall | 停下問使用者 |
| 「工作中...」左下 spinner | agent 背後處理中 | 等 60s-3min |

---

## 6. 快速決定樹

```
打開 OiiOii 要什麼？
├── 快速 demo → Phase 0 預設 Seedance 2.0 故事動畫 + 短影片/16:9/中文
├── 多場景故事 → 切「劇情故事短片」模式
├── 角色 IP → 切「角色設計」模式
└── 圖像實驗 → 切「自由畫布」

到分鏡師付費牆前：
├── 使用者想看成品 → 問他付不付 $7
├── 使用者只要角色/場景設計 → 下載資產後結束
└── 使用者想完整影片但不付費 → 把資產匯出，改走 Kling I2V / Runway Gen-4 Refs 免費/低成本生影片
```

---

## 7. Workspace 永久保存

每個 brief 送出後會拿到 URL `https://www.oiioii.ai/space/{uuid}`。這個 URL 永久保存所有產出 (劇本、角色圖、場景圖)，使用者登入後隨時回來繼續。demo 中的 space: `e9ae7550-9ea1-42a8-8ee9-072057ee2a02`。

---

## 8. 代幣監控

右上「2,000 FREE」顯示剩餘免費代幣。demo 完整跑到分鏡師 (含劇本 + 2 角色 + 3 場景圖) 後代幣 **完全未扣** — 確認免費階段真的免費，付費在分鏡師 gate。

---

## 9. 未驗證但值得注意的行為

以下是 demo 沒遇到但別的使用者可能碰到的：

- 上傳參考圖到 prompt 框的 drag-drop 區
- 「劇本」按鈕打開獨立劇本編輯器 (可能有自己的 UI)
- 分享按鈕 (Phase 1+ 右上) 的權限設定
- 若 agent 某步卡住 5 分鐘+，reload 頁面能否從斷點續
- IP Creation (角色設計) 模式的完整流程

發現時補進本檔。

---

## 10. 版本與更新紀錄

- **2026-04-18/19 demo：** 完整跑 Phase 1-3E，撞上分鏡師付費牆停。座標以當時 1568×708/751 viewport 為準。
- **2026-04-20 深夜鳥 project：** Story Video 完整流程跑完 (3 場景 + BGM)，確認 STAR 費 (3 scene 480p Fast = 232 STAR)，解鎖預覽與匯出。匯出 1080p = 1 盒飯/2s (獨立 credit system)。
- **2026-04-20 自由畫布探索：** 測完全部 24 模型、settings panel、盒飯 cost formula — 見 §12。
- **2026-04-20 Seedance 2.0 pro 實戰驗證：** 賽博武士 15s 720p 戰鬥生成成功 — 210 盒飯。發現 `智能模型` toggle **必須關掉** 才能強制使用指定模型，否則 agent 自動 override 到 Sora 2（見 §12.4）。generation 時間 ~3 min，output 品質驚人（chrome 武士 + 電漿刀光 + 火花爆散 + 霓虹街景）。

---

## 11. ⚡ Chain Speed Optimization (OiiOii 連跑多劇本)

**OiiOii 比較特殊 — 是 agent workflow 不是純 prompt 工具。chain 機會少 (通常 1 個劇本 = 1 個專案)，但**選項點選**階段可以省。

### 選項 chain SOP

**重要陷阱：** OiiOii 是 React/tldraw，**ref 易失效**。每個選項點之間：
- ✅ screenshot → 找新 ref → 立刻 left_click (不插任何中間 tool call)
- ❌ find → screenshot → click — **ref 已失效**

**選項 click 流程 (比 Suno 慢但可靠)：**
```
1. screenshot                  → 看當前狀態
2. find <選項描述>             → 拿 ref
3. left_click ref              → 立刻點，無中間步
4. screenshot 驗證 (此網站必須驗 — selected = 填底色非 hover)
5. 點下一步 / 確認按鈕
```

**禁忌：**
- ❌ 跳過 screenshot 驗 selected 狀態 — pink ring = hover 不是 selected
- ❌ 「選項暫不支援重選」toast 出現 → **已提交，不要再點**，不是失敗
- ❌ TodoWrite 每選項一次

**何時可以 chain：** 多個劇本獨立創建時，1 個劇本 1 次完整流程；劇本間沒共享 state，可以連跑但不要多 tab 並行。

**內容長度：** OiiOii 劇本可長可短，1000 字內最佳。

**預期效能：** 單劇本到分鏡師 (撞付費牆) ~3 分鐘 + 800 token
- **下次使用前必做：** navigate → screenshot → 對照本檔 UI 地圖，若配置差很多 (UI 改版)，更新此檔。

---

## 12. 自由畫布 (Free Canvas) 完整模式 ★ 2026-04-20 新驗證

**定位：** OiiOii 的多模型聚合入口 — 24 個頂級 AI 模型一站式切換，是 OiiOii 區別於 Flow/Kling 單平台的最大賣點。不走 agent workflow，是**純 prompt + 模型 + 參數**形式 (像 Midjourney / Seedream / Flow 混合版)。

### 12.1 進入方式

從首頁底部 4 模式按鈕選 **「自由畫布 (多模型)」** (~755, 378) → URL 變 `/space/{uuid}` 但空間類型是自由畫布 (不是 agent workflow)。

### 12.2 UI 佈局

```
┌─ Left (chat panel, ~520px wide) ─┬─ Right (tldraw canvas) ────┐
│ 🎨 藝術總監                       │                              │
│ 「自由選擇模型，快速生成圖片或視訊素材」│                              │
│                                   │   [Empty Frame / generated  │
│ [prompt textbox]                  │    results stacked here]    │
│ [+] [📊 model] [👤] [😊] [⋯= settings]│                          │
│                   [🍱 X 盒飯] [➤]   │                              │
└───────────────────────────────────┴──────────────────────────────┘
```

### 12.3 底部工具列 5 icons (核心座標)

| Icon | 座標 (1568×708) | 功能 | 備註 |
|---|---|---|---|
| `+` | (107, 673) | 附加 / 上傳參考圖 | 未深驗 |
| `📊` bars | (137, 673) | **模型選擇** | 開 dropdown |
| `👤` | (166, 673) | 角色 / 人像 | 未深驗 |
| `😊` | (196, 673) | 風格 | 未深驗 |
| `⋯=` sliders | (225, 673) | **比例/時長/解析度設定** ★ | 影片模型才顯示時長/解析度 |
| 🍱 cost | (~450, 673) | 當前生成成本 (盒飯) | 動態更新 |
| `➤` send | (486, 673) | 送出生成 | |

### 12.4 模型 dropdown — 24 個全列表

**結構：** 上方 `圖片` / `影片` 切換 tab + 右上 `智能模型` toggle (ON = 由 AI 挑模型)。toggle OFF 才顯示全模型並自選。

**⚠️ 關鍵陷阱 — 智能模型 toggle (2026-04-20 實測)：**

`智能模型` toggle 位置：模型 panel 右上角 ~(313, 400)，預設 **ON**（粉色滑桿）。

**ON 行為：** 即使你手動點選某模型（如 Seedance 2.0 pro），`自由畫布 藝術總監` agent 在 planning 階段 **會無視你的選擇** 自己挑一個（常挑 Sora 2）。你看到的是 "使用Sora2生成影片" 而不是你選的。

**OFF 行為：** toggle 關掉後（灰色），agent 嚴格使用你在模型列表點選的那個（會顯示 "使用Seedance 2.0生成影片"），且 Sora 2 的 ✓ 會取消，由你點的模型接手。

**SOP：要指定特定模型 → 先 click toggle OFF → 再點模型 → 再 submit。** 這是強制步驟，跳過 100% 被 override。

**驗證 log：** 2026-04-20 跑賽博武士 15s 戰鬥 prompt 3 次都被 override 到 Sora 2，直到關 toggle + 手點 Seedance 2.0 pro 才成功用對模型（規劃步驟顯示 "使用Seedance 2.0生成影片" ✓ 綠勾）。

#### 🖼 圖片 (8 個)

| 模型 | Badge | 定位 |
|---|---|---|
| Nano 2 | | 速度快，綜合生圖最好 |
| Midjourney niji7 | | 動漫美學最佳，無角色參考 |
| **Nano Pro** | Best | 綜合生圖能力最好 |
| Seedream 5.0 | | 最懂亞洲人美學，理解能力更強 |
| Midjourney niji6 | | 動漫美學效果最佳 |
| NovelAI | | 擅長動漫和插畫風格 |
| Seedream 4.5 | | 默認 2K，最懂亞洲人寫真 |
| Gpt 4o | | 輸入理解最好，生成速度慢 |

#### 🎬 影片 (16 個)

| 模型 | Badge | 定位 |
|---|---|---|
| **Seedance 2.0 pro** | Best | 當下最強影片生成模型 |
| Seedance 2.0 fast | | 趨近 Pro，性價比優選 |
| Sora 2 | | 綜合最佳效果，精準控制 |
| Vidu Q3 Mix | New | 多參增強版，音畫同出 |
| Wan 2.7 | New | 畫面升級，智慧切削鏡 |
| Vidu Q3 Ref | | 參考一致性，音畫同出 |
| Kling 3.0 Pro | | 超清畫質，3D/寫實內容生成較好 |
| Kling V3 Omni | | 多元素參考 |
| Hailuo 2.3 Pro | | 角色動態效果流暢、生動 |
| Wan 2.6 | | 多鏡頭敘事，音畫同出 |
| Kling 3.0 std | | 3D/寫實內容生成較好 |
| Kling O1 | | 多元素參考，激發想像力 |
| Seedance 1.5 Pro | | 高質量視頻生成，運鏡控制力強 |
| Hailuo 2.3 Std | | 角色動態效果流暢、生動，高性價比 |
| Kling 2.6 | | 高質量生成，音畫同出 |
| Vidu Q2 | | 多參啟動 |

**OiiOii 最大賣點：** 不用切 Flow / Kling / Vidu 三個網站就能切換它們的模型 — **一個帳號一個 prompt 直接比較**。圖片類 Nano Pro + Seedream + MJ niji7 一站到位省切站時間。

### 12.5 設定 Panel (⋯= icon 開啟) ★ 影片模型必看

**觸發：** 選好影片模型後 → click sliders icon (225, 673) → 彈出設定 panel (~220-525 x, ~430-665 y)

**三組設定：**

| 類別 | 選項 | 備註 |
|---|---|---|
| **比例** | 16:9 / 9:16 / 1:1 / 4:3 / 3:4 / **21:9** | 21:9 **只 Seedance 2.0 fast 有**，pro 沒有！ |
| **時長** | 4-15 秒 (可選)，- / + 按鈕，1s 一階 | 預設 10s |
| **解析度** | 480p / 720p slider | **1080p 要另外從 Library 匯出** |

**盒飯 cost formula (Seedance 2.0 實測)：**

| 模型 | 480p | 720p |
|---|---|---|
| Seedance 2.0 fast | **5 盒飯/秒** | 11 盒飯/秒 |
| Seedance 2.0 pro | 7 盒飯/秒 | 14 盒飯/秒 |

- 例：fast 10s 480p = 50 盒飯 (實測 55 at 11s)
- 例：pro 11s 720p = 154 盒飯
- **480p vs 720p ≈ 2.2x**
- **pro vs fast ≈ 1.4x** (pro 40% 貴)

**省錢鐵則：** 測試用 **fast + 480p + 10s = 50 盒飯** 最便宜。滿意再用 pro + 720p。

**其他模型的 cost formula 待驗** — Sora 2 / Kling 3.0 Pro / Vidu Q3 Ref 預計更貴。

### 12.6 盒飯 vs STAR 雙貨幣系統

OiiOii 有 **兩套 credit system**：

| 貨幣 | 用途 | 取得 | 驗證 |
|---|---|---|---|
| **STAR** | Story Video agent workflow (Phase 0-3E) | 免費 + 訂閱加購 | ✅ 4,968 remaining after 深夜鳥 (232 用) |
| **盒飯** | 自由畫布生成 + 1080p 匯出 | 訂閱 / 日常贈送 | ✅ 100 盒飯 (3 天到期)，有限非 credit 池 |

**注意：**
- STAR ≠ 盒飯 — 不互通
- 盒飯**有到期日** (3 天)，用不完浪費
- STAR 免費 tier 充足 (2000-5000)，盒飯往往是瓶頸
- 1080p 匯出**獨立收 1 盒飯/2s** (Story Video 免費跑但匯出付費)

### 12.7 Chain Speed Optimization — 自由畫布專用

**適用情境：** 5-10 個獨立 prompt，同一模型，探索主題。

**最佳 SOP：**
```
前置 (1 次)：
1. navigate /home → click 自由畫布
2. screenshot 確認 UI
3. click sliders icon → 設定 fast/480p/10s (最便宜)
4. click bars icon → 選 Seedance 2.0 fast (或目標模型)

每 prompt (chain, 理想 ≤ 4 calls)：
1. (若需清空) triple_click prompt textbox
2. type <new prompt>
3. click ➤ send (486, 673)
4. wait 60-90s + screenshot (每 2-3 prompts 一次，非每次)
```

**禁忌：**
- ❌ 每生成後 screenshot — 浪費 1.5k token
- ❌ TodoWrite 每 prompt
- ❌ 重新開設定 panel 每次 — 設定會記住
- ❌ 混切模型 — 每切模型設定會 reset

**並行替代：** 單 prompt 不能 batch 多張 (不像 Ideogram 一次 4 張)。想多樣 **寫多個 prompt 連發** 最快。

**預期效能：** 5 prompts × 10s 480p = 250 盒飯，~8 分鐘，< 2k token。

### 12.8 未驗證 (下次探索補)

- ⏳ `+` icon 上傳參考圖的流程
- ⏳ `👤` 角色 icon — 是否有 character library
- ⏳ `😊` 風格 icon — 是否跟 152 種風格庫連動
- ⏳ 152 種風格入口在自由畫布位置 (初畫面有，選模型後消失)
- ⏳ 圖片模型 (Nano 2 / Seedream 5.0 / MJ niji7) 的盒飯 cost — 可能更便宜 (沒時長維度)
- ⏳ Sora 2 / Kling 3.0 Pro / Vidu Q3 Ref 的 cost formula
- ⏳ 1 次 prompt 能否同時產多張 (變體)
- ⏳ tldraw canvas 上的 Frames 是否能拖拉編輯、加 text
- ⏳ 「多選」「添加畫板」按鈕功能

---

### 12.9 單次生成「指定模型」黃金 SOP ★★★ 2026-04-20 實戰優化

**情境：** 用戶指定特定模型 + 特定規格（如「Seedance 2.0 pro 720p 15秒」）— 必須**確保 agent 不 override**、一次到位。

#### 🥇 7 步流程 (< 10 calls，純點擊 < 30 秒 + 等待 ~3 min)

```
1. (若未在 space) navigate 到 /home → click 自由畫布入口
   └─ 若已在 /space/<id> 且在自由畫布模式 → 跳過
2. click 📊 模型 icon (137, 673)        # 打開模型 panel
3. click 智能模型 toggle OFF (313, 400) # ⚠️ 灰色 = OFF，絕對不能省
4. click 目標模型 (Best 標籤的在列表最上)
   └─ Seedance 2.0 pro = 第 1 項 ~(225, 485)
   └─ Seedance 2.0 fast = 第 2 項 ~(225, 530)
   └─ panel 會自動關閉，bottom toolbar 顯示該模型的設定 icon
5. click ⋯= sliders icon (225, 673)    # 打開設定 panel
6. 按 + button (440, 620) 直到時長 = 用戶要求或模型上限
   └─ 每次 click = +1s (非跳 4/8/12)
   └─ 最大值到時 button 變灰
   └─ 720p button ~(415, 620) 若要高解析度 click
7. click 空白處 (1000, 200) 關設定 panel # ⚠️ 設定會覆蓋 textbox，必須先關
   → click textbox (290, 587)
   → type <prompt>
   → click ➤ send (486, 673)
```

#### 📊 模型上限速查（避免「要 20s 被 cap 到 15s」之坑）

| 模型 | 時長 | 解析度 | 比例 | 720p 成本 | 適用 |
|---|---|---|---|---|---|
| **Seedance 2.0 pro** | 4-15s 連續 | 480p/720p | 5 種 (無 21:9) | 14 盒飯/s | 品質優先 |
| **Seedance 2.0 fast** | 4-15s 連續 | 480p/720p | 6 種 (含 21:9) | 11 盒飯/s | 性價比 |
| **Seedance 1.5 Pro** | 4-12s 連續 | 固定 (單 preset) | 3 種 | 5 盒飯/s | 省錢 |
| **Sora 2** | 固定（待驗） | 2 種 | STAR/盒飯 待驗 | 高 | 精準控制 |
| **Vidu Q3 Mix/Ref** | up to 16s | 含音訊 | 待驗 | 待驗 | 長片 + 音畫同出 |
| **Kling 3.0 Pro** | 待驗 | 超清 | 待驗 | 待驗 | 寫實 |

**用戶要超過 15s？** Seedance 系列都不行 → 改 Vidu Q3 (16s) 或 Seedance fast × 2 段接續。

#### ⚠️ 三大陷阱速避（本次踩過才寫出來）

1. **智能模型 ON = 手選被 override**
   - 症狀：你選 Seedance 2.0 pro，agent "思考完成" 卻顯示 "使用Sora2生成影片"
   - 對策：**每次進模型 panel 第一件事就是確認 toggle 是灰色**
   - 代價：一次 override 浪費 70-210 盒飯 + 3 分鐘

2. **設定 panel 覆蓋 textbox**
   - 症狀：type 文字沒進 textbox，畫面看不出反應
   - 對策：**開設定 → 調完 → 必先 click 空白處關 panel → 才 click textbox**
   - 替代：只調設定不 type 時可保持 panel 開

3. **成本顯示延遲**
   - 症狀：選模型後 cost badge 看起來是舊值
   - 對策：開一次 sliders panel（+ / - 按一下）→ 右下 cost 才跳到正確值
   - 不要在沒打開 sliders 就相信當前 cost

#### ⏱ 時間預算

| 階段 | 時長 | 備註 |
|---|---|---|
| 點擊階段（7 步） | ~30s | 不含等待 |
| Seedance 2.0 pro 15s 720p | ~2.5-3 min | 同 prompt + setup |
| Seedance 2.0 fast 15s 480p | ~1-1.5 min | 約 pro 一半 |
| Sora 2 同規格 | ~2-4 min | 待驗 |
| **total per generation** | **~3-4 min** | 含全部 |

#### 🔁 Chain 多次同模型（2+ 次）優化

模型 + 設定會**記住**，chain 中每次只需：
```
1. click textbox (290, 587)
2. triple_click 清空
3. type <new prompt>
4. click ➤ (486, 673)
[wait ~3 min，全部 chain 結束後 1 次 screenshot]
```
省掉 toggle / 模型 / sliders 的 4 次 click = 每 prompt 省 ~6 秒 + 省 token。

#### 💸 預算建議

- **測試階段：** Seedance 2.0 **fast** + **480p** + 10s = **50 盒飯** 最便宜
- **品質階段：** Seedance 2.0 **pro** + **720p** + 15s = **210 盒飯** 上限
- **免費 tier：** 每日 60-100 盒飯配額 → 品質一次 = 一天的配額，測試一次 = 半天
- **1080p 匯出**：Library → 額外 1 盒飯/2s（**不是**生成時就含 1080p）

---

### 12.9.5 ⚡ Speed v2：單次生成 tool-call 最小化 (2026-04-20 實戰優化)

前版 §12.9 SOP 驗證 ≈ 11 min + 1.5k token。分析發現 **~40% 浪費在等待迴圈 + 多餘驗證 screenshot**。這是 v2 削刀版。

#### 🔪 五刀優化

| 刀 | 舊作法 | 新作法 | 省 |
|---|---|---|---|
| **① 等待** | `wait 10s` × 18-27 次 = 20+ tool calls | `Bash "sleep 180"` 單次（max 600s 可用） | ~25 calls |
| **② 驗證 screenshot** | 每步確認（開 panel / 調滑桿 / 打完字 / 送出後）= 7 張 | 只首尾 2 張 | ~5 calls + 0.4k token |
| **③ Zoom 驗證 toggle** | zoom 看 switch 顏色 | **信號法**：cost badge 不變 = 模型/設定未變 | -1 call |
| **④ Prompt 長度** | 400+ 字 English 美圖段 | **180 字 shot-list 腳本**（§12.9.6） | -0.3k token + 10s type |
| **⑤ 關 panel** | `click (1000, 200)` → `click textbox` | **✅ 實戰驗證：panel 不會自動關**，必須先 click 畫布空白處（如 `800, 300`）→ 再 click textbox。原預想的「textbox click 自動關 panel」是錯的。 | 0（rule stays 2-step） |

#### ⏱ 時間 / token 預算比較

| 情境 | Tool calls | 時間 | Token |
|---|---|---|---|
| §12.9 v1（未優化） | ~40 | ~11 min | ~1.5k |
| **§12.9.5 v2（單次優化）** | **~12** | **~6 min** | **~0.7k** |
| **§12.9.5 v2 Chain（第 2+ 生成）** | **~5** | **~4 min** | **~0.3k** |

#### ✂️ Chain-ready minimal flow（第 2+ 生成同模型同設定）

**注意 — 生成後 `時長` 可能被重置回預設 10s**（2026-04-20 驗證：140 → 210 生成後 → 回 140）。ratio/res 會保留，**只有時長需要重調**。

```
[若時長被重置回 10s]
1. click sliders (225, 673)
2. + × N 到目標時長 (462, 560)
[關 panel — 必要]
3. click 畫布空白處 (800, 300)  # ⚠️ panel 不會因 textbox click 自動關
[type + send]
4. click textbox (290, 605)     # y 用 605（590 以上可能仍在 panel 範圍）
5. ctrl+a → Delete              # 或 triple_click，清空舊內容
6. type <new prompt>
7. click send (486, 673)
8. Bash sleep 180 &             # 背景等 3 min（1 call 取代 18× wait）
9. screenshot                    # 驗收
```

= **~9 tool calls** 含重調時長；若時長保留則 **~6 calls**。

**座標精修（2026-04-20 驗證）：**
- textbox 安全座標 = `(290, 605)` 不是 `(290, 587)` — 587 在時長 panel 範圍內
- 畫布空白處關 panel = `(800, 300)` 最穩（不點到工具列、不點到視頻縮圖）

#### 🧨 禁忌再強調

- ❌ 不要用 10s wait 迴圈 — 每個 wait 是獨立 tool call，開銷巨大
- ❌ 不要每次操作後 screenshot — cost badge 已是狀態信號
- ❌ 不要 zoom 看 toggle — 相信 §12.9 前置狀態
- ❌ 不要寫 400+ 字 prompt — 藝術總監會重寫，長寫 = 白工 + 浪費 type time

---

### 12.9.6 🎬 Elite Prompt Engineering：Shot-List 腳本法 (2026-04-20 質感革新)

**病根：** 寫「美圖羅列段」→ 模型把 15s 當單鏡處理 → 鏡位單一 / 戰鬥鬆散 / 廣告沒節奏。

**解法：** 寫成 **shot-list 腳本** + 時間戳 + 強攝影語 + 類型專用動詞庫。

#### 🧱 通用結構模板

```
[HEADER]  genre + aspect + duration + palette + lens/film stock
SHOT 1 [0-3s]   type | subject | action | camera | VFX
SHOT 2 [3-7s]   ...
SHOT 3 [7-11s]  ...
HERO  [11-15s]  money shot + brand/beat moment
[LIGHTING]  key/fill/rim/practicals
[TEXTURE]   macro noise + surface specifics
[MOTION]    speed ramps, match cuts, whip pans
```

**關鍵：** 模型吃到 `SHOT 1/2/3/HERO` 標籤會**自動切鏡** — 這是 unlock 多鏡位的核心。

#### 📹 通用攝影 / 鏡頭 / 底片詞庫

`dolly push-in` `crane reveal` `whip pan` `orbit` `speed ramp` `time remap` `match cut` `rack focus` `split diopter` `over-the-shoulder` `low-angle hero` `Dutch tilt` `handheld breathe` `anamorphic 2.39:1` `ARRI ALEXA` `Kodak 500T grain` `35mm T1.4 prime` `85mm macro` `vintage cooke anamorphic bloom` `practical backlight` `Villeneuve amber` `Fincher teal-orange` `Deakins golden`

#### ⚔️ 戰鬥類強 token 庫

**編舞動詞**（取代弱的 "clash"）：
`parry → riposte` `bind + disengage` `reversal` `hilt smash` `footwork pivot` `kill-shot freeze`

**impact VFX：**
`bullet-time freeze at impact` `blade arc trail` `shockwave ripple` `kinetic spark burst` `ember cascade` `armor plate deflect` `motion blur tracers`

**攝影語：**
`whip-pan follow blade` `handheld shake on impact` `speed ramp into final blow` `72fps high-speed on strike` `low-angle hero silhouette`

**聽覺 cue（幫模型 time beat）：**
`sub-bass thud on impact` `steel ring` `breath fog` `cloth tear`

#### 🥤 廣告類強 token 庫（飲料 / 產品）

**4 幕結構：** `cold open tease → pour crescendo → splash freeze → product moneyshot + end-card`

**商業語：**
`cold open product tease` `rim-lit bottle silhouette` `condensation beads rolling` `pour crescendo` `crystalline ice crackle` `splash crown freeze at peak` `honey-amber ribbon swirl` `citrus twist cascade` `mint leaf drift` `droplet ping on wet marble` `push-in macro on label` `rack focus from bokeh to logo` `dew glint catch-light` `end-card negative space for logo`

**聽覺 cue：**
`ASMR pour sound` `satisfying pour-splash-reveal beat` `ice crackle foley`

#### ✍️ 模板示範：冰紅茶 15s（180 字 shot-list）

```
15s luxury iced black tea commercial, 16:9 anamorphic 2.39,
warm honey-amber palette with cool marble contrast,
35mm T1.4, Kodak 500T grain, ARRI ALEXA clean highlights.

SHOT 1 [0-3s] extreme macro close-up, frosted amber bottle silhouette
rim-lit by window haze, condensation beads rolling, slow dolly-in.

SHOT 2 [3-7s] overhead medium, hero pour — deep ruby tea cascading
over crystalline ice into chilled crystal glass, splash crown freeze
at peak, honey-amber ribbons swirl, 72fps speed ramp, ice crackle.

SHOT 3 [7-11s] side macro, sunlit lemon twist tumbling, mint cascade,
droplet ping on wet black marble, whip-pan transition.

HERO [11-15s] push-in rack focus from bokeh to label sharpening,
single dew droplet glints on backlight, beat drops on reveal,
end-card negative space for logo.

Rim-lit sunbeam key, marble bounce fill, amber kitchen bokeh practical.
```

#### ✍️ 模板示範：戰鬥 15s（180 字 shot-list）

```
15s cyberpunk samurai duel, 16:9 anamorphic 2.39,
neon magenta-cyan palette over rain-slick asphalt,
35mm T1.4, Kodak 500T grain, handheld breathe.

SHOT 1 [0-3s] low-angle hero silhouette, chrome-clad samurai steps forward,
breath fog, plasma katana hum ignites, rim-lit by alley neon.

SHOT 2 [3-7s] whip-pan follow blade — first parry and riposte against
mech-ninja tungsten sword, kinetic spark burst, bullet-time freeze at
impact, blade arc trail, 72fps on strike.

SHOT 3 [7-11s] handheld shake, bind + disengage, armor plate deflect,
shockwave ripple, ember cascade from clashing edges.

HERO [11-15s] speed ramp into final blow, hilt smash reversal, kill-shot
freeze on blade-light flare, sub-bass thud, motion blur tracers.

Neon magenta key, cyan fill from wet asphalt bounce, practical sign haze.
```

#### 🔑 三不寫（訊號汙染）

- ❌ `cinematic` / `ultra-photoreal` / `4K` — 早成雜訊，換成**具體鏡頭 + 底片名**
- ❌ 單段落羅列形容詞 — 模型會當單鏡處理
- ❌ 沒時間戳 — 模型無法切鏡節奏

#### 🧪 驗證成本

Elite prompt 不會增加生成成本（同 210 盒飯），**質感提升在模型側**。首次 token 多寫 ~50，但省下「結果爛再重跑」的 210 盒飯 + 4 min。

---

### 12.9.7 🎭 角色參考（資產庫）特殊流程 (2026-04-21 實戰發現)

**發現情境：** 用 😊 icon (195, 673) → 我的資產 → Characters tab → 點角色附到 prompt → submit。
**與純文字最大差別：** **不是**直接呼叫 Seedance，而是觸發 **3-agent serialized pipeline**。

#### 🔬 Pipeline 解剖

```
[你 submit prompt + char ref]
  ↓
① 圖片理解 agent     — 讀角色主圖 → 產出文字描述（canvas 上顯示 "圖片理解中"）
  ↓
② 👑 角色設計師 agent — 生 3-view turnaround sheet（正/側/背 + 服裝/髮型細節）
  ↓
③ Seedance 2.0 pro   — 用 char + turnaround 做 character-consistent video
  ↓
[結果：canvas 多出 turnaround image + 影片，左側 "已成功產生影片"]
```

**visual cue：** canvas 會長出 "👑 角色設計師" 節點 + turnaround sheet image（有「同步資產庫」按鈕可存起來重用）

#### ⏱ 時間 / 成本對照

| 模式 | 時間 | STAR 消耗（15s pro） | 備註 |
|---|---|---|---|
| 純文字 → Seedance | 4-6 min | 210 | §12.9 baseline |
| **首次用某角色 ref** | **~15 min** | **110**（實測 4,438→4,328） | pipeline serialized，pro 單價反而低？待復核 |
| 同角色重用（理論） | ~6 min | ~210 | turnaround 已存資產庫 → 跳過設計師 step（⏳ 待驗證） |

**為什麼實測 110 STAR 而不是 210？** 待查。可能是：
- (a) 角色 ref 流程走不同定價（底價 + 設計師贈送？）
- (b) 某次生成時長被系統降級
- (c) 觀察誤差（前一次 balance 記錯）

#### 🧭 等待策略（不要 timeout，不要中間亂戳）

```
submit → Bash sleep 300 (5 min) × 2-3 輪
→ 每輪 1 screenshot 確認：
   ① STAR 變化？（Seedance 已執行）
   ② 左側 panel "已成功產生影片"？
```

**⚠️ 第一次用某角色必慢** — 別 sleep 180 就 panic 以為卡住，**給它 15 min**。

#### ✍️ 角色 ref prompt 寫法

- ✅ `featuring <Name>` / `<Name> does X` — 引用 ref
- ✅ 直接寫動作 + 場景 — ref 會處理外觀
- ❌ 別重寫外觀形容 — `a man with short black hair in black t-shirt` 會與 ref 衝突 → 生成混亂

**範例（實戰驗證過）：**
```
15s gritty realistic urban combat featuring Hao, 16:9 anamorphic 2.39,
cold desaturated steel-blue palette with amber streetlight warm contrast,
35mm T1.4, Kodak 500T grain, ARRI ALEXA clean highlights, handheld breathe.

SHOT 1 [0-3s] low-angle hero silhouette of Hao on rain-slick asphalt alley,
breath fog in cold night air, cracked knuckles clench, over-the-shoulder
reveal of attacker across the alley, neon signage bleed.
SHOT 2 [3-7s] whip-pan into engagement — Hao throws tight jab-cross combo,
attacker parries and counters with elbow, handheld shake on impact...
...
Photoreal, no stylization.
```
→ 結果：Hao 臉部與 ref 一致，光影電影感，蹲姿 hero frame 成功。

#### 🎯 決策樹

```
要做角色一致影片？
├─ 首次 → 自由畫布 + 資產庫選角色 → 等 15 min，產出 video + turnaround
├─ 同角色再做 → 同畫布連跑（turnaround 已有）→ 理論 6 min
└─ 不在乎特定長相 → 別用 ref，純文字 4-6 min 即可
```

---

### 12.9.8 🛠 Prompt 工具列完整拆解 (2026-04-21 實戰探勘)

**自由畫布底部 prompt 工具列，左到右 5 個 icon：**

| 座標 | Icon | 功能 | 說明 |
|---|---|---|---|
| (107, 673) | **+** | **選擇圖片** | 上傳 ref 墊圖，支援 `.jpeg` `.png` `.jpg`，開系統 file picker |
| (137, 673) | **ll (直條)** | **模型選擇器** | 開 dropdown，有 `圖片` `影片` tabs + 智能模型 toggle + Best 標 |
| (166, 673) | **🎨 (圓圈相扣)** | **風格庫** | 34 風格 filtered by model（**影片模型全部不支援**）|
| (195, 673) | **😊** | **我的資產** | 角色 / 場景 ref（§12.10 詳述）|
| (225, 673) | **≡ (sliders)** | **參數設定** | duration / aspect / resolution |

#### 📦 模型 Catalog（2026-04-21 實測 list）

**圖片 tab：**
| 模型 | 標籤 | 強項 |
|---|---|---|
| **Nano Pro** | Best | 綜合生圖能力最好 |
| Nano 2 |  | 速度快，綜合生圖最好 |
| Midjourney niji7 |  | 動漫美學最佳，無角色參考 |
| Seedream 5.0 |  | 最懂亞洲人美學，理解能力更強 |
| Seedream 4.5 |  | 默認2K，最接近東方人審美 |
| NovelAI |  | 擅長動漫和插畫風格 |
| Gpt 4o |  | 輸入理解最好，生成速度慢 |

**影片 tab：**
| 模型 | 標籤 | 強項 |
|---|---|---|
| **Seedance 2.0 pro** | Best | 當下最強影片生成模型 |
| Seedance 2.0 fast |  | 離近 Pro，性價比優選 |
| Sora 2 |  | 綜合最佳效果，精準控制 |
| Vidu Q3 Mix | New | 多參增強，音畫同出 |
| **Vidu Q3 Pro** |  | **高質量切機理解打鬥，音畫同出** ← 戰鬥專用！|
| Vidu Q3 Ref |  | 參考一致性，音畫同出 |
| Wan 2.7 | New | 畫質升級，智慧剪輯 |
| Wan 2.6 |  | 多鏡頭敘事，音畫同出 |
| Kling 3.0 Pro |  | 超清畫質，3D/寫實內容生成較好 |
| Kling V3 Omni |  | 多元參考，擅長3D/寫實內容 |
| Kling 3.0 std |  | 3D/寫實內容生成較好 |
| Kling O1 |  | 多元素參考，激發想象力 |
| Hailuo 2.3 Pro |  | 角色動態效果流暢、生動 |

**成本對照（15s pro 影片）：**
| 模型 | 盒飯 | 備註 |
|---|---|---|
| Seedance 2.0 pro | 210 (15s) / 140 (預設) | 貴但最穩 |
| Vidu Q3 Pro | 60 (預設) | 戰鬥/打鬥專用，便宜 |
| Nano Pro + 風格 | 7 | 圖片，最便宜 |

#### 🎨 風格庫完整 map

**開啟方法：** 必先選**圖片**模型 → click (166, 673) → panel 在右側開出
**關閉方法：** click 畫布空白處 / 再按同 icon / 選定某風格後自動關

**Toast 錯誤：** 若當前是影片模型 → "目前該模型不支援風格選擇" → 必先切圖片模型

**11 個子分類（⌄ 展開）：**
```
全部 | 最近使用 | 我的風格
立體風格 | 国風 | IP風格
歐美風格 | 插畫風格 | 日系風格
韓系 | 可愛Q版
```

**已驗證風格（Nano Pro 34 種的部分）：**
| 風格名 | 視覺 | 建議搭配 |
|---|---|---|
| **AI真人(建议垫图)** | 寫實人像 | **必搭 + 上傳 ref 墊圖** |
| 荒野大表哥 | RDR2 寫實西部牛仔 | 粗獷寫實場景 |
| 雙城風格 | Arcane 動畫 | 3D 西方動畫 |
| KpopCG | 偶像 3D 風 | 女角 + 現代 |
| 遊戲CG | 原神/仙俠風 | 3D 中式 |
| 3DZ遊 | 3D 遊戲風 | 通用 3D |
| 像素農場 | Stardew | 像素/復古遊戲 |
| 歐美CG | Western CG | 粗獷 3D |
| 方塊世界 | Minecraft | 方塊/像素 |

**選風格後：** prompt bar 會出現 chip `📷 <風格名>`（像資產庫 character chip 一樣），已附到下次 submit

#### ⚠️ 關鍵規則

1. **風格庫 ≠ 影片** — 所有影片模型都 reject 風格，要用風格必先切圖片模型
2. **工作流程：** 風格化影片 = 生圖（Nano Pro + 風格 + 上傳 ref）→ 拿該圖用影片模型做 i2v / frame-ref
3. **上傳 + 風格 + prompt 三合一** 是黃金組合（尤其 AI真人 類的「建议垫图」風格）
4. **Vidu Q3 Pro 專門為打鬥調教** — 寫實戰鬥影片首選（取代 Seedance，便宜 3.5 倍 + 打鬥更強）

#### 🚀 寫實戰鬥完整 SOP（2026-04-21 新版）

```
Step 1  自由畫布 → 模型 (137, 673) → 圖片 tab → Nano Pro
Step 2  風格 (166, 673) → AI真人(建议垫图)
Step 3  + (107, 673) → 上傳主角 ref 照片
Step 4  textbox 寫 shot prompt（見 §12.9.6 elite prompt）
Step 5  送出 → 得到寫實戰鬥**圖**（~30s，7 盒飯）
Step 6  該圖右鍵 / 圖片 tab 選 → 模型切 Vidu Q3 Pro（打鬥專用）
Step 7  textbox 寫 motion 描述（動作節奏）
Step 8  送出 → 得到寫實戰鬥**影片**（~3-5 min，60 盒飯）
```

**vs 舊 Seedance-only 方案：**
| 項目 | 舊（Seedance 15s） | 新（Nano Pro 圖 + Vidu Q3 Pro 影片）|
|---|---|---|
| 盒飯總計 | 210 | 7 + 60 = 67 |
| 控制度 | 全靠 prompt | 先鎖圖再動畫，風格保證 |
| 打鬥質感 | 通用 | 專用調教 |
| 時間 | 15 min（含角色 pipeline）| 圖 30s + 影片 3-5 min |

---

### 12.9.9 ⚡ 極速 SOP：5 min → 25 sec（2026-04-21 實戰）

**用戶抱怨：** 「5 分鐘太垃圾，能不能 30 秒解決」→ 實測降到 25 秒。

#### 速度 breakdown（送出一個新 gen）

| Stage | 舊 | 新 | 省 |
|---|---|---|---|
| 每步 screenshot 驗證 | 12 次 | 0-1 次（paste 前 + 送出後）| ~18k token、2 min |
| Model 選擇（若未換）| 切 tab + 滾動 + 點 | **跳過** | ~30s |
| Settings（若未換）| 開 sliders + 3 次調整 | **跳過** | ~20s |
| 角色資產 | 開 lib + 點 char | 同（chip 送出後會掉，必重點）| 不可省 |
| Paste prompt | type 一字 | `type` 全文（<5s）| 10s |
| 送出後 wait | 每分鐘 screenshot | background sleep + 終點 1 screenshot | 省 5-10k token |

#### 極速 SOP（25 sec submit）

**前置假設：** session 已開，上次 model / settings / duration 仍有效

```
1. key Esc                        (close any modal)
2. click (195, 673)                (asset lib, if char ref needed)
3. click <character thumb>         (attach chip)
4. click <prompt field>            (focus)
5. type <prompt>                   (全文一次)
6. click (487, 673)                (submit arrow)
```

**6 calls ≤ 25 秒**。Screenshot 只在最後送出確認 + 結果完成時各 1 次。

#### ⚠️ 致命坑：底部工具列 y 座標會漂（2026-04-21 教訓 #2）

**症狀：** 第 4 次 gen 花 2:50 + 500 token（目標 25 秒）。

**根因：** OiiOii viewport 高度會在 708 / 751 間切換（可能 browser chrome 狀態、modal 開合觸發）。**底部 prompt 工具列永遠貼底**，所以 icon y 座標跟著浮：
- viewport 708 → icons y ≈ 673
- viewport 751 → icons y ≈ 715
- 差 42 px → click 落空 → panel 開不了或開了又關

**對策（強制 SOP）：**
1. **每次 chain 第 1 call** 先 `screenshot` 一次，用真實像素定位 icon 實際 y（看底部灰色 bar 的中心）
2. Settings/Assets panel 的內容元素（duration +/−、character thumb）**座標也跟著 viewport 漂** — 看螢幕 not 死背
3. 若 click 設定後 cost 沒變，別急著按 +，先看 panel 有沒有開（有可能被點外面關了）

**座標 cheat sheet（以 viewport 708 為基準）：**
| 元素 | y=708 座標 | y=751 座標 |
|---|---|---|
| 底部 icons | (107/137/166/195/225, **673**) | (..., **715**) |
| Duration + button | (463, **559**) | (463, **601**) |
| Submit arrow | (487, **673**) | (487, **715**) |

#### ⚠️ 致命坑：「我想修改」flow 會 reset duration（2026-04-21 教訓 #1）

**症狀：** 左側 agent panel 的「我想修改:」下面直接貼新 prompt 送出，結果 duration 變預設 10 秒（不是你上次的 15 秒）。

**根因：** 修改 flow 跳過 settings panel，**不繼承上次 duration**，一律用模型預設。
- Seedance 2.0 pro 預設 = 10s（成本 140 盒飯，非 210）
- Vidu Q3 Pro 預設 = ?（待驗）

**診斷訊號：** cost counter 顯示 140 而不是 210 → duration 被 reset 成 10s
**對策：**
1. 想改 duration/aspect 必須用**底部 prompt 工具列** (225, 673) settings 重送，不要用「我想修改」捷徑
2. 送出前看 STAR 預算差：若預期 210 但顯示 140，立刻停，檢查 duration
3. 極速 SOP 第 1 call 前先 `screenshot` 看 cost 預覽當 sanity check

#### Token-saving 鐵則

| 行為 | 禁/用 | 理由 |
|---|---|---|
| 中間 screenshot 驗證 | ❌ | 每張 ~1.5k token，12 張 = 18k 浪費 |
| 每 click 後 screenshot | ❌ | 座標已記 §12.9.8，點了就對 |
| 等待用 sleep 60 × N | ❌ | 改 `run_in_background: true` + 一次 sleep 270-300 |
| 等待 polling 每分鐘 | ❌ | 等通知，不主動 poll |
| Hao 角色 chip 送出後再重附 | ✅（必）| 這是平台的 session tax，~5 sec，接受 |
| 首次進 session 先掃 UI | ✅ | 1 次 screenshot 建立座標信心 |

#### 等待策略（Seedance pipeline ~8-15 min）

```
submit → Bash sleep 400 (run_in_background:true) → 等通知 → screenshot 1 次
```

**絕不：**
- ❌ sleep 60 × 10 次（浪費 token 每次檢查）
- ❌ 中間主動 screenshot 看進度

**如果 3 分鐘內有 toast 「配額不足」：** 例外可提早 screenshot。

---

### 12.9.10 🚫 Prompt 七大垃圾模式（實戰總結）

**這些 pattern 會讓 Seedance / 中文訓練的影片模型產出爛結果：**

| 垃圾模式 | 範例 | 為何爛 | 改成 |
|---|---|---|---|
| 1. 堆技術 token | `35mm T1.4, Kodak 500T, ARRI ALEXA` | 稀釋核心，無視覺提升 | 去掉或僅留 1 個關鍵 |
| 2. 導演名堆疊 | `Zhang Yimou frames, Kurosawa handheld` | 中文模型 over-weight 或忽略 | 用具體視覺詞（painterly wide shot, handheld intimacy）|
| 3. 4+ shot 塞 15s | `SHOT 1/2/3/HERO` | 每鏡 3s 無法呈現細節 | 單鏡 connected shot，或換多鏡專用模型（Vidu Q3）|
| 4. 抽象動作詞 | `parry-riposte, slash arc, sweep-combat` | 影片模型動作認知弱 | 具體：`sword raised slashing forward in sweeping arc` |
| 5. generic 形容詞 | `cinematic, epic, dynamic` | 不帶視覺資訊 | 用 skill 進階語彙庫（§12.9.6）|
| 6. 過多 speed-ramp / fps 指示 | `72fps speed ramp, whip-pan cut` | Seedance 忽略、徒增 token | 選專用模型或刪掉 |
| 7. 多主體不分配位置 | `general + soldiers + banners + enemy` 無空間詞 | 所有 subject 都想擠中央 | 加 `in foreground/background`, `formation behind` |

**黃金框架（<80 字單鏡）：**
```
[時代/地點 setting] [主角 + chip 名] [主要動作 verb-ing]
[服裝 1-2 項] [武器/物件 1 項] [鏡頭角度 1 種]
[背景細節 1-2 項] [光線/色調 1 項] [photorealistic]
```

**本次修正範例：**
```
Ancient Chinese general Aria charging on galloping black warhorse 
through golden dawn battlefield, crimson cloak streaming, lamellar 
bronze armor glinting, jian sword slashing forward in sweeping arc, 
low-angle tracking shot, thick dust plumes kicked up by thundering 
hooves, two hundred soldier formation in background with fluttering 
battle banners, warm golden-copper sunset haze, photorealistic 
cinematic, shallow depth of field
```
~60 字、單一動作流、chip 觸發角色、無導演名、無技術 token 堆。

---

### 12.9.11 🔬 Seedance 正確 playbook（2026-04-21 社群研究證據版）

**前面 §12.9.9/10 是我初步推論，這節是跨 X/Threads/Reddit/小紅書/官方 cookbook 的研究證據。詳完整 playbook 見 [../../references/community-prompt-patterns.md](../../references/community-prompt-patterns.md)。**

#### 官方 8 維公式

`Subject + Action + Scene + Light + Camera + Style + Quality + Constraints`

前面我漏了 **Constraints tail**，這是 Seedance 的關鍵，見下。

#### 證據版 5 鐵則

1. **中文 > 英文 for 武打/古裝**（native multilingual encoder + 中文訓練 corpus 重）
2. **動作全部改慢** — "fast" 是最爛關鍵詞，改 `slow-motion / smooth / sustained / 慢動作 / 流暢 / 連貫`
3. **ONE verb per shot** — charging + swinging + slashing 三動詞會亂。想複雜 → 分 shot 用 `Cut to:`
4. **Constraints tail 必放**：`不抖動、不變形、不多肢、穩定地平線、穩定時間一致性` / `no shake, no warping, no extra limbs, locked horizon, stable temporal coherence`
5. **不要 chaotic wide 戰場** — 騎馬專 tip：低角度 tracking dolly 沿馬側跑 + dust 粒子 + locked horizon + 1 鏡慢動作

#### 戰鬥 three-beat（多鏡時）

```
Shot 1 (wide, 3s): 建立空間 + 角色位置
Camera cut to:
Shot 2 (medium tracking, 4s): 跟拍武打節奏
Camera cut to:
Shot 3 (close-up, 3s): 衝擊 / 呼吸 / 腳步特寫
```

#### Reference video cheat code

上傳 ≤15s 動作參考影片，prompt 寫 `imitate the movements of @video1` — 中國創作者公認武打最大 quality jump。

#### ✅ 針對 Aria 古代將軍的證據版 prompt（中文）

```
古代中國將軍 Aria 主角，身披金色鱗甲、紅披風在風中翻飛，
騎一匹黑色戰馬在黎明戰場上緩慢前行。
戰場中央地帶，遠處千軍列陣、紅色戰旗獵獵。
金色逆光、塵霧漂浮、熒光晨霧。
低角度手持 tracking 鏡頭沿馬側跟拍，輕微晃動、穩定地平線。
墨色留白東方美學、史詩寫實電影感。
慢動作、流暢、連貫、不僵硬、高清 720p。
不抖動、不變形、不多肢、穩定時間一致性。
```

~130 字，符合所有 5 鐵則 + 8 維公式 + Constraints tail。
