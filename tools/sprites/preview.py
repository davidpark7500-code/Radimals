"""Render sprites to a review sheet. Usage: python tools/sprites/preview.py OUT.png [name ...]"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from lib import SPRITES, render  # noqa: E402
import designs  # noqa: E402,F401  (registers sprites)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAL = {'#': '#181818', 'k': '#181818', 'w': '#fbfbf4', 's': '#ffd4a8', 'r': '#ff3f5f', 'R': '#b8203c', 'b': '#3a6cff',
       'n': '#2c2444', 'y': '#ffe03a', 'g': '#57d65a', 'G': '#1f9a48', 't': '#8a5a2c', 'c': '#fff0c8', 'q': '#7ee6ff',
       'l': '#8cf05a', 'L': '#2fa848', 'f': '#ff8c2a', 'F': '#ffe66a', 'z': '#b6ff3b', 'm': '#ff3fa4', 'v': '#a04cff',
       'o': '#19e6d2'}
SPEC = {s['name']: s for s in json.load(open(os.path.join(ROOT, 'art', 'species-todo.json')))}


def hx(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def sheet(names, out, scale=5, cols=7):
    cw, ch = 24 * scale + 24, 24 * scale + 44
    rows = (len(names) + cols - 1) // cols
    img = Image.new('RGB', (cols * cw, rows * ch), (40, 40, 46))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 12)
    except Exception:
        f = ImageFont.load_default()
    for i, n in enumerate(names):
        pal = dict(PAL)
        pal.update(SPEC.get(n, {}).get('colors', {}))
        ox, oy = (i % cols) * cw + 12, (i // cols) * ch + 8
        d.rectangle([ox - 4, oy - 4, ox + 24 * scale + 3, oy + 24 * scale + 3], fill=(200, 240, 168))
        for y, r in enumerate(render(n)):
            for x, c in enumerate(r):
                if c in pal:
                    d.rectangle([ox + x * scale, oy + y * scale, ox + x * scale + scale - 1, oy + y * scale + scale - 1], fill=hx(pal[c]))
        num = SPEC.get(n, {}).get('n', 0)
        d.text((ox - 4, oy + 24 * scale + 8), f'#{num:03d} {n.upper()}', fill=(182, 255, 59), font=f)
    img.save(out)
    print('wrote', out, len(names))


if __name__ == '__main__':
    out = sys.argv[1]
    names = sys.argv[2:] or list(SPRITES)
    sheet(names, out)
