from playwright.sync_api import sync_playwright
import os,time,json,sys
URL='file://'+os.path.abspath('www/index.html')
N=int(sys.argv[1]) if len(sys.argv)>1 else 150
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(URL);time.sleep(1)
    r=pg.evaluate("""async(N)=>{SET.anim=false;window.typeText=async t=>{};window.tween=(o,k,v)=>{o[k]=v;return Promise.resolve();};window.sleep=()=>Promise.resolve();
      window.say=async()=>{};window.sayAll=async()=>{};window.choose=async()=>0;window.blackout=async()=>{};
      let strat='best';
      window.pickMenu=async(items,o)=>{if(items[0]&&items[0].label==='FIGHT')return 0;if(o&&o.id==='moves'){const me=B.me,en=B.en;const dm=me.moves.map((m,i)=>[i,MOVES[m][1]?MOVES[m][1]*eff(MOVES[m][0],SPECIES[en.name].type)*(MOVES[m][0]===SPECIES[me.name].type?1.3:1):0]);
          const att=dm.filter(x=>x[1]>0);if(strat==='best'){att.sort((a,b)=>b[1]-a[1]);return att[0][0];}return att[Math.floor(Math.random()*att.length)][0];}
        const ok=items.map((it,i)=>it.disabled?-1:i).filter(i=>i>=0);return ok.length?ok[0]:-1;};
      const npc=id=>MAPS.r1.npcs.find(n=>n.id===id);const out={};
      for(const st of ['Dialupine','Floppuss','Trollsprout'])for(const s of ['best','rand']){strat=s;let kenny=0,chad=0,toddFull=0,toddAfter=0,hpLeft=0;
        for(let i=0;i<N;i++){G.flags={starter:st};G.party=[makeMon(st,5)];G.bag={};G.money=0;
          const r1=await battle(npc('chad1').team(),{trainer:'CHAD',look:PLAYER_LOOK});closeText();mode='map';busy=false;if(r1==='win'){chad++;hpLeft+=G.party[0].hp/G.party[0].st.hp;}
          const lv=G.party[0].lv;if(r1!=='win'){G.party=[makeMon(st,5)];}
          if(npc('chad1').healAfter&&r1==='win')G.party.forEach(m=>m.hp=m.st.hp);const r2=await battle(npc('todd').team(),{trainer:'SKATER TODD',look:PLAYER_LOOK});closeText();mode='map';busy=false;if(r2==='win')toddAfter++;
          G.party=[makeMon(st,lv)];const r3=await battle(npc('todd').team(),{trainer:'SKATER TODD',look:PLAYER_LOOK});closeText();mode='map';busy=false;if(r3==='win')toddFull++;const lv2=G.party[0].lv;G.party=[makeMon(st,lv2)];const r4=await battle(npc('kenny').team(),{trainer:'K',look:PLAYER_LOOK});closeText();mode='map';busy=false;if(r4==='win')kenny++;}
        out[st+'/'+s]={chadWin:chad/N,hpAfterChad:+(hpLeft/Math.max(1,chad)).toFixed(2),toddAfterChad:toddAfter/N,toddFullHP:toddFull/N,kennyFullHP:kenny/N};}
      return out;}""",N)
    for k,v in r.items():print(k,v)
    print('errs',errs[:3])
