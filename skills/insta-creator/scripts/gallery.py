"""Render a portable, tabbed review gallery from an explicit JSON registry."""
import json,html,sys,os
from pathlib import Path
from urllib.parse import quote

def render(registry, destination):
    registry=Path(registry).resolve();destination=Path(destination).resolve()
    data=json.loads(registry.read_text());items=data['designs'];ids=set();tabs=[];panels=[]
    for item in items:
        ident=item['id']
        if ident in ids: raise ValueError('Duplicate design id: '+ident)
        ids.add(ident)
        if not item['category'] in tabs: tabs.append(item['category'])
        source=(registry.parent/item['path']).resolve()
        if not source.is_file():raise ValueError('Missing design: '+str(source))
        url=quote(os.path.relpath(source,destination.parent),safe='/')
        fields={k:html.escape(str(item.get(k,'')),quote=True) for k in ['id','title','category','style','version','status']}
        panels.append(f'''<article data-category="{fields['category']}" id="{fields['id']}"><h2>{fields['title']}</h2><p>{fields['style']} · {fields['version']} · {fields['status']}</p><iframe loading="lazy" title="{fields['title']}" src="{url}"></iframe><a href="{url}" target="_blank" rel="noopener">Open full preview</a></article>''')
    buttons=''.join('<button data-tab="'+html.escape(t,quote=True)+'">'+html.escape(t)+'</button>' for t in tabs)
    title=html.escape(data.get('title','Design review'))
    result='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+'''</title><style>body{margin:0;background:#111318;color:white;font:16px system-ui}header,main{max-width:1400px;margin:auto;padding:24px}nav{display:flex;gap:12px;flex-wrap:wrap}button{font:inherit;padding:12px 22px;border:1px solid #515866;border-radius:30px;background:#252933;color:white;cursor:pointer}button[aria-selected=true]{background:#8ef0cf;color:#111318}article{margin:30px 0;border-top:1px solid #515866;padding:20px 0}iframe{border:0;width:100%;height:900px;background:#eee}a{color:#8ef0cf}p{color:#b6bdc9}[hidden]{display:none!important}@media(max-width:650px){iframe{height:650px}}</style><header><h1>'''+title+'''</h1><p>Choose a category, compare styles, then approve a version for export.</p><nav>'''+buttons+'''</nav></header><main>'''+''.join(panels)+'''</main><script>const buttons=[...document.querySelectorAll('[data-tab]')];function select(t){if(!buttons.some(b=>b.dataset.tab===t))t=buttons[0]?.dataset.tab;for(const b of buttons)b.setAttribute('aria-selected',b.dataset.tab===t);for(const a of document.querySelectorAll('article'))a.hidden=a.dataset.category!==t;}for(const b of buttons)b.onclick=()=>{location.hash=encodeURIComponent(b.dataset.tab);select(b.dataset.tab)};onhashchange=()=>select(decodeURIComponent(location.hash.slice(1)));onhashchange();</script></html>'''
    destination.parent.mkdir(parents=True,exist_ok=True)
    if destination.exists():
        import time,shutil
        archive=destination.parent/'_Archive';archive.mkdir(exist_ok=True)
        shutil.copy2(destination,archive/(destination.stem+'-'+str(time.time_ns())+destination.suffix))
    destination.write_text(result)
if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('Usage: python3 gallery.py review.json review.html')
    render(*sys.argv[1:])
