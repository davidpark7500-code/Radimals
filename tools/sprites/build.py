"""Inject every sprite from designs.py into www/index.html (between HAND_ART2 markers).
Usage: python tools/sprites/build.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import SPRITES, render  # noqa: E402
import designs  # noqa: E402,F401

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML = os.path.join(ROOT, 'www', 'index.html')
START, END = '/*HAND_ART2_START*/', '/*HAND_ART2_END*/'
ANCHOR = 'for(const n in HAND_ART){MON_ART[n]=HAND_ART[n];delete SPECIES[n].gen;}'

body = ',\n'.join(f"{n}:[" + ','.join(f"'{r}'" for r in render(n)) + ']' for n in SPRITES)
block = (f"{START}\nconst HAND_ART2={{\n{body}\n}};\n"
         "for(const n in HAND_ART2){MON_ART[n]=HAND_ART2[n];if(SPECIES[n])delete SPECIES[n].gen;}\n" + END)
s = open(HTML).read()
if START in s:
    s = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda m: block, s, flags=re.S)
else:
    assert ANCHOR in s, 'anchor not found'
    s = s.replace(ANCHOR, ANCHOR + '\n' + block, 1)
open(HTML, 'w').write(s)
print(f'injected {len(SPRITES)} sprites into www/index.html')
