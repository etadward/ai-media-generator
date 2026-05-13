# Preset Packs — 可直接套用的 Prompt 食譜

**定位：** 當使用者想要「Wes Anderson 風的 5 秒鏡頭」、「Nike 級運動廣告」、「Blade Runner 2049 雨夜」、「宮崎駿夢幻森林」— 不用每次重新從 [cinematic-direction.md](../references/cinematic-direction.md) 挑 token，直接來這裡抓現成的。

**使用方式：**
1. 按「任務類型」找最近的 preset
2. 把 `{BRACKETED}` 占位符換成你的主體/場景
3. 直接貼到目標平台 (若平台建議不同，見每個 preset 的 `Target`)

**每個 preset 的格式：**
- **Use case** — 什麼情境
- **Target** — 推薦平台 + 參數
- **Prompt** — 完整可貼
- **Negative** — 負面提示
- **Why** — 為什麼這些 token 管用
- **Swap points** — 可以改的地方

---

## 📽️ 電影感 Presets (Cinematic)

### 1. Blade Runner 2049 Rainy Cyberpunk (10s)

**Use case:** 賽博龐克雨夜、偵探/復古未來科幻、霓虹城市
**Target:** Kling 2.1 Master 或 2.6 Pro，10s，2.39:1

```
Shot by Roger Deakins, Panavision anamorphic 50mm at T2.0, Arri Alexa LF.
Medium close-up of {SUBJECT: 穿米色長風衣的男子} walking slowly through a
rain-soaked alley at night. Practical neon signs in magenta and cyan glow
from behind him, their reflections rippling in puddles. Cinestill 800T
emulation with heavy red halation around every light source. Volumetric
atmospheric haze. Teal shadows, sodium-amber highlights, 2.39:1 anamorphic
horizontal lens flares. Low-key 4:1 contrast. Slow dolly-in tracking from
slightly below. Breath visible in cold air. Rain streaks backlit as silver
needles.
```

**Negative:**
```
cartoon, anime, 3D render, bright daylight, cheerful, flat lighting,
low contrast, clean, pristine, oversaturated
```

**Why:** Deakins + Panavision anamorphic 是 Blade Runner 2049 招牌。Cinestill 800T halation 是霓虹夜拍的招牌效果。Teal/amber + 2.39:1 鎖住電影感。

**Swap points:** `{SUBJECT}` 換角色；`magenta and cyan` 可改 `orange and teal`；`alley` 可改 `highway underpass` / `subway platform`。

---

### 2. Wes Anderson Symmetrical Deadpan (5s)

**Use case:** 對稱可愛、書本感、粉彩、微幽默
**Target:** Midjourney v7 (`--niji 7 --s 300` 可選) 或 Kling / Sora

```
Wes Anderson style cinematography, perfect vertical symmetry, centered
composition. Flat dollhouse-like tableau of {SUBJECT: 一位身穿薄荷綠制服
的飯店門童} standing at the center of an ornate pastel pink hotel lobby.
Meticulously balanced framing, symmetric everything. Pastel palette: powder
blue, cream, salmon pink, buttercream yellow. Soft diffused daylight,
shadowless, 35mm Kodak film grain. Futura bold signage visible. Subject
faces camera deadpan, hands at sides. Slow whip pan entry or static medium
shot. 2.66:1 Grand Budapest Hotel aspect ratio.
```

**Negative:**
```
dark, moody, asymmetric, gritty, realistic, desaturated, horror, chaotic,
modern minimalist
```

**Why:** Anderson 最招牌的三件事：對稱 + 粉彩 + 中景定格。Futura 字體 token 把「Anderson 世界」感鎖死。

**Swap points:** 把 `hotel lobby` 換成 `submarine interior` / `ski lodge` / `train compartment`；色盤可換 `mustard / olive / burnt orange` (Royal Tenenbaums 版)。

---

### 3. Christopher Nolan IMAX Epic (10s)

**Use case:** 宏大、科幻/戰爭/驚悚、建築感、史詩
**Target:** Kling / Veo 3.1 / Sora 2, 10s, 16:9

```
Shot by Hoyte van Hoytema, IMAX 70mm Kodak Vision3 500T, wide field of
view with ultra-shallow depth of field isolating {SUBJECT: 一位穿著物理
學家大衣的男子}. Nolan-inspired architectural scale, low-angle hero
composition. Subject stands small against massive brutalist concrete
interior, vast space dwarfing him. Desaturated cool blue-grey palette,
minimal warmth, only one practical tungsten source. 1.43:1 IMAX aspect or
2.39:1. Practical explosions or light sources only, no CGI. Deep crushed
shadows, highlight roll-off on concrete texture. Slow push-in dolly.
```

