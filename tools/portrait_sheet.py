"""Render the hand-drawn trainer portraits at 8x. Usage: python tools/portrait_sheet.py [out.png] [name ...]"""
from playwright.sync_api import sync_playwright
import time,os,sys,json
out=sys.argv[1] if len(sys.argv)>1 else 'art/trainer-portraits.png'
names=sys.argv[2:]
JS="""(names)=>{const ks=Object.keys(CAST).filter(k=>CAST[k].art&&(!names.length||names.includes(k)));const cols=Math.min(6,ks.length),S=8,CW=24*S+16,CH=24*S+56,rows=Math.ceil(ks.length/cols);
  document.body.innerHTML='';document.body.style.margin='0';const c=document.createElement('canvas');c.width=cols*CW;c.height=rows*CH;document.body.appendChild(c);const g=c.getContext('2d');g.imageSmoothingEnabled=false;
  g.fillStyle='#1c1c21';g.fillRect(0,0,c.width,c.height);
  ks.forEach((k,i)=>{const x=(i%cols)*CW,y=Math.floor(i/cols)*CH;g.fillStyle='#fbfbf4';g.fillRect(x+4,y+4,CW-8,CH-8);g.drawImage(portrait(CAST[k]),x+8,y+8,24*S,24*S);
    const m=personSet(CAST[k]).down[0];g.drawImage(m,x+CW-44,y+CH-48,32,40);g.fillStyle='#181818';g.font='bold 13px monospace';g.fillText(k,x+10,y+CH-22);});
  return [c.width,c.height,ks.length];}"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--disable-accelerated-2d-canvas','--disable-gpu']); pg=b.new_page(viewport={'width':1300,'height':1000}); pg.goto('file://'+os.path.abspath('www/index.html')); time.sleep(1.2)
    w,h,n=pg.evaluate(JS,names); time.sleep(0.3)
    pg.set_viewport_size({'width':w,'height':h}); pg.screenshot(path=out,clip={'x':0,'y':0,'width':w,'height':h}); b.close(); print('wrote',out,n,w,h)
