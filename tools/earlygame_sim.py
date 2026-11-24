"""Early-game difficulty check, in the order a player actually meets trainers on Route 1:
Chad 1 in the lab right after picking a starter (full HP; you are healed after, win or lose) ->
Skater Todd (line of sight, first thing north of home) -> Bug Kid Kenny with HP carried over from Todd (and at full HP).
Player only attacks: 'best' = strongest attack vs the foe, 'rand' = random attack. No items.
Usage: python tools/earlygame_sim.py [N]"""
from playwright.sync_api import sync_playwright
import os, time, sys
URL = 'file://' + os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'www', 'index.html')
N = int(sys.argv[1]) if len(sys.argv) > 1 else 150
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.goto(URL); time.sleep(1)
    r = pg.evaluate("""async(N)=>{SET.anim=false;window.typeText=async t=>{};window.tween=(o,k,v)=>{o[k]=v;return Promise.resolve();};window.sleep=()=>Promise.resolve();
      window.say=async()=>{};window.sayAll=async()=>{};window.choose=async()=>0;window.blackout=async()=>{};let strat='best';
      window.pickMenu=async(items,o)=>{if(items[0]&&items[0].label==='FIGHT')return 0;if(o&&o.id==='moves'){const me=B.me,en=B.en;const dm=me.moves.map((m,i)=>[i,MOVES[m][1]?MOVES[m][1]*eff(MOVES[m][0],SPECIES[en.name].type)*(MOVES[m][0]===SPECIES[me.name].type?1.3:1):0]);
          const att=dm.filter(x=>x[1]>0);if(strat==='best'){att.sort((a,b)=>b[1]-a[1]);return att[0][0];}return att[Math.floor(Math.random()*att.length)][0];}
        const ok=items.map((it,i)=>it.disabled?-1:i).filter(i=>i>=0);return ok.length?ok[0]:-1;};
      const npc=id=>MAPS.r1.npcs.concat(MAPS.home.npcs).find(n=>n.id===id);const fight=async id=>{const r=await battle(npc(id).team(),{trainer:id,look:PLAYER_LOOK});closeText();mode='map';busy=false;return r==='win';};
      const out={};for(const st of ['Dialupine','Floppuss','Trollsprout'])for(const s of ['best','rand']){strat=s;const c={chadLab:0,todd:0,kennyCarried:0,kennyFull:0};
        for(let i=0;i<N;i++){G.flags={starter:st};G.bag={};G.party=[makeMon(st,5)];
          if(await fight('chad1'))c.chadLab++;G.party.forEach(m=>m.hp=m.st.hp);
          if(await fight('todd')){c.todd++;if(npc('todd').healAfter)G.party.forEach(m=>m.hp=m.st.hp);}else G.party.forEach(m=>m.hp=m.st.hp);
          const save=JSON.stringify(G.party[0]);if(await fight('kenny'))c.kennyCarried++;
          G.party=[JSON.parse(save)];G.party[0].hp=G.party[0].st.hp;if(await fight('kenny'))c.kennyFull++;}
        for(const k in c)c[k]=Math.round(100*c[k]/N)+'%';out[st+'/'+s]=c;}return out;}""", N)
    for k, v in r.items(): print(k, v)
    print('page errors:', errs[:3])
