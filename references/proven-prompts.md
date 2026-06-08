# 經驗證 Prompt 庫 (Proven Prompts) — 可直接複製貼上

**定位：** 不用從零寫。這裡是 2026 從**官方 + 社群**挖出、經來源驗證、**逐字可貼**的高品質 prompt，按用途分類。每個標：情境 ｜ 模型 ｜ 全文 ｜ 為何好 ｜ 來源。

> 用法：找最近的 → 換主體/品牌/色盤 → 貼到目標平台。配合 [concept-first-prompting.md](concept-first-prompting.md)（先有概念）+ [quality-control.md](quality-control.md)（反瑕疵）+ [model-picker.md](model-picker.md)（選對模型）。

## 🔑 廣告 prompt 黃金結構（多來源共識）

`Subject 主體(外觀/材質具體) → Action 動作(拆 beats 不寫摘要) → Setting 場景(時間/光/背景) → Camera 運鏡(orbit/truck/crane/rack focus/macro push-in) → Style 風格(打光名詞+色盤+"commercial")`

**打光語彙 = 廣告片靈魂（高價值 token）：**
- `rim lighting` — 飲料/香水把畫面拉成 3D
- `Chiaroscuro / high-contrast` — 汽車/科技
- `single dramatic spotlight + pure black background` — 精品錶/珠寶
- `golden hour / warm grade` — 美食/生活感

---

## 🍔 美食 / 飲料（食慾感）

**漢堡空中組裝（Kling 3.0 / 通用）**
```
A static shot of a burger as it assembles in mid-air. The entire shot is in dramatic slow-motion. The individual ingredients—a grilled patty, fresh lettuce, tomato, melting cheese, and a toasted bun—fly into place from different directions. The background is a clean, simple, professional studio gradient to keep the focus on the product. Style: TV food commercial.
```
*為何好：mid-air 組裝 + 慢動作經典食慾結構，乾淨棚拍鎖焦點。｜來源 leonardo.ai/news/kling-ai-prompts*

**牛排煎鍋微距 sizzle（Veo 3，ASMR 原生音）**
```
Extreme close-up of a cast-iron pan as butter foams and a steak sears, with macro steam and micro bubbles under overhead practical light with a warm grade. Sizzle and soft kitchen clatter sounds, no dialogue.
```
*為何好：微距+奶油起泡+蒸氣把「滋滋聲」視覺化，Veo 原生 sizzle 音效直接 ASMR。｜來源 skywork.ai/blog/best-veo-3-prompts-2025*

**早餐爆炸重組（Veo 3，三幕病毒公式）**
```
High-definition, cinematic food photography, vibrant and rich textures, golden hour lighting, appetizing and luxurious. Scene 1 (0-2s): A pristine glass jar of chocolate-hazelnut spread sits invitingly on a rustic, weathered wooden table. Scene 2 (2-5s): In breathtaking super slow motion, the jar dramatically bursts open. A vibrant explosion of rich spread, whole roasted hazelnuts, golden-brown toast slices, and glistening fresh red strawberries erupts outwards. Scene 3 (5-8s): With a final flourish, all the scattered ingredients gracefully converge and assemble themselves into a perfectly composed breakfast platter.
```
*為何好：陳列→爆炸→倒放重組三幕，視覺衝擊高。｜來源 veo3promptwriter.com*

**馬丁尼/調酒懸浮（通用 / Veo，飲料 rim light）**
```
Ultra-realistic cinematic video of a martini glass slowly rotating while liquid flows naturally inside. A green olive and a spiraling citrus peel remain suspended as bubbles rise through the drink. Rim lighting separates the glass and splash from a dark background, creating a thin line of light around the edge. Crown splash droplets freeze in mid-air. Macro detail, premium beverage commercial.
```
*為何好：rim lighting 把畫面拉成 3D，懸浮橄欖+crown splash 凍結是高轉換飲品視覺。｜來源 banana-prompts.net*

**咖啡晨間儀式（Veo 3，rack focus 情境）**
```
Coffee being poured from a French press into a ceramic mug in slow motion. Steam rises from the cup. The camera racks focus from the pour to a laptop screen showing email in the background. Morning work ritual. Warm tones, shallow depth of field.
```
*為何好：rack focus 把產品和情境一鏡串起，慢動作蒸氣+暖調生活感。｜來源 simplified.com*

