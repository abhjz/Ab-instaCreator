# Releasing a new version

Users get updates through Claude Code's marketplace auto-update (they turn it on once, see the README). Auto-update compares the `version` in `.claude-plugin/plugin.json`. **Same number = no update**, even if files changed. So every release bumps the number.

## Steps
1. Make and test your changes (`claude --plugin-dir .`).
2. Bump + changelog + tests in one go:
   ```bash
   python3 tools/bump_version.py 0.3.0 "What changed" "Another change"
   ```
   This updates `.claude-plugin/plugin.json`, `package.json` and `CHANGELOG.md`, then runs the tests. The tests fail if the three versions disagree.
3. `claude plugin validate .`
4. Commit and push to `main`:
   ```bash
   git add -A && git commit -m "v0.3.0: short summary" && git push
   ```
5. Check your own copy gets it: `claude plugin marketplace update ab-instacreator && claude plugin update ab-instacreator@ab-instacreator`, then `claude plugin list` shows the new version.
6. Optional: tag it (`git tag v0.3.0 && git push --tags`) and create a GitHub release with the changelog lines.

## Version numbers
- **PATCH** (0.2.1): fixes, docs, gallery images.
- **MINOR** (0.3.0): new styles, layouts, commands or features.
- **MAJOR** (1.0.0): breaking changes (renamed commands, changed output format).

## New styles or layouts
Add the guide under `skills/insta-creator/references/`, then regenerate the gallery: `python3 docs/examples/build_examples.py && node docs/examples/render.cjs` (update README tables if you add a style).

## Private vs public
While the repo is private, users' background auto-update needs git sign-in (`gh auth login` or `GITHUB_TOKEN`). A public repo needs nothing, which is why a public release is the smoothest for users.