**Negative:**
```
warm, cozy, domestic, small scale, saturated, cartoonish, flat composition,
low budget
```

**Why:** Hoytema IMAX + Nolan 建築尺度 + 冷藍色調 = Oppenheimer/Dunkirk/Tenet 配方。Practical explosions 防止 AI 走 CGI 感。

---

### 4. Denis Villeneuve Monumental (10s)

**Use case:** 沙漠科幻、太空、單人面對宇宙、Dune 感
**Target:** Kling 2.6 Pro / Seedance 1.0 Pro, 10s, 2.39:1

```
Greig Fraser cinematography, Arri Alexa 65 with Panavision Panaspeed.
Villeneuve monumental scale: {SUBJECT: a hooded figure in desert gear} as
a tiny silhouette against a massive alien landscape of ochre sand dunes
and brutalist geometric architecture looming in the haze. Desaturated
sepia and steel palette, muted warmth. Low contrast atmospheric dust
suspension, golden hour low sun with visible aerial perspective
compressing distance. Slow crane up revealing scale. 2.39:1 anamorphic,
no lens flare, restrained. Cinematic grain from Kodak Vision3 250D
emulation. Harsh wind-blown sand particles as visible texture.
```

**Negative:**
```
lush green, urban city, high saturation, close-up, intimate, warm cozy,
flat lighting, small scale
```

**Why:** Greig Fraser 大片幅 + Villeneuve 的「一個人對宇宙」視覺 = Dune/Arrival 招牌。沙塵粒子 + aerial perspective 做出尺度感。

---

### 5. Wong Kar-wai Neon Longing (10s)

**Use case:** 霓虹情調、慢動作步態、HK 90s、紅綠對撞
**Target:** Kling (運鏡最準)，10s，2.35:1

```
Wong Kar-wai style, Christopher Doyle handheld cinematography, stepped-
frame slow motion, Fuji 8mm film grain. {SUBJECT: 一位身穿紅色旗袍的女子}
walks slowly through a rain-slick Hong Kong alley at night, lit by buzzing
magenta and green neon signs. Saturated red and emerald color collision,
deep shadows, Christopher Doyle's signature hot saturated highlights. In
the Mood for Love palette. Medium close-up tracking behind her, stepped
slow motion at 48fps rendered at 24fps for print effect. Cinestill 800T
halation. Fan blowing hair. Cigarette smoke curling in light.
```

**Negative:**
```
bright daylight, modern, clean, minimalist, desaturated, wide landscape,
outdoors nature
```

**Why:** Doyle handheld + stepped frame 是 WKW 招牌。紅綠對撞 (旗袍紅 + 霓虹綠) 是他的色彩簽名。

---

### 6. Studio Ghibli / Makoto Shinkai Dreamy Anime (10s)

**Use case:** 日系動漫、溫柔懷舊、自然光奇幻、城市 + 星空
**Target:** Kling (風格強) 或 Midjourney `--niji 7 --s 250`, Sora 2

```
Makoto Shinkai cinematic anime combined with Studio Ghibli hand-painted
backgrounds. {SUBJECT: a teenage girl with a red school backpack} stands
on a rooftop at dusk, overlooking a hyper-detailed Tokyo cityscape with
volumetric god rays piercing through pink-orange cumulus clouds. Lens
flare across frame. Cel-shaded character with soft watercolor painted
background. Warm amber-to-cool blue gradient sky. Gentle wind lifting
hair. Bittersweet longing mood. 16:9, painterly aesthetic, subtle film
grain. One static wide then slow push-in to medium shot.
```

**Negative:**
```
photorealistic, 3D render, dark grim, cyberpunk, adult sophisticated,
muted colors, flat sky
```

**Why:** Shinkai 的 volumetric 光 + Ghibli 的手繪背景 = 目前 AI 模型對「動漫美感」最穩的雙錨。

---

### 7. Kurosawa Wuxia Duel (10s)

**Use case:** 武俠、武士、竹林、雨中決鬥
**Target:** Kling 2.6 Pro / Seedance 1.0 Pro, 10s

```
Kurosawa-inspired samurai epic, multi-camera telephoto compression feel.
{SUBJECT A: 一位穿深靛藍武服的武士} and {SUBJECT B: 一位穿褪紅袍的對手}
face each other in tense standoff in a rain-drenched bamboo grove at dawn.
Low-angle hero wide shot. Shot on Arri Alexa with 200mm compressed
background, bamboo stalks rhythmic. Practical wind machine blowing rain
sideways. Desaturated earth tones with blood-red accent. 2.39:1
anamorphic. 120fps slow motion on the draw of a blade, flash of silver.
Kodak Vision3 500T grain holding under overcast sky. No score, only wind
and rain.
```

