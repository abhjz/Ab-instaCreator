# Ab-instaCreator

**Instagram posts, connected carousels and stories, designed by your AI assistant.** Give it product photos, a product link and your brand. It builds editable designs in many styles and layouts, you review them on one page, then it exports approved PNGs and a caption with exactly five hashtags.

Works in **Claude Code** and **Codex**. It never posts to Instagram for you.

![Ab-instaCreator](docs/banner.png)

## What it creates

| Format | What you get |
|---|---|
| **Posts** | Single designs at 1080×1440 (or 1080×1350 / 1080×1080) |
| **Connected carousels** | 2–3 slides cut from one continuous scene, so the product flows across the swipe |
| **Stories** | 1080×1920 with a clean area reserved for the Instagram poll sticker |

**20 style guides:** minimalism, maximalism, futuristic, vector art, collage, retro, cyberpunk, pop art, glassmorphism, clay, pixel art, editorial, Y2K, Swiss, surreal, bohemian, Victorian, graffiti, aurora, handwritten.

**4 layout patterns:** centered seam hero · off-center hero bleeding across the seam · a different photo per slide (2–3 photos) · big cropped hero with a small alternate angle. The assistant varies layouts across the options it gives you.

Plus: brand profile (logo, palette, fonts, language), product facts saved with their source link, a tabbed review page, and approval-gated PNG export.

## Gallery

Every example below is a brand-neutral placeholder design made with the plugin's own style guides and layouts. Your real photos, logo and copy replace the placeholders.

### All 20 styles (2-slide connected carousels)

| | |
|---|---|
| ![Minimalism](docs/examples/styles/minimalism.png)<br>**1. Minimalism** · Seam hero | ![Maximalism](docs/examples/styles/maximalism.png)<br>**2. Maximalism** · Off-center hero |
| ![Futuristic](docs/examples/styles/futuristic.png)<br>**3. Futuristic** · Cropped hero + alternate angle | ![Vector art](docs/examples/styles/vector-art.png)<br>**4. Vector art** · Photo per slide |
| ![Collage](docs/examples/styles/collage.png)<br>**5. Collage** · Photo per slide | ![Retro](docs/examples/styles/retro.png)<br>**6. Retro** · Seam hero |
| ![Cyberpunk](docs/examples/styles/cyberpunk.png)<br>**7. Cyberpunk** · Off-center hero | ![Pop art](docs/examples/styles/pop-art.png)<br>**8. Pop art** · Off-center hero |
| ![Glassmorphism](docs/examples/styles/glassmorphism.png)<br>**9. Glassmorphism** · Cropped hero + alternate angle | ![Clay](docs/examples/styles/clay.png)<br>**10. Clay** · Seam hero |
| ![Pixel art](docs/examples/styles/pixel-art.png)<br>**11. Pixel art** · Photo per slide | ![Editorial](docs/examples/styles/editorial.png)<br>**12. Editorial** · Seam hero |
| ![Y2K](docs/examples/styles/y2k.png)<br>**13. Y2K** · Off-center hero | ![Swiss](docs/examples/styles/swiss.png)<br>**14. Swiss** · Photo per slide |
| ![Surreal](docs/examples/styles/surreal.png)<br>**15. Surreal** · Cropped hero + alternate angle | ![Bohemian](docs/examples/styles/bohemian.png)<br>**16. Bohemian** · Seam hero |
| ![Victorian](docs/examples/styles/victorian.png)<br>**17. Victorian** · Cropped hero + alternate angle | ![Graffiti](docs/examples/styles/graffiti.png)<br>**18. Graffiti** · Off-center hero |
| ![Aurora](docs/examples/styles/aurora.png)<br>**19. Aurora** · Cropped hero + alternate angle | ![Handwritten](docs/examples/styles/handwritten.png)<br>**20. Handwritten** · Photo per slide |

### Stories

Each story keeps the lower middle clear for Instagram's poll sticker. Nothing fake is burned into the PNG.

| | | | |
|---|---|---|---|
| ![Minimalism](docs/examples/stories/minimalism.png) | ![Cyberpunk](docs/examples/stories/cyberpunk.png) | ![Pop art](docs/examples/stories/pop-art.png) | ![Aurora](docs/examples/stories/aurora.png) |
| **Minimalism** | **Cyberpunk** | **Pop art** | **Aurora** |

### Layout patterns

