# Color
Colors come from, in order: (1) the user's brand palette, (2) a palette the user names, (3) a proposal from the `palette-603010` skill. Never impose a company's colors. Use the 60/30/10 rule: 60% base (background, large surfaces), 30% support (product, panels, main text), 10% accent (ONE focal thing: a headline word, CTA, glow or object).

## Choosing
1. **Brand palette exists** (`brand.local.json`): map `background` → 60 base, `surface` → 30 support, `accent` → 10 accent. Keep it. If a pair fails contrast, adjust shades within the brand family or swap the text color; tell the user.
2. **No palette, or the user asks "which colors"**: load the `palette-603010` skill. Offer 2–3 palettes that fit the product mood and the style, one line each (mood + why the accent works). Give hex with roles: `60 #062C30 · 30 #E5D4B8 · 10 #FF4E00`.
3. **Several design options**: give each option a different palette so options differ in more than style. Do not just recolor one layout.
4. **From the product photo**: note the product's dominant color and lightness. A dark product needs a light support/base or a rim light, glow or lighter plane behind it; a light product needs a darker base. The accent should sit about 150–180° from the base hue; it may echo a color already on the product (feels natural). Product colors the user confirms override anything guessed from a photo.

## Applying
- Base = scene background (flat or a soft same-hue gradient). Support = product backdrop/panels/cards and main text. Accent = used once or twice per slide; if it spreads, it stops being a focal point.
- Carousels: the palette is identical on every slice of the connected scene. Do not shift the base between slides.
- Bright bases (sky blue, yellow, neon green, turquoise, cyan) cannot carry white text: use the darkest palette color or near-black on them. Neon accents only on dark bases. Text on a bright accent pill uses the base or near-black; on a deep accent pill use white.
- Arabic: heavier weight and larger size on borderline pairs; always re-check contrast on the exact rendered size.

## Contrast check (required before review and export)
Run for every text/background pair that appears:
`python3 <palette-skill-dir>/scripts/contrast.py "#TEXT" "#BACKGROUND"` or `--palette <slug>` for all common pairs.
≥ 4.5 body text · 3–4.5 large/bold headlines only · < 3 shapes, glows, pills only (never text). Fix failures before showing the user, and record the chosen palette in the review registry (`"palette": {"base": "#…", "support": "#…", "accent": "#…"}`) so the review page shows the swatches.

## Starting points per style (suggestions, not rules)
| Style | Try first | Alternative |
|---|---|---|
| Minimalism | Monochrome Brown | Sky Fresh |
| Maximalism | Mauve Loud | Midnight Neon |
| Futuristic | Navy Idea | Midnight Neon |
| Vector art | Sky Fresh | Olive Standout |
| Collage | Brick Hook | Monochrome Brown |
| Retro | Olive Standout | Brick Hook |
| Cyberpunk | Midnight Neon | Navy Idea |
| Pop art | Mauve Loud | Sky Fresh |
| Glassmorphism | Navy Idea | Teal Brand |
| Clay | Mauve Loud (softened) | Sky Fresh |
| Pixel art | Midnight Neon | Petrol Gaming |
| Editorial | Monochrome Brown | Brick Hook |
| Y2K | Sky Fresh | Mauve Loud |
| Swiss | Brick Hook | Teal Brand |
| Surreal | Mauve Loud | Navy Idea |
| Bohemian | Olive Standout | Brick Hook |
| Victorian | Monochrome Brown | Mauve Loud |
| Graffiti | Midnight Neon | Brick Hook |
| Aurora | Petrol Gaming | Navy Idea |
| Handwritten | Olive Standout | Monochrome Brown |