**Negative:**
```
bright saturated colors, modern clothing, cartoon, clean environment,
cheerful, indoor, daylight sunny
```

**Why:** Kurosawa 的 telephoto + 雨 + 多角色 standoff 是招牌。200mm 壓縮把竹林變詩意節奏。

---

### 8. K-drama Romance Soft Warm (5s)

**Use case:** 韓劇、溫柔情感、柔焦、暖色
**Target:** Kling 2.1 Master / Seedance, 5s, 16:9 或 9:16

```
K-drama modern cinematography, Netflix original look. Medium close-up of
{SUBJECT: 一位穿米色毛衣的男子} turning slowly to look at camera, soft
longing smile. Warm diffused tungsten practical from window behind, subtle
rim light on hair. Muted peach and beige palette. Phase One IQ4 sensor
look, 85mm f/1.4 extreme shallow depth of field, creamy bokeh. Slight warm
color grade, clean skin tones, no grain. Steady tripod, almost imperceptible
drift. Breath visible, quiet intimate moment. Seoul apartment dusk.
```

**Negative:**
```
high contrast dramatic, harsh shadows, desaturated, urban grit, dark moody,
noir, cyberpunk, anime
```

**Why:** K-drama 的「暖 + 柔 + 85mm」是全球模型都認的美學。

---

### 9. A24 Indie Naturalism (8s)

**Use case:** 文青獨立、真實不美化、冷靜敘事
**Target:** Flux 1.1 Pro (靜) 或 Kling / Sora

```
A24 indie film aesthetic, naturalistic unglamorous cinematography. Medium
shot of {SUBJECT: a weary middle-aged woman in a thrift store cardigan}
sitting at a kitchen table in morning light. Handheld subtle shake, 35mm
film grain, Kodak Vision3 500T. Available natural light only, overcast
sky through window, no fill. Slight green color cast typical of A24. Real
skin texture with freckles visible, no beauty retouching. Asymmetric
composition, space above her head. Extended duration, stillness. Static
tripod or locked-off. 1.85:1.
```

**Negative:**
```
glossy, Hollywood glamor, saturated, dramatic lighting, stylized, epic,
cinematic score feel, commercial polish
```

**Why:** A24 是反 Hollywood 美學 — 綠色漂移 + 真實皮膚 + 自然光是密碼。

---

### 10. 1970s New Hollywood Grain (8s)

**Use case:** 復古美式、Taxi Driver / Dog Day / The Long Goodbye 感
**Target:** Kling / Midjourney `--s 200 --raw`

```
1970s New Hollywood grit cinematography, Kodak 5254 negative emulation
with heavy grain. {SUBJECT: a man in a brown corduroy suit} walks down a
litter-strewn New York street in late afternoon sun. Zoom lens from 70mm
to 35mm during the take. Hazy urban smog compressing light. Warm amber
sodium vapor street lamps just starting to buzz on. Saturated browns and
ochres with washed-out highlights. Film gate weave and light flicker.
1.85:1. Robert Mulligan / Gordon Willis cinematography.
```

**Negative:**
```
clean digital, modern, crisp, saturated, HDR, smooth, polished, daylight
bright
```

**Why:** Kodak 5254 + zoom + 1970s 城市髒亂 = Taxi Driver 配方。Gordon Willis (The Godfather DP) token 拉美學。

---

## 🎬 廣告 Presets (Commercial)

### 11. Apple Product Hero (15s)

**Use case:** 科技產品、極簡奢華、白底無雜
**Target:** Flux 1.1 Pro (靜), 4:5 或 16:9

```
Apple product commercial aesthetic. {PRODUCT: iPhone 17 Pro in titanium}
floating in pure white infinity cyclorama. Impossibly clean seamless
gradient background, no visible light source. 100mm macro at f/8 on
product, razor-sharp edge detail. Slow dolly-in + product rotation on
invisible axis. Perfect reflection on imaginary glass table surface. Cool
white 5600K lighting with rim light separating product from background.
Phase One IQ4 150MP rendering, commercial product photography precision,
zero grain, zero imperfection. 35% of frame is negative space top and
bottom for headline text.
```

**Negative:**
```
cluttered, dark, moody, grainy, vintage, warm, organic, handheld, rustic,
filmic
```

