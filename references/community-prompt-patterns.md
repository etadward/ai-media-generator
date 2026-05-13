# Community-Validated Prompt Patterns (研究證據版)

**Source:** 2026-04-21 三 agent 平行研究（X/Threads/Reddit/小紅書/Bilibili/官方 cookbook + fal.ai / Google Cloud / OpenAI Cookbook 等）
**用法：** 任何時候生 prompt 前先查這檔找目標模型的**簽名 token + 長度甜蜜點 + 禁忌**。

---

## ⭐ 跨模型 5 條 META rule（通吃）

1. **鏡頭詞彙是通用貨幣** — `35mm / 85mm / dolly / handheld / low-angle / rack focus / teal-orange` 幾乎所有模型都吃（MJ/Flux/Nano/Sora/Veo/Seedance/Kling/Runway）。想要寫實感就一定用。
2. **Subject 放最前 10-15 token** — 所有模型都 early-weight 開頭。"ancient Chinese general" 一定 BEFORE "in battlefield fog"。
3. **導演名分裂** — 不是所有模型都吃：
   - ✅ 吃：MJ v7、SDXL、Sora 2、Veo 3.1
   - ❌ 刷掉：Flux（BFL 訓練時 scrubbed）、Nano Banana Pro
   - ⚠️ 不穩：Ideogram、Seedance（弱證據）、Kling（可能 over-weight 出現 "in the style of" artifact）
   - **對策**：中文模型（Seedance / Wan / Hailuo）改用具體視覺詞（墨色、留白、金色逆光、大遠景、慢鏡頭）
4. **ONE verb per shot** — 兩個以上動詞 = 模型自選 = 混亂。Seedance 特別嚴重（"combining two motion verbs makes the model choose chaos"）。想要複雜動作？分 shot 用 `Cut to:`。
5. **Anchor-noun 字串一致** — 多鏡頭時同一物件用**完全相同的名稱**。"olive sweater" 不能下一鏡變 "green knit" — Runway、Wan 會 break。

---

## 🎥 影片模型 per-model 簽名

### Seedance 2.0 pro / 1.5
- **結構：** 8 維 — Subject + Action + Scene + Light + Camera + Style + Quality + **Constraints**
- **長度：** 60-100 字（useful 30-200）
- **簽名 token：**
  - 鏡頭：`low-angle circling`, `over-shoulder counter`, `lateral whip-pan`, `snap zoom on impact`, `handheld shake`, `orbit 環繞`, `tracking 跟拍`, `特寫衝擊`
  - 語氣：中文武打/古裝寫中文 > 英文（native multilingual encoder）
  - 物理詞：`realistic weight transfer, momentum, recovery` > "powerful"
  - 視覺：`sword light trails, splashing water, flying rubble, sparks, shockwaves`
- **Constraints tail（必放）：** `no shake, no warping, no extra limbs, locked horizon, stable temporal coherence`
- **禁忌：**
  - ❌ "fast" — 最爛關鍵詞，degrades quality。改 "slow-motion / smooth / sustained"
  - ❌ 多動詞同句（charging + swinging + slashing = 災難）
  - ❌ 多主體獨立動作（A 打 B 閃 C 射 → 三者都 fail）
  - ❌ 負面 prompt `--no blur`（不支援）
  - ❌ chaotic wide 戰場 → 失敗率最高
  - ❌ 英文導演名（Kurosawa-style）— 弱證據
- **戰鬥 three-beat**：wide 建立間距 → medium 跟拍節奏 → close-up 衝擊/呼吸/腳步
- **騎馬專 tip：** 低角度 tracking dolly **沿馬側**跑 + dust/steam 粒子 + locked horizon + 1 鏡慢動作（不要 chaotic wide cavalry charge）
- **Reference video cheat：** 上傳 ≤15s 動作參考 + prompt 寫 `imitate the movements of @video1` — 中國創作者公認武打最大 quality jump

