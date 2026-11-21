"""Before/after sheet for the 48px pilot: current 24px sprite (at its 2x in-game size), the 48px
redesign (1x = same on-screen box), and both silhouettes. Usage: python tools/sprites/pilot_sheet.py OUT.png"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
import pilot48 as V1  # noqa: E402
import pilot48v2 as V2  # noqa: E402
P48, PAL48 = V2.P48, V2.PAL48
from preview import PAL, SPEC, hx  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXTRA = {'d': '#000000', 'e': '#c9ced8', 'G': '#1f9a48', 't': '#8a5a2c'}


def current24(name):
    """Pull the current 24x24 rows out of the game file (MON_ART / HAND_ART / HAND_ART2)."""
    html = open(os.path.join(ROOT, 'www', 'index.html')).read()
    m = re.search(r'\b' + name + r"\s*:\s*\[((?:\s*'[^']{24}'\s*,?){24})\]", html)
    return re.findall(r"'([^']{24})'", m.group(1)) if m else None


def draw(img, rows, pal, ox, oy, px, sil=False):
    d = ImageDraw.Draw(img)
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch == '.' or (ch not in pal and not sil):
                continue
            col = (24, 24, 24) if sil else hx(pal[ch])
            d.rectangle([ox + x * px, oy + y * px, ox + (x + 1) * px - 1, oy + (y + 1) * px - 1], fill=col)


def main(out):
    Z = 4                          # zoom: 48 screen px -> 192 px
    cell = 48 * Z
    names = list(P48)
    W = 20 + 4 * (cell + 20)
    H = 60 + len(names) * (cell + 40)
    img = Image.new('RGB', (W, H), (34, 34, 40))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 18)
    except Exception:
        f = ImageFont.load_default()
    for i, h in enumerate(['NOW (24px x2)', 'PILOT v1', 'PILOT v2 (plush)', 'v2 silhouette']):
        d.text((20 + i * (cell + 20), 20), h, fill=(182, 255, 59), font=f)
    for row, n in enumerate(names):
        y = 60 + row * (cell + 40)
        pal_old = dict(PAL); pal_old.update(SPEC.get(n, {}).get('colors', {}))
        pal_new = dict(PAL); pal_new.update(EXTRA); pal_new.update(PAL48[n])
        old = current24(n)
        v1 = V1.render48(n)
        new = V2.render48(n)
        pal_v1 = dict(PAL); pal_v1.update(EXTRA); pal_v1.update(V1.PAL48[n])
        for col in range(4):
            x = 20 + col * (cell + 20)
            d.rectangle([x, y, x + cell - 1, y + cell - 1], fill=(206, 240, 176))
        if old:
            draw(img, old, pal_old, 20, y, 2 * Z)
        draw(img, v1, pal_v1, 20 + (cell + 20), y, Z)
        draw(img, new, pal_new, 20 + 2 * (cell + 20), y, Z)
        draw(img, new, pal_new, 20 + 3 * (cell + 20), y, Z, sil=True)
        d.text((20, y + cell + 8), n.upper(), fill=(255, 255, 255), font=f)
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main(sys.argv[1])
