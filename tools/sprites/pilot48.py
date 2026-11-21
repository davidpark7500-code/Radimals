"""SUPERSEDED by pilot48v2.py (kept for history). PILOT v1: 48x48 redesigns of the three starter lines, applying the design principles in
art/CREATURE-DESIGN-GUIDE.md. Not wired into the game. Render: python tools/sprites/pilot_sheet.py OUT.png

Palette letters for 48px sprites: a main, d main-shadow, b light/belly, c accent, plus the globals.
Every creature faces LEFT (toward the player) in a 3/4 pose.
"""
from lib import C

P48 = {}
PAL48 = {}


def sprite48(name, pal):
    def deco(fn):
        P48[name] = fn
        PAL48[name] = pal
        return fn
    return deco


def render48(name):
    c = C(48)
    P48[name](c)
    return [''.join(r) for r in c.g]


def cord(c, pts, col='c'):
    """Coiled phone cord along a path: alternating loops."""
    for i, (x, y) in enumerate(pts):
        c.ell(x, y, 1.6, 1.6, col)
    return c


def flames(c, base_x, base_y, tongues, col='f', core='F'):
    """tongues: list of (dx, height, lean)."""
    for dx, h, lean in tongues:
        x = base_x + dx
        c.poly([(x - 3, base_y), (x + 3, base_y), (x + lean, base_y - h)], col)
        c.poly([(x - 1.5, base_y), (x + 1.5, base_y), (x + lean * .6, base_y - h * .55)], core)
    return c


# ---------------------------------------------------------------- FIRE: wolf pup with a modem's scream
@sprite48('Dialupine', {'a': '#e8582a', 'd': '#a8361a', 'b': '#ffe0b0', 'c': '#d9cfb6'})
def dialupine(c):
    # coiled phone-cord tail (behind body)
    cord(c, [(36, 36), (39, 34), (41, 31), (42, 28), (41, 25), (39, 23), (40, 20)])
    c.rect(38, 16, 42, 19, 'w')                      # RJ11 plug on the tail tip
    # haunch + body
    c.ell(29, 36, 8, 8, 'a')
    c.ell(33, 39, 6, 5, 'a')
    # front legs
    c.rect(17, 34, 20, 44, 'a'); c.rect(23, 36, 26, 44, 'a')
    c.rect(16, 43, 21, 45, 'b'); c.rect(22, 43, 27, 45, 'b')
    c.rect(31, 42, 38, 45, 'b')                      # hind paw
    # chest / belly
    c.ell(22, 33, 6, 7, 'b')
    # head
    c.ell(18, 20, 10, 9, 'a')
    # ears (far ear first)
    c.poly([(21, 14), (27, 4), (29, 15)], 'd')
    c.poly([(11, 13), (13, 2), (20, 12)], 'a')
    c.poly([(13, 12), (14, 5), (18, 12)], 'b')
    # flame tuft on the crown (fire reads from the head, not a tail flame)
    flames(c, 16, 13, [(0, 10, -2), (5, 13, 1), (10, 9, 3)])
    # snout, open screaming mouth
    c.ell(8, 23, 6, 4, 'b')
    c.poly([(2, 25), (11, 25), (12, 31), (5, 30)], 'k')
    c.rect(5, 28, 10, 30, 'r')
    c.outline()
    c.shadow('a', 'd')
    # face details (not outlined)
    c.rect(2, 21, 3, 22, 'k')                        # nose
    c.px(3, 21, 'w')
    c.eye(14, 16, 'wide', -1)
    c.brow(12, 14, 'L', 4)
    c.px(4, 25, 'w'); c.px(9, 25, 'w')               # fangs
    # modem status LEDs along the back (line signature)
    for x, y in [(27, 29), (30, 30), (33, 32)]:
        c.px(x, y, 'z')
    # screech lines
    c.line(0, 34, 2, 32, 'k'); c.line(0, 37, 3, 37, 'k')