### Kling 3.0 / 2.1（快手）
- **結構：** Scene → Characters → Action → Camera → Audio
- **長度：** 40-80 字（comma-separated film-crew shorthand）
- **簽名 token：** aspect ratio 後綴 `16:9 / 2.39:1`、`35mm handheld`、`85mm`、`Steadicam weaving`、`whip pans`、`rack focus`、`teal-orange grade`
- **中文 vs 英文：** 平手無明顯差
- **禁忌：** >4-5 distinct nouns break it；"slow motion" 放負面 prompt 沒用；stacking 相機運動

### Sora 2（OpenAI）
- **結構：** Shot-list briefing a cinematographer
- **長度：** 40-100 字
- **簽名 token：**
  - **Format anchor**（Sora 最強）：`bodycam`, `surveillance`, `ring doorbell`, `TED Talk stage`
  - 冒號對白：`Detective: "You're lying."`
  - 光線方向明確：`warm key from left, cool rim from neon`
  - 語氣詞：`professional`, `deadpan`, `dramatic`
- **Trick：** 2×4s stitched > 1×8s（官方 cookbook 推薦）
- **禁忌：** 會話語氣 ("please make")、模糊形容詞、over-direct physics

### Veo 3.1（Google Flow）
- **結構：** [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]
- **長度：** 1-2 句 simple / 4-8 複雜 / timecode blocks 150+ 字
- **簽名 token（唯一 load-bearing audio）：**
  - `SFX: rustle of leaves, distant bird calls`
  - `Ambient: swelling orchestral score`
  - 對白用 `"quoted"`
  - Timecode：`[00:00-00:02] Medium shot from behind ...`
- **禁忌：** 負面 `no buildings` → 反寫 `desolate landscape`；under-specified camera；5+ SFX lines

### Runway Gen-4 / Aleph
- **結構：** 主角-動作-相機 子句
- **長度：** **25-60 字（最短）**
- **簽名 token：** `camera tracks from behind`, `trailing position`, **Novel View verbs**（`reverse shot`, `low angle`, `medium full shot`）
- **Aleph 特色：** 可對既有影片下 re-light / re-frame 指令
- **禁忌：** conversational greeting、synonym drift、stacking camera moves

### Hailuo 2.3（MiniMax）
- **結構：** [Camera Shot + Motion] + [Subject] + [Action] + [Scene] + [Lighting] + [Mood]
- **長度：** 30-60 字
- **簽名 token：** hyphenated 相機動詞 — `walk-right`, `pan-down`, `static shot`, `dolly zoom`；perspective `bird's eye view / macro view`
- **強項：** micro-expressions、ink-painting / CGI stylizations
- **禁忌：** 多主體 blocking（2.3 仍偏 single-subject）、dense 英文、abstract concept

### Wan 2.6 / 2.7（阿里通義萬相）
- **結構：** `Shot N (label, Ns): ...` 區塊；支援 up to 15s + native audio
- **長度：** 20w（with `prompt_extend=true`）or 60-120w 結構 shot list
- **簽名 token：** shot block、camera verbs (`track`, `push-in`, `orbit`)、**anchor 重複**嚴格
- **中文 > 英文** — 明顯優勢（native Alibaba 中文訓練）
- **禁忌：** synonym drift、maximum motion（slow push-in > whip pans）、too many beats per shot

---

## 🖼 圖片模型 per-model 簽名

### Midjourney v7
- **結構：** `[subject], [5-8 details], [lighting], [camera/lens], --ar X:Y --stylize N --style raw --sref/--oref`
- **長度：** 30-60 comma chips
- **Params：**
  - `--ar` 3:4/9:16/16:9
  - `--stylize 60-150` 寫實 portrait / 400-750 fantasy
  - `--style raw` 給寫實用，消 MJ house style
  - `--chaos 0-25`、`--exp 5-25`（v7 新）
  - `--sref` 風格 ref + `--sw 50-500`
  - `--oref` 角色 ref + `--ow 100`
- **範例（古代戰士）：**
```
cowboy shot, realistic, male warrior, ancient chinese, beard, long black hair, han_armor, chinese_armor, battleground, volume fog, cinematic pose --ar 97:128 --style raw --stylize 750
```
- **禁忌：** 長散文、`--stylize 1000 --chaos 100` 同開（mush）、`--style raw` 配 "artistic/dreamy"（自相矛盾）

