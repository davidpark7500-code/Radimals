"""Random-battle fuzz + rule checks. Usage: python tools/fuzz.py"""
from playwright.sync_api import sync_playwright
import time,os
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.goto('file://'+os.path.abspath('www/index.html')); time.sleep(1)
    pg.evaluate("()=>{SET.anim=false;window.typeText=async t=>{tbText.textContent=t;};window.tween=(o,k,v)=>{o[k]=v;return Promise.resolve();};}")
    pg.keyboard.press('z'); time.sleep(0.3); pg.evaluate("()=>{menuState&&menuState.a();}"); time.sleep(0.3)
    for _ in range(6): pg.keyboard.press('z'); time.sleep(0.05)
    pg.evaluate("()=>{closeText();mode='map';}")
    rep=pg.evaluate("""async()=>{const out={battles:0,catches:0,wins:0,losses:0,runs:0,issues:[]};const names=DEX.slice();const rand=a=>a[Math.floor(Math.random()*a.length)];
      window.pickMenu=async(items)=>{const ok=items.map((it,i)=>it.disabled?-1:i).filter(i=>i>=0);return ok.length?rand(ok):-1;};window.say=async()=>{};window.sayAll=async()=>{};window.choose=async()=>0;window.blackout=async()=>{G.party.forEach(m=>m.hp=m.st.hp);};
      for(let i=0;i<120;i++){G.party=[makeMon(rand(names),1+Math.floor(Math.random()*49)),makeMon(rand(names),1+Math.floor(Math.random()*49))];G.box=[];G.bag={slammer:5,mega:2,holo:1,juice:2,pizza:1,ringpop:1,capri:1};G.money=1000;G.flags.lastSleep='sleep1';G.map='home';
        const foes=Math.random()<0.5?[makeMon(rand(names),1+Math.floor(Math.random()*49))]:[makeMon(rand(names),5+Math.floor(Math.random()*30)),makeMon(rand(names),5+Math.floor(Math.random()*30))];const trainer=foes.length>1;let r='?';
        try{r=await battle(foes,trainer?{trainer:'FUZZ',look:PLAYER_LOOK}:{});out.battles++;out[r==='catch'?'catches':r==='win'?'wins':r==='lose'?'losses':'runs']++;
          for(const m of G.party.concat(G.box)){if(!Number.isFinite(m.hp)||m.hp<0||m.hp>m.st.hp)out.issues.push('hp '+m.name);if(m.lv>50)out.issues.push('lv '+m.name);if(m.moves.length>4||!m.moves.length)out.issues.push('moves '+m.name);}
          if(mode!=='map')out.issues.push('mode '+mode);}catch(e){out.issues.push('EXC '+e.message);}closeText();mode='map';}
      for(const n of names)for(const ball of [1,3,99]){const t=makeMon(n,25);t.hp=1;const pc=catchChance(t,ball);if(!(pc>0&&pc<=1))out.issues.push('catch '+n);}
      return out;}""")
    print(rep); print('page errors:',errs); b.close()
