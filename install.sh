#!/usr/bin/env bash
# Usage: ./install.sh [claude|codex|all]   (default: all)
# Codex target: $CODEX_SKILLS_DIR (default ~/.agents/skills; older setups may use ~/.codex/skills).
# Copies the skill into the host's skills folder. Claude can alternatively load the whole
# repo as a plugin: claude --plugin-dir <this folder>
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
SRC="$ROOT/skills/insta-creator"
TARGET="${1:-all}"
put(){ mkdir -p "$1"; rm -rf "$1/insta-creator"; cp -R "$SRC" "$1/insta-creator"; echo "Installed -> $1/insta-creator"; }
case "$TARGET" in
  claude) put "${CLAUDE_HOME:-$HOME/.claude}/skills" ;;
  codex)  put "${CODEX_SKILLS_DIR:-$HOME/.agents/skills}" ;;
  all)    put "${CLAUDE_HOME:-$HOME/.claude}/skills"; put "${CODEX_SKILLS_DIR:-$HOME/.agents/skills}" ;;
  *) echo "Usage: $0 [claude|codex|all]"; exit 1 ;;
esac
echo "Next: bash <installed skill>/scripts/setup.sh   # one-time Playwright + Chromium"
echo "Then start a NEW session and ask for an Instagram post."
