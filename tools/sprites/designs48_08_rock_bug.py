"""Dex 91-105: shoulder-carried rocks, novelty rocks, and the bug zoo."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Boomboxer: a boxer dog with a boombox on its shoulder
@sprite48('Boomboxer', {'a': '#c8905a', 'd': '#8e5a30', 'b': '#fff0dc', 'c': '#2a2a38', 'e': '#c9ced8'})
def boomboxer(c):
    c.ell(24, 34, 12, 10, 'a')
    c.ell(23, 37, 7, 6, 'b')
    c.ell(16, 44, 4, 2, 'a'); c.ell(31, 44, 4, 2, 'a')
    # boxing glove up
    c.ell(10, 32, 5, 5, 'r')
    # boombox on its shoulder
    c.rect(24, 8, 46, 22, 'c')
    c.ell(18, 21, 11, 9, 'a')
    c.ell(10, 14, 3, 5, 'd'); c.ell(26, 13, 3, 5, 'd')
    c.outline()
    c.shadow('a', 'd')
    c.ring(30, 16, 4, 4, 1, 'e'); c.ring(40, 16, 4, 4, 1, 'e'); c.px(30, 16, 'e'); c.px(40, 16, 'e')
    c.rect(33, 10, 37, 12, 'q'); c.line(27, 7, 43, 7, 'e')
    c.px(8, 30, 'w')
    c.ell(14, 25, 6, 4, 'b')
    bigeye(c, 12, 18); bigeye(c, 21, 18, 3, 5)
    c.rect(9, 23, 11, 24, 'k')
    c.line(11, 28, 16, 28, 'k'); c.px(17, 27, 'k')
    for x, y in [(2, 6), (4, 3), (1, 10)]:
        c.rect(x, y, x + 1, y + 1, 'k')                                                    # notes, loud


# ---------------------------------------------------------------- Brickphone / Brickzilla: rhinos whose horn is the antenna
@sprite48('Brickphone', {'a': '#5a6070', 'd': '#363b48', 'b': '#c9d0dc', 'c': '#b6ff3b'})
def brickphone(c):
    c.ell(28, 32, 13, 10, 'a')
    for x in (19, 25, 33, 38):
        c.ell(x, 42, 3, 3, 'a')
    c.ell(14, 26, 10, 9, 'a')
    c.ell(25, 17, 3, 4, 'a')                                                                  # ear
    # stubby antenna horn with a round knob (short, chunky)
    c.rect(7, 13, 9, 19, 'd'); c.ell(8, 12, 2.5, 2.5, 'k')
    c.outline()
    c.shadow('a', 'd')
    # keypad on its flank, little screen
    c.rect(26, 26, 36, 29, 'c')
    for x in (27, 31, 35):
        for y in (32, 35, 38):
            c.px(x, y, 'b')
    bigeye(c, 11, 23); bigeye(c, 19, 23, 3, 5)
    c.line(6, 31, 10, 31, 'k')
    blush(c, 14, 30)


@sprite48('Brickzilla', {'a': '#4a5060', 'd': '#2a2e3a', 'b': '#c0c8d4', 'c': '#b6ff3b'})
def brickzilla(c):
    c.ell(28, 29, 17, 12, 'a')
    for x, col in [(16, 'd'), (38, 'd'), (21, 'a'), (42, 'a')]:
        c.ell(x, 41, 5, 5, col)
    c.ell(12, 24, 11, 10, 'a')
    c.rect(4, 8, 7, 17, 'd'); c.ell(5, 7, 3, 3, 'k')
    c.ell(23, 15, 3, 4, 'a')
    c.outline()
    c.shadow('a', 'd')
    # armor plates = stacked phones, one cracked screen
    for x in (22, 30, 38):
        c.rect(x, 20, x + 5, 30, 'd'); c.rect(x + 1, 21, x + 4, 24, 'c')
    c.line(31, 21, 34, 24, 'k')
    for x, y in [(19, 34), (40, 22), (12, 33)]:
        c.line(x, y, x + 2, y + 1, 'k')                                                         # scuffs
    bigeye(c, 8, 21); bigeye(c, 16, 21, 3, 5)
    c.line(7, 20, 11, 20, 'k'); c.line(16, 20, 19, 20, 'k')
    c.line(3, 29, 9, 29, 'k'); c.px(5, 30, 'w')


# ---------------------------------------------------------------- Petrock / Petrocksteady: the perfect pet
@sprite48('Petrock', {'a': '#a8a29a', 'd': '#706a62', 'b': '#d8d2c8', 'c': '#c89a5a'})
def petrock(c):
    # cardboard carry box with air holes, straw bedding
    c.rect(6, 28, 42, 46, 'c')
    c.ell(24, 26, 13, 9, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x in (12, 18, 30, 36):
        c.ell(x, 37, 1.5, 1.5, 't')
    c.line(6, 31, 42, 31, 't')
    for x in range(9, 40, 4):
        c.line(x, 29, x + 2, 26, 'y')                                                             # straw
    # googly eyes (glued on, slightly crooked)
    c.ell(18, 23, 4, 4, 'w'); c.ell(29, 22, 4, 4, 'w')
    c.ell(19, 25, 2, 2, 'k'); c.ell(28, 24, 2, 2, 'k')
    c.ring(18, 23, 4, 4, 1, 'k'); c.ring(29, 22, 4, 4, 1, 'k')
    c.line(22, 30, 25, 30, 'k')
    c.px(30, 18, 'b'); c.px(17, 30, 'd')


@sprite48('Petrocksteady', {'a': '#9a948c', 'd': '#625c54', 'b': '#d0cac0', 'c': '#a04cff'})
def petrocksteady(c):
    # velvet cushion + price tag
    c.ell(24, 40, 20, 6, 'c')
    c.ell(24, 27, 15, 12, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(6, 40), (42, 40), (24, 45)]:
        c.px(x, y, 'y')                                                                           # tassels
    c.rect(11, 20, 37, 25, 'k'); c.px(14, 21, 'q'); c.px(30, 21, 'q'); c.line(23, 22, 25, 22, 'k')
    c.line(19, 32, 29, 32, 'k'); c.px(30, 31, 'k')                                                 # smug
    c.line(38, 18, 43, 12, 'k'); c.rect(41, 7, 47, 12, 'w'); c.px(43, 9, 'g'); c.px(45, 9, 'g')    # $50 tag
    c.px(15, 18, 'b'); c.px(16, 17, 'b')


# ---------------------------------------------------------------- Gargoylie: a stone gargoyle pup judging recess
@sprite48('Gargoylie', {'a': '#8a8f9e', 'd': '#585c6a', 'b': '#c8ccd8', 'c': '#5a5e6c'})
def gargoylie(c):
    # roof ledge
    c.rect(0, 40, 47, 46, 'c')
    # little bat wings
    c.poly([(10, 20), (1, 12), (3, 24), (10, 28)], 'd'); c.poly([(38, 20), (47, 12), (45, 24), (38, 28)], 'd')
    c.ell(24, 31, 11, 10, 'a')
    c.ell(24, 19, 11, 9, 'a')
    c.poly([(14, 13), (12, 4), (19, 10)], 'a'); c.poly([(30, 10), (36, 4), (34, 13)], 'a')         # horns/ears
    c.ell(16, 40, 4, 2, 'a'); c.ell(32, 40, 4, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(18, 34), (30, 30), (22, 12)]:
        c.line(x, y, x + 2, y + 2, 'd')                                                               # stone cracks
    c.line(0, 43, 47, 43, 'd')
    bigeye(c, 17, 17); bigeye(c, 27, 17)
    c.line(16, 16, 21, 17, 'k'); c.line(27, 17, 32, 16, 'k')                                         # judging
    c.line(21, 25, 27, 25, 'k')
    c.px(22, 26, 'w'); c.px(26, 26, 'w')
    c.ell(24, 33, 5, 4, 'b')


# ---------------------------------------------------------------- Cassettle / Cassettitan: cows whose spots are tape reels
@sprite48('Cassettle', {'a': '#f4f4f0', 'd': '#c4c4bc', 'b': '#ffd0d8', 'c': '#2a2a38'})
def cassettle(c):
    c.line(38, 30, 44, 36, 'a', 2); c.ell(45, 38, 2, 2, 'c')                                          # tail tuft, low
    c.rect(16, 26, 40, 38, 'a')
    for x in (18, 23, 33, 38):
        c.rect(x - 1, 38, x + 1, 44, 'a')
    c.ell(14, 24, 10, 9, 'a')
    c.ell(5, 19, 3, 2, 'a'); c.ell(23, 17, 3, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    # cassette window with two reels as cow spots
    c.rect(20, 28, 37, 35, 'c')
    c.ring(25, 31, 2, 2, 1, 'w'); c.ring(32, 31, 2, 2, 1, 'w')
    c.line(26, 33, 31, 33, 't')
    c.rect(20, 26, 37, 27, 'r')                                                                         # label stripe: SIDE A
    for x in (18, 23, 33, 38):
        c.rect(x - 1, 43, x + 1, 44, 'c')
    c.ell(9, 28, 5, 3, 'b')
    c.px(7, 28, 'k'); c.px(11, 28, 'k')
    bigeye(c, 9, 20, 3, 4); bigeye(c, 16, 20, 3, 4)
    c.rect(12, 12, 14, 15, 'y')                                                                          # tiny horn nub
    blush(c, 18, 26)


@sprite48('Cassettitan', {'a': '#e8e8e0', 'd': '#acaca4', 'b': '#ffc8d0', 'c': '#2a2a38'})
def cassettitan(c):
    c.rect(14, 20, 44, 38, 'a')
    for x, col in [(17, 'd'), (39, 'd'), (21, 'a'), (43, 'a')]:
        c.rect(x - 2, 38, x + 1, 45, col)
    c.ell(12, 22, 11, 10, 'a')
    # curved horns
    c.poly([(5, 14), (1, 6), (5, 3), (4, 8), (8, 12)], 'y'); c.poly([(17, 13), (22, 5), (25, 6), (21, 10), (19, 15)], 'y')
    c.outline()
    c.shadow('a', 'd')
    c.rect(20, 23, 41, 34, 'c')
    c.ring(26, 28, 3, 3, 1, 'w'); c.ring(35, 28, 3, 3, 1, 'w')
    c.line(37, 27, 33, 24, 'y', 1)                                                                        # pencil in the reel
    # unspooled tape mane
    for y in (16, 20, 24):
        c.line(22, y, 30, y + 3, 't'); c.line(30, y + 3, 26, y + 6, 't')
    c.ell(7, 27, 5, 3, 'b'); c.px(5, 27, 'k'); c.px(9, 27, 'k')
    bigeye(c, 6, 18, 3, 4); bigeye(c, 14, 18, 3, 4)
    c.line(5, 17, 9, 18, 'k'); c.line(14, 18, 17, 17, 'k')
    for x in (17, 21, 39, 43):
        c.rect(x - 2, 44, x + 1, 45, 'c')


# ---------------------------------------------------------------- Blockstack: a caterpillar made of four falling blocks
@sprite48('Blockstack', {'a': '#3ae0ff', 'd': '#1a9ab8', 'b': '#c8f8ff', 'c': '#ffffff'})
def blockstack(c):
    for i in range(4):
        c.rect(6 + i * 9, 24, 14 + i * 9, 32, 'a')
    for x in (10, 19, 28, 37):
        c.rect(x - 1, 33, x, 36, 'a')
    c.outline()
    for i in range(4):
        x = 6 + i * 9
        c.line(x, 24, x + 8, 24, 'b'); c.line(x, 24, x, 32, 'b'); c.line(x + 8, 25, x + 8, 32, 'd'); c.line(x + 1, 32, x + 8, 32, 'd')
    bigeye(c, 7, 26, 3, 4); bigeye(c, 11, 26, 2, 4)
    c.line(8, 31, 11, 31, 'k')
    # the gap it was made for
    c.rect(4, 40, 44, 46, 'v')
    c.clear(6, 40, 42, 41)
    for x in range(4, 45, 4):
        c.line(x, 40, x, 46, 'n')
    c.px(24, 18, 'y'); c.px(23, 19, 'y'); c.px(25, 19, 'y'); c.px(24, 20, 'y')
    blush(c, 14, 29)


# ---------------------------------------------------------------- Pixelpest: a fly with a tiny LCD for a body
@sprite48('Pixelpest', {'a': '#c8d4a0', 'd': '#8a9868', 'b': '#eef4d8', 'c': '#3a4a2a'})
def pixelpest(c):
    c.ell(14, 14, 8, 6, 'q'); c.ell(32, 12, 9, 6, 'q')                                                     # wings
    c.ell(24, 28, 11, 11, 'a')
    c.ell(13, 24, 8, 7, 'a')
    for x0, x1 in [(17, 13), (24, 24), (31, 35)]:
        c.line(x0, 37, x1, 44, 'c', 1)
    c.outline()
    c.shadow('a', 'd')
    c.ring(14, 14, 8, 6, 1, 'w'); c.ring(32, 12, 9, 6, 1, 'w')
    # the LCD with a pixel... mess on it (beeps at 3 AM)
    c.rect(19, 23, 33, 33, 'c'); c.rect(20, 24, 32, 32, 'g')
    for x, y in [(24, 29), (25, 28), (26, 29), (25, 27), (28, 25), (29, 26)]:
        c.px(x, y, 'k')
    c.ell(9, 20, 3, 3, 'r'); c.ell(16, 19, 3, 3, 'r')                                                      # fly eyes
    c.rect(9, 20, 10, 21, 'k'); c.rect(16, 19, 17, 20, 'k'); c.px(9, 20, 'w'); c.px(16, 19, 'w')
    c.line(10, 28, 13, 28, 'k')
    for x, y in [(40, 30), (42, 27)]:
        c.px(x, y, 'k')


# ---------------------------------------------------------------- Anklehop / Anklehopper: grasshoppers with step counters
@sprite48('Anklehop', {'a': '#7ad64a', 'd': '#4a9a26', 'b': '#e0ffd0', 'c': '#3a6cff'})
def anklehop(c):
    # big folded jumping legs
    c.poly([(28, 32), (42, 22), (44, 26), (34, 36)], 'd'); c.line(42, 25, 44, 42, 'd', 2)
    c.ell(25, 32, 11, 7, 'a')
    c.ell(14, 26, 9, 8, 'a')
    for x in (16, 22):
        c.line(x, 38, x - 2, 44, 'd', 2)
    c.outline()
    c.shadow('a', 'd')
    # pedometer clipped to its middle
    c.rect(22, 27, 32, 35, 'c'); c.rect(23, 28, 31, 31, 'g')
    c.px(24, 29, 'k'); c.px(26, 29, 'k'); c.px(27, 30, 'k'); c.px(29, 29, 'k'); c.px(30, 30, 'k')
    c.line(10, 19, 5, 9, 'k'); c.line(14, 19, 14, 8, 'k')                                                       # antennae
    bigeye(c, 9, 23); bigeye(c, 16, 23, 3, 5)
    c.line(10, 31, 14, 31, 'k')
    blush(c, 7, 29)


@sprite48('Anklehopper', {'a': '#5cc432', 'd': '#2e8018', 'b': '#d8ffc8', 'c': '#3a6cff'})
def anklehopper(c):
    c.poly([(26, 28), (44, 14), (47, 19), (34, 34)], 'd'); c.line(45, 18, 46, 44, 'd', 3)
    c.ell(25, 30, 14, 9, 'a')
    c.ell(12, 22, 10, 9, 'a')
    for x in (14, 22, 30):
        c.line(x, 38, x - 2, 45, 'd', 2)
    c.outline()
    c.shadow('a', 'd')
    c.rect(20, 25, 34, 35, 'c'); c.rect(21, 26, 33, 30, 'g')
    for x in (22, 26, 30):
        c.ring(x + 1, 28, 1, 1.4, 1, 'k')                                                                       # 999
    # bandaged ankle (the flaw)
    c.rect(43, 34, 47, 37, 'w'); c.px(45, 35, 'r')
    c.line(8, 15, 2, 4, 'k'); c.line(12, 14, 13, 3, 'k')
    bigeye(c, 6, 19); bigeye(c, 14, 19, 3, 5)
    c.line(5, 18, 9, 18, 'k'); c.line(14, 18, 17, 18, 'k')
    c.line(6, 27, 11, 27, 'k'); c.px(12, 26, 'k')


# ---------------------------------------------------------------- Mothballer: a round, fuzzy moth in a grandparent cardigan
@sprite48('Mothballer', {'a': '#f4f0e6', 'd': '#c8c0ac', 'b': '#ffffff', 'c': '#8a5aa8'})
def mothballer(c):
    # argyle sweater wings
    c.poly([(16, 20), (2, 10), (4, 30), (16, 30)], 'c'); c.poly([(32, 20), (46, 10), (44, 30), (32, 30)], 'c')
    c.ell(24, 28, 10, 12, 'a')
    c.outline(diag=True)
    c.shadow('a', 'd')
    for x, y in [(8, 18), (40, 18), (10, 25), (38, 25)]:
        c.poly([(x, y - 3), (x + 3, y), (x, y + 3), (x - 3, y)], 'y')
    # feathery antennae
    c.line(19, 17, 14, 8, 'k'); c.line(29, 17, 34, 8, 'k')
    for x, y in [(15, 10), (33, 10)]:
        c.px(x - 1, y, 'k'); c.px(x + 1, y - 1, 'k')
    bigeye(c, 18, 22); bigeye(c, 26, 22)
    c.line(22, 29, 25, 29, 'k')
    blush(c, 16, 27); blush(c, 29, 27)
    for x in (21, 24, 27):
        c.px(x, 34, 'd')                                                                                        # cardigan buttons
    c.px(4, 40, 'q'); c.px(6, 38, 'q')                                                                         # whiff


# ---------------------------------------------------------------- Captula: a tarantula hoarding its winnings
@sprite48('Captula', {'a': '#8a5a3a', 'd': '#5a361e', 'b': '#e8c8a8', 'c': '#ff3fa4'})
def captula(c):
    for x0, x1, y1 in [(14, 4, 40), (17, 8, 45), (30, 40, 45), (33, 44, 40), (14, 3, 30), (33, 45, 30), (18, 12, 22), (30, 36, 22)]:
        c.line(x0 if x0 < 24 else x0, 32, x1, y1, 'a', 2)
    c.ell(24, 33, 11, 9, 'a')
    c.ell(24, 22, 9, 7, 'a')
    c.outline()
    c.shadow('a', 'd')
    # stack of won caps on its back
    for i, col in enumerate('cyqm'):
        c.ell(24, 30 - i * 2 + 10, 7, 2, col)
    for i in range(4):
        c.line(17, 40 - i * 2, 31, 40 - i * 2, 'k')
    bigeye(c, 18, 19); bigeye(c, 26, 19)
    c.px(23, 18, 'k'); c.px(24, 18, 'k')                                                                       # extra little eyes
    c.line(22, 26, 26, 26, 'k'); c.px(27, 25, 'k')
    blush(c, 16, 24); blush(c, 30, 24)


# ---------------------------------------------------------------- Rantz: an ant with a complaint sign
@sprite48('Rantz', {'a': '#e8402a', 'd': '#a42418', 'b': '#ffd0c8', 'c': '#f4f0e0'})
def rantz(c):
    # three-part ant body
    c.ell(34, 36, 7, 6, 'a')
    c.ell(24, 34, 5, 4, 'a')
    c.ell(16, 28, 9, 8, 'a')
    for x0, x1 in [(22, 18), (25, 26), (28, 33)]:
        c.line(x0, 37, x1, 44, 'd', 2)
    # holding up a protest sign
    c.line(8, 30, 6, 14, 't', 2)
    c.rect(0, 4, 14, 14, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.line(2, 7, 11, 7, 'r'); c.line(2, 10, 9, 10, 'k')                                                        # "NO!" scribble
    c.line(14, 21, 10, 13, 'k'); c.line(19, 21, 22, 12, 'k')
    bigeye(c, 11, 25); bigeye(c, 19, 25, 3, 5)
    c.line(10, 24, 14, 25, 'k'); c.line(19, 25, 22, 24, 'k')
    c.ell(14, 32, 1.5, 1.2, 'k')                                                                                 # mid-rant
    blush(c, 21, 30)
