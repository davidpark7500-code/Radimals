"""Broad bug sweep: long battle fuzz with invariants, every dialogue string fits the text box,
save/load round trip (incl. saves from before Nov 2026 features), field items, swarms, shop.
Usage: python tools/sweep.py   (exit 1 on any issue)"""
from playwright.sync_api import sync_playwright
import json, os, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = 'file://' + os.path.join(ROOT, 'www', 'index.html')
issues = []


def boot(pg):
    pg.goto(URL); time.sleep(1)
    pg.keyboard.press('z'); time.sleep(0.4)
    for _ in range(20):
        if pg.evaluate('()=>!!menuState'):
            break
        pg.keyboard.press('z'); time.sleep(0.15)
    pg.evaluate('()=>menuState.a()'); time.sleep(0.3)
    for _ in range(60):
        if pg.evaluate("()=>mode==='map'&&!textOpen"):
            break
        pg.keyboard.press('z'); time.sleep(0.08)


with sync_playwright() as p:
    b = p.chromium.launch()

    # ---------------------------------------------------------------- 1. long fuzz with invariants
    pg = b.new_page(viewport={'width': 390, 'height': 844}); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    boot(pg)
    rep = pg.evaluate("""async()=>{const out={battles:0,issues:[],res:{}};const names=DEX.concat(['Glitchy']);const rand=a=>a[Math.floor(Math.random()*a.length)];
      SET.anim=false;window.typeText=async t=>{tbText.textContent=t;};window.tween=(o,k,v)=>{o[k]=v;return Promise.resolve();};window.sleep=()=>Promise.resolve();
      window.pickMenu=async(items)=>{const ok=items.map((it,i)=>it.disabled?-1:i).filter(i=>i>=0);return ok.length?rand(ok):-1;};window.say=async()=>{};window.sayAll=async()=>{};window.choose=async()=>0;
      window.blackout=async()=>{G.party.forEach(m=>m.hp=m.st.hp);};G.flags.starter='Dialupine';
      for(let i=0;i<500;i++){G.party=[];for(let k=0;k<1+Math.floor(Math.random()*6);k++)G.party.push(makeMon(rand(names),1+Math.floor(Math.random()*49)));G.box=[];
        G.bag={slammer:5,mega:2,holo:1,gold:i%50?0:1,juice:2,pizza:1,ringpop:1,capri:2,warhead:1};G.money=1000;G.flags.lastSleep='sleep1';G.map=rand(['home','r1','r3','beach','woods','snow','net']);
        const n=Math.random()<0.6?1:2+Math.floor(Math.random()*3),foes=[];for(let k=0;k<n;k++)foes.push(makeMon(rand(names),1+Math.floor(Math.random()*49)));
        if(Math.random()<.3)foes[0].holo=true;const trainer=n>1;let r='?';
        try{r=await battle(foes,trainer?{trainer:'FUZZ',look:PLAYER_LOOK}:{});out.battles++;out.res[r]=(out.res[r]||0)+1;
          for(const m of G.party.concat(G.box)){const id=m.name+' L'+m.lv;
            if(!Number.isFinite(m.hp)||m.hp<0||m.hp>m.st.hp)out.issues.push('hp '+id);if(!(m.lv>=1&&m.lv<=50))out.issues.push('lv '+id);
            if(m.moves.length>4||!m.moves.length)out.issues.push('moves '+id);if(m.sts)out.issues.push('status kept after battle '+id+' '+m.sts);
            if(m.stg&&Object.keys(m.stg).length)out.issues.push('stages kept '+id);if(!Number.isFinite(m.exp)||m.exp<m.lv**3-1)out.issues.push('exp '+id);if(m.swarm!==undefined)out.issues.push('swarm flag leaked '+id);}
          for(const k in G.bag)if(!(Number.isInteger(G.bag[k])&&G.bag[k]>=0))out.issues.push('bag '+k+'='+G.bag[k]);
          if(G.party.length>6)out.issues.push('party>6');if(mode!=='map')out.issues.push('mode '+mode);if(B.en||B.me)out.issues.push('battle state left over');if(textOpen)out.issues.push('text left open');
        }catch(e){out.issues.push('EXC '+e.message+' '+(e.stack||'').split('\\n')[1]);}closeText();mode='map';busy=false;}
      return out;}""")
    print('fuzz:', {k: rep[k] for k in ('battles', 'res')}, 'issues:', sorted(set(rep['issues']))[:20])
    issues += ['fuzz: ' + i for i in sorted(set(rep['issues']))] + ['fuzz page error: ' + e for e in errs]
    pg.close()

    # ---------------------------------------------------------------- 2. every dialogue string fits, at 3 screen widths
    for W in (330, 390, 600):
        pg = b.new_page(viewport={'width': W, 'height': 900}); pg.goto(URL); time.sleep(1)
        res = pg.evaluate("""()=>{const strs=new Set();const grab=v=>{if(typeof v==='string'&&v.length>20&&/[a-z]/.test(v))strs.add(v);};
          const src=document.querySelector('script').textContent;for(const m of src.matchAll(/(['`])((?:\\\\.|(?!\\1).){40,}?)\\1/g)){const t=m[2];if(!t.includes('${')&&!/[{};=<>]/.test(t))strs.add(t.replace(/\\\\n/g,'\\n').replace(/\\\\'/g,"'"));}
          for(const n in SPECIES)grab(SPECIES[n].desc);
          tb.classList.add('on');textOpen=true;const inner=tbInner();let worst=0,bad=[];
          for(const t of strs){for(const pgt of paginate(t,inner)){tbText.textContent=pgt;const h=tbText.offsetHeight;if(h>inner+1){bad.push(pgt.slice(0,50));}worst=Math.max(worst,h-inner);}}
          tbText.textContent='';tb.classList.remove('on');textOpen=false;return{n:strs.size,bad:bad.slice(0,5),worst};}""")
        print(f'dialogue fit @{W}:', res['n'], 'strings, overflow pages:', len(res['bad']))
        issues += [f'text overflow @{W}: ' + x for x in res['bad']]
        pg.close()

    # ---------------------------------------------------------------- 3. save / load round trip + an OLD save without new fields
    pg = b.new_page(viewport={'width': 390, 'height': 844}); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    boot(pg)
    pg.evaluate("""async()=>{G.flags.starter='Floppuss';G.party=[makeMon('CDRompuss',22)];G.money=4321;G.caught={Floppuss:1,Milkwog:1};G.chain={n:'Milkwog',c:4};
      G.stickers={'FIRST SLAM':1};G.stats={crit:3};G.map='r1';G.x=5;G.y=5;SLOT=2;await save();
      const old=JSON.parse(JSON.stringify(G));delete old.chain;delete old.stickers;delete old.stats;delete old.seenEff;delete old.swarm;old.flags={starter:'Dialupine'};old.party=[makeMon('Modemauler',30)];
      localStorage.setItem(SAVEKEY().replace(/s2$/,'s3'),JSON.stringify(old));}""")
    pg.reload(); time.sleep(1)
    pg.keyboard.press('z'); time.sleep(0.5)
    for _ in range(20):
        if pg.evaluate('()=>!!menuState'):
            break
        pg.keyboard.press('z'); time.sleep(0.15)
    pg.evaluate("()=>{menuState.move('down');menuState.a();}"); time.sleep(0.3)
    pg.evaluate("()=>menuState&&menuState.a()"); time.sleep(0.4)   # CONTINUE
    got = pg.evaluate("()=>({money:G.money,lead:G.party[0]&&G.party[0].name,chain:G.chain,map:G.map,stickers:G.stickers})")
    print('save round trip:', got)
    if got['money'] != 4321 or got['lead'] != 'CDRompuss' or (got['chain'] or {}).get('c') != 4:
        issues.append('save round trip mismatch ' + json.dumps(got))
    # old save in slot 3: load it and fight + catch with it
    pg.reload(); time.sleep(1); pg.keyboard.press('z'); time.sleep(0.5)
    for _ in range(20):
        if pg.evaluate('()=>!!menuState'):
            break
        pg.keyboard.press('z'); time.sleep(0.15)
    pg.evaluate("()=>{menuState.move('down');menuState.move('down');menuState.a();}"); time.sleep(0.3)
    pg.evaluate("()=>menuState&&menuState.a()"); time.sleep(0.4)
    r = pg.evaluate("""async()=>{SET.text='instant';SET.anim=false;const auto=setInterval(()=>{if(textResolve)advance();if(menuState&&menuState.a)menuState.a();},10);
      let res;try{G.party[0].moves=['Flame Broil'];const w=wildMon('Milkwog',3);res=await battle([w]);}catch(e){res='EXC '+e.message;}clearInterval(auto);closeText();
      return{res,lead:G.party[0].name,chain:G.chain,stickers:Object.keys(G.stickers||{}),mode};}""")
    print('old save battle:', r)
    if r['res'] not in ('win', 'catch') or r['mode'] != 'map':
        issues.append('old save battle failed ' + json.dumps(r))
    issues += ['save page error: ' + e for e in errs]

    # ---------------------------------------------------------------- 4. field items, swarm expiry, shop limits
    r = pg.evaluate("""async()=>{const out=[];SET.text='instant';const auto=setInterval(()=>{if(textResolve)advance();},5);
      // Sour Bomb raises a level and can trigger evolution checks without throwing
      const m=makeMon('Dialupine',15);G.party=[m];G.bag.warhead=2;tab='B';mode='map';openMenu();
      const btn=[...document.querySelectorAll('.row button')].find(x=>x.textContent.includes('DIALUPI')&&x.closest('.row').textContent.includes('SOUR BOMB'));
      if(!btn)out.push('no sour bomb button');else{btn.click();await new Promise(r=>setTimeout(r,1500));if(!(m.lv===16||m.name!=='Dialupine'))out.push('sour bomb did not level: L'+m.lv);}
      closeMenu&&closeMenu();closeText();
      // swarm only lives for the visit
      G.swarm={map:'r1',name:'Sockpup',left:6};G.map='r2';await maybeSwarm();if(G.swarm&&G.swarm.map==='r1')out.push('swarm did not expire on leaving');
      // shop: cannot buy what you cannot afford
      G.money=100;const items=[];const pm=window.pickMenu;window.pickMenu=async(it,o)=>{items.push(it);return -1;};try{await shop();}catch(e){out.push('shop EXC '+e.message);}window.pickMenu=pm;
      if(items[0]&&items[0].some(it=>it.label.includes('$')&&!it.disabled&&parseInt(it.label.split('$')[1])>100))out.push('shop lets you buy over budget');
      clearInterval(auto);closeText();return out;}""")
    print('field checks:', r or 'ok')
    issues += ['field: ' + x for x in r]
    issues += ['page error: ' + e for e in errs if e not in issues]
    b.close()

print('\nSWEEP', 'PASS' if not issues else 'FAIL')
for i in issues:
    print(' -', i)
sys.exit(1 if issues else 0)
