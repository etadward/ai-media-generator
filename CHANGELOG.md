# Changelog

All notable changes to this skill are documented here.

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