---

## 🚗 汽車 / 精品 / 產品 Hero

**超跑鹽湖高速跟拍（Kling，速度感）**
```
The camera trucks (moves laterally) at the same high speed, perfectly parallel to the car and its driver. The car stays locked in the center of the frame. In the second half of the shot, the car executes a quick, slight S-curve maneuver, kicking up a small plume of white salt dust from its tires. The camera perfectly mirrors this S-curve. Cinematic, car commercial, high-energy.
```
*為何好：truck 鏡頭 + 車鎖中心 + 鏡頭 mirror S 彎是汽車速度感核心技法。｜來源 leonardo.ai/news/kling-ai-prompts*

**電動車雨夜大燈揭幕（通用 / Seedance / Veo）**
```
Create a 5-second cinematic product reveal for a minimalist matte black electric car. Start with an extreme macro shot of the LED headlight flickering on in a dark, rain-slicked studio. Execute a slow, sweeping crane shot upward to reveal the car's silhouette. Use high-contrast "Chiaroscuro" lighting with cold blue accents. Ultra-realistic textures, 4K resolution, 60fps. End with a subtle glow on the product.
```
*為何好：大燈微距→crane 上升揭全車經典 reveal 節奏，Chiaroscuro+冷藍高級電動車語彙。｜來源 adcreative.ai*

**腕錶水珠懸浮微距（Seedance 2.0 / 通用，精品打光教科書）**
```
A premium wristwatch floating in mid-air, slowly rotating with precision, water droplets suspended around it catching the light like diamonds, pure black background with a single dramatic spotlight from above, extreme macro detail showing every texture on the watch face, high-end jewelry commercial aesthetic, ultra-smooth rotation.
```
*為何好：純黑+單頂光+鑽石般懸浮水珠是精品錶廣告教科書打光。｜來源 atlascloud.ai*

**香水花瓣慢落 + hard cut 噴霧（Seedance 2.0）**
```
Macro shot of a luxury perfume bottle among scattered pink peonies, shallow depth of field, petals floating in warm afternoon light, soft ambient music. Camera glides closer, a feminine hand enters frame from the right, fingers gently touch the glass bottle. Hard cut to slow-motion spray, golden mist diffuses through the air, particles catching rim light against a dark background.
```
*為何好：靜物美學→hard cut 噴霧製造節奏轉折，金 mist 顆粒+rim light 是香水標誌畫面。｜來源 seedance.tv*

**奢華腕錶 360 轉（Veo 3.1）**
```
Premium watch rotating 360 degrees, silver and gold details catching light, deep navy background, multiple dramatic spotlight sources, slow orbital camera movement, luxury brand commercial quality.
```
*為何好：360 轉+multiple spotlight+orbital movement 給足打光與運鏡。｜來源 veo3ai.io*

---

## 🎬 電影感 / 運鏡（官方範本）

**吊臂揭示 hiker→canyon（Veo 3.1，Google 官方）**
```
Crane shot starting low on a lone hiker and ascending high above, revealing they are standing on the edge of a colossal, mist-filled canyon at sunrise, epic fantasy style, awe-inspiring, soft morning light.
```
*為何好：官方「camera move→主體→揭示→風格→光」標準結構。｜來源 cloud.google.com Veo 3.1 guide*

**淺景深雨夜公車（Veo 3.1，Google 官方）**
```
Close-up with very shallow depth of field, a young woman's face, looking out a bus window at the passing city lights with her reflection faintly visible on the glass, inside a bus at night during a rainstorm, melancholic mood with cool blue tones, moody, cinematic.
```
*為何好：reflection faintly visible 是高級細節指令，cool blue tones 鎖調色。｜來源 cloud.google.com*

---

## 🎞 多鏡頭敘事（時間碼 / 分鏡）