**Why:** Apple 廣告的 DNA 是 `infinity cyclorama + macro + 冷 5600K + 留白`。

---

### 12. Nike Heroic Sport (30s, tell as shot list)

**Use case:** 運動品牌、激勵、低角、慢動作
**Target:** Kling 2.6 Pro + Phantom slow-mo token

```
Nike commercial heroic aesthetic, 200fps Phantom Flex 4K slow motion.

Shot 1 (0-3s): Extreme close-up of {SUBJECT: a female sprinter}'s eye
reflecting the finish line, sweat bead rolling down brow, harsh stadium
arc lamp rim light. Alexa 65, 100mm macro.

Shot 2 (3-10s): Low-angle tracking following feet pounding the track,
200mm telephoto compressed stadium lights into bokeh orbs. Dust kicks up
in slow motion.

Shot 3 (10-20s): Hero silhouette mid-stride, arms raised, backlit against
stadium arc lamp. Sweat droplets frozen in air. Saturated brand red gel
light from behind. Bleach bypass crushed blacks.

Shot 4 (20-30s): Athlete collapses to knees on finish line, warm golden
hour sun bleeds through stadium structure. Tear mixes with sweat. Kodak
Vision3 500T, natural grain. Bold white sans-serif tagline space bottom.
```

**Negative:**
```
clean polished beauty, soft warm cozy, feminine delicate, urban casual,
quiet still, pastel
```

**Why:** Nike 的「低機位 + 慢動作 + 汗珠 + bleach bypass」是三十年不變的配方。

---

### 13. Chanel Luxury Fashion (30s)

**Use case:** 奢侈品、時尚電影感、黑白或金色
**Target:** Runway Gen-4 / Flux 1.1 Pro / Kling, 靜態美

```
Chanel-inspired luxury fashion film. Medium close-up of {SUBJECT: a woman
in pearls and black silk dress} with face partially obscured by shadow or
turned away. Phase One medium format, 80mm f/2.8, shot through a gauze
scrim. Natural window light from Parisian apartment, soft north-facing
daylight only. Muted ivory and gold palette with deep charcoal shadows.
Kodak Portra 400 in 120 medium format, Noritsu scan, subtle grain and
light leak. 35mm film aesthetic, restrained refinement. Slow 2-second
static beats with slight camera drift. 4:5 aspect for print campaign
use. No branding visible.
```

**Negative:**
```
bright colorful, saturated, commercial product shot, cluttered, casual,
modern minimal, tech, industrial, suburban
```

**Why:** Chanel/LV 等奢侈品的密碼 = 中片幅 + 自然窗光 + 巴黎公寓 + 不露臉。

---

### 14. Rolex Macro Watch (15s)

**Use case:** 精密機械、微距、奢侈錶
**Target:** Flux 1.1 Pro (靜態細節最強), 1:1

```
Haute horlogerie extreme macro. {PRODUCT: a vintage Rolex Submariner
watch} on seamless obsidian black velvet. 100mm macro at f/11 focus-
stacked, micron-level sharpness on dial engravings and crown serrations.
3-point lighting: softbox 45° key, backlit rim separating bezel from
black, fill card for shadow detail. Sub-pixel sharp, crystal perfectly
clear. Slight shallow DoF on movement jewels in a second focus-stack
frame. Cool 5000K daylight balance. Deep obsidian blacks, saturated
metallic highlights, 1:1 square. Phase One XF IQ4 150MP. No retouching
needed — it was shot right.
```

**Negative:**
```
handheld, soft, dreamy, warm, vintage film grain, flat, amateur, colorful
background, dirty, scratched
```

**Why:** 奢華錶的三件事：`100mm macro + focus stack + obsidian velvet`。沒有第四樣。

---

### 15. Coca-Cola Warm Family (30s)

**Use case:** 快消溫情、家庭、節慶、亮色
**Target:** Seedance 1.0 Pro (multi-shot), 30s, 16:9

```
Coca-Cola commercial warmth. Three-beat 30-second family scene.

Beat 1: Aerial drone dusk shot descending toward a suburban home with
warm glowing windows, decorated for holidays, Kodak Portra 800 emulation.

Cut to: Medium shot of a multi-generational family gathered at a dinner
table, warm tungsten practical chandelier overhead, soft amber glow on
faces. Shallow DoF 85mm, handheld subtle intimate. {SUBJECT: 一個小女孩}
reaches for a chilled Coke bottle, condensation on glass catching light.

Cut to: Extreme close-up of the bottle cap opening with a satisfying
"kss" sound, bubbles rising. 240fps slow motion. Warm saturated brand red
as the dominant accent against amber interior. Portra 400 grain.
```