| Layout | Used in |
|---|---|
| **Seam hero**: product centered on the seam | Minimalism, Clay, Retro, Editorial, Bohemian |
| **Off-center hero**: large, anchored low, bleeding across the seam | Maximalism, Cyberpunk, Pop art, Y2K, Graffiti |
| **Photo per slide**: a different photo on each slide | Vector art, Collage, Pixel art, Swiss, Handwritten |
| **Cropped hero + alternate angle** | Futuristic, Glassmorphism, Surreal, Victorian, Aurora |

The assistant mixes styles and layouts, so you can ask for "Swiss style with an off-center hero".

## Install

You need: Node.js 18+, Python 3, and Claude Code or Codex.

### Claude Code (plugin)
The repo is private, so your GitHub account needs access and git must be signed in (`gh auth login` is the easy way).

```bash
claude plugin marketplace add abhjz/Ab-instaCreator
claude plugin install ab-instacreator@ab-instacreator
```

Or from a local folder (download the ZIP, extract it):

```bash
claude plugin marketplace add /absolute/path/to/Ab-instaCreator
claude plugin install ab-instacreator@ab-instacreator
```

Try without installing: `claude --plugin-dir /absolute/path/to/Ab-instaCreator`

### Codex (skill)
```bash
git clone https://github.com/abhjz/Ab-instaCreator.git
cd Ab-instaCreator
./install.sh codex
```
This copies the skill to `~/.agents/skills/insta-creator`. Using a different folder? `CODEX_SKILLS_DIR=~/.codex/skills ./install.sh codex`.

### Both at once (skill mode)
`./install.sh all` installs the skill into `~/.claude/skills` and `~/.agents/skills`.

### One-time export setup (both hosts)
```bash
bash skills/insta-creator/scripts/setup.sh
```
Installs Playwright + Chromium into `~/.ab-instacreator` (shared, survives updates). Or just tell your assistant: "set up the export tools".

**Start a NEW session after installing.**

## Use it

| Step | Claude Code | Codex |
|---|---|---|
| 1. Brand (first time only) | `/ab-instacreator:insta-setup` | "Use $insta-creator to set up my brand" |
| 2. Create | `/ab-instacreator:insta 2-slide carousel, 3 styles` + attach photos + paste the product link | "Use $insta-creator: 2-slide carousel, 3 styles" + photos + link |
| 3. Review | Open `review.html`. Toggle connected / separate view. | same |
| 4. Revise | Plain words: "use style B", "move the product lower" | same |
| 5. Approve + export | `/ab-instacreator:insta-export` | "Export the approved version" |
| 6. Post | You post it yourself | same |

Other commands: `/ab-instacreator:insta-styles` shows style comparisons. Skill mode (no plugin) has no slash commands: just describe what you want and mention `insta-creator`.

Tips: more photos give more layouts. Say the size if you want a story (1080×1920) or a square (1080×1080). Say "different layouts" for different product placements. Default post size is 1080×1440.

## Output
In your project folder (never inside the plugin): `review.html`, one editable HTML per design, `facts.json`, and after approval `design-Slide-1.png`, `design-Slide-2.png`, … plus the caption (exactly five hashtags). Existing PNGs are never overwritten.

## Update
```bash
claude plugin marketplace update ab-instacreator
claude plugin update ab-instacreator@ab-instacreator
```
Codex: `git pull && ./install.sh codex`.

## Troubleshooting
| Problem | Fix |
|---|---|
| Repo link gives 404 | The repo is private. Sign in with an account that has access (`gh auth login`). |
| Plugin/commands missing | Run `claude plugin list`, then open a new session. |
| Skill not found in Codex | Check the folder from `install.sh`, then open a new session. |
| "Playwright not found" | `bash skills/insta-creator/scripts/setup.sh` |
| No Chromium | Same command, or set `CHROME_PATH` to an existing Chrome. |
| Export refuses to write | The file exists. Export a new version folder. |
| Product image missing after moving a project | Keep the `assets/` folder next to the HTML. |
| Arabic text looks wrong | Supply an Arabic font and check RTL. Bundled Raleway is English only. |

## Limits and privacy
- No Instagram posting, scheduling, API keys or uploads.
- Background removal and web browsing use your assistant's own tools; your host may send images to its service.
- Tested: Claude Code on macOS (plugin validate, demo exports, real product designs). Codex install is untested; mobile/cloud is not guaranteed.

See the [Arabic guide](README.md), [workflow](skills/insta-creator/references/workflow.md), [styles](skills/insta-creator/references/styles.md), [layout patterns](skills/insta-creator/references/layout-patterns.md), [development notes](docs/DEVELOPMENT.md).

## License
MIT. See [LICENSE](LICENSE) and [NOTICE](NOTICE.md) (Raleway font is OFL 1.1).
