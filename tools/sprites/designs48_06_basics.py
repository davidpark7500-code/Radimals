"""Dex 61-75: school supplies, mall life, couch life, spooky geese."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Binderling / Binderbeast: turtles with binder shells
@sprite48('Binderling', {'a': '#5ce6a0', 'd': '#2ea86a', 'b': '#e0fff0', 'c': '#ff3fa4', 'e': '#c9ced8'})
def binderling(c):
    c.ell(12, 30, 8, 7, 'a')                                                   # head poking out
    c.ell(14, 43, 3, 2, 'a'); c.ell(34, 43, 3, 2, 'a')
    # binder shell, slightly open with a velcro flap
    c.rect(18, 18, 42, 40, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.rect(20, 20, 40, 38, 'm'); c.line(30, 18, 30, 40, 'R')
    for y in (23, 29, 35):
        c.ring(24, y, 1.5, 1.5, 1, 'e')                                         # rings
    c.rect(38, 26, 42, 32, 'n')                                                  # velcro flap
    for y in range(27, 32, 2):
        c.line(39, y, 41, y, 'v')
    c.line(22, 24, 28, 24, 'w'); c.line(22, 30, 27, 30, 'w')                      # notebook paper
    bigeye(c, 7, 27, 3, 4); bigeye(c, 13, 27, 3, 4)
    c.line(9, 34, 12, 34, 'k')
    blush(c, 5, 32)
    c.px(44, 22, 'k'); c.px(45, 25, 'k')                                         # RRRIP


@sprite48('Binderbeast', {'a': '#3ad08a', 'd': '#1e8a56', 'b': '#d8ffe8', 'c': '#2e7dff', 'e': '#c9ced8'})
def binderbeast(c):
    c.ell(10, 28, 9, 8, 'a')
    for x, col in [(14, 'd'), (38, 'd'), (18, 'a'), (41, 'a')]:
        c.ell(x, 42, 4, 3, col)
    c.rect(16, 12, 46, 40, 'c')
    # pencils stuck in the shell (angled, short)
    c.line(24, 12, 20, 5, 'y', 2); c.line(32, 12, 33, 4, 'y', 2); c.line(40, 12, 44, 6, 'y', 2)
    c.outline()
    c.shadow('a', 'd')
    c.rect(18, 14, 44, 38, 'q'); c.line(31, 12, 31, 40, 'n')
    for x, y in [(20, 5), (33, 4), (44, 6)]:
        c.px(x, y, 'm')
    for y in (18, 25, 32):
        c.ring(22, y, 1.5, 1.5, 1, 'e')
    for i, y in enumerate(range(18, 36, 4)):
        c.line(34, y, 42, y, 'w')
    c.rect(36, 30, 41, 35, 'f'); c.line(36, 33, 41, 31, 'd')                    # crushed juice box
    bigeye(c, 4, 24, 3, 5); bigeye(c, 11, 24, 3, 5)
    c.line(3, 23, 7, 24, 'k'); c.line(11, 24, 14, 23, 'k')
    c.line(4, 32, 10, 32, 'k'); c.px(6, 33, 'w')


# ---------------------------------------------------------------- Fannypacker: a raccoon wearing it in the front
@sprite48('Fannypacker', {'a': '#8a8a9a', 'd': '#5a5a6a', 'b': '#e8e8f0', 'c': '#ff3fa4'})
def fannypacker(c):
    # ringed tail
    c.ell(38, 34, 6, 4, 'a'); c.ell(43, 28, 4, 4, 'a')
    c.ell(24, 34, 11, 10, 'a')
    c.ell(23, 37, 7, 6, 'b')
    c.ell(17, 44, 3, 2, 'd'); c.ell(30, 44, 3, 2, 'd')
    c.ell(22, 19, 12, 10, 'a')
    c.poly([(12, 13), (12, 4), (18, 10)], 'a'); c.poly([(27, 10), (32, 4), (32, 13)], 'a')
    c.outline()
    c.shadow('a', 'd')
    c.line(37, 31, 39, 37, 'k'); c.line(42, 25, 45, 30, 'k')
    # mask
    c.ell(16, 19, 5, 3, 'k'); c.ell(28, 19, 5, 3, 'k')
    c.ell(22, 24, 4, 3, 'b')
    # the fanny pack, worn in front, neon
    c.rect(13, 31, 34, 33, 'q')
    c.rect(17, 30, 30, 37, 'c'); c.line(18, 33, 29, 33, 'y'); c.px(29, 31, 'w')
    bigeye(c, 14, 17); bigeye(c, 26, 17)
    c.rect(21, 23, 23, 24, 'k')
    c.line(20, 26, 24, 26, 'k')
    blush(c, 11, 23); blush(c, 31, 23)


# ---------------------------------------------------------------- Goofyputt / Goofypuddle: pink putty pups
@sprite48('Goofyputt', {'a': '#ff8ac0', 'd': '#d8588e', 'b': '#ffe0ee', 'c': '#ff3f3f'})
def goofyputt(c):
    # half of the plastic egg it came in, as a little bed
    c.ell(24, 40, 15, 6, 'c')
    c.clear(0, 30, 47, 37)
    c.ell(24, 32, 11, 9, 'a')
    c.ell(15, 22, 4, 5, 'a'); c.ell(32, 22, 4, 5, 'a')                            # droopy ears
    c.outline()
    c.shadow('a', 'd')
    c.line(10, 37, 38, 37, 'R')
    # copied comics on its belly
    c.rect(19, 34, 29, 39, 'w'); c.line(20, 36, 23, 36, 'k'); c.ell(26, 36, 1, 1, 'k'); c.line(20, 38, 28, 38, 'q')
    bigeye(c, 17, 27); bigeye(c, 27, 27)
    c.line(22, 32, 24, 32, 'k')
    blush(c, 14, 31); blush(c, 31, 31)
    c.px(44, 25, 'k'); c.px(46, 22, 'k')                                          # boing


@sprite48('Goofypuddle', {'a': '#ff7ab4', 'd': '#cc4a84', 'b': '#ffe0ee', 'c': '#ff3f3f'})
def goofypuddle(c):
    # melted into a puddle, still smiling
    c.ell(24, 40, 22, 6, 'a')
    c.ell(22, 30, 12, 9, 'a')
    c.ell(12, 22, 4, 6, 'a'); c.ell(33, 22, 4, 6, 'a')
    for x in (6, 15, 34, 41):
        c.ell(x, 44, 2.5, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(8, 40), (38, 39), (30, 43)]:
        c.ell(x, y, 2, 1, 'b')
    bigeye(c, 15, 26); bigeye(c, 26, 26)
    c.line(18, 33, 24, 33, 'k'); c.px(17, 32, 'k'); c.px(25, 32, 'k')
    c.rect(19, 34, 22, 35, 'c')                                                     # tongue out
    blush(c, 12, 30); blush(c, 29, 30)
    soft_flame(c, 40, 22, 7, 0, 'y', 'F')                                           # the sun did this


# ---------------------------------------------------------------- Springee / Springstretch: spring-coil caterpillars
@sprite48('Springee', {'a': '#c9ced8', 'd': '#8a93ab', 'b': '#ffffff', 'c': '#ff3fa4'})
def springee(c):
    # arched over a stair step: coil rings
    c.rect(26, 38, 47, 46, 't'); c.rect(0, 44, 26, 46, 't')
    pts = [(12, 40), (13, 34), (16, 28), (20, 24), (25, 22), (30, 23), (34, 27), (36, 32)]
    for x, y in pts:
        c.ring(x, y, 4, 4.5, 2, 'a')
    c.ell(10, 36, 7, 6, 'c')                                                        # head
    c.outline()
    c.shadow('a', 'd')
    for x, y in pts:
        c.px(x - 2, y - 3, 'b')
    bigeye(c, 5, 33, 3, 4); bigeye(c, 11, 33, 3, 4)
    c.line(7, 39, 10, 39, 'k')
    blush(c, 3, 38)


@sprite48('Springstretch', {'a': '#b8bec8', 'd': '#7a8296', 'b': '#ffffff', 'c': '#a04cff'})
def springstretch(c):
    # a long coil tied in a knot around itself
    pts = [(10, 38), (12, 30), (18, 24), (26, 22), (34, 24), (38, 30), (36, 37), (30, 41), (22, 40), (17, 34),
           (19, 27), (26, 28), (33, 33), (40, 40)]
    for x, y in pts:
        c.ring(x, y, 4, 4.5, 2, 'a')
    c.ell(9, 13, 8, 7, 'c')
    c.line(10, 20, 12, 28, 'a', 3)
    c.outline()
    c.shadow('a', 'd')
    bigeye(c, 4, 10, 3, 4); bigeye(c, 11, 10, 3, 4)
    c.line(3, 9, 7, 10, 'k'); c.line(11, 10, 14, 9, 'k')                              # still annoyed since 1993
    c.line(6, 16, 10, 16, 'k')


# ---------------------------------------------------------------- Mallrat / Mallratking
@sprite48('Mallrat', {'a': '#9aa0b0', 'd': '#666c80', 'b': '#f0e0e8', 'c': '#2e7dff'})
def mallrat(c):
    c.line(34, 40, 45, 34, 'm', 2); c.line(45, 34, 46, 28, 'm', 2)                     # tail curled up
    c.ell(26, 35, 10, 8, 'a')
    c.ell(19, 44, 3, 1.5, 'm'); c.ell(31, 44, 3, 1.5, 'm')
    c.ell(18, 22, 11, 9, 'a')
    c.ell(10, 13, 5, 5, 'a'); c.ell(26, 12, 5, 5, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.ell(10, 13, 3, 3, 'b'); c.ell(26, 12, 3, 3, 'b')
    # backwards cap
    c.ell(19, 14, 8, 3, 'c'); c.rect(25, 13, 31, 15, 'c')
    # soft pretzel in its paws
    c.ring(20, 34, 4, 3, 1, 't'); c.px(18, 33, 'w'); c.px(22, 35, 'w')
    bigeye(c, 11, 19); bigeye(c, 21, 19, 3, 5)
    c.rect(6, 25, 7, 26, 'm')
    c.line(9, 28, 13, 28, 'k')
    c.rect(9, 29, 10, 30, 'w')
    blush(c, 14, 25)


@sprite48('Mallratking', {'a': '#8a90a4', 'd': '#585e74', 'b': '#f0e0e8', 'c': '#ffcf3a'})
def mallratking(c):
    # sitting on a pile of fountain coins
    c.ell(24, 43, 18, 4, 'c')
    c.ell(25, 31, 13, 11, 'a')
    c.ell(24, 34, 8, 7, 'b')
    c.line(36, 40, 45, 32, 'm', 2)
    c.ell(18, 17, 11, 9, 'a')
    c.ell(9, 9, 5, 5, 'a'); c.ell(27, 8, 5, 5, 'a')
    # coin crown + red cape
    c.poly([(11, 9), (13, 3), (16, 7), (19, 2), (22, 7), (25, 3), (26, 9)], 'c')
    c.poly([(30, 22), (44, 28), (42, 42), (34, 40)], 'R')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(10, 42), (17, 44), (30, 44), (38, 42), (23, 41)]:
        c.ring(x, y, 1.6, 1, 1, 'd')
    c.px(19, 4, 'R'); c.px(13, 5, 'q'); c.px(25, 5, 'q')
    # fountain key on a lanyard
    c.line(20, 26, 24, 30, 'k'); c.ring(25, 31, 1.5, 1.5, 1, 'c')
    bigeye(c, 10, 15); bigeye(c, 20, 15, 3, 5)
    c.line(9, 14, 13, 14, 'k'); c.line(20, 14, 23, 14, 'k')
    c.rect(5, 20, 6, 21, 'm')
    c.line(8, 23, 14, 23, 'k'); c.px(15, 22, 'k')


# ---------------------------------------------------------------- Couchpotato: a potato sloth that never gets up
@sprite48('Couchpotato', {'a': '#c8965a', 'd': '#946630', 'b': '#f0d8b0', 'c': '#2e7dff'})
def couchpotato(c):
    # the couch
    c.rect(2, 34, 46, 44, 'c'); c.rect(2, 26, 8, 44, 'c'); c.rect(40, 26, 46, 44, 'c')
    # potato sloth slumped across it
    c.ell(25, 31, 15, 9, 'a')
    c.ell(13, 24, 3, 5, 'a')                                                           # arm up holding remote
    c.outline()
    c.shadow('a', 'd')
    c.line(2, 38, 46, 38, 'n')
    for x, y in [(21, 27), (32, 30), (27, 35), (36, 26)]:
        c.px(x, y, 'd')                                                                 # potato eyes (the other kind)
    c.rect(11, 17, 14, 22, 'k'); c.px(12, 18, 'r')                                      # remote
    c.ell(22, 30, 6, 4, 'b')
    c.line(17, 27, 20, 27, 'k'); c.line(24, 27, 27, 27, 'k')                             # sleepy eyes
    c.line(20, 32, 23, 32, 'k')
    blush(c, 15, 30); blush(c, 27, 30)
    # TV glow on its face
    for x, y in [(30, 22), (33, 20), (36, 22)]:
        c.px(x, y, 'q')


# ---------------------------------------------------------------- Gooshpod: a pea pod with bursting gummy peas
@sprite48('Gooshpod', {'a': '#5cd64a', 'd': '#2e962a', 'b': '#d8ffc8', 'c': '#ff3f8a'})
def gooshpod(c):
    # open pod as a little boat-shaped body
    c.poly([(4, 30), (14, 38), (34, 38), (44, 30), (34, 34), (14, 34)], 'a')
    c.ell(24, 34, 18, 5, 'a')
    c.line(44, 30, 46, 22, 'a', 2)                                                       # curly stem
    c.ell(12, 44, 2, 1.5, 'd'); c.ell(36, 44, 2, 1.5, 'd')
    # three gummy peas (the middle one is the face)
    for x, col in [(13, 'c'), (35, 'v')]:
        c.ell(x, 28, 5, 5, col)
    c.ell(24, 25, 7, 7, 'y')
    c.outline()
    c.shadow('a', 'd')
    for x in (13, 35):
        c.px(x - 2, 25, 'w')
    c.px(22, 20, 'w'); c.px(23, 20, 'w')
    bigeye(c, 19, 23, 3, 4); bigeye(c, 26, 23, 3, 4)
    c.ell(24, 30, 1.2, 1, 'k')
    blush(c, 17, 28); blush(c, 29, 28)
    # juice squirting from the left pea
    for x, y in [(6, 22), (4, 19), (7, 18)]:
        c.px(x, y, 'c')


# ---------------------------------------------------------------- Freshprints / Freshroyal: husky pups with fresh kicks
@sprite48('Freshprints', {'a': '#6a7aa0', 'd': '#404c70', 'b': '#f4f6ff', 'c': '#ff3fa4'})
def freshprints(c):
    c.ell(36, 30, 4, 6, 'a')                                                              # curled tail
    c.ell(25, 34, 11, 8, 'a')
    c.ell(24, 37, 7, 5, 'b')
    # neon high-tops
    c.rect(14, 41, 21, 46, 'c'); c.rect(28, 41, 35, 46, 'c')
    c.ell(19, 21, 12, 10, 'a')
    c.poly([(9, 15), (9, 4), (16, 11)], 'a'); c.poly([(23, 11), (29, 4), (30, 15)], 'a')
    c.outline()
    c.shadow('a', 'd')
    c.line(14, 44, 21, 44, 'w'); c.line(28, 44, 35, 44, 'w')
    c.ell(16, 24, 8, 5, 'b')
    bigeye(c, 12, 19); bigeye(c, 22, 19)
    c.rect(8, 24, 10, 25, 'k')
    c.line(13, 28, 17, 28, 'k'); c.px(18, 27, 'k')
    blush(c, 9, 26); blush(c, 26, 26)
    # paw prints left in wet cement
    for x in (2, 8):
        c.ell(x + 1, 44, 1.2, 1, 'd'); c.px(x, 42, 'd'); c.px(x + 2, 42, 'd')


@sprite48('Freshroyal', {'a': '#5a6a96', 'd': '#343e66', 'b': '#f4f6ff', 'c': '#ffcf3a'})
def freshroyal(c):
    c.ell(38, 26, 5, 7, 'a')
    c.ell(26, 32, 14, 10, 'a')
    c.ell(24, 35, 9, 7, 'b')
    c.rect(11, 40, 20, 46, 'm'); c.rect(29, 40, 38, 46, 'm')
    c.ell(18, 16, 12, 10, 'a')
    c.poly([(8, 11), (8, 0), (15, 7)], 'a'); c.poly([(22, 7), (28, 0), (29, 11)], 'a')
    c.outline()
    c.shadow('a', 'd')
    c.line(11, 43, 20, 43, 'w'); c.line(29, 43, 38, 43, 'w')
    # gold chain + flipped-up shades
    for x in range(14, 34, 2):
        c.px(x, 26 + (1 if 18 < x < 30 else 0), 'c')
    c.ell(24, 31, 2.5, 2.5, 'c')
    c.rect(9, 10, 27, 12, 'k'); c.px(11, 10, 'q'); c.px(21, 10, 'q')
    c.ell(15, 19, 8, 5, 'b')
    bigeye(c, 11, 14); bigeye(c, 21, 14)
    c.line(10, 13, 15, 13, 'k'); c.line(21, 13, 26, 13, 'k')
    c.rect(7, 19, 9, 20, 'k')
    c.line(12, 23, 19, 23, 'k'); c.px(20, 22, 'k')
    c.px(13, 24, 'c')                                                                        # gold tooth


# ---------------------------------------------------------------- Creepskin / Shiverskin: mildly scary geese
@sprite48('Creepskin', {'a': '#a0d860', 'd': '#6a9c30', 'b': '#f0ffd8', 'c': '#ffb02e'})
def goosebumpy(c):
    c.ell(27, 35, 12, 9, 'a')
    c.ell(37, 32, 5, 6, 'd')                                                                  # wing
    c.line(17, 28, 14, 18, 'a', 4)
    c.ell(14, 15, 7, 6, 'a')
    c.ell(21, 44, 3, 1.5, 'c'); c.ell(31, 44, 3, 1.5, 'c')
    c.outline()
    c.shadow('a', 'd')
    # goosebumps all over
    for x, y in [(22, 33), (27, 37), (32, 34), (25, 40), (30, 30), (12, 13)]:
        c.px(x, y, 'b'); c.px(x + 1, y + 1, 'd')
    c.poly([(2, 16), (8, 14), (8, 18)], 'c')
    bigeye(c, 10, 12, 3, 4); bigeye(c, 16, 12, 3, 4)
    c.line(9, 20, 12, 21, 'k'); c.line(12, 21, 14, 20, 'k')                                   # wobbly nervous mouth
    blush(c, 17, 17)
    # its own warning label
    c.rect(32, 22, 42, 27, 'y'); c.px(37, 23, 'k'); c.px(37, 24, 'k'); c.px(37, 26, 'k')
    for x, y in [(3, 8), (5, 6)]:
        c.px(x, y, 'q')                                                                        # sweat


@sprite48('Shiverskin', {'a': '#7ac43a', 'd': '#4a8a1a', 'b': '#e8ffd0', 'c': '#ffb02e'})
def goosepimple(c):
    # a vampire-caped goose
    c.poly([(26, 16), (46, 22), (44, 44), (20, 40)], 'v')
    c.ell(26, 34, 13, 9, 'a')
    c.line(16, 27, 13, 15, 'a', 5)
    c.ell(13, 12, 8, 7, 'a')
    c.ell(20, 44, 3, 1.5, 'c'); c.ell(32, 44, 3, 1.5, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.line(28, 18, 44, 24, 'R')
    c.poly([(0, 13), (7, 11), (7, 17)], 'c')
    c.px(4, 16, 'w'); c.px(6, 16, 'w')                                                          # tiny fangs: the twist
    bigeye(c, 9, 9, 3, 4); bigeye(c, 15, 9, 3, 4)
    c.line(8, 8, 12, 9, 'k'); c.line(15, 9, 18, 8, 'k')
    c.line(9, 16, 13, 16, 'k'); c.px(14, 15, 'k')
    for x, y in [(22, 33), (28, 37), (31, 31)]:
        c.px(x, y, 'b')