**Negative:**
```
cold, blue, minimalist, dark, sad, alone, industrial, urban grit,
cyberpunk, moody
```

**Why:** 溫情廣告的密碼：`warm tungsten + Portra 顆粒 + 手持 + 低 DoF 家人特寫`。

---

### 16. Tesla Tech Futurism (10s)

**Use case:** 科技前衛、極簡、冷調、未來感
**Target:** Veo 3.1 / Kling, 10s

```
Tesla-inspired futuristic commercial. {PRODUCT: an all-white minimalist
car} parked in a seamless white environment with deep ocean blue gradient
floor. Cool 6500K lighting, zero warmth. Single key softbox from 45° top,
practical LED floor accent lighting brand blue. Aerospace precision
composition, 2.35:1 wide. Slow dolly-in + 360° orbit combined. Zero grain,
zero film feel, pure digital clean. Low contrast smooth highlights on
body paint. Panavision Primo 50mm at f/5.6. Subtle reflection of clean
geometric overhead light on polished chrome. High-tech, near-silent
machine aesthetic.
```

**Negative:**
```
warm, vintage, film grain, organic, suburban, messy, rustic, saturated,
hand-crafted
```

**Why:** Tesla/Apple 共享「零暖色 + 零顆粒 + 精確幾何」的未來感 DNA。

---

## 🎼 MV Presets (Music Video)

### 17. Hiro Murai Surreal Lowlight (20s)

**Use case:** 超現實 MV、Childish Gambino / FKA twigs 感
**Target:** Kling / Sora 2, 20s (extend to 10s + 10s)

```
Hiro Murai surreal dreamlike aesthetic. One continuous handheld take of
{SUBJECT: a figure in a white robe} walking through a dimly lit abandoned
suburban street at night. Practical streetlamp every 30 feet providing
pools of warm tungsten, darkness between. Thin layer of ground haze
catching light. Desaturated palette, warm amber pools against crushed blue-
green darkness. Slow deliberate pace, unsettling stillness. Silhouette
revealed and re-absorbed by shadow. Kodak Vision3 500T, visible grain.
35mm Alexa, subtle handheld float. One take, no cuts. Run-down decay
textures on houses behind. Subject occasionally turns to look off-frame,
no payoff reveal.
```

**Negative:**
```
bright, saturated, cheerful, urban glamorous, high-energy, fast cuts,
daylight, clean
```

**Why:** Murai 的「一個人 + 低光 + 郊區 + 一鏡到底 + 不解釋」= Atlanta / This Is America MV 美學。

---

### 18. Cole Bennett Lyrical Lemonade (15s)

**Use case:** Hip-hop MV、動漫 cut-out、高飽和特效
**Target:** Runway Gen-4 + Aleph (特效疊加) 或 Kling

```
Cole Bennett Lyrical Lemonade aesthetic. {SUBJECT: a rapper in chrome
chain and designer fit} performs directly to camera in a warped surreal
environment. Fisheye 14mm wide. Saturated primary colors. Cartoon-style
cutout VFX overlays: glowing halos, cash symbols, anime-style impact
stars reacting to beats. Camera zooms aggressively in/out matched to
bass drops. Smoke bomb color gas filling background. Practical strobes
flash on beat. Bleach-bypass contrast, punchy saturated reds and yellows
and cyans. 24fps standard speed with occasional step-frame on punch lines.
```

**Negative:**
```
realistic naturalistic, subtle, muted, cinematic slow, arthouse, luxury
static, minimalist
```

**Why:** Bennett 的 MV DNA = `fisheye + cut-out VFX + 飽和色煙 + 節拍剪輯`。

---

### 19. Jonathan Glazer Clinical Unease (15s)

**Use case:** 冷感 MV、高級 fashion film、Radiohead / Massive Attack 感
**Target:** Runway Gen-4 / Kling, 15s

```
Jonathan Glazer clinical precision. Static locked-off medium shot.
{SUBJECT: a figure in institutional white clothing} standing motionless
in a sterile empty white cube space, slight tilt of head. Cold 5600K
fluorescent overhead flat lighting, zero shadow character, surgical
clinical. Desaturated palette, dead whites and pale skin. Extended
duration, subject barely breathes. Unsettling symmetry. Uncomfortable
stillness. Sennheiser microphone-dry room tone only. Shot on Alexa 35
with clean digital rendering, slight film grain layer Vision3 200T. 1.85:1.
```

**Negative:**
```
dynamic, fast, warm, cozy, saturated colorful, handheld energetic,
performance, dancing, party, bright
```

