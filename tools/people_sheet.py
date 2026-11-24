"""Render every character (map sprites + battle portrait) to art/people-sheet.png.
Usage: python tools/people_sheet.py [out.png]"""
from playwright.sync_api import sync_playwright
import time,os,sys
out=sys.argv[1] if len(sys.argv)>1 else 'art/people-sheet.png'
JS="""()=>{const list=[];const seen={};
  const add=(name,look,tr)=>{const k=JSON.stringify(look);if(seen[k]){return;}seen[k]=1;list.push({name,look,tr});};
  add('PLAYER BIKE',BIKE_LOOK,false);
  for(const k in (typeof CAST!=='undefined'?CAST:{}))add(k,CAST[k],!!CAST[k].art);
  for(const k in MAPS)for(const n of MAPS[k].npcs||[]){if(!n.look)continue;add(n.trainer||n.id,n.look,!!n.trainer||n.special==='leader');}
  if(typeof LEADERS!=='undefined')for(const k in LEADERS)add(LEADERS[k].name,LEADERS[k].look,true);
  const CW=520,CH=112,cols=3,rows=Math.ceil(list.length/cols);
  document.body.innerHTML='';document.body.style.background='#1c1c21';document.body.style.margin='0';
  const c=document.createElement('canvas');c.width=cols*CW;c.height=rows*CH;document.body.appendChild(c);const g=c.getContext('2d');g.imageSmoothingEnabled=false;
  g.fillStyle='#1c1c21';g.fillRect(0,0,c.width,c.height);
  list.forEach((e,i)=>{const x=(i%cols)*CW,y=Math.floor(i/cols)*CH;g.fillStyle='#5fae58';g.fillRect(x+4,y+4,CW-8,CH-8);
    const set=personSet(e.look);let dx=x+8;const S=4;
    for(const d of['down','left','up','right'])for(let f=0;f<set[d].length&&f<3;f++){const s=set[d][f];g.drawImage(s,dx,y+8+(20-s.height)*S,s.width*S,s.height*S);dx+=s.width*S+2;if(d==='right')break;}
    if(e.tr){const p=portrait(e.look);g.fillStyle='#fbfbf4';g.fillRect(x+CW-104,y+6,98,98);g.drawImage(p,x+CW-103,y+7,96,96);}
    g.fillStyle='#181818';g.font='bold 12px monospace';g.fillText(String(e.name).slice(0,28),x+10,y+CH-12);});
  return [c.width,c.height,list.length];}"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--disable-accelerated-2d-canvas','--disable-gpu']); pg=b.new_page(viewport={'width':1560,'height':1400}); pg.goto('file://'+os.path.abspath('www/index.html')); time.sleep(1.2)
    w,h,n=pg.evaluate(JS); time.sleep(0.4)
    pg.set_viewport_size({'width':w,'height':h}); pg.screenshot(path=out,clip={'x':0,'y':0,'width':w,'height':h}); b.close(); print('wrote',out,n,'characters',w,h)
