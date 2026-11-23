const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const c=await b.newContext({viewport:{width:430,height:932},locale:'de-DE'});const p=await c.newPage();
const log=m=>fs.appendFileSync('out.txt',m+'\n');const txt=async()=>(await p.evaluate(()=>document.body.innerText));
await p.goto((process.argv[2]||'https://dl.youtilly.de/tenders'),{waitUntil:'networkidle',timeout:60000});await p.waitForTimeout(1500);
await p.locator('input').first().fill('objektservicealdermann@gmail.com');await p.getByText('Weiter',{exact:true}).click();
await p.getByText('Anmeldecode per E-Mail erhalten').click({timeout:20000});
await p.getByText('Ein Anmeldecode ist auf dem Weg').waitFor({timeout:30000});
log('CODEPAGE '+new Date().toISOString());
const n=await p.locator('input').count();log('inputs '+n+' '+JSON.stringify(await p.$$eval('input',a=>a.map(i=>[i.type,i.name,i.autocomplete,i.maxLength]))));
for(let i=0;i<240;i++){if(fs.existsSync('code.txt'))break;await p.waitForTimeout(1000);}
if(!fs.existsSync('code.txt')){log('NOCODE');await b.close();return}
const code=fs.readFileSync('code.txt','utf8').trim();
const ins=p.locator('input:visible');const k=await ins.count();
if(k>=6){for(let i=0;i<6;i++)await ins.nth(i).fill(code[i]);}else{await ins.first().click();await p.keyboard.type(code,{delay:80});}
await p.waitForTimeout(1500);const a=p.getByText('Anmelden',{exact:true});if(await a.count())await a.click().catch(()=>{});
await p.waitForTimeout(7000);log('AFTER '+(await txt()).slice(0,500));
await p.goto('https://dl.youtilly.de/tenders',{waitUntil:'networkidle'});await p.waitForTimeout(6000);
log('TENDER '+(await txt()));await p.screenshot({path:'t1.png',fullPage:true});
await c.storageState({path:'state.json'});
await b.close();log('DONE')})().catch(e=>fs.appendFileSync('out.txt','ERR '+e.message+'\n'));
