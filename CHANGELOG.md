# Changelog

All notable changes to this skill are documented here.

## [1.2.1] - 2026-05-19 — Story-mode warning (correction)

**Critical correction to v1.2.0.** While documenting v1.2.0 I had appended a §12.10.1 claiming「Seedance 2.0 故事動畫」chip from home page is a "3-batch express SOP". **This was wrong** — caught immediately by the user during validation:

- Story-mode is NOT a fast direct-generation path
- Send routes to a script-editing panel requiring duration + aspect + dialogue language selections
- Then multi-shot editing flow
- Then commit → STAR cost is multiples of a standard 15s ad

### Corrected guidance now in §12.10.1

- Story-mode = long multi-shot pipeline (30s-1min+ video)
- Estimated cost: 420-840+ STAR (~NT$100-200)
- Standard 15s ad: ALWAYS use §12.10 自由畫布 6-batch (210 STAR ~NT$50)
- Story-mode only worthwhile for genuine multi-shot narratives where you want OiiOii to auto-split shots

### STAR / NT$ conversion (user-confirmed)

210 STAR ≈ NT$50 → 1 STAR ≈ NT$0.24 → Seedance 2.0 pro ≈ NT$3.3/sec.

Full cost matrix added to §12.10.1.

### Lesson documented

"Chip pre-selected" ≠ "fast path". Always walk the flow once before assuming, and abort before any commit point if cost mismatches user intent.

### Files changed

- `automation/site-profiles/oiioii.md` — §12.10.1 fully rewritten as warning + correct guidance

---

## [1.2.0] - 2026-05-19 — OiiOii Seedance 2.0 pro Express SOP

Second-round real-world optimization based on a full interior-design ad generation session.

### New section: `automation/site-profiles/oiioii.md §12.10`

A **6-batch / ~25-second SOP** to take Seedance 2.0 pro 15s ads from home page to submitted, supersedes parts of §12.9.x where OiiOii UI has changed.

### Three new gotchas documented

1. **`\n` in `type` action triggers submit** — every newline = Enter keypress. Critical lesson. Single-line prompts with `[bracketed labels]` keep section semantics without using newlines.
2. **Canvas-embedded prompt input is transient** — clicking on canvas dismisses it, it's actually a thumbnail empty frame. Always use the LEFT panel's persistent input (findable via `find "main prompt textbox"`).
3. **「智能模型」toggle defaults ON** — system picks cheap models unless manually overridden. Must click model selector + pick Seedance 2.0 pro explicitly.

### Verified coordinates (viewport 705)

Full cheat sheet for the bottom toolbar + settings panel, validated against current OiiOii UI:
- Model chip, image/video tabs, all 4 video models
- Aspect ratio row (16:9 / 9:16 / 4:3 / 3:4 / 1:1 / 21:9)
- Duration controls (+1s per click, 10s default)
- Resolution buttons (480p / 720p / 1080p)
- Send button, cost preview

### Cost matrix (verified)

| Model | 5s | 10s | 15s |
|---|---|---|---|
| Seedance 2.0 pro | 70 | 140 | 210 |
| Seedance 2.0 fast | ~49 | ~98 | ~147 |

Rule of thumb: **Seedance 2.0 pro = 14 STAR/sec**.

### Hidden bonus discovered

Typing on the canvas-embedded input triggers a **free GPT-Image2 / Nano Pro** single-frame generation (no STAR cost). This produces a perfect reference image that can be used for i2v in the next step, dramatically improving visual consistency.

### Commercial ad prompt template

A `{swap}`-style template for ad prompts using v1.1.0 8-dimension + bracketed labels structure, with 5 vertical-market variations (interior / beauty / food / fashion / automotive).

### Files changed

- `automation/site-profiles/oiioii.md` — +124 lines (new §12.10)

---

## [1.1.0] - 2026-05-18 — Seedance 2.0 Community Evidence Update

Major upgrade to the Seedance 2.0 playbook based on 107 community-curated prompts.

### Source

Researched and consolidated from [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) (CC BY 4.0) — 6 hand-picked Featured + 101 community-validated prompts, last updated 2026-05-18. All reproduced content is attributed to original X handles per-preset.

### Corrected previous claims

