"""Dex 136-150: screensavers, the snowy peak, and The Internet."""
import math
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Glowpegger: a crown jellyfish of pegs, never off
@sprite48('Glowpegger', {'a': '#22222e', 'd': '#111118', 'b': '#44445a', 'c': '#ff3fa4'})
def glowpegger(c):
    c.ell(24, 16, 18, 13, 'a')
    c.clear(0, 18, 47, 47)
    c.rect(6, 16, 42, 21, 'a')
    for x in (8, 14, 20, 28, 34, 40):
        c.rect(x - 1, 21, x + 1, 38 + (x % 5), 'a')
    c.poly([(14, 6), (16, 0), (20, 4), (24, 0), (28, 4), (32, 0), (34, 6)], 'a')
    c.outline()
    cols = 'cyqzfm'
    k = 0
    for y in range(6, 20, 2):
        for x in range(8, 41, 2):
            if ((x - 24) / 18) ** 2 + ((y - 16) / 13) ** 2 < .85:
                c.px(x, y, cols[k % 6]); k += 1
    for x in (8, 14, 20, 28, 34, 40):
        for y in range(23, 40, 2):
            c.px(x, y, cols[(x + y) % 6])
    for x, y in [(16, 1), (24, 1), (32, 1)]:
        c.px(x, y, 'y')
    c.rect(15, 9, 19, 14, 'k'); c.rect(29, 9, 33, 14, 'k')
    c.rect(15, 9, 16, 10, 'w'); c.rect(29, 9, 30, 10, 'w')
    c.line(19, 17, 29, 17, 'w'); c.px(18, 16, 'w'); c.px(30, 16, 'w')


# ---------------------------------------------------------------- Snakebyte: a pixel snake from a tiny gray screen
@sprite48('Snakebyte', {'a': '#3a5a1a', 'd': '#1e3010', 'b': '#a8c470', 'c': '#c4d890'})
def snakebyte(c):
    # a blocky pixel snake coiled in an S, free-standing, LCD-green
    path = [(40, 40), (36, 40), (32, 40), (28, 40), (24, 40), (20, 40), (16, 40), (12, 40), (8, 40), (8, 36), (8, 32),
            (12, 32), (16, 32), (20, 32), (24, 32), (28, 32), (32, 32), (32, 28), (32, 24)]
    for x, y in path:
        c.rect(x - 2, y - 2, x + 1, y + 1, 'b')
    c.rect(24, 10, 37, 23, 'b')                                                           # big square head
    c.rect(40, 14, 43, 17, 'r'); c.px(42, 13, 'L')                                        # pixel apple
    c.outline()
    for x, y in path:
        c.rect(x - 2, y - 2, x + 1, y - 2, 'c'); c.px(x + 1, y + 1, 'a')                  # bevel: LCD pixel blocks
    c.rect(24, 10, 37, 10, 'c')
    bigeye(c, 26, 13, 3, 4); bigeye(c, 32, 13, 3, 4)
    c.line(27, 20, 34, 20, 'a'); c.px(35, 19, 'a')
    c.line(37, 17, 39, 18, 'r')                                                            # tongue toward the apple
    blush(c, 24, 18)


# ---------------------------------------------------------------- Electricslide: an eel line-dancing on a light-up floor
@sprite48('Electricslide', {'a': '#3a6cff', 'd': '#1e40b0', 'b': '#cfe0ff', 'c': '#ffcf3a'})
def electricslide(c):
    # light-up dance floor
    for i, x in enumerate(range(2, 46, 7)):
        c.rect(x, 40, x + 6, 46, 'mqyz'[i % 4])
    # eel body in an S, standing on its tail, one fin out
    c.line(26, 40, 30, 32, 'a', 5); c.line(30, 32, 24, 22, 'a', 5); c.line(24, 22, 26, 14, 'a', 5)
    c.ell(25, 11, 8, 7, 'a')
    c.poly([(20, 24), (8, 18), (10, 26)], 'd'); c.poly([(32, 30), (42, 24), (40, 32)], 'd')
    c.outline()
    c.shadow('a', 'd')
    for x0, y0, x1, y1 in [(27, 37, 29, 33), (27, 27, 25, 23)]:
        c.line(x0, y0, x1, y1, 'c')                                                              # electric stripe
    bigeye(c, 20, 8, 3, 4); bigeye(c, 27, 8, 3, 4)
    c.line(22, 15, 27, 15, 'k'); c.px(21, 14, 'k'); c.px(28, 14, 'k')
    blush(c, 18, 13); blush(c, 31, 13)
    for x, y in [(4, 8), (42, 10), (6, 30)]:
        c.line(x, y, x + 2, y - 2, 'c'); c.line(x + 2, y - 2, x + 1, y, 'c'); c.line(x + 1, y, x + 3, y - 3, 'c')