@sprite48('Modemauler', {'a': '#e04a24', 'd': '#8e2a14', 'b': '#ffd49a', 'c': '#d9cfb6'})
def modemauler(c):
    # cord tail, thicker, raised
    cord(c, [(40, 30), (42, 27), (43, 24), (44, 21), (43, 18), (44, 15), (45, 12)], 'c')
    c.rect(43, 7, 47, 10, 'w')
    # back legs
    c.poly([(33, 30), (41, 30), (42, 44), (36, 44)], 'd')
    c.rect(35, 42, 43, 45, 'b')
    # body (prowling, head low)
    c.ell(28, 29, 13, 8, 'a')
    # front legs (far then near)
    c.poly([(22, 32), (27, 32), (26, 44), (21, 44)], 'd')
    c.poly([(15, 30), (21, 30), (19, 44), (13, 44)], 'a')
    c.rect(12, 42, 20, 45, 'b'); c.rect(20, 42, 27, 45, 'b')
    # head
    c.ell(13, 25, 9, 7, 'a')
    c.poly([(9, 19), (12, 8), (17, 18)], 'a')        # ear
    c.poly([(11, 17), (12, 11), (15, 17)], 'b')
    # snout + snarl
    c.poly([(0, 25), (8, 21), (12, 27), (6, 32), (0, 30)], 'b')
    c.poly([(1, 28), (9, 28), (8, 32), (2, 31)], 'k')
    # flame mane from crown down the spine
    flames(c, 14, 21, [(0, 9, -3), (5, 13, -1), (10, 14, 1), (15, 13, 2), (20, 11, 3), (25, 8, 3)])
    c.outline()
    c.shadow('a', 'd')
    c.rect(0, 24, 1, 25, 'k')
    c.eye(9, 22, 'wide', -1); c.brow(7, 20, 'L', 4)
    for x in (2, 4, 6, 8):
        c.px(x, 28, 'w')
    c.px(3, 31, 'w'); c.px(7, 31, 'w')
    # LED strip along the flank (same signature, now a full bar)
    for i, col in enumerate('zzzgzy'):
        c.px(22 + i * 3, 30, col)
    c.line(20, 33, 38, 33, 'd')


# ---------------------------------------------------------------- WATER: platypus with a floppy-disk bill
@sprite48('Floppuss', {'a': '#3f7fe0', 'd': '#2650a8', 'b': '#a8dcff', 'c': '#26262f', 'e': '#c9ced8'})
def floppuss(c):
    # low, flat platypus body; beaver-paddle tail
    c.ell(41, 35, 5, 3, 'd')
    c.ell(28, 34, 13, 7, 'a')
    c.ell(26, 38, 9, 3, 'b')
    # webbed feet
    c.poly([(17, 38), (22, 38), (23, 44), (13, 44)], 'a')
    c.poly([(31, 39), (36, 39), (38, 44), (29, 44)], 'a')
    c.rect(11, 43, 23, 45, 'c'); c.rect(28, 43, 39, 45, 'c')
    # head
    c.ell(18, 27, 8, 7, 'a')
    # FLOPPY-DISK BILL, seen face-on: 13x13 square
    c.rect(1, 22, 13, 34, 'c')
    c.outline()
    c.shadow('a', 'd')
    # disk anatomy: sliding metal shutter on top, label below, notched corner, hub hole
    c.rect(4, 22, 10, 26, 'e'); c.rect(7, 23, 8, 25, 'c')
    c.rect(3, 29, 11, 33, 'w'); c.line(4, 30, 10, 30, 'b'); c.line(4, 32, 8, 32, 'b')
    c.px(1, 22, '#'); c.px(12, 33, 'e')
    # face
    c.eye(17, 23, 'tall', -1); c.brow(15, 21, 'L', 3)
    c.line(14, 31, 16, 30, 'k')                      # smirk at the hinge
    # splash
    c.px(45, 40, 'q'); c.px(46, 41, 'q'); c.px(44, 41, 'q'); c.px(47, 38, 'q')


@sprite48('CDRompuss', {'a': '#2f6ad0', 'd': '#1c3f8a', 'b': '#9fd6ff', 'c': '#26262f', 'e': '#c9ced8'})
def cdrompuss(c):
    # the tail is now a CD: big disc behind the body
    c.ell(36, 24, 11, 11, 'e')
    # standing upright, chest out
    c.ell(23, 30, 11, 12, 'a')
    c.ell(21, 33, 7, 8, 'b')
    c.rect(16, 39, 21, 44, 'a'); c.rect(26, 39, 31, 44, 'a')
    c.rect(12, 43, 22, 45, 'c'); c.rect(25, 43, 34, 45, 'c')
    c.rect(14, 27, 31, 31, 'd')                      # arms crossed
    c.ell(20, 14, 9, 8, 'a')
    # CD-DRIVE BILL: drive face with the tray slid OUT, a disc riding in it
    c.rect(2, 9, 14, 15, 'c')
    c.rect(1, 15, 13, 20, 'e')
    c.outline()
    c.shadow('a', 'd')
    c.ell(7, 17, 4, 2, 'w'); c.px(7, 17, 'e'); c.px(5, 16, 'm'); c.px(9, 18, 'q')
    c.rect(4, 11, 7, 12, 'z')                        # busy LED
    c.rect(10, 12, 12, 13, 'e')                      # eject button
    # rainbow sheen + hub on the tail disc
    for (x, y), col in zip([(41, 16), (44, 19), (45, 24), (44, 29), (41, 32)], 'myqgy'):
        c.px(x, y, col); c.px(x - 1, y, col)
    c.ell(36, 24, 2, 2, 'w'); c.px(36, 24, 'k')
    c.eye(19, 10, 'tall', -1); c.brow(17, 8, 'L', 4)
    c.line(15, 21, 18, 20, 'k')
    c.line(15, 29, 30, 29, 'a')