The 2026-04-21 version contained 4 wrong assertions about Seedance 2.0 that have been corrected:

| Wrong (2026-04-21) | Corrected (2026-05-18) |
|---|---|
| `cinematic` is banned generic | Seedance 2.0 actively eats it (Featured #1/#3/#6 + 50%+ community) |
| 35mm/50mm lens tokens don't work | Lens focal lengths DO work (Wing Chun: `35mm follow / 50mm lateral tracking / 28mm push-in`) |
| 4+ shots in 15s is failure | 3-5 shots/15s is the sweet spot IF time blocks are used |
| Length sweet spot: 60-100 chars | Single-shot 60-100; Multi-shot 200-700 chars |
| All director names degrade | Auteur DP names ⚠️ weak; art movement / brand styles (Pixar / Ghibli / 90s anime / Fast and Furious) ✅ effective |

### New patterns documented

1. **Bracketed labels** (`[Style]`, `[Scene]`, `[Character]`, `[Shot N]`, `[Audio]`, `[Constraints]`) — the dominant Seedance 2.0 multi-shot structure
2. **Sub-labels within shot** (`Visuals:`, `Action:`, `Details:`, `Atmosphere:`, `Special Effects Details:`)
3. **Quoted dialogue with lip-sync** — including bilingual Japanese + English subtitles
4. **Format anchors** (`ESPN-style 16:9`, `IMAX Fantasy Camera`, `Sony A7S3`, `Unreal Engine 5 fluid rendering`)
5. **Native 4-modal audio** — `Sound design:` / `Audio Profile:` sectioning
6. **Negative as exclusion list** (natural language, not flag syntax)
7. **Lip-sync directives** (`200-400ms pauses, mouth only moves slightly`)
8. **Time block formats** — all of `[00:00-00:05]`, `(0-2s)`, `[00–05s]`, `0-3 seconds:`, `[0–2 SEC]` work
9. **Author attribution** for social-proof tracking

### New presets (10 added to templates/preset-packs.md)

Indexed S1-S10 — covering Romance, Hollywood Fashion, Healing/Lifestyle, Anime Duel, Music Video, Street Racing, Wing Chun, Sports Broadcast, Bilingual Anime, Epic Fantasy War. Mix of Chinese (5) and English (5) prompts.

### Files changed

- `references/seedance.md` — +205 lines (2026-05-18 section + corrections + 9 patterns + 2 templates)
- `references/community-prompt-patterns.md` — Seedance section completely rewritten (+62 net)
- `templates/preset-packs.md` — +411 lines (10 new community-validated presets)

---

## [1.0.0] - 2026-05-13

First open-source release.

### Core

- `SKILL.md` — top-level skill entry with auto-pilot pipeline, hard rules, and platform-aware token selection
- `references/community-prompt-patterns.md` — cross-platform research consolidation (5 meta rules + per-model signatures for 7 video and 5 image models)
- 14+ platform-specific prompt-craft references in `references/`
- 5 advanced vocabulary libraries (cinematic / commercial / VFX / sound / editing / camera-language)
- 30+ ready-to-use presets in `templates/preset-packs.md`

### Browser automation

- `automation/click-protocol.md` — reliable-click decision tree + token-optimization rules
- `automation/browser-guide.md` — high-level platform navigation
- Verified site profiles: OiiOii (with Seedance 2.0 pro deep playbook), Flow (Veo 3.1), Kling 3.0, Suno v5
- Stub site profiles for: Midjourney, Seedream, Runway, Sora, Vidu, Ideogram

### Evidence baseline

Built iteratively across real-world tasks with two rounds of head-to-head benchmarking:

- Iteration-1: with-skill 95% vs baseline 47% on objective assertions
- Iteration-2: with-skill won 3/3 head-to-head subjective evaluations on "senior director thinking"

### Notable design decisions

- **Meta priority order:** writing the prompt correctly once ≫ submitting fast 10 times. A wrong prompt costs ~10 min regeneration; a slow submit costs ~5 min.
- **Platform-aware token selection:** director names work on Midjourney / Sora 2 / Veo but degrade Flux / Nano Banana Pro / Seedance / Wan output. The skill enforces this split.
- **Token-efficient mode:** lazy-load references; never read all 12,000+ lines into context.
