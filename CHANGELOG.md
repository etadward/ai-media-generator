# Changelog

All notable changes to this skill are documented here.

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
