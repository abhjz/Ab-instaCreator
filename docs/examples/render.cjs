// Renders ./_html/*.html to PNGs. Usage: node render.cjs   (needs Playwright; run skills/insta-creator/scripts/setup.sh once)
const path=require('path'),os=require('os');
let pw;for(const t of [process.env.PLAYWRIGHT_MODULE,'playwright',path.join(process.env.AB_INSTACREATOR_HOME||path.join(os.homedir(),'.ab-instacreator'),'node_modules','playwright')].filter(Boolean)){try{pw=require(t);break}catch(e){}}
if(!pw)throw Error('Playwright not found; run skills/insta-creator/scripts/setup.sh');
const fs=require('fs');
(async()=>{const b=await pw.chromium.launch();
for(const f of fs.readdirSync(path.join(__dirname,'_html')).filter(f=>f.endsWith('.html'))){
 if(f==='palettes.html'){const q=await b.newPage({viewport:{width:1600,height:1000}});await q.goto('file://'+path.join(__dirname,'_html',f));await q.screenshot({path:path.join(__dirname,'..','palettes.png'),fullPage:true});await q.close();continue}
 const story=f.startsWith('story-');const w=story?1080:2160,h=story?1920:1440,s=story?0.4:0.5;
 const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:s});
 await p.goto('file://'+path.join(__dirname,'_html',f));await p.evaluate(()=>document.fonts.ready);
 const out=path.join(__dirname,story?'stories':'styles',f.replace(/^(style|story)-/,'').replace('.html','.png'));
 await p.screenshot({path:out});await p.close()}
await b.close()})();
