"""Render all 151 to art/all-151-radimals.png. Usage: python tools/sheet.py"""
from playwright.sync_api import sync_playwright
import time,os
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1560,'height':2000}); pg.goto('file://'+os.path.abspath('www/index.html')); time.sleep(1.2)
    pg.evaluate("""()=>{document.body.innerHTML='';document.body.style.background='#1c1c21';document.body.style.margin='0';const c=document.createElement('canvas');c.width=1560;c.height=1990;document.body.appendChild(c);const g=c.getContext('2d');g.imageSmoothingEnabled=false;g.fillStyle='#1c1c21';g.fillRect(0,0,1560,1990);
      DEX.forEach((n,i)=>{const x=(i%13)*120,y=Math.floor(i/13)*164;const hand=!SPECIES[n].gen;g.fillStyle=hand?'#243a2a':'#26262c';g.fillRect(x+4,y+4,112,156);g.strokeStyle=hand?'#b6ff3b':'#3a3a42';g.lineWidth=2;g.strokeRect(x+5,y+5,110,154);
        const sp=MONSPR[n],k=72/sp.width;g.save();g.translate(x+24,y+12);g.scale(k,k);g.drawImage(sp,0,0);g.restore();g.fillStyle='#fbfbf4';g.font='bold 11px "RadPix",monospace';g.fillText('#'+String(SPECIES[n].n).padStart(3,'0'),x+10,y+100);g.fillStyle=hand?'#b6ff3b':'#c8c8d0';g.fillText(n.toUpperCase().slice(0,13),x+10,y+114);g.fillStyle='#8a8a94';g.font='10px "RadPix",monospace';g.fillText(SPECIES[n].type.toUpperCase(),x+10,y+128);g.fillStyle=hand?'#b6ff3b':'#66666e';g.fillText(MONSPR[n].width>24?'48PX':(hand?'24PX':'GENERATED'),x+10,y+146);});}""")
    time.sleep(0.6); os.makedirs('art',exist_ok=True); pg.screenshot(path='art/all-151-radimals.png',full_page=True); b.close(); print('wrote art/all-151-radimals.png')
