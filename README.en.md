# Ab-instaCreator

Give your assistant product photos, a source link and your brand. Review editable HTML options, revise, then export approved PNGs with a five-hashtag caption.

## Included
- Twenty original style recipes covering minimalism through handwritten design.
- Brand onboarding: palette, fonts, logo, language, handle and writing examples.
- Connected carousel composition, single posts, stories and poll space.
- Portable tabbed HTML review generator, version-preserving workflow and full-size PNG exporter.
- Raleway English variable font with its OFL license; Arabic requires an appropriate supplied font.
- Working geometric carousel and poll-story examples. The assistant composes designs using the recipes; this is not a 20-theme automatic design engine.

## Install

Download [the full package](Ab-instaCreator-v0.1.0.zip), extract it, and use the extracted folder path below. This release is distributed as a source ZIP; direct GitHub marketplace installation is not available yet.
Private repository: your GitHub account must have access.

```bash
claude plugin marketplace add /absolute/path/to/Ab-instaCreator
claude plugin install ab-instacreator@ab-instacreator
```

For local Claude Code testing: `claude --plugin-dir /absolute/path/to/Ab-instaCreator`.
For a Codex skill, copy the complete `skills/insta-creator` directory into your configured skills directory and start a new session. Loading Claude marketplaces in Codex is not claimed.

## Ask naturally
“Create a two-slide connected carousel from this folder and product link. Give me three styles.”
“Keep the style, but align the title and subtitle as a block.”
“Create a story with space for a four-choice Instagram poll.”
“Export the approved version and give me the caption.”

## Run helpers
Node.js, Python 3, Playwright and Chromium are required. Image editing and source browsing use the host assistant's available tools.

```bash
npm install
npx playwright install chromium
python3 skills/insta-creator/scripts/gallery.py skills/insta-creator/examples/review.example.json output/review.html
node skills/insta-creator/scripts/export.cjs skills/insta-creator/templates/scene.html output/demo --approved
npm test
```

Default post/carousel: 1080×1440. Alternative post presets: 1080×1350 and 1080×1080. Story: 1080×1920. Approval must be real; `--approved` is a record of user approval, not a substitute. Existing PNGs are never overwritten. Inspect every export visually.

No Instagram posting, embedded service keys or automatic asset uploads. The assistant/service used for image processing may transmit supplied assets; local rendering itself uses a local browser. Mobile/cloud compatibility depends on the host and is not guaranteed.

See the [Arabic walkthrough](README.md), [workflow](Ab-instaCreator-v0.1.0.zip), [style index](Ab-instaCreator-v0.1.0.zip) and [development notes](Ab-instaCreator-v0.1.0.zip).