# ---------------------------------------------------------------- Walkiehawkie / Walkiehawker: hawks with radios built in
@sprite48('Walkiehawkie', {'a': '#ffb02e', 'd': '#c8780a', 'b': '#fff0d0', 'c': '#2a2a38'})
def walkiehawkie(c):
    c.poly([(32, 36), (44, 40), (42, 44), (30, 42)], 'd')
    c.ell(24, 32, 11, 11, 'a')
    c.ell(16, 20, 10, 9, 'a')
    # stubby rubber antenna on its head, tilted (short and knobbed)
    c.line(20, 12, 24, 6, 'c', 2); c.ell(25, 5, 2, 2, 'c')
    c.ell(19, 44, 3, 1.5, 'y'); c.ell(29, 44, 3, 1.5, 'y')
    c.outline()
    c.shadow('a', 'd')
    # speaker grille chest + push-to-talk button wing
    c.rect(19, 29, 31, 38, 'c')
    for y in (31, 33, 35):
        c.line(21, y, 29, y, 'e' if False else 'd')
    c.rect(33, 27, 35, 31, 'r')
    c.poly([(2, 20), (8, 18), (8, 23)], 'y')
    bigeye(c, 10, 17); bigeye(c, 18, 17, 3, 5)
    c.ell(9, 25, 1.5, 1.2, 'k')                                                                    # "OVER"
    blush(c, 13, 23)
    for x, y in [(1, 12), (3, 9), (0, 16)]:
        c.px(x, y, 'k')


@sprite48('Walkiehawker', {'a': '#ff9a1a', 'd': '#b85a04', 'b': '#fff0d0', 'c': '#2a2a38'})
def walkiehawker(c):
    # wings spread, shouting into the street
    c.poly([(30, 20), (47, 8), (46, 26), (34, 34)], 'd')
    c.poly([(16, 26), (2, 34), (4, 40), (18, 36)], 'd')
    c.ell(25, 30, 12, 12, 'a')
    c.ell(16, 16, 10, 9, 'a')
    c.line(19, 8, 24, 2, 'c', 2); c.ell(25, 2, 2, 2, 'c')
    c.ell(20, 44, 4, 1.5, 'y'); c.ell(31, 44, 4, 1.5, 'y')
    c.outline()
    c.shadow('a', 'd')
    c.rect(19, 26, 33, 37, 'c')
    for y in (28, 30, 32, 34):
        c.line(21, y, 31, y, 'd')
    c.poly([(1, 16), (8, 13), (8, 19)], 'y')
    bigeye(c, 10, 13); bigeye(c, 18, 13, 3, 5)
    c.line(9, 12, 13, 12, 'k'); c.line(18, 12, 21, 12, 'k')
    c.ell(9, 21, 2, 1.6, 'k'); c.px(9, 22, 'r')
    for x, y in [(1, 4), (4, 1), (0, 9)]:
        c.line(x, y, x + 2, y, 'k')


# ---------------------------------------------------------------- Discodisc: a pangolin curled into a mirrored movie disc
@sprite48('Discodisc', {'a': '#c9ced8', 'd': '#8a93ab', 'b': '#ffffff', 'c': '#ff3fa4'})
def discodisc(c):
    c.ell(26, 26, 18, 18, 'a')
    c.ell(10, 36, 7, 6, 'b')                                                                        # face peeking out
    c.ell(8, 44, 3, 1.5, 'd'); c.ell(16, 44, 3, 1.5, 'd')
    c.outline()
    c.shadow('a', 'd')
    # mirrored scale grid + rainbow glints
    for r in (6, 11, 15):
        c.ring(26, 26, r, r, 1, 'd')
    c.ell(26, 26, 2.5, 2.5, 'k'); c.px(26, 26, 'w')
    for (x, y), col in zip([(20, 12), (36, 16), (40, 28), (32, 40), (16, 22)], 'myqgc'):
        c.px(x, y, col); c.px(x + 1, y, col); c.px(x, y + 1, 'w')
    bigeye(c, 6, 33, 3, 4); bigeye(c, 12, 33, 3, 4)
    c.line(8, 40, 12, 40, 'k')
    blush(c, 4, 38); blush(c, 15, 38)
    for x, y in [(2, 10), (46, 6), (44, 44)]:
        c.px(x, y, 'y'); c.px(x - 1, y, 'F'); c.px(x + 1, y, 'F'); c.px(x, y - 1, 'F'); c.px(x, y + 1, 'F')