### Nano Banana Pro / Nano（Gemini 3 Pro Image）
- **結構：** 自然段落，director-style 敘事
- **長度：** 80-150 字
- **簽名：**
  - `"quoted text"` = 字面渲染
  - **多圖 reference = superpower**（直接描述組合）
  - NO `--params`
- **禁忌：** 10-字短 prompt under-deliver、`--ar` 語法會被忽略

### Flux 1.1 Pro / Kontext
- **結構：** 長自然段 + 攝影技術詞
- **長度：** 80-200 字
- **簽名：** `Kodak Ektachrome 64 cross-processed`, `35mm spherical lens at f/5.6`, `Dappled forest light at 1/125`
- **Kontext edit：** `"Change her hairstyle to ..., maintain the exact same character and facial features"`
- **禁忌：** **Artist names 無效**（BFL 訓練時刷掉）、`--ar` 語法不支援

### Ideogram 3
- **結構：** `[scene], "quoted text" in [font] typography, [style]`
- **長度：** 40-80 字
- **簽名：** `"text"` 字面渲染（早放）、style preset (Auto/Realistic/Design/3D/Anime)
- **禁忌：** >5 字文字會 degrade、quoted text 放 prompt 尾

### Seedream 5.0 / 4.5（字節跳動）
- **結構：** 重要詞在前（early-weight）
- **長度：** 30-100 字
- **反直覺：** **英文 > 中文 for photoreal**；但中文 prompt 做中文字渲染更準
- **範例：**
```
Corporate headshot of a middle-aged Asian businessman, navy suit, neutral gray background, soft box lighting from 45-degree angle, sharp focus on eyes.
```

---

## 🎯 跨模型 workflow 組合（實戰）

### 寫實戰鬥短片（當前 use case）
1. **Nano Pro / Midjourney v7 + your character ref** → 生 key frame 圖（含武打氛圍）
2. **Kling 3.0 / Sora 2 / Veo 3.1** 用該圖做 i2v
   - Kling：40-80 字、handheld + whip pans
   - Sora 2：format anchor (`bodycam footage of ancient battle`)
   - Veo 3.1：加 `SFX: horse hooves, steel clash` + `Ambient: battle drums`
3. 需要更長敘事 → Wan 2.6 multi-shot `Shot 1/2/3` 結構（中文寫）

### 電商產品 15s
1. Nano Banana Pro 多圖（產品 + 背景 + 模特）
2. Veo 3.1 用圖做動畫 + SFX

### Poster / Logo（要文字準確）
1. Ideogram 3 `"PRODUCT NAME" in art deco typography`
2. 需要多語言文字（中日）→ 用該語言寫 prompt

---

## 📌 重要踩坑記（2026-04-21 實戰驗證）

1. **Seedance 英文戰鬥 prompt = 失敗** — 4 shot 擠 15s、導演名堆、fast 動詞、chaotic wide → 效果差
2. **修正方向**：中文 + 8 維公式 + 單鏡單動詞 + Constraints tail + 低角度跟馬側
3. **Cost 預覽 sanity check**：Seedance 15s pro = 210，10s = 140。顯示 140 → duration 被 reset
4. **"我想修改" flow 會 reset duration** → 一律用底部 prompt 工具列 settings 手動設

---

## 🔗 Sources（研究時的權威站）

- OpenAI Sora 2 Prompting Guide Cookbook
- Google Cloud - Ultimate Veo 3.1 Guide
- Runway Gen-4 / Aleph Prompting Guides
- fal.ai Kling 3.0 / Wan 2.6 / Seedream 4.5 prompt guides
- BFL Flux Kontext docs
- Ideogram prompting docs
- Midjourney v7 official docs (docs.midjourney.com)
- Google Cloud Nano Banana Ultimate Prompting Guide
- Atlas Cloud Seedance Library
- awesome-seedance-2-prompts (GitHub)
- 知乎 / 腾讯新聞 / CSDN 即夢 Seedance 官方手册全拆解
- Bilibili 鏡頭語言提示詞教學