**8 秒 4 鏡頭探險敘事（Veo 3.1，Google 官方 timestamp）⭐**
```
[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal a hidden path.
[00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with awe as she gazes upon ancient, moss-covered ruins. SFX: The rustle of dense leaves, distant exotic bird calls.
[00:04-00:06] Tracking shot following the explorer as she steps into the clearing and runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder and reverence.
[00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small in the center of the vast, forgotten temple complex, half-swallowed by the jungle. SFX: A swelling, gentle orchestral score begins to play.
```
*為何好：一個 prompt 切 4 鏡頭，各帶 shot type + SFX + Emotion，角色跨鏡一致。｜來源 cloud.google.com*

**Seedance 時間軸分段（武士竹林，0–4s/4–9s/9–13s）**
```
Multi-shot cinematic. 0–4s Wide shot: the samurai walks forward from a distance through a bamboo forest. 4–9s Medium tracking shot: he draws his sword and takes his opening stance with leaves falling around him. 9–13s Close-up: the blade cuts through the air with slow-motion water splashes. Photorealistic, 35mm film quality, professional color grading, film grain.
```
*為何好：Seedance 招牌時間軸分段，每段獨立寫動作+運鏡仍連戲。｜來源 higgsfield.ai / vmake.ai*

**Kling 15 秒多鏡頭 + Audio（火星溫室）**
```
Shot 1: Wide establishing shot of a desolate Mars colony greenhouse during a red dust storm. Shot 2: Cut to a macro close-up of a small green sprout. A botanist's gloved hand gently touches the leaf. Shot 3: Over-the-shoulder shot. The botanist stands up, looking out the reinforced glass window at the storm. Audio: Low hum of life-support systems, muffled howling wind outside. Cold blue interior lighting.
```
*為何好：Kling 3.0 原生 15s 單 prompt 多鏡頭，`Shot 1/2/3 + Audio:` 結構免 extend。｜來源 klingaio.com*

---

## 🗣 原生對白 / 音訊

**偵探黑色電影對白（Veo 3.1，ingredients-to-video，Google 官方）**
```
Using the provided images for the detective, the woman, and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, "Of all the offices in this town, you had to walk into mine."
```
*為何好：參考圖鎖角色一致 + says in a weary voice 指定語氣 + 引號對白生原生語音。可串第二句做雙人對話。｜來源 cloud.google.com*

**東京 vlogger 自拍對白（Veo 3，含防字幕技巧）**
```
A selfie video of a travel blogger exploring a bustling Tokyo street market. She's wearing a vintage denim jacket and has excitement in her eyes. The afternoon sun creates beautiful shadows between vendor stalls. She's sampling street foods while talking, occasionally looking into the camera. The image is slightly grainy, film-like. She speaks in a British accent and says: "Okay, you have to try this place when you visit Tokyo. The takoyaki here is absolutely incredible." She ends with a thumbs up.
```
*為何好：指定 accent + 完整口語腳本 + film-like grain。⚠️ Veo 會自動燒字幕 → 不要字幕就加 `(no subtitles!)`。｜來源 replicate.com/blog/using-and-prompting-veo-3*

**Kling 雙角色對白 + 自動對嘴**
```
A tense corporate boardroom. Alternating medium shots focusing on the speakers. [Character A: Older CEO, deep gravelly authoritative voice]: "We are not selling the company. Not today, not ever." Immediately, [Character B: Young Rival, sharp fast-paced angry tone] stands up abruptly and points: "Then you are sinking this ship with everyone on board!"
```
*為何好：`[角色: 音色描述]: "台詞"` 是 Kling 原生對白正解語法，自動對嘴+切 medium shot。｜來源 klingaio.com*

---

## 🔒 一致性鎖法（角色/產品跨鏡不變）

**Seedance `@AssetName` + 顯式鎖（商品雙鏡頭）**
```
[Shot 1: Macro] @ProductRef rotating slowly on a velvet pedestal, soft rim lighting, luxury aesthetic. [Shot 2: Lifestyle] A hand in elegant attire reaching out to grab @ProductRef on a marble countertop. 60fps, creamy bokeh, commercial grade.
```
*為何好：`@ProductRef` 同商品橫跨「特寫旋轉」+「手取情境」不變形 = OiiOii 商品 i2v 痛點解法。句末可加 `Reference @ProductRef for consistent shape and label.`｜來源 vmake.ai*

