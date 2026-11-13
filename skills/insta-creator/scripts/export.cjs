const fs=require('node:fs'),path=require('node:path'),{pathToFileURL}=require('node:url');
const os=require('node:os');
function loadPlaywright(){
 const skillDir=path.resolve(__dirname,'..'),repoRoot=path.resolve(__dirname,'..','..','..');
 const tries=[process.env.PLAYWRIGHT_MODULE,'playwright',...[process.cwd(),skillDir,repoRoot,process.env.AB_INSTACREATOR_HOME||path.join(os.homedir(),'.ab-instacreator')].map(d=>path.join(d,'node_modules','playwright'))].filter(Boolean);
 for(const t of tries){try{return require(t)}catch(e){}}
 throw Error('Playwright not found. Run: bash '+path.join(skillDir,'scripts','setup.sh')+' once (installs to ~/.ab-instacreator), or set PLAYWRIGHT_MODULE');
}
function findChrome(){
 if(process.env.CHROME_PATH)return process.env.CHROME_PATH;
 return ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].find(p=>fs.existsSync(p));
}
async function main(){
 const args=process.argv.slice(2);if(args.length!==3||args[2]!=='--approved')throw Error('Usage: node export.cjs design.html output-folder --approved (only after user approval)');
 const input=path.resolve(args[0]),out=path.resolve(args[1]);if(!fs.existsSync(input))throw Error('HTML does not exist');
 const {chromium}=loadPlaywright();
 let browser;
 try{browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})})}
 catch(e){const c=findChrome();if(!c)throw Error('No browser. Run setup.sh (installs Chromium) or set CHROME_PATH. '+e.message);browser=await chromium.launch({headless:true,executablePath:c})}
 try{
 const page=await browser.newPage({viewport:{width:1200,height:2000},deviceScaleFactor:1});
 await page.goto(pathToFileURL(input).href);await page.emulateMedia({reducedMotion:'reduce'});
 await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(im=>im.decode()));document.documentElement.classList.add('exporting')});
 await page.addStyleTag({content:'[data-review-only]{display:none!important}*,*::before,*::after{animation:none!important;transition:none!important}'});
 const slides=page.locator('[data-export-slide]'),n=await slides.count();if(!n)throw Error('No data-export-slide elements');
 const plans=[];for(let i=0;i<n;i++){
 const loc=slides.nth(i),size=await loc.evaluate(e=>({w:Number(e.dataset.width),h:Number(e.dataset.height)}));
 if(!Number.isInteger(size.w)||!Number.isInteger(size.h)||size.w<1||size.h<1||size.w>8000||size.h>8000)throw Error('Invalid artboard dimensions');
 const file=path.join(out,path.basename(input,'.html')+'-Slide-'+(i+1)+'.png');if(fs.existsSync(file))throw Error('Refusing to overwrite '+file);plans.push({loc,size,file});
 }
 fs.mkdirSync(out,{recursive:true});
 for(const {loc,size,file} of plans){
 await loc.evaluate((e,s)=>{e.style.width=s.w+'px';e.style.height=s.h+'px';e.style.transform='none';e.style.zoom='1';e.style.flex='none';},size);
 const box=await loc.boundingBox();if(!box||Math.abs(box.width-size.w)>.1||Math.abs(box.height-size.h)>.1)throw Error('Export CSS still scales the artboard or an ancestor');
 await loc.screenshot({path:file,animations:'disabled'});const buf=fs.readFileSync(file);if(buf.readUInt32BE(16)!==size.w||buf.readUInt32BE(20)!==size.h)throw Error('Wrong PNG dimensions');console.log(JSON.stringify({file,width:size.w,height:size.h}));
 }
 }finally{await browser.close()}
}
main().catch(e=>{console.error(e.message);process.exitCode=1});
