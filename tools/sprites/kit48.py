"""48px Radimal drawing kit: registry + shared helpers (eyes, blush, flames, cords).
Design rules: art/CREATURE-DESIGN-GUIDE.md. Designs live in designs48_*.py; build with build48.py.
Palette letters: a main, d main shadow, b light/belly, c accent, e metal/extra, plus game globals.
"""

from lib import C

P48 = {}
PAL48 = {}
ORDER = []


def sprite48(name, pal):
    def deco(fn):
        assert name not in P48, 'duplicate sprite ' + name
        P48[name] = fn
        PAL48[name] = pal
        ORDER.append(name)
        return fn
    return deco


def render48(name):
    c = C(48)
    P48[name](c)
    rows = [''.join(r) for r in c.g]
    assert len(rows) == 48 and all(len(r) == 48 for r in rows), name
    return rows


def load_all():
    import glob, importlib, os
    here = os.path.dirname(os.path.abspath(__file__))
    for f in sorted(glob.glob(os.path.join(here, 'designs48_*.py'))):
        importlib.import_module(os.path.basename(f)[:-3])
    return P48


def bigeye(c, x, y, w=4, h=5, look=-1):
    """Glossy eye: dark fill, 2x2 highlight on the look side, sparkle on the opposite corner."""
    c.rect(x, y, x + w - 1, y + h - 1, 'k')
    hx = x if look < 0 else x + w - 2
    c.rect(hx, y, hx + 1, y + 1, 'w')
    c.px(x + w - 1 if look < 0 else x, y + h - 1, 'w')
    return c


def blush(c, x, y):
    c.rect(x, y, x + 2, y, 'm')
    return c


def soft_flame(c, x, y, h, lean=0, col='f', core='F'):
    """Rounded flame curl (plush-friendly: no needle points)."""
    c.ell(x, y - h * .35, 2.6, h * .45, col)
    c.ell(x + lean, y - h * .8, 1.6, h * .3, col)
    c.ell(x, y - h * .3, 1.2, h * .25, core)
    return c


def coil(c, pts, col='c', hi='e'):
    """Phone cord drawn as open, overlapping loops (reads as a spiral, never as a solid shaft).
    Call AFTER outline(): the dark cord color is its own outline."""
    for x, y in pts:
        c.ring(x, y, 2, 2.4, 1, col)
    for x, y in pts:
        c.px(x - 1, y - 2, hi)
    return c


def plug(c, x, y, facing=1):
    """Small square clear RJ11 plug lying flat, gold pins on the end, clip on top."""
    c.rect(x, y, x + 4, y + 3, '#')
    c.rect(x + 1, y + 1, x + 3, y + 2, 'q')
    pin = x + 3 if facing > 0 else x + 1
    c.px(pin, y + 1, 'y'); c.px(pin, y + 2, 'y')
    c.px(x + 2, y, 'e')
    return c


