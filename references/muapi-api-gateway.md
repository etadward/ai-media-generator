# MuAPI API-Gateway（瀏覽器自動化的 API 備援）

> 本 skill 目前 **100% 靠瀏覽器自動化**（`automation/site-profiles/{kling,flow,oiioii,…}.md`），任一平台改版 / login-gated / 不穩就整條斷。MuAPI 是同模型覆蓋的 **API 備援路徑**，當某平台瀏覽器 UI 卡住時改走它。**定位是 fallback，不是取代**。

## 是什麼

[MuAPI.ai](https://muapi.ai) 是一個 unified gateway：單一 `x-api-key`、統一的 submit→poll 契約，覆蓋 **200+ 個生成模型**（Google / ByteDance / xAI / MiniMax / Runway… 等多家），呼叫端不需要每家各自的 SDK。涵蓋 Nano Banana 2 / Seedream / Seedance / Veo / Kling 等本 skill 已用的主力模型。

## 怎麼用（submit → poll）

```
# 提交（model-endpoint 依目標模型，見 muapi.ai 文件）
POST https://api.muapi.ai/api/v1/{model-endpoint}
  Header: x-api-key: <KEY>
  Body: { prompt / image / 參數... }
  → 回 { request_id }

# 輪詢直到 completed
GET https://api.muapi.ai/api/v1/predictions/{request_id}/result
  Header: x-api-key: <KEY>
  → status: pending | completed | failed；completed 時帶輸出 URL
```

**金鑰走 OpenClaw 後端 / .env，不寫進對話**（依 Security Baseline：secret ingress/egress）。不要把 `x-api-key` 印進 transcript 或外送通道。

## 何時切過來（trigger）

- 某平台瀏覽器 profile 連續失敗（login wall / DOM 改版 / anomaly flag 擋住）且短期修不動。
- 需要批次 / 無人值守生成，瀏覽器分頁掛著不可靠時。
- 需要某個瀏覽器路徑做不到的模型，而 MuAPI 有覆蓋。

## Trade-off（為何是備援不是預設）

- MuAPI 是**付費計量** gateway（access key、per-generation 收費），且把模型覆蓋綁在單一 vendor；而你已付費的平台走瀏覽器自動化是「使用當下免額外付費」。
- 因此預設仍走瀏覽器自動化（省錢），**只在瀏覽器路徑 flaky 時**切 MuAPI。兩條路並存。

## 長任務韌性

影片 / lipsync 動輒數分鐘：提交後**存下 `request_id`**，session / 分頁掛掉也能重新輪詢接回，不要假設提交當下的 session 全程存活（見 [templates/auto-pilot.md](../templates/auto-pilot.md) Stage 7 的 request_id 持久化慣例）。

---

來源：評估 `Anil-matcha/Open-Generative-AI`（2026-06-16，Partial Adopt）。該 app 本體屬消費級媒體生成（Reference Only），但其 unified-gateway + submit→poll→persist→resume plumbing 對本 skill 的「無 API fallback」缺口是具體加值。完整評估見 `memory/draft/reference_open_generative_ai.md`。
