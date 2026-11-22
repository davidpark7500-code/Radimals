"""World integrity audit. Usage: python tools/audit.py"""
from playwright.sync_api import sync_playwright
import time,os
URL='file://'+os.path.abspath('www/index.html')
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.goto(URL); time.sleep(1)
    rep=pg.evaluate("""()=>{const out=[];const walk=(m,x,y)=>{const M=MAPS[m];if(!M)return 'nomap '+m;if(x<0||y<0||x>=M.w||y>=M.h)return 'oob';return SOLID.includes(M.rows[y][x])?'solid':null;};
      for(const k in MAPS){const M=MAPS[k];for(let y=0;y<M.h;y++)for(let x=0;x<M.w;x++){const c=M.rows[y][x];if('DEU'.includes(c)&&!(M.warps&&M.warps[x+','+y]))out.push(k+' door '+x+','+y+' no warp');}
        for(const key in (M.warps||{})){const w=M.warps[key];const e=walk(w.map,w.x,w.y);if(e)out.push(k+' warp '+key+' -> '+e);}
        for(const n of M.npcs){G.flags={starter:'Dialupine'};G.pogs=[];const e=walk(k,n.x,n.y);if(e)out.push(k+' npc '+n.id+' '+e);if(n.team)try{n.team()}catch(err){out.push(n.id+' team '+err)}}
        for(const o of (M.items||[])){if(walk(k,o.x,o.y))out.push(k+' item solid');if(!ITEMS[o.item])out.push(k+' bad item '+o.item);}
        for(const d in (M.edges||{})){const o=MAPS[M.edges[d]];if(!o){out.push(k+' edge nomap');continue;}
          if(d==='top'||d==='bottom'){let ok=0;for(let x=0;x<M.w;x++){const y=d==='top'?0:M.h-1;if(!SOLID.includes(M.rows[y][x])){ok++;if(walk(M.edges[d],x,d==='top'?o.h-1:0))out.push(k+' edge '+d+' x='+x);}}if(!ok)out.push(k+' edge '+d+' closed');}
          else{let ok=0;for(let y=0;y<M.h;y++){const x=d==='left'?0:M.w-1;if(!SOLID.includes(M.rows[y][x])){ok++;if(walk(M.edges[d],d==='left'?o.w-1:0,y))out.push(k+' edge '+d+' y='+y);}}if(!ok)out.push(k+' edge '+d+' closed');}}
        for(const w of (M.wild||[]).concat(M.fish||[]))if(!SPECIES[w])out.push(k+' wild '+w);}
      for(const s in SPECIES){for(const l in SPECIES[s].learn)for(const mv of [].concat(SPECIES[s].learn[l]))if(!MOVES[mv])out.push(s+' move '+mv);if(SPECIES[s].evo&&!SPECIES[SPECIES[s].evo[1]])out.push(s+' evo');{const A=MON_ART[s],z=A&&A.length;if(!A||(z!==24&&z!==48)||A.some(r=>r.length!==z))out.push(s+' art size');}}
      const avail=new Set();for(const k in MAPS)for(const w of (MAPS[k].wild||[]).concat(MAPS[k].fish||[]))avail.add(w);['Dialupine','Floppuss','Trollsprout','Y2Kraken','Keychainos'].forEach(n=>avail.add(n));
      let grew=true;while(grew){grew=false;for(const n of DEX){const ev=SPECIES[n].evo;if(avail.has(n)&&ev&&!avail.has(ev[1])){avail.add(ev[1]);grew=true;}}}
      const miss=DEX.filter(n=>!avail.has(n));if(miss.length)out.push('UNOBTAINABLE: '+miss.join(','));
      out.push('species '+DEX.length+' hand-drawn '+DEX.filter(n=>!SPECIES[n].gen).length);return out;}""")
    print("\n".join(rep)); print('page errors:',errs); b.close()
