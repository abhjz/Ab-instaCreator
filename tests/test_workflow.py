import importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module(name):
 p=ROOT/'skills/insta-creator/scripts'/f'{name}.py';spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class WorkflowTests(unittest.TestCase):
 def test_gallery_moves_and_escapes(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);(p/'design.html').write_text('<h1>demo</h1>');reg=p/'review.json';reg.write_text(json.dumps({'title':'<test>','designs':[{'id':'one','category':'Posts','title':'A < B','path':'design.html'}]}));out=p/'nested/review.html';module('gallery').render(reg,out);s=out.read_text();self.assertIn('../design.html',s);self.assertIn('A &lt; B',s);module('gallery').render(reg,out);self.assertEqual(len(list((out.parent/'_Archive').glob('*.html'))),1)
 def test_missing_asset_fails(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);reg=p/'r.json';reg.write_text(json.dumps({'designs':[{'id':'a','category':'Posts','path':'missing.html'}]}))
   with self.assertRaises(ValueError):module('gallery').render(reg,p/'out.html')
 def test_caption_all_positions(self):
  c=module('check_caption');self.assertEqual(len(c.check('#one text #two #three #four #five')),5)
  with self.assertRaises(ValueError):c.check('#one #two #three #four #five #six')
  with self.assertRaises(ValueError):c.check('#one #one #three #four #five')
 def test_twenty_guides_and_manifest(self):
  self.assertEqual(len(list((ROOT/'skills/insta-creator/references/styles').glob('*.md'))),20)
  manifest=json.loads((ROOT/'.claude-plugin/plugin.json').read_text());market=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text());self.assertEqual(manifest['name'],market['plugins'][0]['name']);self.assertTrue((ROOT/'skills/insta-creator/SKILL.md').is_file())
def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class PaletteTests(unittest.TestCase):
 def test_skills_have_matching_names(self):
  import re
  for d in (ROOT/'skills').iterdir():
   if d.is_dir():
    head=(d/'SKILL.md').read_text().split('---')[1];self.assertEqual(re.search(r'^name:\s*(\S+)',head,re.M).group(1),d.name)
 def test_nine_valid_palettes(self):
  import re
  ps=json.loads((ROOT/'skills/palette-603010/palettes.json').read_text())['palettes'];self.assertEqual(len(ps),9)
  for p in ps:
   for k in('base','support','accent'):self.assertRegex(p[k],r'^#[0-9A-F]{6}$')
 def test_contrast_math(self):
  c=load(ROOT/'skills/palette-603010/scripts/contrast.py','contrast')
  self.assertAlmostEqual(c.ratio('#FFFFFF','#000000'),21,places=1);self.assertLess(c.ratio('#FFFFFF','#52C5FF'),3);self.assertGreater(c.ratio('#FFFFFF','#062C30'),7)
  for p in c.palettes():self.assertIn(p['name'],c.report(p))
 def test_gallery_swatches_and_injection(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td);(p/'d.html').write_text('x');reg=p/'r.json'
   reg.write_text(json.dumps({'designs':[{'id':'a','category':'Posts','path':'d.html','palette':{'base':'#062C30','support':'#E5D4B8','accent':'red;}</style><script>x</script>'}}]}));out=p/'o.html';module('gallery').render(reg,out);h=out.read_text()
   self.assertIn('#062C30',h);self.assertNotIn('<script>x</script>',h)
 def test_color_guide_wired(self):
  self.assertTrue((ROOT/'skills/insta-creator/references/color.md').is_file());self.assertIn('color.md',(ROOT/'skills/insta-creator/SKILL.md').read_text());self.assertTrue((ROOT/'commands/insta-palette.md').is_file())
class VersionTests(unittest.TestCase):
 def test_versions_agree(self):
  import re
  a=json.loads((ROOT/'.claude-plugin/plugin.json').read_text())['version'];b=json.loads((ROOT/'package.json').read_text())['version']
  c=re.search(r'^## (\d+\.\d+\.\d+)',(ROOT/'CHANGELOG.md').read_text(),re.M).group(1)
  self.assertEqual(a,b);self.assertEqual(a,c)
class InstallTests(unittest.TestCase):
 def test_install_both_hosts(self):
  import subprocess,os
  with tempfile.TemporaryDirectory() as td:
   env=dict(os.environ,CLAUDE_HOME=td+'/c',CODEX_SKILLS_DIR=td+'/x/skills');subprocess.run(['bash',str(ROOT/'install.sh'),'all'],check=True,env=env,capture_output=True)
   for h in('c','x'):self.assertTrue((Path(td)/h/'skills/insta-creator/SKILL.md').is_file());self.assertTrue((Path(td)/h/'skills/insta-creator/scripts/export.cjs').is_file());self.assertTrue((Path(td)/h/'skills/palette-603010/scripts/contrast.py').is_file())
if __name__=='__main__':unittest.main()
