"""Rewind Road / Y2K Ascent regulars, the boss and the legendary."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


def sparkles(c, pts, col='F'):
    for x, y in pts:
        c.px(x, y, col); c.px(x - 1, y, 'f'); c.px(x + 1, y, 'f'); c.px(x, y - 1, 'f'); c.px(x, y + 1, 'f')


# ---------------------------------------------------------------- Gelpenguin: penguin chick whose beak is a gel pen
@sprite48('Gelpenguin', {'a': '#2a2a3a', 'd': '#15151f', 'b': '#f4f0ff', 'c': '#c58cff'})
def gelpenguin(c):
    c.ell(24, 30, 13, 14, 'a')
    c.ell(23, 33, 9, 10, 'b')
    c.ell(11, 31, 3, 7, 'a'); c.ell(37, 30, 3, 7, 'a')           # flippers
    c.ell(18, 44, 4, 2, 'y'); c.ell(29, 44, 4, 2, 'y')
    # gel-pen beak: pastel barrel with a clip, nib pointing left
    c.rect(4, 22, 13, 26, 'c'); c.poly([(1, 24), (4, 22), (4, 26)], 'w')
    c.outline()
    c.shadow('a', 'd')
    c.line(7, 21, 12, 21, 'e' if False else 'w'); c.px(12, 22, 'w')  # clip
    bigeye(c, 15, 18); bigeye(c, 25, 18)
    blush(c, 14, 25); blush(c, 27, 25)
    # pastel doodles on its belly + a squiggle it just wrote
    for x, y, col in [(19, 31, 'm'), (26, 34, 'q'), (21, 38, 'z'), (27, 39, 'c')]:
        c.px(x, y, col); c.px(x + 1, y, col); c.px(x, y + 1, col)
    for i, x in enumerate(range(0, 9)):
        c.px(x, 33 + (i % 3 == 1) - (i % 3 == 2), 'c')


# ---------------------------------------------------------------- VHSaur / Rewindosaur: dinos wearing VHS tapes
@sprite48('VHSaur', {'a': '#5fc46a', 'd': '#3a8a44', 'b': '#e6f8d6', 'c': '#26262f', 'e': '#9aa3b5'})
def vhsaur(c):
    c.poly([(36, 36), (46, 38), (44, 42), (34, 41)], 'a')         # tail
    c.ell(25, 36, 12, 8, 'a')
    c.ell(17, 43, 3, 2, 'a'); c.ell(31, 43, 3, 2, 'a')
    c.ell(15, 22, 11, 10, 'a')                                     # big head
    # VHS tape worn as a shell on its back
    c.rect(22, 24, 41, 34, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.ring(28, 29, 2, 2, 1, 'e'); c.ring(35, 29, 2, 2, 1, 'e'); c.px(28, 29, 'w'); c.px(35, 29, 'w')
    c.rect(24, 26, 39, 26, 'w')                                     # label strip
    c.ell(12, 27, 6, 4, 'b')
    bigeye(c, 8, 19); bigeye(c, 18, 19)
    c.line(8, 30, 13, 30, 'k')
    # tape ribbon tongue (the bite)
    c.line(5, 31, 2, 35, 'k'); c.line(2, 35, 5, 37, 'k')
    blush(c, 5, 26); blush(c, 21, 25)
    c.px(13, 31, 'w')                                               # baby tooth


@sprite48('Rewindosaur', {'a': '#4bb056', 'd': '#2c6e34', 'b': '#e2f6d0', 'c': '#26262f', 'e': '#9aa3b5'})
def rewindosaur(c):
    # back plates = a stack of tapes
    for x, y in [(22, 12), (30, 10), (38, 14)]:
        c.rect(x - 4, y, x + 4, y + 10, 'c')
    c.poly([(38, 32), (47, 26), (47, 31), (40, 38)], 'a')
    c.ell(28, 30, 15, 10, 'a')
    c.ell(25, 34, 9, 6, 'b')
    for x, col in [(18, 'd'), (36, 'd'), (22, 'a'), (39, 'a')]:
        c.ell(x, 41, 4, 4, col)
    c.rect(16, 44, 26, 46, 'b'); c.rect(34, 44, 44, 46, 'b')
    c.ell(12, 22, 10, 8, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(22, 12), (30, 10), (38, 14)]:
        c.px(x - 2, y + 4, 'e'); c.px(x + 2, y + 4, 'e'); c.line(x - 3, y + 1, x + 3, y + 1, 'w')
    # tracking lines across the body (adjust the tracking)
    for y in (27, 31):
        c.line(16, y, 40, y, 'q')
    # loose tape ribbon from the tail
    c.line(47, 28, 44, 33, 'k'); c.line(44, 33, 47, 37, 'k')
    bigeye(c, 5, 19); bigeye(c, 13, 19, 3, 5)
    c.line(4, 18, 8, 18, 'k'); c.line(13, 18, 16, 18, 'k')
    c.line(2, 27, 10, 27, 'k'); c.px(4, 28, 'w'); c.px(8, 28, 'w')
    blush(c, 15, 25)


# ---------------------------------------------------------------- Bloblamprey: an eel rising out of a lava lamp
@sprite48('Bloblamprey', {'a': '#ff5a8a', 'd': '#c43464', 'b': '#ffe0ec', 'c': '#ffb02e', 'e': '#8a93ab'})
def lavalamprey(c):
    # lamp base
    c.poly([(14, 46), (34, 46), (30, 38), (18, 38)], 'e')
    # the eel's body IS the glass: tapered, glowing
    c.poly([(17, 38), (31, 38), (29, 20), (19, 20)], 'a')
    c.ell(24, 14, 10, 9, 'a')                                       # head
    c.ell(24, 6, 4, 3, 'e')                                         # lamp cap as a little hat
    c.outline()
    c.shadow('a', 'd')
    # floating lava blobs inside
    for x, y, r in [(22, 33, 2), (27, 27, 2.5), (21, 24, 1.5), (26, 35, 1.2)]:
        c.ell(x, y, r, r, 'c')
    c.line(20, 22, 20, 36, 'b')                                     # glass shine
    # round lamprey mouth, but cute: a little "o"
    bigeye(c, 17, 11); bigeye(c, 27, 11)
    c.ring(22, 18, 2, 1.6, 1, 'k'); c.px(22, 18, 'R')
    blush(c, 15, 17); blush(c, 29, 17)
    # warm glow
    for x, y in [(10, 26), (37, 22), (36, 32), (11, 18)]:
        c.px(x, y, 'c')


# ---------------------------------------------------------------- Skipmanta: a manta ray shaped like a portable CD player
@sprite48('Skipmanta', {'a': '#3a6cff', 'd': '#2244b0', 'b': '#dce6ff', 'c': '#d3d8e0', 'e': '#9aa3b5'})
def skipmanta(c):
    # wide wings
    c.poly([(2, 30), (16, 16), (32, 16), (46, 30), (32, 34), (16, 34)], 'a')
    # the disc lid in the middle
    c.ell(24, 25, 10, 8, 'c')
    # whip tail with headphone cord
    c.line(34, 33, 46, 42, 'a', 2)
    c.ell(14, 37, 3, 2, 'a'); c.ell(34, 37, 3, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.ring(24, 25, 10, 8, 1, 'e'); c.ell(24, 25, 1.5, 1.5, 'e'); c.px(24, 25, 'k')
    c.px(19, 22, 'm'); c.px(28, 21, 'q'); c.px(30, 27, 'y')         # disc rainbow
    # headphones over its head-horns
    c.ell(14, 20, 2, 3, 'k'); c.ell(34, 20, 2, 3, 'k'); c.line(14, 17, 34, 17, 'k')
    bigeye(c, 16, 27, 3, 4); bigeye(c, 29, 27, 3, 4)
    c.line(21, 32, 26, 32, 'k')
    blush(c, 12, 31); blush(c, 33, 31)
    # skip marks
    c.px(6, 22, 'k'); c.px(8, 20, 'k'); c.px(5, 19, 'k')


# ---------------------------------------------------------------- Frostingroo: a joey with a pouch full of frosting
@sprite48('Frostingroo', {'a': '#d89a6a', 'd': '#a06a40', 'b': '#fbe6cc', 'c': '#ff7ab8'})
def frostingroo(c):
    c.poly([(30, 40), (46, 44), (44, 46), (28, 45)], 'a')          # big tail on the ground
    c.ell(24, 33, 10, 11, 'a')
    c.ell(23, 36, 7, 7, 'b')
    c.ell(16, 44, 5, 2, 'a'); c.ell(29, 44, 5, 2, 'a')              # big feet
    c.ell(22, 17, 10, 9, 'a')
    c.ell(16, 5, 3, 7, 'a'); c.ell(27, 5, 3, 7, 'a')                # ears
    c.ell(16, 6, 1, 4, 'b'); c.ell(27, 6, 1, 4, 'b')
    c.ell(13, 29, 3, 3, 'a'); c.ell(33, 29, 3, 3, 'a')              # paws guarding the pouch
    c.outline()
    c.shadow('a', 'd')
    # pouch overflowing with pink frosting + sprinkles
    c.ell(23, 35, 7, 3, 'c'); c.ell(20, 33, 3, 2, 'c'); c.ell(26, 33, 3, 2, 'c')
    for x, y, col in [(19, 34, 'y'), (23, 33, 'q'), (26, 35, 'z'), (21, 36, 'w')]:
        c.px(x, y, col)
    c.line(17, 38, 29, 38, 'd')
    bigeye(c, 15, 15); bigeye(c, 25, 15)
    c.rect(12, 21, 13, 22, 'k')
    c.line(16, 23, 19, 23, 'k')
    c.px(14, 24, 'c'); c.px(15, 24, 'c')                            # frosting on its face. it shared nothing.
    blush(c, 12, 19); blush(c, 28, 19)


# ---------------------------------------------------------------- Y2Kraken (boss): a kraken with a CRT head and cable tentacles
@sprite48('Y2Kraken', {'a': '#7a3cff', 'd': '#4a1ea8', 'b': '#e2d4ff', 'c': '#b6ff3b', 'e': '#c9ced8'})
def y2kraken(c):
    # tentacles: thick cables curling out
    for x0, y0, x1, y1, x2, y2 in [(10, 30, 3, 38, 6, 45), (16, 34, 12, 42, 16, 46), (24, 36, 24, 44, 28, 46),
                                   (32, 34, 36, 42, 32, 46), (38, 30, 45, 38, 42, 45)]:
        c.line(x0, y0, x1, y1, 'a', 3); c.line(x1, y1, x2, y2, 'a', 3)
    # body
    c.ell(24, 28, 16, 9, 'a')
    # CRT monitor head
    c.rect(9, 3, 39, 25, 'e')
    c.outline()
    c.shadow('a', 'd')
    c.rect(12, 6, 36, 21, 'k')
    # screen: angry pixel eyes and the clock stuck at 00:00
    c.rect(15, 9, 18, 12, 'c'); c.rect(29, 9, 32, 12, 'c')
    c.line(14, 8, 19, 9, 'c'); c.line(28, 9, 33, 8, 'c')
    for x in (17, 20, 25, 28):
        c.ring(x, 17, 1, 1.6, 1, 'r')
    c.px(22, 16, 'r'); c.px(22, 18, 'r')
    c.line(12, 14, 36, 14, 'n')                                      # scanline
    c.rect(24, 22, 33, 23, 'd'); c.px(35, 23, 'z')                    # vents + power LED
    # suckers
    for x, y in [(4, 38), (12, 42), (24, 42), (36, 42), (44, 38)]:
        c.px(x, y, 'b')
    c.ell(24, 30, 6, 2, 'b')


# ---------------------------------------------------------------- Keychainos (legendary): a forgotten virtual-pet egg, now divine
@sprite48('Keychainos', {'a': '#ffe9f4', 'd': '#e0b0cc', 'b': '#ffffff', 'c': '#ff3fa4', 'e': '#c9ced8'})
def pixelgodchi(c):
    # keychain loop as a halo
    c.ring(24, 4, 6, 2, 1, 'y')
    # little wings
    c.poly([(8, 22), (1, 12), (3, 26), (9, 30)], 'b'); c.poly([(40, 22), (47, 12), (45, 26), (39, 30)], 'b')
    # the egg body
    c.ell(24, 26, 15, 17, 'a')
    c.outline()
    c.shadow('a', 'd')
    # LCD with its pixel face
    c.rect(15, 15, 33, 31, 'e'); c.rect(16, 16, 32, 30, 'g')
    for x, y in [(19, 20), (20, 20), (19, 21), (20, 21), (27, 20), (28, 20), (27, 21), (28, 21)]:
        c.px(x, y, 'k')
    c.line(21, 26, 26, 26, 'k'); c.px(20, 25, 'k'); c.px(27, 25, 'k')
    c.px(30, 17, 'c'); c.px(31, 18, 'c'); c.px(29, 18, 'c')          # a pixel heart: it remembers
    # three buttons
    for x in (18, 24, 30):
        c.ell(x, 36, 1.6, 1.6, 'c')
    # sparkles
    for x, y in [(5, 5), (43, 6), (4, 40), (44, 41)]:
        c.px(x, y, 'y'); c.px(x - 1, y, 'F'); c.px(x + 1, y, 'F'); c.px(x, y - 1, 'F'); c.px(x, y + 1, 'F')


# ---------------------------------------------------------------- Microwavern / Magmawavern: hermit crabs living in pastry pockets
@sprite48('Microwavern', {'a': '#e8a64a', 'd': '#b87420', 'b': '#ffe0a8', 'c': '#ff5a3a', 'e': '#9fd6ff'})
def hotpockit(c):
    # pastry-pocket shell
    c.rect(20, 18, 42, 38, 'a')
    # crab body peeking out the front
    c.ell(16, 33, 9, 7, 'c')
    # claws
    c.ell(6, 30, 4, 4, 'c'); c.ell(9, 40, 4, 3, 'c')
    # eye stalks
    c.rect(12, 19, 13, 26, 'c'); c.rect(18, 19, 19, 26, 'c')
    c.ell(12, 18, 3, 3, 'w'); c.ell(19, 18, 3, 3, 'w')
    for x in (14, 20, 26):
        c.ell(x, 43, 1, 2, 'c')
    c.outline()
    c.shadow('a', 'd')
    # crimped edge + vents; one corner still frozen
    for y in range(19, 38, 3):
        c.px(41, y, 'd')
    for x in range(21, 42, 3):
        c.px(x, 19, 'd')
    c.rect(36, 30, 41, 37, 'e'); c.px(38, 32, 'w')
    for x in (26, 31):
        c.line(x, 24, x + 3, 24, 'd')
    soft_flame(c, 30, 16, 5, 1, 'w', 'w')                           # steam
    c.rect(11, 17, 12, 18, 'k'); c.rect(18, 17, 19, 18, 'k')
    c.px(11, 17, 'w'); c.px(18, 17, 'w')
    c.line(12, 35, 16, 35, 'k'); c.px(17, 34, 'k')
    blush(c, 9, 33)


@sprite48('Magmawavern', {'a': '#d8782a', 'd': '#9c4a14', 'b': '#ffd08a', 'c': '#ff3a2a', 'e': '#ffe66a'})
def scorchpockit(c):
    c.rect(18, 12, 44, 38, 'a')
    c.ell(16, 32, 11, 9, 'c')
    # big crusher claw + small claw
    c.ell(5, 22, 6, 6, 'c'); c.ell(7, 40, 4, 3, 'c')
    c.rect(12, 15, 13, 23, 'c'); c.rect(19, 15, 20, 23, 'c')
    c.ell(12, 14, 3, 3, 'w'); c.ell(20, 14, 3, 3, 'w')
    for x in (14, 21, 28, 35):
        c.ell(x, 43, 1.5, 2, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.line(2, 21, 7, 23, 'k')                                         # claw mouth
    for y in range(13, 38, 3):
        c.px(43, y, 'd')
    for x in range(19, 44, 3):
        c.px(x, 13, 'd')
    # lava cracks in the crust
    c.line(24, 20, 30, 26, 'f'); c.line(30, 26, 28, 32, 'f'); c.line(34, 18, 38, 24, 'f')
    for x, y, h in [(24, 12, 7), (31, 12, 9), (38, 12, 7)]:
        soft_flame(c, x, y, h, 0)
    c.rect(11, 13, 12, 14, 'k'); c.rect(19, 13, 20, 14, 'k')
    c.line(10, 11, 13, 12, 'k'); c.line(18, 12, 21, 11, 'k')
    c.line(11, 34, 18, 34, 'k'); c.px(13, 35, 'w')
    blush(c, 8, 31)


# ---------------------------------------------------------------- Sparklerp / Fizzlerp: axolotls whose gills are sparklers
@sprite48('Sparklerp', {'a': '#ff8ab0', 'd': '#d85a84', 'b': '#ffe8f0', 'c': '#8a93ab'})
def sparklerp(c):
    c.poly([(32, 34), (45, 30), (46, 35), (34, 40)], 'a')          # tail
    c.ell(26, 35, 10, 7, 'a')
    c.ell(25, 38, 6, 4, 'b')
    for x in (18, 23, 30, 34):
        c.ell(x, 43, 2, 2, 'a')
    c.ell(18, 23, 12, 10, 'a')
    # sparkler-stick gills
    for x0, y0, x1, y1 in [(8, 18, 2, 12), (9, 23, 2, 22), (27, 17, 33, 10), (28, 22, 35, 20)]:
        c.line(x0, y0, x1, y1, 'c', 1)
    c.outline()
    c.shadow('a', 'd')
    sparkles(c, [(2, 11), (1, 22), (34, 9), (36, 20)])
    bigeye(c, 11, 21); bigeye(c, 21, 21)
    c.line(14, 29, 19, 29, 'k'); c.px(13, 28, 'k'); c.px(20, 28, 'k')
    blush(c, 8, 27); blush(c, 25, 27)


@sprite48('Fizzlerp', {'a': '#e86a94', 'd': '#a83e66', 'b': '#ffe0ec', 'c': '#6a7088'})
def fizzlerp(c):
    c.poly([(34, 36), (47, 38), (46, 43), (34, 42)], 'a')
    c.ell(26, 34, 13, 9, 'a')
    c.ell(24, 37, 8, 5, 'b')
    for x, col in [(16, 'd'), (34, 'd'), (21, 'a'), (37, 'a')]:
        c.ell(x, 42, 4, 3, col)
    # arms crossed: sulking
    c.rect(15, 30, 33, 34, 'd')
    c.ell(18, 20, 12, 10, 'a')
    for x0, y0, x1, y1 in [(8, 15, 1, 6), (7, 21, 0, 19), (28, 14, 34, 5), (29, 20, 37, 17)]:
        c.line(x0, y0, x1, y1, 'c', 2)
    c.outline()
    c.shadow('a', 'd')
    # one gill still blazing, the rest burnt out and smoking (the flaw)
    sparkles(c, [(1, 5), (2, 8), (4, 6)])
    for x, y in [(0, 17), (35, 3), (38, 15)]:
        c.px(x, y, 'e' if False else 'w'); c.px(x + 1, y - 2, 'w')
    bigeye(c, 11, 18); bigeye(c, 21, 18)
    c.line(10, 18, 15, 19, 'k'); c.line(21, 19, 25, 18, 'k')           # half-lidded sulk
    c.line(10, 17, 15, 17, 'a'); c.line(21, 17, 25, 17, 'a')
    c.line(13, 26, 18, 25, 'k')
    blush(c, 8, 24); blush(c, 25, 24)
