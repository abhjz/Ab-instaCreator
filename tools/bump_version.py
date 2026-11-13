#!/usr/bin/env python3
"""Release helper. Usage: python3 tools/bump_version.py 0.3.0 "First change" ["Second change" ...]
Updates plugin.json + package.json + CHANGELOG.md, then runs the tests. Commit and push afterwards;
installed copies update when the version number changes."""
import json, re, subprocess, sys, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
if len(sys.argv) < 3 or not re.fullmatch(r"\d+\.\d+\.\d+", sys.argv[1]):
    sys.exit(__doc__)
ver, notes = sys.argv[1], sys.argv[2:]
for f in (".claude-plugin/plugin.json", "package.json"):
    p = ROOT / f; d = json.loads(p.read_text()); d["version"] = ver
    p.write_text(json.dumps(d, indent=2) + "\n")
cl = ROOT / "CHANGELOG.md"; s = cl.read_text()
entry = f"## {ver} · {datetime.date.today()}\n" + "".join(f"- {n}\n" for n in notes) + "\n"
cl.write_text(s.replace("# Changelog\n", "# Changelog\n" + entry, 1))
subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], cwd=ROOT, check=True)
print(f"Bumped to {ver}. Next: git add -A && git commit -m 'v{ver}' && git push")