**Kling 產品文字穩定（旋轉時 logo 不崩）**
```
Slow macro dolly-in of a luxury crystal perfume bottle on a velvet pedestal. Clearly embossed on the glass label is the word "ETTREAL" in an elegant gold serif font. Soft golden hour lighting creates refractive caustics on the velvet. The bottle slowly rotates 45 degrees, ensuring the text "ETTREAL" remains perfectly stable and readable throughout the motion.
```
*為何好：「remains perfectly stable and readable throughout the motion」明令鎖字防旋轉崩壞。把 ETTREAL 換你的品牌。｜來源 klingaio.com*

**Vidu `@tag` 雙掛（多角色動漫一致）**
```
@SCENE_BG @Akari_front @Akari_profile enters from the left sprinting, lavender energy trail, dolly-in, rim light.
```
*為何好：`@角色_front`+`@角色_profile` 正側面雙掛確保轉身一致，tag 順序=優先序（主體放最前）。`@` 在輸入框打會跳已註冊資產選單。｜來源 vidu.com*

**Gemini Omni 對話式多輪編輯（每輪只改一變數）**
```
Turn 1: 10-second clip: a person opening a sleek black product box on a wooden desk in a minimalist apartment. Morning light. Slow zoom in.
Turn 2: Make it sunset light instead of morning. Keep everything else identical.
Turn 3: Now make the box white instead of black. Keep the lighting and camera move the same.
```
*為何好：Omni 招牌對話式編輯，每輪改一個變數 + 「Keep everything else identical」鎖其餘，跨輪記憶保留。｜來源 opus.pro*

**Omni 產品片含負面約束（落地頁 hero）**
```
Create a 6-second premium product video. Use the uploaded image as the main product reference. Keep the product shape, material, color, label, and logo placement consistent. Place the product in a clean studio environment with soft lighting and subtle reflections. Use a slow camera push-in from the front. Elegant, minimal, high-end. Do not change the product design. Do not add random text or extra objects.
```
*為何好：明鎖 shape/material/color/label/logo 五項 + 3 條負面約束防變形/亂加字。｜來源 medium（Omni guide）*

---

## ⚙️ 跨模型語法速查

| 模型 | 一致性鎖法 | 多鏡頭語法 | 對白/音 |
|---|---|---|---|
| **Veo 3.1 / Omni** | Ingredients(≤3-4 圖) + 句中複述關鍵細節 | `[00:00-00:02]` 時間碼分鏡 | 引號對白 + `says in a X voice` + `(no subtitles!)` |
| **Kling 3.0** | 逐拍動作+`remains in sharp focus`；文字加`stable and readable` | `Shot 1/2/3 + Audio:`（原生 15s） | `[角色: 音色]: "台詞"` 自動對嘴 |
| **Seedance 2.0** | `@Character1`/`@ProductRef` + `Reference @X for consistent...` | `[Shot 1:][Cut to:]` 或 `0–4s/4–9s` | `@Audio1` 配樂；最多 12 asset |
| **Vidu Q3** | `@角色_front`+`@角色_profile`，tag 順序=優先序 | 逐 clip(4s/段) `@tag+動作+運鏡` | 原生音畫；`says: "台詞"` 自動 lip-sync |

**鐵則：用了 @reference / Ingredients 就別再重述角色長相 —— 只寫動作/運鏡**（與 i2v 黃金公式同源）。

## 來源（全部已標於各 prompt）
官方：cloud.google.com Veo 3.1 guide · deepmind.google/models/veo · klingaio.com · vidu.com · replicate.com/blog · labs.google/flow/tv（Show Prompt）
社群（標 source 附全文）：veo3ai.io · seedance.tv · atlascloud.ai · vmake.ai · higgsfield.ai · leonardo.ai · simplified.com · adcreative.ai · skywork.ai · banana-prompts.net · opus.pro

## 連動
- 先有概念 → [concept-first-prompting.md](concept-first-prompting.md)
- 反瑕疵 → [quality-control.md](quality-control.md)
- 選模型 → [model-picker.md](model-picker.md)
- 成套主題範本 → [../templates/preset-packs.md](../templates/preset-packs.md)