**Why:** Glazer 的不安來自「看起來像醫院/監獄但沒事發生」。Zero shadow + static + 延長時長是密碼。

---

### 20. Michel Gondry Handmade Whimsy (15s)

**Use case:** 童趣實驗 MV、紙藝、Björk / Rosalía / White Stripes 感
**Target:** Kling (物理強), 15s

```
Michel Gondry handmade practical magic. {SUBJECT: a woman in a yellow
raincoat} walks through a visibly cardboard-constructed miniature city
with paper clouds and yarn rivers. In-camera practical effects only —
visible tape, visible cardboard, charming imperfection. Warm childlike
wonder aesthetic. Stop-motion jitter feel. Subtle handheld. Saturated
primary colors with clear hand-crafted texture. Super 8mm film emulation,
grain and light leaks. Available natural light, no fill. Whimsical
impossible scale contrasts (giant flower, tiny person). 1.66:1.
```

**Negative:**
```
digital CGI, photorealistic, polished commercial, minimalist clean, dark
moody, horror, serious dramatic
```

**Why:** Gondry 的魔法是「你看得見道具」。Prompt 寫明 `cardboard / tape / yarn` 反而保留手工感。

---

## 🎨 時尚 / 美妝 Presets

### 21. Vogue Italia Editorial (15s)

**Use case:** 高端編輯、時尚雜誌封面級
**Target:** Flux 1.1 Pro / Midjourney v7 `--s 400 --raw`

```
Vogue Italia editorial fashion photography. Medium 3/4 shot of {SUBJECT: 
a model in avant-garde couture} against a deep saturated emerald green
backdrop. Steven Meisel theatrical lighting, single hard key from camera-
right, deep shadow side. Face turned in 3/4 profile, intense gaze.
Fashion-forward strong brow and lip. Phase One XF IQ4 150MP, Schneider
80mm f/4. Crisp focus on eye. Film grain layer Kodak Ektachrome E100
emulation, crisp micro-contrast. Slight dress fabric movement. 4:5 print
magazine aspect. Saturated yet refined color, no filter. No retouching on
skin texture.
```

**Negative:**
```
casual, smiling, soft pastel, cute, beauty retouched, glossy, commercial,
shopping, suburban
```

**Why:** Vogue Italia 的密碼 = Meisel + 單硬光 + 深色背景 + 中片幅。

---

### 22. Beauty Campaign Clamshell (10s)

**Use case:** 美妝、香水、保養品
**Target:** Flux Kontext (可修) / Seedream 4.5, 10s

```
Luxury beauty campaign aesthetic. Extreme close-up of {SUBJECT: a model's
flawless skin and lips} filling frame. Clamshell beauty lighting: large
softbox above + reflector card below, shadowless luminous glow. 85mm
macro at f/2.8, extreme shallow DoF on lips. Skin texture with subtle
pore detail, not plastic but refined. Peach, cream, blush palette. Subtle
golden hour warm rim. Perfectly diffused highlights on lips. Slight
product reflection in the model's eye ({PRODUCT: a crystal perfume
bottle} visible as reflection only). 2048×2048, no retouching needed —
lighting does the work.
```

**Negative:**
```
harsh shadows, grunge, gritty, yellow unflattering, oily, dry cracked,
dark moody, orange tan fake, over-filtered
```

**Why:** 美妝廣告 = 無陰影 clamshell + 85mm macro + 自然皮膚細節。

---

## 🌌 VFX 情境 Presets

### 23. Wuxia Bamboo Duel Slow Motion (10s)

**Use case:** 武俠 + VFX + 竹林
**Target:** Kling 2.6 Pro / Seedance Pro, 10s

```
Two wuxia swordmasters mid-duel in a bamboo forest at dawn. Shot on Arri
Alexa with 2.39:1 Panavision anamorphic. {SUBJECT A: 青衣武者} and
{SUBJECT B: 白衣武者} mid-leap in opposing arcs, blades catching first
morning sun as horizontal lens flare streaks. 240fps Phantom slow motion.
Bamboo leaves drift around them in slow motion particles. Visible
volumetric god rays through the bamboo canopy, atmospheric mist. Practical
wind machine effect on robes, silk flowing. Zhang Yimou saturated emerald
green + blood accent color grade. Slight wire-work weightlessness.
Kodak Vision3 250D emulation.
```

**Negative:**
```
modern urban, clean daylight, stationary, fast-cut, cartoon, daylight
bright, saturated rainbow
```

