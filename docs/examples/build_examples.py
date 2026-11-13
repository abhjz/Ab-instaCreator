#!/usr/bin/env python3
"""Generates the brand-neutral README gallery: 20 style examples (2-slide connected carousels)
and 4 stories. Output HTML goes to ./_html, rendered PNGs to ./styles and ./stories by render.cjs.
Placeholders only: no real products, logos or brands. Some themes use common macOS/Windows system
fonts for flavour; the PNGs are what the README shows."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "_html"; OUT.mkdir(exist_ok=True)
FONT = "../../../skills/insta-creator/assets/Raleway-Variable.ttf"
SERIF = "'Didot','Bodoni 72','Playfair Display',Georgia,serif"
SANS = "Raleway,'Helvetica Neue',Arial,sans-serif"

# ---------------- themes ----------------
# bg: scene background · fg/mut/acc: text, muted, accent · font · hw: headline weight · hc: text-transform
# card: css for spec cards · o: object colour vars · deco: html behind content · extra: extra css
def T(**k): return k
THEMES = {
 "minimalism": T(title="Minimalism", layout="A", bg="#efede8", fg="#15161a", mut="#6b6a66", acc="#15161a", font=SANS, hw=700, hc="none", ls="-2px",
    card="border-bottom:2px solid #15161a1a", o="--d1:#4b5563;--d2:#111827;--s1:#7dd3fc;--s2:#6366f1;--s3:#1e1b4b;--r1:#fff;--r2:#d1d5db;--r3:#6b7280", deco=""),
 "maximalism": T(title="Maximalism", layout="B", bg="radial-gradient(circle at 15% 20%,#ff4d8d 0 22%,transparent 23%),radial-gradient(circle at 85% 80%,#2ec4b6 0 26%,transparent 27%),radial-gradient(circle at 60% 10%,#ffd23f 0 14%,transparent 15%),repeating-linear-gradient(45deg,#1a1033 0 40px,#241447 40px 80px)", fg="#fff", mut="#fff", acc="#ffd23f", font=SANS, hw=900, hc="uppercase", ls="-2px",
    card="background:#ff4d8d;border:6px solid #fff;color:#1a1033;border-radius:30px;padding:30px 36px;box-shadow:14px 14px 0 #ffd23f", o="--d1:#ffd23f;--d2:#ff4d8d;--s1:#2ec4b6;--s2:#7c3aed;--s3:#1a1033;--r1:#fff;--r2:#ffd23f;--r3:#ff4d8d", deco=""),
 "futuristic": T(title="Futuristic", layout="D", bg="radial-gradient(ellipse 1100px 800px at 1080px 700px,#0b3a6b,transparent 70%),linear-gradient(#050b1a,#02060f)", fg="#e6f6ff", mut="#7fb7d6", acc="#38e8ff", font=SANS, hw=300, hc="uppercase", ls="6px",
    card="border:1px solid #38e8ff66;background:#38e8ff0f;padding:30px 36px;border-radius:4px;box-shadow:0 0 30px #38e8ff22", o="--d1:#8fa3b8;--d2:#1b2a3d;--s1:#38e8ff;--s2:#1d4ed8;--s3:#020617;--r1:#fff;--r2:#38e8ff;--r3:#0b3a6b",
    deco='<div class="abs" style="left:0;top:0;width:2160px;height:1440px;background:linear-gradient(#38e8ff10 1px,transparent 1px),linear-gradient(90deg,#38e8ff10 1px,transparent 1px);background-size:80px 80px"></div><div class="abs" style="left:780px;top:260px;width:900px;height:900px;border:2px solid #38e8ff44;border-radius:50%"></div><div class="abs" style="left:880px;top:360px;width:700px;height:700px;border:2px dashed #38e8ff33;border-radius:50%"></div>'),
 "vector-art": T(title="Vector art", layout="C", bg="#ffe8d6", fg="#263238", mut="#5a6b73", acc="#ff6b6b", font=SANS, hw=800, hc="none", ls="-1px",
    card="border-top:5px solid #263238", o="--d1:#2a9d8f;--d2:#264653;--s1:#ffd166;--s2:#ff6b6b;--s3:#ef476f;--r1:#ffd166;--r2:#ff6b6b;--r3:#ef476f",
    deco='<div class="abs" style="left:-200px;top:900px;width:900px;height:900px;border-radius:50%;background:#ffd166"></div><div class="abs" style="left:1780px;top:-330px;width:700px;height:700px;border-radius:50%;background:#2a9d8f"></div><div class="abs" style="left:900px;top:1050px;width:0;height:0;border-left:260px solid transparent;border-right:260px solid transparent;border-bottom:450px solid #ff6b6b"></div>'),
 "collage": T(title="Collage", layout="C", bg="#e6dccb", fg="#222", mut="#6b5f4e", acc="#d64933", font=SERIF, hw=800, hc="none", ls="-1px",
    card="background:#fffdf7;padding:28px 34px;box-shadow:6px 8px 0 #0002;transform:rotate(-1.5deg)", o="--d1:#6b7280;--d2:#1f2937;--s1:#fde68a;--s2:#f59e0b;--s3:#92400e;--r1:#fff;--r2:#fca5a5;--r3:#d64933",
    deco='<div class="abs" style="left:380px;top:120px;width:700px;height:1100px;background:#fffdf7;transform:rotate(-3deg);box-shadow:8px 10px 0 #0002"></div><div class="abs" style="left:1200px;top:300px;width:520px;height:700px;background:#d64933;transform:rotate(4deg)"></div><div class="abs" style="left:640px;top:90px;width:180px;height:50px;background:#f3d98099;transform:rotate(-8deg)"></div>'),
 "retro": T(title="Retro", layout="A", bg="linear-gradient(#f4e1c1 0 90%,#e8b86a 90% 93%,#d9822b 93% 96%,#b5532a 96% 98%,#7a2e1f 98%)", fg="#3b2314", mut="#7a4a2a", acc="#b5532a", font="Georgia,serif", hw=900, hc="none", ls="-2px",
    card="border-bottom:3px solid #3b2314", o="--d1:#e8b86a;--d2:#7a2e1f;--s1:#f4e1c1;--s2:#d9822b;--s3:#b5532a;--r1:#fff3c4;--r2:#f59e0b;--r3:#b5532a", deco=""),
 "cyberpunk": T(title="Cyberpunk", layout="B", bg="radial-gradient(ellipse 900px 700px at 760px 1000px,#14506a,transparent 70%),#090a10", fg="#f2f4f8", mut="#aab2bd", acc="#f4ff3a", font=SANS, hw=800, hc="uppercase", ls="-1px",
    card="border:1px solid #ffffff30;background:#ffffff0f;border-radius:6px;padding:30px 36px;clip-path:polygon(0 0,calc(100% - 28px) 0,100% 28px,100% 100%,0 100%)", o="--d1:#4b5563;--d2:#111827;--s1:#7dd3fc;--s2:#6366f1;--s3:#1e1b4b;--r1:#fff;--r2:#f4ff3a;--r3:#14506a", deco=""),
 "pop-art": T(title="Pop art", layout="B", bg="radial-gradient(#00000026 18%,transparent 19%) 0 0/36px 36px,#ffd400", fg="#111", mut="#111", acc="#e8262b", font="Impact,'Arial Black',sans-serif", hw=900, hc="uppercase", ls="1px",
    card="background:#fff;border:8px solid #111;padding:26px 34px;box-shadow:12px 12px 0 #111", o="--d1:#e8262b;--d2:#7a0d10;--s1:#fff;--s2:#1e5bff;--s3:#0a2a8a;--r1:#fff;--r2:#e8262b;--r3:#7a0d10", deco=""),
 "glassmorphism": T(title="Glassmorphism", layout="D", bg="radial-gradient(circle at 20% 30%,#7c3aed 0,transparent 40%),radial-gradient(circle at 80% 70%,#06b6d4 0,transparent 42%),radial-gradient(circle at 55% 95%,#f472b6 0,transparent 35%),#0f0b2e", fg="#fff", mut="#d9d6f5", acc="#fff", font=SANS, hw=700, hc="none", ls="-2px",
    card="background:linear-gradient(135deg,#ffffff2e,#ffffff0d);border:1px solid #ffffff55;backdrop-filter:blur(24px);border-radius:32px;padding:34px 38px", o="--d1:#c4b5fd;--d2:#4c1d95;--s1:#a5f3fc;--s2:#8b5cf6;--s3:#312e81;--r1:#fff;--r2:#c4b5fd;--r3:#7c3aed", deco=""),
 "clay": T(title="Clay", layout="A", bg="#fbe8e0", fg="#4a2c2a", mut="#8a6a66", acc="#ef8a73", font=SANS, hw=800, hc="none", ls="-1px",
    card="background:#fff4ef;border-radius:44px;padding:30px 38px;box-shadow:inset -8px -10px 18px #e8c7bb,inset 8px 10px 18px #fff,10px 14px 24px #d9aea1", o="--d1:#f4b6a6;--d2:#ef8a73;--s1:#ffe3da;--s2:#f6b8a6;--s3:#ef8a73;--r1:#ffe3da;--r2:#f4b6a6;--r3:#ef8a73",
    extra=".dev{border-radius:120px;box-shadow:inset -14px -18px 30px #00000022,inset 14px 16px 26px #ffffff88,0 40px 50px #c98f8266}.dev:after{border-radius:96px}"),
 "pixel-art": T(title="Pixel art", layout="C", bg="#1b1b3a", fg="#fff", mut="#9aa0ff", acc="#ffcc00", font="'Courier New',Menlo,monospace", hw=900, hc="uppercase", ls="0",
    card="background:#2a2a5a;border:6px solid #ffcc00;padding:24px 30px;box-shadow:8px 8px 0 #000", o="--d1:#ff4d6d;--d2:#7a1230;--s1:#7cf5ff;--s2:#2d6cff;--s3:#102070;--r1:#fff;--r2:#ffcc00;--r3:#ff4d6d",
    extra=".dev,.orb{border-radius:0!important;box-shadow:12px 12px 0 #000!important}.dev:after{border-radius:0!important}.orb{background:var(--r3)!important;clip-path:polygon(20% 0,80% 0,80% 10%,90% 10%,90% 20%,100% 20%,100% 80%,90% 80%,90% 90%,80% 90%,80% 100%,20% 100%,20% 90%,10% 90%,10% 80%,0 80%,0 20%,10% 20%,10% 10%,20% 10%)}",
    deco='<div class="abs" style="left:0;bottom:0;width:2160px;height:160px;background:repeating-linear-gradient(90deg,#2d6cff 0 80px,#2457c9 80px 160px)"></div>'),
 "editorial": T(title="Editorial", layout="A", bg="#f7f5f0", fg="#111", mut="#555", acc="#b3261e", font=SERIF, hw=700, hc="none", ls="-3px",
    card="border-top:2px solid #111;border-bottom:1px solid #111;padding:18px 0", o="--d1:#6b7280;--d2:#111827;--s1:#fecaca;--s2:#b3261e;--s3:#450a0a;--r1:#fff;--r2:#e5e7eb;--r3:#6b7280", deco='<div class="abs" style="left:84px;top:150px;width:1992px;height:2px;background:#111"></div>'),
 "y2k": T(title="Y2K", layout="B", bg="radial-gradient(circle at 20% 20%,#ffd1f0,transparent 40%),radial-gradient(circle at 80% 80%,#b8f3ff,transparent 40%),linear-gradient(135deg,#e9e4ff,#fdf2ff)", fg="#3a1c71", mut="#7a5fc0", acc="#ff3fb4", font="'Trebuchet MS',Verdana,sans-serif", hw=900, hc="none", ls="-1px",
    card="background:linear-gradient(135deg,#ffffffcc,#ffffff66);border:3px solid #fff;border-radius:40px;padding:30px 38px;box-shadow:0 10px 30px #b69cff66", o="--d1:#e5e7eb;--d2:#9ca3af;--s1:#fbcfe8;--s2:#a78bfa;--s3:#38bdf8;--r1:#fff;--r2:#f9a8d4;--r3:#a78bfa",
    deco='<div class="abs" style="left:1700px;top:120px;font-size:140px;color:#ff3fb4">✦</div><div class="abs" style="left:140px;top:1100px;font-size:100px;color:#38bdf8">✦</div><div class="abs" style="left:1000px;top:90px;font-size:70px;color:#a78bfa">✧</div>'),
 "swiss": T(title="Swiss", layout="C", bg="#f5f4f0", fg="#101010", mut="#555", acc="#e63312", font=SANS, hw=800, hc="none", ls="-3px",
    card="border-top:3px solid #101010;padding:16px 0", o="--d1:#4b5563;--d2:#111827;--s1:#7dd3fc;--s2:#6366f1;--s3:#1e1b4b;--r1:#fff;--r2:#fca5a5;--r3:#dc2626",
    deco='<div class="abs" style="left:560px;top:0;width:600px;height:1440px;background:#e63312"></div>'),
 "surreal": T(title="Surreal", layout="D", bg="linear-gradient(#ffd9c7,#ffb6a0 45%,#6fb7c4 46%,#2c6e7f)", fg="#2b1d3a", mut="#5d4a6e", acc="#7a1fa2", font="Georgia,serif", hw=700, hc="none", ls="-1px",
    card="background:#ffffffbb;border-radius:36px;padding:30px 38px", o="--d1:#f5f5f4;--d2:#a8a29e;--s1:#fde68a;--s2:#fb7185;--s3:#7a1fa2;--r1:#fff;--r2:#fda4af;--r3:#a21caf;--alt:#fff",
    deco='<div class="abs" style="left:300px;top:1000px;width:800px;height:90px;background:radial-gradient(#0004,transparent 70%)"></div>'),
 "bohemian": T(title="Bohemian", layout="A", bg="#f1e4d3", fg="#4a2f1f", mut="#8a6a50", acc="#c8755a", font="Georgia,serif", hw=700, hc="none", ls="-1px",
    card="border-bottom:2px dashed #c8755a", o="--d1:#c8755a;--d2:#7d3f2a;--s1:#f6e0c8;--s2:#9caf88;--s3:#5f7a50;--r1:#f6e0c8;--r2:#9caf88;--r3:#c8755a",
    deco='<div class="abs" style="left:700px;top:560px;width:760px;height:900px;border-radius:380px 380px 0 0;background:#c8755a"></div><div class="abs" style="left:780px;top:640px;width:600px;height:820px;border-radius:300px 300px 0 0;background:#9caf88"></div><div class="abs" style="left:-100px;top:1000px;width:500px;height:500px;border-radius:50%;background:#e9c9a8"></div>'),
 "victorian": T(title="Victorian", layout="D", bg="radial-gradient(ellipse at 50% 50%,#5a1a2e,#2b0a14 75%)", fg="#f3e2b3", mut="#c9b27a", acc="#d4af37", font="'Didot','Bodoni 72',Georgia,serif", hw=700, hc="none", ls="0",
    card="border:2px solid #d4af37;outline:2px solid #d4af3766;outline-offset:6px;padding:28px 36px;background:#00000033", o="--d1:#d4af37;--d2:#7a5c12;--s1:#f3e2b3;--s2:#8b2e45;--s3:#2b0a14;--r1:#f3e2b3;--r2:#d4af37;--r3:#7a5c12",
    deco='<div class="abs" style="left:40px;top:40px;width:2080px;height:1360px;border:3px solid #d4af37"></div><div class="abs" style="left:62px;top:62px;width:2036px;height:1316px;border:1px solid #d4af3799"></div>'),
 "graffiti": T(title="Graffiti", layout="B", bg="repeating-linear-gradient(90deg,#6b6e72 0 90px,#63666a 90px 92px),#6b6e72", fg="#fff", mut="#e5e5e5", acc="#39ff88", font="Impact,'Arial Black',sans-serif", hw=900, hc="uppercase", ls="2px",
    card="background:#111;border:5px solid #ff2e88;padding:26px 34px;transform:rotate(-2deg);box-shadow:10px 10px 0 #39ff88", o="--d1:#ff2e88;--d2:#7a0f43;--s1:#39ff88;--s2:#00b4ff;--s3:#0b1f5e;--r1:#fff;--r2:#39ff88;--r3:#ff2e88",
    deco='<div class="abs" style="left:1480px;top:150px;width:500px;height:18px;background:#ff2e88;transform:rotate(-3deg)"></div><div class="abs" style="left:100px;top:1180px;width:40px;height:200px;border-radius:0 0 40px 40px;background:#39ff88"></div><div class="abs" style="left:190px;top:1180px;width:28px;height:120px;border-radius:0 0 28px 28px;background:#39ff88"></div>'),
 "aurora": T(title="Aurora", layout="D", bg="radial-gradient(ellipse 1100px 420px at 900px 260px,#10b98188,transparent 70%),radial-gradient(ellipse 900px 380px at 1500px 420px,#8b5cf688,transparent 70%),radial-gradient(ellipse 800px 300px at 300px 520px,#38bdf855,transparent 70%),#04120f", fg="#ecfff7", mut="#9ad9c4", acc="#6ee7b7", font=SANS, hw=700, hc="none", ls="-2px",
    card="background:#ffffff10;border:1px solid #6ee7b744;border-radius:28px;padding:32px 38px;backdrop-filter:blur(14px)", o="--d1:#6b7280;--d2:#0f172a;--s1:#6ee7b7;--s2:#8b5cf6;--s3:#0f172a;--r1:#fff;--r2:#6ee7b7;--r3:#8b5cf6", deco=""),
 "handwritten": T(title="Handwritten", layout="C", bg="repeating-linear-gradient(#fdf9ef 0 59px,#9ec5ee 59px 61px)", fg="#1e3a8a", mut="#4b5d9a", acc="#e11d48", font="'Bradley Hand','Segoe Print','Marker Felt',cursive", hw=700, hc="none", ls="0",
    card="background:#fff59d;padding:26px 30px;transform:rotate(-2deg);box-shadow:5px 7px 0 #0002", o="--d1:#6b7280;--d2:#1f2937;--s1:#bfdbfe;--s2:#60a5fa;--s3:#1e3a8a;--r1:#fff;--r2:#fecdd3;--r3:#e11d48",
    deco='<div class="abs" style="left:0;top:0;width:2160px;height:1440px;border-left:4px solid #e11d4855;margin-left:120px;pointer-events:none"></div>'),
}

CSS = """@font-face{font-family:Raleway;src:url('__FONT__');font-weight:100 900}*{box-sizing:border-box}body{margin:0}
.pair{display:flex;width:2160px}.slide{width:1080px;height:1440px;overflow:hidden;position:relative;flex:none}.scene{width:2160px;height:1440px;position:absolute;left:0;top:0;overflow:hidden}.second .scene{left:-1080px}.abs{position:absolute}
.dev{position:absolute;border-radius:64px;background:linear-gradient(145deg,var(--d1),var(--d2) 60%);box-shadow:inset 0 0 0 4px #ffffff22,0 60px 80px #0007}.dev:after{content:'';position:absolute;inset:26px;border-radius:44px;background:linear-gradient(160deg,var(--s1),var(--s2) 60%,var(--s3))}
.orb{position:absolute;border-radius:50%;background:radial-gradient(circle at 32% 28%,var(--r1),var(--r2) 30%,var(--r3) 78%);box-shadow:0 50px 70px #0006}
.h{margin:0;line-height:.98}.l{font-size:22px;letter-spacing:4px;font-weight:700;text-transform:uppercase}.p{font-size:30px;line-height:1.4}
.alt{color:var(--alt,var(--mut))}.k{font-size:19px;letter-spacing:3px;text-transform:uppercase;opacity:.75}.v{font-size:42px;font-weight:800;margin:4px 0 0}.row{display:flex;justify-content:space-between;font-size:30px;padding:22px 0}.chip{display:inline-block;border:2px solid currentColor;padding:14px 24px;font-size:24px;font-weight:700;letter-spacing:2px;margin:0 10px 12px 0}"""

def hl(t): return f'<span style="color:var(--acc)">{t}</span>'

def layout(t):
    L = t["layout"]
    brand = '<div class="abs l" style="left:84px;top:84px;color:var(--mut)">Your brand</div>'
    h1 = 'Product<br>name'
    if L == "A":   # seam hero
        return f'''<div class="dev" style="left:870px;top:250px;width:420px;height:860px;transform:rotate(-6deg)"></div>{brand}
<div class="abs" style="left:84px;top:200px;width:700px"><div class="l" style="margin-bottom:22px;color:var(--acc)">Category</div><h2 class="h hd" style="font-size:108px">{h1}</h2></div>
<div class="abs p" style="left:84px;top:1170px;color:var(--mut)">One clear benefit.<br>Verified from your link.</div>
<div class="abs" style="left:1360px;top:200px;width:640px"><div class="l" style="margin-bottom:22px;color:var(--acc)">Why it matters</div><h2 class="h hd" style="font-size:84px">Made for<br>real use.</h2></div>
<div class="abs" style="left:1360px;top:960px;width:640px"><div class="row cd"><span>Spec one</span><b>Value</b></div><div class="row cd"><span>Spec two</span><b>Value</b></div><div class="row cd"><span>Spec three</span><b>Value</b></div></div>'''
    if L == "B":   # off-center bleed
        return f'''<div class="dev" style="left:640px;top:760px;width:700px;height:1200px;transform:rotate(12deg)"></div>{brand}
<div class="abs l" style="left:1480px;top:84px;color:var(--mut)">Spec sheet</div>
<div class="abs" style="left:84px;top:190px;width:900px"><h2 class="h hd" style="font-size:112px">Big hero.<br>{hl("Bold")} cut.</h2><p class="p" style="margin-top:24px;color:var(--mut)">Product bleeds across the seam.</p></div>
<div class="abs cd" style="left:1480px;top:260px;width:520px"><div class="k">Power</div><div class="v">Value</div><div class="k" style="margin-top:22px">Size</div><div class="v">Value</div><div class="k" style="margin-top:22px">Mode</div><div class="v">Value</div></div>
<div class="abs" style="left:1560px;top:1250px;color:var(--acc)"><span class="chip">Feature</span><span class="chip">Feature</span></div>'''
    if L == "C":   # photo per slide
        return f'''<div class="orb" style="left:400px;top:640px;width:560px;height:560px;z-index:1"></div>
<div class="dev" style="left:1030px;top:130px;width:430px;height:880px;transform:rotate(8deg);z-index:2"></div>{brand}
<div class="abs" style="left:84px;top:230px;width:440px"><div class="l" style="margin-bottom:26px;color:var(--acc)">01 / 02</div><h2 class="h hd" style="font-size:150px">01</h2><p class="p" style="margin-top:34px;font-weight:700">First product.<br>First photo.</p></div>
<div class="abs l" style="left:1600px;top:84px;color:var(--mut)">02 / 02</div>
<div class="abs" style="left:1600px;top:190px;width:400px"><h2 class="h hd" style="font-size:66px">Second<br>angle.</h2></div>
<div class="abs cd" style="left:1560px;top:960px;width:440px"><div class="row"><span>Spec</span><b>Value</b></div><div class="row"><span>Spec</span><b>Value</b></div><div class="row"><span>Spec</span><b>Value</b></div></div>'''
    # D: big cropped hero + small alternate angle
    return f'''<div class="dev" style="left:640px;top:560px;width:740px;height:1250px;transform:rotate(16deg)"></div>{brand}
<div class="abs" style="left:84px;top:190px;width:640px"><div class="l" style="margin-bottom:22px;color:var(--acc)">Category</div><h2 class="h hd" style="font-size:104px">{h1}</h2><p class="p" style="margin-top:26px;color:var(--mut)">A new addition to<br>your collection.</p></div>
<div class="abs cd" style="left:1580px;top:190px;width:420px"><div class="k">Material</div><div class="v">Value</div><div class="k" style="margin-top:22px">Size</div><div class="v">Value</div></div>
<div class="abs cd" style="left:1580px;top:540px;width:420px"><div class="k">Power</div><div class="v">Value</div><div class="k" style="margin-top:22px">Mode</div><div class="v">Value</div></div>
<div class="orb" style="left:1580px;top:930px;width:340px;height:340px"></div>
<div class="abs l alt" style="left:1580px;top:1310px">Alternate angle</div>'''

def carousel(key, t):
    css = CSS.replace('__FONT__', FONT)
    css += f'.scene{{background:{t["bg"]};color:{t["fg"]};font-family:{t["font"]};{t["o"]};--fg:{t["fg"]};--mut:{t["mut"]};--acc:{t["acc"]}}}'
    css += f'.hd{{font-weight:{t["hw"]};text-transform:{t["hc"]};letter-spacing:{t["ls"]}}}.cd{{{t["card"]}}}'
    css += t.get("extra", "")
    scene = t.get("deco","") + layout(t)
    return f"<!doctype html><meta charset=utf-8><style>{css}</style><div class=pair><div class=slide><div class=scene>{scene}</div></div><div class='slide second'></div></div><script>document.querySelector('.second').append(document.querySelector('.scene').cloneNode(true))</script>"

def story(key, t, variant):
    css = CSS.replace('__FONT__', FONT)
    css += f'.slide{{width:1080px;height:1920px}}.scene{{width:1080px;height:1920px;position:absolute;background:{t["bg"]};color:{t["fg"]};font-family:{t["font"]};{t["o"]};--fg:{t["fg"]};--mut:{t["mut"]};--acc:{t["acc"]}}}'
    css += f'.hd{{font-weight:{t["hw"]};text-transform:{t["hc"]};letter-spacing:{t["ls"]}}}.cd{{{t["card"]}}}' + t.get("extra", "")
    head = {"a": "Which one<br>feels like you?", "b": "This<br>or that?", "c": "Quick<br>tip.", "d": "New<br>drop."}[variant]
    sub = {"a": "Tap your pick below.", "b": "Vote in the poll.", "c": "One idea, done in a minute.", "d": "Available this week."}[variant]
    obj = {"a": '<div class="orb" style="left:620px;top:690px;width:280px;height:280px"></div><div class="dev" style="left:300px;top:670px;width:200px;height:310px;transform:rotate(-8deg);border-radius:48px"></div>',
           "b": '<div class="dev" style="left:380px;top:680px;width:320px;height:290px;transform:rotate(-6deg);border-radius:56px"></div>',
           "c": '<div class="orb" style="left:390px;top:680px;width:300px;height:300px"></div>',
           "d": '<div class="dev" style="left:340px;top:670px;width:200px;height:310px;transform:rotate(10deg);border-radius:48px"></div><div class="orb" style="left:610px;top:720px;width:240px;height:240px"></div>'}[variant]
    scene = f'''{t.get("deco","").replace("2160px","1080px") if key in ("pop-art","aurora") else ""}
<div class="abs l" style="left:84px;top:210px;color:var(--mut)">Your brand</div>
<div class="abs" style="left:84px;top:290px;width:900px"><h2 class="h hd" style="font-size:118px">{head}</h2><p class="p" style="margin-top:22px;color:var(--mut)">{sub}</p></div>
{obj}
<div class="abs l" style="left:84px;bottom:260px;color:var(--mut)">yourwebsite.com</div>'''
    return f"<!doctype html><meta charset=utf-8><style>{css}</style><div class=slide><div class=scene>{scene}</div></div>"

if __name__ == "__main__":
    for k, t in THEMES.items():
        (OUT / f"style-{k}.html").write_text(carousel(k, t))
    for k, v in [("minimalism", "a"), ("cyberpunk", "b"), ("pop-art", "c"), ("aurora", "d")]:
        (OUT / f"story-{k}.html").write_text(story(k, THEMES[k], v))
    print(len(THEMES), "styles +4 stories")