# ---------------------------------------------------------------- Toastwing: a pigeon with a toaster body, toast popping up
@sprite48('Toastwing', {'a': '#d8dce6', 'd': '#9aa0b0', 'b': '#ffffff', 'c': '#e8a64a'})
def toastwing(c):
    # stubby round pigeon wings (not angel wings)
    c.ell(8, 24, 6, 8, 'd'); c.ell(40, 24, 6, 8, 'd')
    # chrome toaster body
    c.rect(12, 16, 36, 38, 'a')
    # toast popping out of the slots like a crest
    c.rect(16, 8, 22, 17, 'c'); c.rect(26, 8, 32, 17, 'c')
    c.ell(17, 41, 3, 1.5, 'm'); c.ell(31, 41, 3, 1.5, 'm')
    c.outline()
    c.shadow('a', 'd')
    c.rect(17, 9, 21, 11, 't'); c.rect(27, 9, 31, 11, 't')                                         # golden crust
    c.line(13, 17, 35, 17, 'b')
    c.rect(36, 26, 38, 29, 'k')                                                                      # lever
    for x, y in [(6, 21), (5, 25), (42, 21), (43, 25)]:
        c.line(x, y, x + 2, y, 'a')                                                                  # feather lines
    c.poly([(8, 30), (12, 28), (12, 32)], 'y')                                                       # little beak, side
    bigeye(c, 16, 24); bigeye(c, 27, 24)
    c.line(21, 32, 25, 32, 'k')
    blush(c, 14, 30); blush(c, 30, 30)


# ---------------------------------------------------------------- Screensaurus: a dinosaur built from 3D pipes
@sprite48('Screensaurus', {'a': '#3ad08a', 'd': '#1e8a56', 'b': '#c8ffe4', 'c': '#ff3f5f'})
def screensaurus(c):
    # pipe segments with ball joints, bending at right angles
    for x0, y0, x1, y1, col in [(8, 18, 8, 30, 'a'), (8, 30, 28, 30, 'a'), (28, 30, 40, 30, 'c'), (40, 30, 40, 40, 'c'),
                                (14, 30, 14, 44, 'y'), (26, 30, 26, 44, 'y'), (36, 30, 46, 24, 'c')]:
        c.line(x0, y0, x1, y1, col, 4)
    for x, y, col in [(8, 30, 'a'), (28, 30, 'a'), (40, 30, 'c'), (14, 30, 'y'), (26, 30, 'y')]:
        c.ell(x + 1.5, y + 1.5, 3.5, 3.5, col)
    c.ell(10, 14, 8, 7, 'a')                                                                          # head joint
    c.outline()
    c.shadow('a', 'd')
    for x0, y0, x1, y1 in [(8, 31, 27, 31), (14, 33, 14, 43), (26, 33, 26, 43)]:
        c.line(x0, y0, x1, y1, 'b')                                                                    # pipe shine
    bigeye(c, 6, 11, 3, 4); bigeye(c, 12, 11, 3, 4)
    c.line(4, 18, 12, 18, 'k'); c.px(6, 19, 'w'); c.px(10, 19, 'w')                                   # pipe-maze with teeth
    blush(c, 15, 16)


# ---------------------------------------------------------------- Slushpuppy / Slushhound: half ice, half syrup
@sprite48('Slushpuppy', {'a': '#8ae0ff', 'd': '#3aa8d8', 'b': '#e8faff', 'c': '#ff4a6a'})
def slushpuppy(c):
    c.ell(30, 36, 9, 7, 'a')
    for x in (23, 28, 34, 37):
        c.ell(x, 43, 2.5, 2, 'a')
    c.ell(18, 25, 12, 11, 'a')
    c.ell(9, 18, 4, 6, 'c'); c.ell(27, 16, 4, 6, 'c')                                                   # cherry-syrup ears
    c.outline()
    c.shadow('a', 'd')
    # syrup drizzle over the head + ice crystal texture
    c.poly([(10, 16), (26, 15), (24, 20), (21, 18), (18, 22), (15, 18), (12, 21)], 'c')
    for x, y in [(30, 33), (35, 37), (26, 39), (12, 30)]:
        c.px(x, y, 'b'); c.px(x + 1, y + 1, 'w')
    bigeye(c, 12, 23); bigeye(c, 21, 23)
    c.rect(8, 29, 9, 30, 'k')
    c.line(13, 32, 17, 32, 'k'); c.rect(14, 33, 15, 34, 'c')
    blush(c, 9, 28); blush(c, 25, 28)
    c.px(4, 12, 'q'); c.px(3, 15, 'q')                                                                  # brain freeze


