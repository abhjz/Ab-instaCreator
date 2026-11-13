#!/usr/bin/env python3
"""Writes _html/palettes.html (3x3 sheet of the nine 60/30/10 palettes) from palette-603010/palettes.json. render.cjs turns it into docs/palettes.png."""
import json, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location('c', ROOT / 'skills/palette-603010/scripts/contrast.py'); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
ps = c.palettes(); cards = ''
for p in ps:
    b, s, a = p['base'], p['support'], p['accent']
    on = '#FFFFFF' if c.ratio('#FFFFFF', b) >= c.ratio('#0A0A0A', b) else '#0A0A0A'
    pill = '#FFFFFF' if c.ratio('#FFFFFF', a) >= c.ratio('#0A0A0A', a) else '#0A0A0A'
    cards += f'''<div class="card"><div class="bar"><i style="flex:60;background:{b}"></i><i style="flex:30;background:{s}"></i><i style="flex:10;background:{a}"></i></div>
<div class="demo" style="background:{b};color:{on}"><span class="dot" style="background:{s}"></span><span>Headline</span><em style="background:{a};color:{pill}">accent</em></div>
<h3>{p['name']}</h3><p>{p['mood']}</p><code>60 {b} · 30 {s} · 10 {a}</code></div>'''
html = f'''<!doctype html><meta charset=utf-8><style>*{{box-sizing:border-box}}body{{margin:0;padding:36px;width:1600px;background:#0e0f14;color:#fff;font-family:'Helvetica Neue',Arial,sans-serif}}
h1{{margin:0 0 6px;font-size:40px}}.sub{{color:#aab;margin:0 0 28px;font-size:20px}}.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.card{{background:#171923;border-radius:18px;padding:16px;border:1px solid #ffffff18}}.bar{{display:flex;height:16px;border-radius:8px;overflow:hidden;margin-bottom:12px}}.bar i{{display:block}}
.demo{{height:120px;border-radius:12px;display:flex;align-items:center;gap:18px;padding:0 22px;font-size:26px}}.dot{{width:56px;height:56px;border-radius:50%}}.demo em{{font-style:normal;font-weight:800;padding:8px 18px;border-radius:30px;font-size:24px}}
h3{{margin:14px 0 2px;font-size:22px}}p{{margin:0 0 8px;color:#9aa;font-size:15px}}code{{font-size:14px;color:#cfd3e6}}</style>
<h1>9 tested 60/30/10 palettes</h1><p class=sub>60% base · 30% support · 10% accent. Included as the palette-603010 skill; contrast-checked before every design.</p><div class=g>{cards}</div>'''
(HERE / '_html').mkdir(exist_ok=True); (HERE / '_html/palettes.html').write_text(html)