**Why:** 武俠 + 240fps 慢動作 + 竹葉粒子 + god rays = Zhang Yimou 招牌。

---

### 24. Underwater Caustics Dreamscape (10s)

**Use case:** 水下世界、夢幻、游泳池、珊瑚礁
**Target:** Kling / Veo 3.1 (物理), 10s

```
Underwater dreamscape cinematography. {SUBJECT: a woman in a flowing white
dress} floating serenely below the surface, hair suspended in current.
Golden hour sunlight caustics dappling on sandy floor, visible suspended
particles in water. Bubbles rising in slow streams around her. Blue-green
color shift, aerial perspective thickening with depth. Hoyte van Hoytema
underwater housing aesthetic. Wide 24mm lens, slight fisheye. Backlit
from sun above, volumetric light columns penetrating the water. 120fps
slow motion for dress fabric simulation. Kodak Vision3 500T. 2.39:1.
```

**Negative:**
```
dry land, above water, fast action, gritty urban, dark horror, neon
cyberpunk, cartoon anime
```

**Why:** 水下三要素：caustics + 懸浮粒子 + 上方體積光。

---

### 25. Haunted Hospital Corridor (10s)

**Use case:** 恐怖、心理驚悚、工業驚駭
**Target:** Kling (低光強) / Runway, 10s

```
Abandoned hospital corridor at night. Slow forward dolly through the
endless perspective-vanishing hall. Flickering green fluorescent
practicals hanging askew, one out every three. Thin layer of atmospheric
haze drifting. Peeling institutional paint texture, rusted gurneys against
walls. Muted desaturated palette with sickly green fluorescent cast.
Wide 18mm lens creating deep deep perspective, subject (if any) distant
as tiny silhouette. Hiro Murai low-light lowfi unease. Locked tripod,
subtle drift only. Vision3 500T grain. No music cue, dry room tone only.
1.85:1.
```

**Negative:**
```
warm cheerful, daylight, modern clean, people smiling, colorful, bright
fluorescents even, domestic, suburban
```

**Why:** 恐怖 = 閃爍綠螢光 + 深透視 + atmospheric haze。Hiro Murai token 加深不安。

---

### 26. Magical Forest Fireflies (10s)

**Use case:** 奇幻、夢幻、Ghibli 感魔法
**Target:** Kling / Seedream (靜圖), 10s

```
Enchanted forest at twilight. {SUBJECT: a young traveler with a lantern}
walks a moss-covered path lit only by hundreds of floating bioluminescent
particles (fireflies mixed with magical glowing motes) rising upward.
Dense volumetric god rays piercing through giant ancient tree canopy.
Practical small LED accent mushrooms on the forest floor glowing soft
cyan and green. Cool blue-green base with warm lantern-glow accent on
subject. Terrence Malick Lubezki Steadicam drift, natural light feel.
Slight handheld organic movement. Ghibli hand-painted texture on
backgrounds. 2.39:1. Kodak Vision3 500T grain.
```

**Negative:**
```
modern urban, clean minimalist, harsh daylight, tech futuristic, dry
desert, stadium lights
```

**Why:** 魔幻森林的三層光：環境藍綠 + 粒子 + 主角暖光，缺一不可。

---

### 27. Volcanic Eruption Hero (10s)

**Use case:** 自然災害、壯觀、尺度
**Target:** Kling 2.6 Pro / Veo 3.1, 10s

```
Volcanic eruption at dusk, epic scale. {SUBJECT: a solitary silhouette
on a distant ridge} as tiny reference for the monumental lava fountain
erupting behind. Molten orange rock spewing skyward, black smoke plume
reaching stratosphere. Volcanic ash falling foreground, lightning within
the ash cloud (volcanic lightning). Hoyte van Hoytema IMAX 70mm
cinematography. Low-angle hero wide, crane descending. Warm magma orange
vs cold blue twilight sky high-contrast collision. Practical fire glow
on the silhouette's edges. Kodak Vision3 500T heavy grain under low
light. 1.43:1 IMAX or 2.39:1.
```

**Negative:**
```
intimate close-up, domestic interior, daylight calm, urban city, bright
happy, cartoon, stylized anime
```

**Why:** 尺度感 = 巨大自然 + 渺小人類 + Hoytema IMAX 鏡語。

---

### 28. 80s Synthwave Neon Drive (10s)

**Use case:** 復古未來、合成波、Drive / Kavinsky MV 感
**Target:** Kling / Runway, 10s

