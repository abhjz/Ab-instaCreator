# Development
Entry point: `skills/insta-creator/SKILL.md`. The root contains both a Claude plugin manifest and a self-contained marketplace entry. Repository name is Ab-instaCreator; technical plugin/marketplace id is ab-instacreator; skill id is insta-creator.

`gallery.py` renders a project registry with local relative design paths, category tabs, status and style labels. It fails on duplicate ids or missing files and archives prior gallery HTML. `export.cjs` captures fixed-size artboards after fonts/images load, suppresses guides, validates dimensions, and refuses overwrites. It requires an explicit approval flag.

`templates/scene.html` demonstrates one continuous scene clipped into two slides. `templates/story.html` demonstrates an export-hidden poll guide. Templates are editable scaffolds, not automatic artwork generation.

Hosts: Claude Code loads the repo as a plugin (`.claude-plugin/`, `commands/`, `skills/`); Codex uses the skill folder via `./install.sh codex` (`skills/insta-creator/agents/openai.yaml`). `install.sh [claude|codex|all]` copies the skill; `scripts/setup.sh` installs Playwright + Chromium to `~/.ab-instacreator` (override with `AB_INSTACREATOR_HOME`), which `export.cjs` searches before other locations.

Run `npm test`, then export both templates to a fresh temporary directory. Inspect every rendered image. Integration-tested locally with existing Playwright and Chrome on macOS. For an installed Playwright elsewhere, install its browser with `npx playwright install chromium`. Optional environment overrides: AB_INSTACREATOR_HOME is the runtime folder; PLAYWRIGHT_MODULE is the resolved module path; CHROME_PATH selects an existing browser executable. No machine-specific paths are stored in this repository.

Before a release, review the publication file list. Keep private brand files, working outputs, secrets and third-party reference imagery out of Git. No production brand is included. GitHub upload is not proof of successful plugin installation; verify that separately in the target host.

Layout guidance lives in `skills/insta-creator/references/layout-patterns.md`. License: MIT (Raleway under OFL 1.1, see NOTICE.md).

Releases and versioning: see `docs/RELEASING.md` (`tools/bump_version.py` bumps plugin.json, package.json and the changelog together).
