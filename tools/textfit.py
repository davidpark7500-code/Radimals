"""Text-box fit check: drives dialogue, menus, shop, battle, binder at 4 screen widths and fails if the
in-screen text box content ever overflows. Usage: python tools/textfit.py [shots_dir]"""
from playwright.sync_api import sync_playwright
import time,os,sys
OUT=sys.argv[1] if len(sys.argv)>1 else None
MON="""()=>{window._ovf=[];setInterval(()=>{const tb=document.querySelector('#textbox');if(!tb.classList.contains('on'))return;
 const cs=getComputedStyle(tb),inner=tb.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom);
 const t=document.querySelector('#tbtext'),o=document.querySelector('#tbopts');const used=t.offsetHeight+(o.offsetHeight?o.offsetHeight+parseFloat(getComputedStyle(o).marginTop):0);
 if(used>inner+1)window._ovf.push(Math.round(used-inner)+'px: '+t.textContent.slice(0,50)+' | '+o.textContent.slice(0,40));
 for(const b of o.querySelectorAll('button'))if(b.style.display!=='none'&&b.scrollWidth>b.clientWidth+40)window._ovf.push('clip: '+b.textContent);},30);}"""
def st(pg): return pg.evaluate("()=>({mode,m:!!menuState,t:textOpen,ty:typing,r:!!textResolve,busy})")
def run(pg,n=400,pick=None):
    for i in range(n):
        s=st(pg)
        if s['mode'] in('map',) and not s['t'] and not s['busy']: return
        if s['m'] and pick: pg.evaluate(pick)
        else: pg.keyboard.press('z')
        time.sleep(0.06)
def wm(pg,n=60):
    for i in range(n):
        if pg.evaluate('()=>!!menuState'): return True
        time.sleep(0.05)
    return False
def shot(pg,name):
    if OUT: pg.screenshot(path=os.path.join(OUT,name),clip=pg.evaluate("()=>{const r=document.querySelector('#bezel').getBoundingClientRect();return{x:r.x,y:r.y,width:r.width,height:r.height}}"))
bad=0
with sync_playwright() as p:
    b=p.chromium.launch()
    for W in (320,330,390,600):  # 320 @3x = iPhone Display Zoom, the fractional-scale path
        pg=b.new_page(viewport={'width':W,'height':900},device_scale_factor=3 if W==320 else 2 if W==390 else 1); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file://'+os.path.abspath('www/index.html')); time.sleep(1); pg.evaluate(MON); pg.evaluate("()=>{localStorage.setItem('radimals98v3_s2',JSON.stringify(Object.assign({},G,{party:[makeMon('Modemauler',34)],pogs:['arcade','foodcourt','rink'],playT:45240000})));}")
        pg.keyboard.press('z'); time.sleep(0.3)
        for k in range(10):
            if wm(pg,10): break
            pg.keyboard.press('z')
        time.sleep(0.2); W==390 and shot(pg,'1-floppy.png')
        pg.evaluate("()=>menuState.a()"); time.sleep(0.5); W==390 and shot(pg,'2-dialogue-page.png'); run(pg)
        pg.evaluate("()=>{G.flags.starter='Dialupine';G.party=[makeMon('Dialupine',15)];G.money=9000;G.map='mart3';G.x=4;G.y=3;G.dir='up';G.seenEff={'Fire>Grass':1,'Basic>Grass':1}}")
        # long text + menus straight from the engine
        pg.evaluate("()=>{(async()=>{await say('PROF. DIALTONE: This is a deliberately long line of dialogue that would have overflowed the old box, because it keeps going and going like a 56k modem handshake that never connects, and then it keeps going some more just to be sure the pager splits it.');await pickMenu(['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN'].map(l=>({label:l,sub:'a sub label'})),{text:'A long prompt above a long menu so the window has to scroll the rows instead of spilling out of the box.'});closeText();})();}")
        time.sleep(0.2); W==390 and shot(pg,'3-long-say.png'); run(pg,pick="()=>{menuState.move('down');menuState.move('down');menuState.move('down');menuState.move('down');}")
        for k in range(8):
            if st(pg)['m']: break
            pg.keyboard.press('z'); time.sleep(0.1)
        W==390 and shot(pg,'4-windowed-menu.png'); pg.evaluate("()=>menuState&&menuState.a()"); run(pg)
        # shop
        pg.evaluate("()=>{shop();}"); wm(pg); pg.evaluate("()=>{menuState.move('down');menuState.move('down');}"); time.sleep(0.1); W==390 and shot(pg,'5-shop.png')
        pg.evaluate("()=>menuState.b()"); run(pg)
        # battle: move menu with hints + status chip
        pg.evaluate("()=>{battle([makeMon('Trollsprout',12)]);}"); 
        for k in range(60):
            s=st(pg)
            if s['m'] and pg.evaluate("()=>tbText.textContent.startsWith('What will')"): break
            pg.keyboard.press('z'); time.sleep(0.08)
        pg.evaluate("()=>{B.en.sts='brn';B.me.sts='par';}"); time.sleep(0.15); W==390 and shot(pg,'6-battle-menu.png')
        pg.evaluate("()=>menuState.a()"); wm(pg); time.sleep(0.1); W==390 and shot(pg,'7-move-hints.png')
        pg.evaluate("()=>menuState.b()"); wm(pg); pg.evaluate("()=>{menuState.move('down');menuState.move('right');menuState.a()}"); run(pg)
        # binder entry with habitat
        pg.evaluate("()=>{G.seen.Milkwog=1;closeMenu&&closeMenu();say(`#${SPECIES.Milkwog.n} MILKWOG (${SPECIES.Milkwog.type})\\n${SPECIES.Milkwog.desc}\\n${habitat('Milkwog')}`);}"); time.sleep(1.2); W==390 and shot(pg,'8-binder-habitat.png'); run(pg)
        o=pg.evaluate("()=>window._ovf"); print(W,'overflow events:',len(o),o[:5],'errors:',errs); bad+=len(o)+len(errs)
        if W==390:
            pg.evaluate("()=>{closeText();tab='H';openMenu();}"); time.sleep(0.3)
            if OUT: pg.screenshot(path=os.path.join(OUT,'9-settings.png'),full_page=False)
        pg.close()
    b.close()
print('TEXTFIT', 'PASS' if not bad else 'FAIL')
sys.exit(1 if bad else 0)
