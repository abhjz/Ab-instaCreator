# HTML review and PNG delivery
Each design HTML has fixed artboards marked `data-export-slide`, with integer `data-width` and `data-height`. For a connected scene, duplicate identical scene markup inside each viewport and offset by -index×width. Preview CSS can scale display; export CSS must restore exact size and remove wrappers, controls and guides. `templates/scene.html` demonstrates the contract.

Gallery registry stores id, title, category (posts/stories or custom product tab), style, version, path and status. `scripts/gallery.py review.json review.html` renders tabs, hash navigation and style names. Registry is project-owned. Append revisions; do not silently replace accepted designs. All HTML and images stay with their relative dependencies when shared.

Export command from repository root:
`node <skill-dir>/scripts/export.cjs design.html output-folder --approved` (`<skill-dir>` = the folder holding SKILL.md; first run `bash <skill-dir>/scripts/setup.sh` if Playwright is missing)
`--approved` records approval already obtained from the user; never add it on your own merely to bypass the gate. Existing files cause a failure; choose a new version. Export waits for fonts and images, blocks failed images, enforces positive dimensions, hides review guides, and produces one PNG per artboard. It cannot judge aesthetics; inspect every PNG afterward. Runtime supports `PLAYWRIGHT_MODULE` and `CHROME_PATH` overrides; normal installs use local Playwright and its Chromium.

Deliver direct PNG links, dimensions, caption with exactly five hashtags, and source/editable HTML link. A separate story is its own 1080×1920 composition, not a stretched post. Preserve text hierarchy when adapting. An HTML review hosted only on a local disk cannot be opened by another person's computer; share the whole folder/ZIP or an explicitly authorized hosted page. Do not claim an external deployment happened unless verified.

Validate a draft caption with `python3 scripts/check_caption.py caption.txt`; the check counts hashtags anywhere in the text and rejects duplicates.