# ---------------------------------------------------------------- GRASS: lucky troll with a living hairdo
@sprite48('Trollsprout', {'a': '#f2b48a', 'd': '#c47d58', 'b': '#ffe6cc', 'c': '#ff3fa4'})
def trollsprout(c):
    # HAIR: a tall leafy plume, half the sprite's height (the silhouette)
    c.poly([(14, 22), (10, 8), (15, 13), (16, 1), (21, 10), (25, 0), (28, 11), (34, 4), (32, 15), (38, 12), (33, 22)], 'L')
    c.poly([(16, 20), (15, 11), (19, 14), (21, 5), (24, 13), (27, 6), (28, 15), (32, 10), (30, 20)], 'l')
    # body: round, pot-bellied
    c.ell(24, 36, 9, 8, 'a')
    # feet
    c.ell(18, 44, 4, 2, 'a'); c.ell(30, 44, 4, 2, 'a')
    # arms: one waving up
    c.poly([(15, 33), (8, 23), (11, 21), (18, 31)], 'a')
    c.ell(9, 21, 2, 2, 'a')
    c.poly([(31, 33), (37, 38), (35, 40), (30, 36)], 'a')
    # head with big ears
    c.ell(23, 25, 9, 7, 'a')
    c.poly([(12, 23), (8, 19), (15, 21)], 'a')
    c.poly([(33, 22), (38, 18), (32, 26)], 'a')
    c.outline()
    c.shadow('a', 'd')
    # gem belly button (signature)
    c.ell(24, 37, 2, 2, 'c'); c.px(23, 36, 'w')
    # face: wide lucky grin, squinty eyes
    c.eye(18, 23, 'big', -1); c.eye(25, 23, 'big', -1)
    c.line(17, 29, 28, 29, 'k'); c.px(16, 28, 'k'); c.px(29, 28, 'k')
    c.rect(19, 30, 26, 30, 'w')
    c.px(14, 27, 'm'); c.px(31, 27, 'm')             # blush
    # little sprout sparkle
    c.px(37, 3, 'y'); c.px(36, 4, 'y'); c.px(38, 4, 'y'); c.px(37, 5, 'y')


@sprite48('Trolltree', {'a': '#d99a6c', 'd': '#9c6440', 'b': '#ffe0c0', 'c': '#ff3fa4'})
def trolltree(c):
    # canopy hair: a full tree crown
    c.ell(24, 10, 18, 10, 'L')
    c.ell(16, 7, 7, 5, 'l'); c.ell(30, 6, 8, 5, 'l')
    c.rect(20, 16, 28, 21, 't')                      # trunk of hair
    # body: stocky, wide
    c.ell(24, 33, 13, 11, 'a')
    # root feet
    c.poly([(12, 40), (19, 40), (21, 46), (8, 46)], 't')
    c.poly([(28, 40), (35, 40), (40, 46), (27, 46)], 't')
    # arms like branches
    c.poly([(11, 28), (2, 34), (4, 37), (13, 33)], 'a')
    c.poly([(36, 28), (45, 33), (43, 36), (35, 33)], 'a')
    # head
    c.ell(23, 23, 9, 6, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.shadow('L', 'G')
    # bird nest in the canopy (keeps the joke: "the hair is now load-bearing")
    c.ell(35, 4, 3, 1, 't'); c.px(34, 3, 'w'); c.px(36, 3, 'q')
    # gem belly glowing
    c.ell(24, 35, 3, 3, 'c'); c.px(23, 34, 'w')
    for x, y in [(19, 35), (29, 35), (24, 30), (24, 40)]:
        c.px(x, y, 'm')
    # scowl
    c.eye(17, 21, 'big', -1); c.eye(25, 21, 'big', -1)
    c.brow(15, 19, 'L', 4); c.brow(25, 19, 'R', 4)
    c.line(18, 27, 28, 27, 'k'); c.px(17, 28, 'k'); c.px(29, 28, 'k')
    c.px(20, 28, 'w'); c.px(26, 28, 'w')             # tusks
