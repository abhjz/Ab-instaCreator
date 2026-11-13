# Changelog
## 0.2.0 · 2026-11-13
- Works as a standalone skill in Claude Code and Codex: `install.sh [claude|codex|all]` and `scripts/setup.sh` (Playwright + Chromium next to the skill).
- `export.cjs` finds Playwright in several locations and falls back to a system Chrome; clearer errors.
- Host-neutral skill wording; command files use `${CLAUDE_PLUGIN_ROOT}`; docs paths are skill-relative.
- Added install test.
- Layout patterns guide: off-center hero, photo per slide, big cropped hero + alternate angle.
- `setup.sh` installs the export runtime to ~/.ab-instacreator (shared, survives updates).
- Rewrote setup docs (EN + AR): GitHub marketplace, Codex, update, troubleshooting.

## 0.1.0 · 2026-11-13
- Brand-neutral content workflow with twenty style guides.
- Connected carousel and poll-story scaffolds.
- Tabbed review generator, approval-aware PNG export and caption checks.
- Arabic and English documentation, font license and local checks.