```
1980s synthwave retro-future aesthetic. Low-angle tracking shot alongside
{SUBJECT: a matte black retro cafe racer motorcycle}, rider silhouette
backlit. Driving through a neon-saturated empty freeway tunnel at night.
Saturated magenta and cyan LED wash. Horizontal anamorphic lens flares
on every light source. Chrome reflections. VHS fuzz and light chromatic
aberration. 2.39:1. Kodak Vision3 500T grain plus subtle video scanline
overlay. Moebius / Tron Legacy inspired color palette. Cool synth-pink
sunset visible at tunnel end. 60fps slight motion blur on environment,
subject stabilized.
```

**Negative:**
```
warm earth tones, natural daylight, rural, vintage 1970s, grunge, natural
film look, documentary realism
```

**Why:** 80s 合成波 = `magenta + cyan + chrome + VHS fuzz + anamorphic flare`。

---

## 📱 9:16 短影音 Presets

### 29. TikTok UGC Authentic (9:16, 10s)

**Use case:** 真實 UGC 感、非商業、有機
**Target:** Kling 9:16 / Seedance, 10s

```
Authentic TikTok UGC aesthetic. Vertical 9:16 handheld iPhone front
camera selfie-style. {SUBJECT: 一位年輕人} talking to camera in natural
room lighting, slight motion blur from handheld. Messy background
(bedroom or kitchen detail visible, lived-in). No filter, no retouching,
subject's real skin texture and casual outfit. 4K/30fps iPhone 15 Pro
look, auto white balance slightly warm. Center framed with head top
third, face eye-contact. Ambient ambient room tone. Natural eyes, no
ring light glow in eyes (important: avoid the "influencer ring" look).
```

**Negative:**
```
polished commercial, studio lighting, professional camera, retouched
flawless, luxury brand aesthetic, perfect composition, graded
cinematic
```

**Why:** UGC 的關鍵是「不像廣告」。要明確寫 `no ring light glow in eyes` 擋掉 AI 的 influencer 預設值。

---

### 30. Food ASMR Overhead (9:16, 10s)

**Use case:** 美食、ASMR、料理直拍
**Target:** Kling I2V (首幀食物靜圖起跑) / Seedance, 9:16, 10s

```
Food ASMR overhead 90° top-down vertical 9:16. Extreme close-up of
{SUBJECT: a sizzling steak being sliced} on dark wooden board. Steam
rising, lit dramatically by side rim light at 45°. Slow 240fps Phantom
motion on knife cutting, juices glistening. Shallow DoF 100mm macro at
f/4. Saturated but natural food colors — deep caramel crust, pink medium
interior. Dark cinematic background, negative space for text overlay top.
Kodak Vision3 500T emulation but clean, minimal grain. SFX (for Veo 3):
knife crunch through crust, sizzle, ambient restaurant kitchen.
```

**Negative:**
```
wide landscape, full table cluttered, horizontal 16:9, cartoonish
saturated, dry not glistening, dusty
```

**Why:** 美食 ASMR = `overhead 90° + side rim light + 240fps + 蒸氣`。

---

## 如何使用這些 Preset

### Quick Start
1. **找最近的 preset** — 用 Ctrl+F 搜 "Nike"、"Wes Anderson"、"水下" 等關鍵字
2. **換占位符** — `{SUBJECT}` / `{PRODUCT}` / `{SCENE}` 填具體內容
3. **貼到目標平台** — 每個 preset 已標 `Target` 推薦平台
4. **加 negative** — 把對應的 negative 貼到平台的 negative 欄 (若有)

### 進階
- **混搭**：把 preset A 的 `Style & Lighting` + preset B 的 `Camera & Subject` 拼起來
- **調 intensity**：覺得太過 → 拿掉 1-2 個 token (例如拿掉 DP 名);覺得太弱 → 從 [cinematic-direction.md](../references/cinematic-direction.md) 補 1-2 個
- **修改版**：成功的組合存成自己的 preset，建立個人語彙庫

### 針對平台微調
- **Midjourney v7**：把 preset 主文放前面，參數 `--ar 16:9 --s 200 --raw --v 7` 放尾
- **Flux 1.1 Pro**：preset 已是自然語言句子，直接用，去掉 `shot on XXX` 可讓輸出更 neutral
- **Kling I2V**：把 preset 的「主體描述」拿掉，只留動作 + 風格 + 運鏡 (見 [kling.md](../references/kling.md) I2V 黃金法則)
- **Sora 2**：把 10s preset 拆成 3 beats，每 beat 一段
- **Seedance Pro**：用 `Cut to:` 串多個 preset 成多鏡
- **Runway Aleph**：改成動詞開頭 (`restyle...` / `add...`) 配既有影片
