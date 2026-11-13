#!/usr/bin/env bash
# One-time runtime setup for PNG export (Playwright + Chromium).
# Installs into ~/.ab-instacreator (override: AB_INSTACREATOR_HOME) so it survives plugin
# updates and is shared by Claude Code and Codex. Safe to re-run.
set -euo pipefail
command -v node >/dev/null || { echo "Node.js 18+ is required: https://nodejs.org"; exit 1; }
command -v python3 >/dev/null || { echo "Python 3 is required"; exit 1; }
HOME_DIR="${AB_INSTACREATOR_HOME:-$HOME/.ab-instacreator}"
mkdir -p "$HOME_DIR"; cd "$HOME_DIR"
[ -f package.json ] || echo '{"name":"ab-instacreator-runtime","private":true,"dependencies":{"playwright":"^1.56.1"}}' > package.json
npm install --no-audit --no-fund
npx playwright install chromium
echo "OK: export runtime ready in $HOME_DIR"
