# Image-to-Video (i2v) Workflow — 先生圖再動畫化

**核心 paradigm shift（2026-05-19 確認）：** 任何「影片廣告」task，i2v 通常 > t2v。理由：

1. **成本控制** — 圖 7-15 STAR 可試多版，影片 210 STAR 一錘定音
2. **視覺一致** — 圖固定後，i2v 只負責「動」，不會幻覺出新角色 / 新場景
3. **客戶 approval flow** — 圖先給客戶看，approved 才燒影片預算
4. **多版本擴充** — 一張 hero 圖 → N 個 i2v 角度 / 鏡頭

**Source attribution：** 整合自 [`cliprise/awesome-image-to-video-prompts`](https://github.com/cliprise/awesome-image-to-video-prompts) + [`underwoodxie/promptsref-gpt-image-prompts`](https://github.com/underwoodxie/promptsref-gpt-image-prompts) + OiiOii 實戰（2026-05-19 球鞋廣告 session）。

---

## 🧠 i2v 的真正核心原則

**「i2v = motion prompting，不是 scene rebuilding」**

> In text-to-video, you describe the whole scene.
> In image-to-video, the image already gives the model: subject / composition / color palette / lighting / framing / style / background / visual hierarchy / mood.

所以 i2v prompt **只該寫**：
- camera movement（相機運動）
- subject motion（主體動作）
- environmental motion（環境動態）
- timing（時序）
- direction / speed（方向 / 速度）
- what must stay stable（什麼不能變）
- what must not happen（避免什麼）

❌ **不要重複圖已有的視覺元素**（顏色、構圖、燈光、風格、背景）— 浪費 token + 反而引發模型「干擾既有圖」的副作用。

---

## 📐 i2v 5-Part Prompt Formula

```
1. Preserve [important details that must NOT change]
2. Camera: [ONE primary movement]
3. Motion: [1-2 controlled scene elements]
4. Final beat: [ending frame description]
5. Avoid [common failure modes]
```

**範例（短版，單鏡 5-7s）：**

```
Preserve the product shape, label and lighting. Camera: slow push-in. 
Motion: soft steam rises and background lights move slightly. 
Final beat: product centered in a hero frame. 
Avoid text, logo distortion, shape changes and flicker.
```

**範例（長版，多鏡 15s）：**

```
Using the uploaded image as exact visual reference, create a 15-second 
horizontal product ad.
Preserve: exact product shape, color palette, label placement, lighting 
direction, and floor reflection. Product stays rigid.

[00:00-00:05] Camera: slow dolly-in from 3/4 hero angle. Motion: subtle 
highlight sweep across surface, reflection ripples in floor.

[00:05-00:10] Camera: 360-degree orbit clockwise revealing back and right 
profile. Motion: volumetric light beam rises from beneath, dust particles 
drift upward.

[00:10-00:15] Camera: pull-back to wide hero frame. Motion: background 
corner glow expands. Final beat: product rotates back to original 3/4 
position, frozen on iconic silhouette.

Sound design: low-frequency synth pad, soft whoosh transitions, sub-bass 
impact on final beat freeze.

Constraints: no text, no logo distortion, no shape changes, no extra 
products, no flicker, no warping, stable horizon, stable temporal 
coherence. ONE camera motion per shot.
```

---

## 🎨 5 種 source image 類型（決策樹）

### 1. Hero Shot（單一主視覺）— 廣告最常用

**用途：** 產品廣告、人像廣告、品牌主視覺

**圖該長怎樣：**
- 單一主體置中或黃金比例
- 乾淨背景（漸層 / 純色 / 簡單環境）
- 完整 lighting 已設定好
- 留 negative space 給文字 / logo（後期可加）
- 鏡頭角度 = 你想做影片時的「起始角度」

**GPT-Image2 prompt 範本：**
```
Premium {BRAND}-style {PRODUCT} product photography hero shot, {ASPECT} composition. 
Single {PRODUCT_DESCRIPTION} {POSITIONING (floating/levitating/standing)} {SURFACE}. 
Studio lighting: {DIRECTION 1}, {DIRECTION 2}, {VOLUMETRIC_GLOW}. 
Background: {GRADIENT/COLOR}. 
Camera angle: {3/4 hero front / extreme close-up / overhead / etc.}, {high/low/eye-level} angle. 
Hyper-detailed: {SURFACE TEXTURE 1}, {SURFACE TEXTURE 2}, {LOGO/LABEL}. 
Style: editorial luxury, Apple-product reveal aesthetic, 8K, photorealistic, 
no text, no watermark, ultra-clean composition with negative space on {SIDE}.
```

**對應 i2v：** 單鏡 5-10s push-in / orbit / pull-back

### 2. Storyboard（分鏡圖，3-12 frames grid）

**用途：** 多鏡敘事影片、分鏡確認、客戶 brief 對齊

**圖該長怎樣：**
- 2×3 / 3×4 / 3×3 grid 排版
- 每 frame 對應一個 shot
- 每 frame 有微小 caption（或無 caption）
- 風格全 grid 統一

**GPT-Image2 prompt 範本：**
```
Create a high-end {ASPECT} storyboard pitch deck in {3×4} grid (12 frames), 
editorial layout, {STYLE_REFERENCE (Wes Anderson / Bloom & Wild / etc.)} aesthetic, 
{COLOR_PALETTE}. Structured flow: {ACT1} → {ACT2} → {ACT3} → {CLOSURE}. 
Each frame split: top cinematic image + bottom storyboard notes. 
{ART_DIRECTION_TERMS}, fleeting perfection mood. 
A single {EMOTIONAL_CENTER} runs through all frames as anchor.
```

**對應 i2v：** Step 2 — 把 storyboard 整個丟給 video model，prompt 寫「animate the provided {N}×{M} storyboard into a smooth cinematic video. Preserve exact shot order and continuity. Use {MOTION_TYPE 1}, {MOTION_TYPE 2}, {MOTION_TYPE 3}. {LIGHTING_TRANSITION}. No new shots, no reordering.」

範例 → 見 [preset-packs.md §Luxury Botanical Storyboard](../templates/preset-packs.md)（Seedance 2.0 證實此 workflow 有效）

### 3. Concept Board / 視覺示意圖（schematic）

**用途：** 抽象產品說明、流程展示、SaaS UI 動畫、建築 diagram

**圖該長怎樣：**
- 多元素組合 layout（左圖 / 中圖 / 右圖 / annotation）
- 帶數字 / 標籤 / 箭頭 / dimension
- 風格：technical drafting / blueprint / architectural board

**GPT-Image2 prompt 範本：**
```
An expert {DOMAIN} designer's presentation board for {SUBJECT}, 
featuring {LEFT_PANEL} on the left, {CENTER_PANEL} in the center, 
and {RIGHT_PANEL} on the right, with {LIGHTING_AMBIANCE}. 
Visual style transitions from {COLOR1} to {COLOR2}, 
clean grid layout, {STYLE_TIER (museum-grade / industrial / editorial)} 
presentation, ultra-detailed cinematic realism, 
title block reading "{TITLE}".
```

**對應 i2v：** 短 i2v 7-10s — 「camera slowly pans across the board left-to-right, lights pulse on highlighted elements, subtle particle motion in background」

### 4. Character Sheet（角色設計圖）

**用途：** 動畫主角、品牌吉祥物、遊戲角色

**圖該長怎樣：**
- 同一角色 3-5 個角度（front / side / back / 3/4 / detail）
- 統一服裝 / 表情 / 比例
- 中性背景（白色 / 灰色）

**GPT-Image2 prompt 範本：**
```
Character design sheet for {CHARACTER_NAME}: 
{CHARACTER_DESCRIPTION (age, gender, ethnicity, build, hairstyle, outfit, accessories)}. 
Layout: front view (center-left), 3/4 view (center-right), side profile (right), 
extreme close-up of face (top), full back view (bottom). 
Style: {ART_STYLE}, neutral gray studio background, soft even lighting, 
consistent proportions across all views, model sheet aesthetic, 
clean line work, vibrant color hold.
```

**對應 i2v：** 「animate the front view rotating 360 degrees, hair and clothing react naturally, expression cycles through {EMOTIONS}」

### 5. Mood Board（風格參考板）

**用途：** 風格 lock-in、客戶 alignment、創意 pitch

**圖該長怎樣：**
- 6-12 小圖 collage / Pinterest-style grid
- 主題色 / 質感 / 構圖 references
- 中央可能有 hero shot + 周圍 supporting elements

**GPT-Image2 prompt 範本：**
```
Mood board for "{CAMPAIGN_NAME}" — premium editorial collage. 
3×4 grid containing: hero portrait (center, 2×2 cells), 
texture macro shots (3 cells), color swatches (2 cells), 
location photography (3 cells), product detail (2 cells). 
Cohesive {COLOR_PALETTE} palette, {TYPOGRAPHY_NOTE if relevant}, 
{ERA_REFERENCE (90s editorial / Y2K / mid-century / etc.)} aesthetic. 
Magazine-spread layout, paper texture, subtle drop shadows between tiles.
```

**對應 i2v：** 「animate the mood board with subtle motion — hero portrait blinks naturally, texture macros shift in light, color swatches pulse slightly. Camera holds static. Final beat: hold on hero portrait close-up.」

---

## 🎬 Per-Platform i2v 簽名（基於 v1.3.0 community evidence）

### Seedance 2.0 pro i2v

- **支援：** OiiOii 自由畫布內，直接在 prompt 內引用「資產 N」即可
- **格式：** `[i2v 起始幀] 以資產 N 為起始幀 [比例] 16:9 [時長] 15 秒 + 5-part formula`
- **甜蜜點：** 多鏡 200-500 字，bracketed labels 完整套
- **特殊強項：** 動態粒子 / volumetric 光束 / 反射波紋特別強
- **禁忌：** 不要重述圖中已有的顏色 / 構圖

### Kling 3.0 i2v

- **格式：** 短句 40-80 字 + 鏡頭詞為主
- **甜蜜點：** 「camera tracks {direction}, subject {action}, environment {motion}」三句結構
- **特殊強項：** 人物表情 / handheld 真實感
- **禁忌：** stacking 多個相機運動

### Veo 3.1 i2v

- **格式：** 自由文本 OR JSON-structured（v1.3.0 新發現）
- **JSON 格式 i2v：**
  ```json
  {
    "source": "uploaded_image_as_first_frame",
    "camera": {"movement": "slow dolly-in", "duration": "0-5s"},
    "motion": {"subject_action": "rigid product, no shape change", "scene": "highlight sweep + reflection ripple"},
    "audio": {"sfx": "soft whoosh", "ambient": "low synth pad"},
    "constraints": ["no text", "no logo distortion", "stable horizon"]
  }
  ```
- **特殊強項：** 原生音訊（SFX + Ambient + Dialogue）

### Sora 2 i2v

- **格式：** Shot-list briefing a cinematographer，第一句 anchor 圖
- **第一句範本：** `Using the uploaded image as the exact starting frame, ...`
- **甜蜜點：** 40-100 字
- **特殊強項：** Format anchor + 對白 lip-sync
- **禁忌：** 對話式語氣

### Runway Gen-4 / Aleph i2v

- **格式：** **最短** — 25-60 字
- **範本：** `Starting from the uploaded image, {ONE_VERB} {direction}. {1 lighting/motion modifier}.`
- **強項：** Aleph 可對既有影片 re-light / re-frame
- **禁忌：** synonym drift、>60 字

### Hailuo / Wan i2v

- **Hailuo：** `[Camera Shot + Motion] + [Subject preserve] + [Lighting]`，30-60 字
- **Wan 2.6：** 中文 multi-shot Shot block，每 shot anchor-noun 一致

---

## ✅ Source Image Preparation Checklist

**Source 圖弱 → 影片必弱。** 上傳前自檢：

- [ ] 明確主體（一眼看出 hero 是什麼）
- [ ] 構圖穩定（沒有歪扭）
- [ ] 乾淨邊緣（沒 stray pixels）
- [ ] 良好照明（沒過曝 / 死黑）
- [ ] 背景單純（不喧賓奪主）
- [ ] 足夠深度（前 / 中 / 後景區分，i2v 才有縱深可動）
- [ ] 無假文字（會 distort）
- [ ] 無小到難辨識的 label / logo
- [ ] 無扭曲的手 / 臉
- [ ] 無 motion blur 殘留（會被誤讀為運動方向）
- [ ] 無 oversharpened artifacts
- [ ] aspect ratio 接近最終輸出（避免 i2v 強制裁切）

---

## 🎯 i2v 強項 vs 弱項

### ✅ Strong use cases（i2v 必選）

- 產品廣告 / e-commerce
- Social media 短片
- AI art 動畫化
- 唱片封面 motion
- 時尚 lookbook
- 房地產 teaser
- 美食慢動作
- App promo
- SaaS hero video
- UGC-style 產品 clip
- Cinematic establishing shot
- Thumbnail-to-video
- 簡單角色動畫
- 一圖多片活動（1 hero → 8 social variants）

### ⚠️ Risky use cases（建議用 t2v 或 Wan 2.6 multi-shot）

- 長動作序列（>15s 複雜動作）
- 複雜人群
- 精細手部操作
- 嚴格 lip sync
- 細小可讀文字
- 複雜物理（破碎 / 流體 / 衝撞）
- 多角色 choreography
- 中途換衣 / 換身分
- 必須完美的產品 label
- 一鏡到底長片
- 政治敏感 / 名人肖像

---

## 🚀 完整 i2v workflow（OiiOii 自由畫布實戰版）

按 [oiioii.md §12.10](../automation/site-profiles/oiioii.md) 自由畫布 SOP，**i2v 是 10-batch 流程**（含右鍵加入對話那一步）：

```
=== 階段 A：生圖（5-batch）===
1. navigate /home + click 最近項目第二張 進 saved workspace
2. click 模型 chip → 切「圖片」tab → 選 GPT-Image2 (Best)
3. click prompt input → type GPT-Image2 hero shot prompt → screenshot
4. click send → wait 60s
5. screenshot 驗收 hero 圖

=== 階段 B：轉影片（5-batch）===
6. click 模型 chip → 切「影片」tab → 選 Seedance 2.0 pro
7. click 設定 → reset 比例 16:9 + duration 15s + 解析度 720p
8. 🔴 **右鍵 canvas 上的 hero 圖 → 選「加入對話」** ← 關鍵！圖會 attach 到 prompt 區
9. click prompt input → type i2v prompt（5-part formula：Preserve / Camera / Motion / Final / Avoid，**不要寫「資產 N」**，因為圖已經 attach）→ click send
10. background sleep 480s → 驗收 i2v 影片
```

⚠️ **絕對不要漏掉 step 8**（右鍵加入對話）— 跳過會走 t2v 路徑，造型歪、運鏡爛、無 image-anchor 質感。

**成本：**
- 階段 A：7 STAR（GPT-Image2，~NT$1.7）
- 階段 B：210 STAR（Seedance 2.0 pro 15s，~NT$50）
- **總計：217 STAR ≈ NT$52**
- 對比純 t2v：210 STAR ≈ NT$50

**多花 NT$2，買的是：**
1. 客戶確認 hero 圖 的機會
2. 失敗重做時，只重做影片（210）不用重做圖（7）
3. 風格 lock — 影片 100% 對齊 hero 視覺
4. 一張圖可衍生 N 個 i2v variants（每個 +210，但 image 成本攤平）

---

## 🆕 OiiOii 自由畫布 i2v 探索進度（2026-05-19，兩次失敗）

### ⛔ 兩個流程都實測 broken — 真正 i2v 操作仍待驗證

| 版本 | 我寫的「正解」 | 實測結果 |
|---|---|---|
| **v1.4.0** | prompt 內提「資產 N」讓 agent 自動關聯 | ❌ 鞋子造型歪、走 t2v 路徑 |
| **v1.4.1** | 右鍵圖 → **加入對話** | ❌ 「鞋子完全不同」（用戶 2026-05-19 報告）|

兩次都把「以為」當「正解」寫進 skill，兩次都被打臉。共燒 ~420 STAR ≈ NT$100。

### 🔍 失敗原因推測

**「加入對話」可能只是把圖加進 LLM agent 的 chat history**（讓藝術總監知道你想做球鞋廣告），**沒真的把圖檔注入 Seedance 的 i2v API endpoint**。

藝術總監看到圖 → 理解 user intent → 寫 prompt 給 Seedance → 但 Seedance 收到的仍是純文字 → 走 t2v 生成 → 鞋子當然不一樣。

### 🎯 待驗證的真正 i2v 觸發點

回看 canvas 右鍵 context menu 7 個選項：

| 選項 | 推測用途 | 驗證狀態 |
|---|---|---|
| **✏️ 生成影片** | **真正的 i2v 直接觸發**（最大嫌疑）| ⏳ 未測 |
| 🖼 生成圖片 | i2i 模式 | ⏳ 未測 |
| 反推提示詞（4 STAR）| Image → prompt 反推 | ⏳ 未測 |
| 💬 加入對話 | 只丟給 agent 看，**不鎖 i2v** | ❌ 已測，broken |
| 複製 (Ctrl+C) | 標準 | — |
| 下載 | 標準 | — |
| 刪除 | 標準 | — |

**下次嘗試：先試「✏️ 生成影片」option** — 應該會直接開 i2v 工具列，設參數後送。預期它會真正把圖檔當起始幀。

### 待驗證的其他可能機制（如果「生成影片」也失敗）

1. **拖拉圖到 prompt input** — 之前 drag 是 pan canvas，但可能還有其他 drop zone
2. **+ 按鈕 → 選擇圖片** + 從本地上傳 — 強制走 file upload 路徑，可能才能真 attach
3. **點圖選中 → 出現 floating action bar** — 還沒探索過
4. **canvas 上 frame 的「+ 替換」icon** — 可能是替換 ref slot 而非當前圖
5. **不切換到 Seedance 2.0 pro，保留 智能模型** — 讓 agent 自己決定 i2v
6. **canvas 上拉一條線從圖到 prompt area** — node-graph 風格的關聯（OiiOii canvas 是 tldraw 風）

### 📌 教訓（baked 進 memory）

寫進 `feedback_verify_before_documenting.md`：**未實測完整 UI options 不要把「以為」寫成 SOP**。每個 context menu / 按鈕 / 操作要實際走一遍，看 model 真實輸出，才能寫進 skill。否則就是「自吹自擂式 v1.x.0 → 打臉 → v1.x.1 → 再打臉」的循環。

### 暫時 SOP（保守版，待真正 i2v 驗證後更新）

```
1. 生 hero 圖（GPT-Image2 / Nano Banana 等）
2. 確認生成滿意（如果不滿意先 redo image，再考慮 i2v）
3. 🚧 i2v 觸發方式待驗證：右鍵 → 「生成影片」是最有可能的真正觸發點
4. 不要再相信「加入對話」這個選項作為 i2v 機制
```

### 2. canvas 上的 frame 可被 drag-move（會破壞 layout）

如果意外 drag 了 canvas 上的 frame，不要慌 — 不影響 asset 引用。「資產 N」的索引獨立於 canvas layout。

### 3. + 按鈕 = 本地檔案上傳（非 canvas asset 引用）

prompt input 左下的 `+` 按鈕只能上傳**本地圖檔**（.jpg .png .jpeg）。要用 canvas 上的 GPT-Image2 圖，**走「資產 N」prompt 引用**。

### 4. 「我想修改」flow reset 所有 settings（不只 duration）

確認 §12.10.2 #2 更新：「我想修改」每次 reset：
- duration → 10s
- 比例 → 可能變 1:1（非預期）
- 解析度 → 通常保留 720p
**永遠在送出前重新確認三項都對。**

### 5. 風格庫 panel popup 觸發點

如果不小心點到 `ref_234`（或附近按鈕），會 popup「風格庫」panel。**按 Escape** 關掉，不影響 state。

---

## 📋 i2v vs t2v 決策樹

```
任務是「廣告」？
├─ 是 → i2v（成本控制 + 客戶 approval）
└─ 否 → 看以下：

需要客戶先看 hero 視覺？
├─ 是 → i2v
└─ 否 → 看以下：

風格極致細節要求（特定品牌 / 美術指導鎖定）？
├─ 是 → i2v
└─ 否 → 看以下：

預期會做多個 variants（不同角度 / 9:16 + 16:9）？
├─ 是 → i2v（一圖 N 影片）
└─ 否 → 看以下：

任務是「長故事 / 多角色互動」（>15s + 多場景）？
├─ 是 → t2v + Wan 2.6 multi-shot
└─ 否 → t2v + Seedance 2.0 pro 多鏡（210 STAR 直接燒）
```

---

## 🔗 延伸資源

- [community-prompt-patterns.md](community-prompt-patterns.md) — per-platform i2v 簽名 token
- [oiioii.md §12.10](../automation/site-profiles/oiioii.md) — OiiOii 自由畫布操作 SOP
- [preset-packs.md](../templates/preset-packs.md) — Storyboard / Hero shot 範本
- [external-resources.md](external-resources.md) — Upstream prompt repos catalog
- [`cliprise/awesome-image-to-video-prompts`](https://github.com/cliprise/awesome-image-to-video-prompts) — 原始 i2v 研究參考
- [`underwoodxie/promptsref-gpt-image-prompts`](https://github.com/underwoodxie/promptsref-gpt-image-prompts) — GPT-Image2 prompt 範本
