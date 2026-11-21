"""Review sheet for 48px designs: current 24px art (2x) beside the 48px redesign and its silhouette.
Usage: python tools/sprites/sheet48.py OUT.png [names...]   (default: every 48px design)"""
import os, re, sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit48  # noqa: E402
from preview import PAL, SPEC, hx  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OLD_HTML = os.path.join(ROOT, 'art', 'legacy-24px-art.json')


def old24(name):
    import json
    if os.path.exists(OLD_HTML):
        return json.load(open(OLD_HTML)).get(name)
    return None


def draw(d, rows, pal, ox, oy, px, sil=False):
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch == '.' or (ch not in pal and not sil):
                continue
            d.rectangle([ox + x * px, oy + y * px, ox + (x + 1) * px - 1, oy + (y + 1) * px - 1],
                        fill=(24, 24, 24) if sil else hx(pal[ch]))


def main(out, names):
    kit48.load_all()
    names = names or kit48.ORDER
    Z = 3
    cell = 48 * Z
    per = 3                       # creatures per row; each creature = 3 cells
    cw = 3 * cell + 40
    rows_n = (len(names) + per - 1) // per
    img = Image.new('RGB', (per * cw + 20, rows_n * (cell + 34) + 20), (34, 34, 40))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 15)
    except Exception:
        f = ImageFont.load_default()
    for i, n in enumerate(names):
        ox = 20 + (i % per) * cw
        oy = 10 + (i // per) * (cell + 34)
        for k in range(3):
            d.rectangle([ox + k * (cell + 4), oy, ox + k * (cell + 4) + cell - 1, oy + cell - 1], fill=(206, 240, 176))
        po = dict(PAL); po.update(SPEC.get(n, {}).get('colors', {}))
        pn = dict(PAL); pn.update({'G': '#1f9a48', 't': '#8a5a2c'}); pn.update(kit48.PAL48[n])
        o = old24(n)
        if o:
            draw(d, o, po, ox, oy, 2 * Z)
        r = kit48.render48(n)
        draw(d, r, pn, ox + cell + 4, oy, Z)
        draw(d, r, pn, ox + 2 * (cell + 4), oy, Z, sil=True)
        num = SPEC.get(n, {}).get('n', 0)
        d.text((ox, oy + cell + 6), f'#{num:03d} {n.upper()}  (old | new | silhouette)', fill=(182, 255, 59), font=f)
    img.save(out)
    print('wrote', out, len(names))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
