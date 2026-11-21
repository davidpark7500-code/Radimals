"""Scripted full-arc run: starter -> leaders -> tower -> boss -> Internet -> legendary. Usage: python tools/playthrough.py"""
from playwright.sync_api import sync_playwright
import time,os
def st(pg): return pg.evaluate("()=>({mode:mode,m:!!menuState,t:textOpen,ty:typing,r:!!textResolve,busy:busy,txt:document.querySelector('#tbtext').textContent.slice(0,40)})")
def drive(pg,limit=900,pref=None):
    last=None;same=0
    for i in range(limit):
        s=st(pg)
        if s['mode']=='map' and not s['t'] and not s['busy']: return True
        key=(s['txt'],s['m'],s['r']); same=same+1 if key==last else 0; last=key
        if same>60: print('  STUCK',s); return False
        if s['m']:
            if s['txt'].startswith('Choose a move'): pg.evaluate("()=>{menuState.move('down');menuState.a();}")
            elif pref and s['txt'].startswith(pref[0]): pg.evaluate("(n)=>{for(let i=0;i<n;i++)menuState.move('down');menuState.a();}",pref[1])
            else: pg.keyboard.press('z')
        elif s['ty'] or s['r']: pg.keyboard.press('z')
        time.sleep(0.1)
    return False
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.goto('file://'+os.path.abspath('www/index.html')); time.sleep(1.2)
    pg.keyboard.press('z'); time.sleep(0.3); pg.evaluate("()=>{menuState&&menuState.a();}"); drive(pg)
    pg.evaluate("()=>{G.map='lab';G.x=6;G.y=4;G.dir='up';}"); pg.keyboard.press('z'); drive(pg); print('starter',pg.evaluate("()=>G.party.map(m=>m.name)"))
    pg.evaluate("()=>{G.party=[makeMon('CDRompuss',48),makeMon('Modemauler',48),makeMon('Trolltree',48)];G.money=9000;}")
    for mp,who,x,y,d in [('r1','chad1',9,11,'up'),('arcade','lead_arcade',4,2,'up'),('foodcourt','lead_foodcourt',4,2,'up'),('rink','lead_rink',4,2,'up'),('r3','chad2',10,18,'up'),('vault','lead_vault',4,2,'up'),('lab','prof',6,4,'up'),('tower1','mike',4,5,'up'),('tower2','pat',5,5,'right'),('tower3','chad3',4,5,'up'),('tower3','kraken',4,2,'up'),('r3','aol',13,6,'up'),('r3','aol',13,6,'up')]:
        pg.evaluate("(a)=>{G.map=a[0];G.x=a[1];G.y=a[2];G.dir=a[3];G.party.forEach(m=>m.hp=m.st.hp);}",[mp,x,y,d]); time.sleep(0.2); pg.keyboard.press('z'); time.sleep(0.3); ok=drive(pg); print(who,'ok' if ok else 'FAIL',pg.evaluate("()=>({caps:G.pogs.length,champ:!!G.flags.champion,gold:G.bag.gold||0,cd:!!G.key.cd})"))
    pg.evaluate("()=>{G.map='lab';G.x=6;G.y=4;G.dir='up';}"); pg.keyboard.press('z'); drive(pg,pref=('PROF. DIALTONE: A FREE',0)); print('on the internet:',pg.evaluate("()=>G.map==='net'"))
    print('page errors:',errs); b.close()