@sprite48('Slushhound', {'a': '#6ad0f8', 'd': '#2a8ac0', 'b': '#e0f8ff', 'c': '#e8304a'})
def slushhound(c):
    c.ell(29, 30, 14, 10, 'a')
    for x, col in [(18, 'd'), (37, 'd'), (22, 'a'), (40, 'a')]:
        c.rect(x - 2, 36, x + 1, 44, col)
    c.ell(13, 20, 11, 10, 'a')
    c.ell(6, 13, 3, 6, 'c'); c.ell(20, 11, 3, 6, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.poly([(16, 22), (42, 22), (40, 27), (36, 24), (32, 28), (28, 24), (24, 28), (20, 25)], 'c')         # syrup down the back
    bigeye(c, 7, 17); bigeye(c, 15, 17, 3, 5)
    c.line(6, 16, 10, 16, 'k'); c.line(15, 16, 18, 16, 'k')
    c.line(3, 26, 10, 26, 'k')
    c.rect(4, 27, 4, 29, 'w'); c.rect(8, 27, 8, 29, 'w')                                                 # icicle fangs
    # melting drips onto the carpet
    for x in (18, 30, 38):
        c.px(x, 45, 'q'); c.px(x, 46, 'q')


# ---------------------------------------------------------------- Abominabull: a yeti bull mad about the lift line
@sprite48('Abominabull', {'a': '#f4f8ff', 'd': '#b8c4d8', 'b': '#ffffff', 'c': '#3a6cff'})
def abominabull(c):
    c.ell(28, 30, 16, 13, 'a')
    for x, col in [(16, 'd'), (38, 'd'), (21, 'a'), (41, 'a')]:
        c.ell(x, 42, 5, 4, col)
    c.ell(13, 21, 11, 10, 'a')
    c.poly([(6, 14), (0, 6), (4, 4), (8, 11)], 'd'); c.poly([(18, 12), (24, 4), (26, 7), (21, 14)], 'd')    # horns
    c.outline(diag=True)
    c.shadow('a', 'd')
    for x, y in [(30, 22), (36, 30), (24, 34), (40, 24)]:
        c.line(x, y, x + 1, y + 3, 'd')                                                                    # fur
    # ski goggles pushed up + lift ticket on a zip tie
    c.rect(5, 13, 22, 16, 'c'); c.rect(7, 14, 12, 15, 'f'); c.rect(15, 14, 20, 15, 'f')
    c.rect(32, 36, 37, 40, 'y'); c.px(34, 37, 'k')
    c.ell(9, 26, 5, 3, 'm')
    c.px(7, 26, 'k'); c.px(11, 26, 'k')
    bigeye(c, 8, 18); bigeye(c, 16, 18, 3, 5)
    c.line(7, 17, 11, 18, 'k'); c.line(16, 18, 19, 17, 'k')
    for x, y in [(1, 22), (2, 26)]:
        c.line(x, y, x + 2, y + 1, 'q')                                                                    # snort


# ---------------------------------------------------------------- Chatbrat / Chatroomer: The Internet's locals
@sprite48('Chatbrat', {'a': '#c08ad8', 'd': '#8a4aa8', 'b': '#f8e8ff', 'c': '#ffffff'})
def chatbrat(c):
    # a chatty monkey whose tail curls into a speech bubble
    c.ring(38, 14, 8, 7, 3, 'a')
    c.line(32, 32, 36, 20, 'a', 2)
    c.ell(24, 34, 9, 8, 'a')
    c.ell(18, 22, 11, 10, 'a')
    c.ell(7, 21, 3, 4, 'a'); c.ell(29, 19, 3, 4, 'a')
    c.ell(18, 44, 3, 1.5, 'd'); c.ell(30, 44, 3, 1.5, 'd')
    # tiny keyboard in its hands
    c.rect(12, 34, 28, 38, 'k')
    c.outline()
    c.shadow('a', 'd')
    c.ell(38, 14, 5, 4, 'c')
    c.line(35, 13, 36, 13, 'k'); c.px(38, 13, 'k'); c.line(40, 12, 41, 14, 'k')                         # a/s/l
    for x in range(13, 28, 2):
        c.px(x, 35, 'w'); c.px(x, 37, 'w')
    c.ell(18, 26, 6, 4, 'b')
    bigeye(c, 12, 19); bigeye(c, 21, 19)
    c.line(16, 28, 20, 28, 'k'); c.px(21, 27, 'k')
    blush(c, 9, 25); blush(c, 25, 25)


@sprite48('Chatroomer', {'a': '#3a3050', 'd': '#201a30', 'b': '#6a5a8a', 'c': '#b6ff3b'})
def chatroomer(c):
    # an owl lurking behind a CRT, only eyes and ear tufts showing
    c.ell(24, 16, 14, 12, 'a')
    c.poly([(11, 10), (9, 1), (16, 6)], 'a'); c.poly([(37, 10), (39, 1), (32, 6)], 'a')
    c.rect(6, 22, 42, 46, 'e' if False else 'b')
    c.outline()
    c.shadow('a', 'd')
    c.rect(9, 25, 39, 40, 'k')
    # "lol" on the screen
    c.line(16, 29, 16, 35, 'c'); c.ring(22, 33, 2, 2, 1, 'c'); c.line(27, 29, 27, 35, 'c')
    c.px(31, 34, 'c'); c.px(31, 35, 'c')
    c.rect(12, 42, 36, 44, 'd')
    # big lurking eyes over the top
    c.ell(17, 15, 5, 5, 'y'); c.ell(31, 15, 5, 5, 'y')
    c.ell(18, 16, 2, 3, 'k'); c.ell(30, 16, 2, 3, 'k'); c.px(17, 14, 'w'); c.px(29, 14, 'w')
    c.line(12, 10, 21, 12, 'a'); c.line(27, 12, 36, 10, 'a')                                               # heavy lids
    c.poly([(22, 19), (26, 19), (24, 22)], 'f')


# ---------------------------------------------------------------- Emailephant: an elephant with envelope ears
@sprite48('Emailephant', {'a': '#9aa8c8', 'd': '#6a78a0', 'b': '#e4e8f4', 'c': '#ffffff'})
def emailephant(c):
    c.ell(30, 32, 13, 10, 'a')
    for x, col in [(21, 'd'), (38, 'd'), (25, 'a'), (41, 'a')]:
        c.rect(x - 2, 38, x + 2, 45, col)
    c.ell(16, 22, 11, 10, 'a')
    # trunk curled up, holding a letter
    c.line(7, 26, 4, 34, 'a', 4); c.line(4, 34, 8, 38, 'a', 3)
    # envelope ears
    c.rect(20, 12, 36, 26, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.line(20, 12, 28, 19, 'd'); c.line(28, 19, 36, 12, 'd')
    c.rect(32, 13, 35, 16, 'r')                                                                               # stamp
    # inbox badge
    c.ell(37, 24, 4, 3, 'r'); c.line(35, 24, 39, 24, 'w')
    c.ring(13, 15, 2, 2, 1, 'k'); c.px(14, 15, 'k')                                                            # @ on the forehead
    bigeye(c, 9, 19, 3, 4); bigeye(c, 16, 19, 3, 4)
    c.line(11, 27, 14, 27, 'k')
    blush(c, 7, 24)
    c.rect(7, 36, 12, 40, 'c'); c.line(7, 36, 9, 38, 'd'); c.line(9, 38, 12, 36, 'd')                         # letter in trunk


# ---------------------------------------------------------------- Bufferfly: wings are loading spinners
@sprite48('Bufferfly', {'a': '#6a4aff', 'd': '#3a20c0', 'b': '#e4dcff', 'c': '#b6ff3b'})
def bufferfly(c):
    c.ell(12, 16, 10, 10, 'a'); c.ell(36, 16, 10, 10, 'a')
    c.ell(14, 34, 8, 7, 'd'); c.ell(34, 34, 8, 7, 'd')
    c.ell(24, 26, 4, 12, 'b')
    c.ell(24, 13, 5, 5, 'b')
    c.outline()
    # spinner dots, fading around each wing (still loading)
    for cx, cy, r in [(12, 16, 6), (36, 16, 6)]:
        for i in range(8):
            a = i * math.pi / 4
            col = 'c' if i < 3 else ('z' if i < 5 else 'd')
            c.ell(cx + math.cos(a) * r, cy + math.sin(a) * r, 1.2, 1.2, col)
    for x in (14, 34):
        c.ring(x, 34, 4, 3, 1, 'b')
    c.line(22, 9, 17, 2, 'k'); c.line(26, 9, 31, 2, 'k')
    bigeye(c, 21, 11, 2, 3); bigeye(c, 25, 11, 2, 3)
    c.line(23, 16, 25, 16, 'k')
    # progress bar under it, one pixel in
    c.rect(10, 44, 38, 46, 'k'); c.rect(11, 45, 12, 45, 'c')
