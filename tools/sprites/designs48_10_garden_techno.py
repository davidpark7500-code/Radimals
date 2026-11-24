"""Dex 121-135: the rest of the garden and the first wave of Techno."""
import math
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


def spark(c, x, y, col='z'):
    c.line(x, y, x + 2, y - 2, col); c.line(x + 2, y - 2, x + 1, y, col); c.line(x + 1, y, x + 3, y - 3, col)


# ---------------------------------------------------------------- Dandylion: a lion cub with a dandelion-puff mane
@sprite48('Dandylion', {'a': '#ffc84a', 'd': '#d8921a', 'b': '#fff4d0', 'c': '#ffffff'})
def dandylion(c):
    c.line(34, 38, 44, 34, 'a', 2); c.ell(45, 33, 2, 2, 'c')                                     # tail tuft = a seed
    c.ell(28, 36, 10, 7, 'a')
    for x in (21, 26, 33, 37):
        c.ell(x, 43, 2.5, 2, 'a')
    # puffball mane
    c.ell(18, 21, 15, 14, 'c')
    c.ell(18, 23, 9, 8, 'a')
    c.outline()
    c.shadow('a', 'd')
    for i in range(16):
        a = i * math.pi * 2 / 16
        c.line(18 + math.cos(a) * 10, 21 + math.sin(a) * 10, 18 + math.cos(a) * 14, 21 + math.sin(a) * 13, 'd' if False else 'e' if False else 'q')
    c.ell(14, 26, 5, 3, 'b')
    bigeye(c, 12, 20); bigeye(c, 20, 20)
    c.rect(11, 25, 13, 26, 'k')
    c.line(12, 28, 15, 28, 'k')
    blush(c, 9, 25); blush(c, 23, 25)
    # wishes floating off
    for x, y in [(38, 8), (42, 14), (44, 4)]:
        c.px(x, y, 'w'); c.px(x - 1, y - 1, 'w'); c.px(x + 1, y - 1, 'w'); c.px(x, y + 1, 'd')


# ---------------------------------------------------------------- Taffyard: a dachshund made of rolled fruit tape
@sprite48('Taffyard', {'a': '#ff4a6a', 'd': '#c42444', 'b': '#ffd0d8', 'c': '#ffcf3a'})
def fruityfoot(c):
    c.rect(14, 28, 38, 36, 'a')
    c.ell(40, 32, 5, 5, 'a')                                                                       # rolled-up end (tail)
    for x in (16, 22, 30, 36):
        c.ell(x, 40, 2, 3, 'a')
    c.ell(12, 24, 9, 8, 'a')
    c.ell(6, 22, 3, 6, 'd')
    c.outline()
    c.shadow('a', 'd')
    # printed shapes on the tape + the roll spiral
    for x, col in [(18, 'c'), (25, 'z'), (32, 'q')]:
        c.ell(x, 31, 2, 2, col)
    c.ring(40, 32, 3, 3, 1, 'b'); c.px(40, 32, 'd')
    c.line(14, 35, 38, 35, 'b')
    bigeye(c, 9, 21); bigeye(c, 16, 21, 3, 5)
    c.rect(4, 26, 5, 27, 'k')
    c.line(8, 30, 12, 30, 'k')
    c.rect(9, 31, 11, 32, 'r')                                                                     # stuck tongue
    blush(c, 18, 26)


# ---------------------------------------------------------------- Slimeball: a chameleon dumped in green slime
@sprite48('Slimeball', {'a': '#7a5ae0', 'd': '#4a30a8', 'b': '#e8e0ff', 'c': '#7aff3a'})
def slimeon(c):
    # curled tail
    c.ring(38, 34, 6, 6, 3, 'a')
    c.ell(26, 32, 12, 8, 'a')
    for x in (18, 24, 30, 35):
        c.ell(x, 41, 2.5, 2, 'a')
    c.ell(13, 24, 10, 9, 'a')
    # slime dumped on its head, dripping
    c.ell(16, 16, 12, 5, 'c')
    for x, h in [(6, 8), (12, 12), (20, 6), (26, 10), (32, 14)]:
        c.rect(x, 18, x + 2, 18 + h, 'c'); c.ell(x + 1, 18 + h, 1.6, 1.6, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.px(10, 14, 'w'); c.px(11, 14, 'w')
    # chameleon turret eye
    c.ell(14, 24, 4, 4, 'b'); bigeye(c, 13, 22, 3, 4)
    c.line(4, 29, 9, 29, 'k'); c.px(3, 28, 'k')
    c.px(4, 27, 'c')                                                                               # in its ears somehow
    blush(c, 17, 28)


# ---------------------------------------------------------------- Weedwhack: a goat kid with a trimmer-spool tail
@sprite48('Weedwhack', {'a': '#f0ece0', 'd': '#b8b0a0', 'b': '#ffffff', 'c': '#ff8a1a'})
def weedwhack(c):
    c.ell(28, 32, 12, 9, 'a')
    for x in (20, 25, 32, 36):
        c.rect(x - 1, 38, x + 1, 45, 'a')
    c.ell(14, 22, 10, 9, 'a')
    c.ell(7, 18, 4, 2, 'a')                                                                         # ear
    c.poly([(14, 14), (12, 7), (17, 12)], 'd'); c.poly([(20, 14), (21, 7), (23, 13)], 'd')          # little horns
    # orange trimmer-head tail spinning
    c.ell(42, 26, 4, 4, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.px(42, 26, 'k')
    for a in range(0, 360, 60):
        r = math.radians(a)
        c.line(42 + math.cos(r) * 4, 26 + math.sin(r) * 4, 42 + math.cos(r + .6) * 8, 26 + math.sin(r + .6) * 8, 'g')
    for x in (20, 25, 32, 36):
        c.rect(x - 1, 44, x + 1, 45, 'k')
    bigeye(c, 9, 19, 3, 4); bigeye(c, 16, 19, 3, 4)
    c.line(5, 27, 9, 27, 'k')
    # leaf in its mouth, a squashed tomato below
    c.ell(3, 28, 2, 1, 'L')
    c.ell(6, 44, 3, 1.5, 'r'); c.px(5, 42, 'L')
    c.px(10, 25, 'm')


# ---------------------------------------------------------------- Fernbaby / Fernfury: forest deer with fern ears/antlers
@sprite48('Fernbaby', {'a': '#c8a070', 'd': '#946a40', 'b': '#fff0dc', 'c': '#4ac84a'})
def fernbaby(c):
    c.ell(28, 34, 10, 7, 'a')
    for x in (21, 26, 32, 36):
        c.rect(x - 1, 39, x, 45, 'a')
    c.ell(17, 24, 10, 9, 'a')
    # fern-frond ears
    for x0, y0, x1, y1 in [(10, 18, 2, 8), (24, 17, 33, 8)]:
        c.line(x0, y0, x1, y1, 'c', 2)
        for i in range(1, 6):
            t = i / 6
            x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            c.px(x - 1, y - 1, 'c'); c.px(x + 1, y + 1, 'c')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(26, 31), (30, 33), (33, 30)]:
        c.px(x, y, 'b')                                                                              # fawn spots
    c.ell(13, 28, 5, 3, 'b')
    bigeye(c, 11, 21); bigeye(c, 20, 21)
    c.rect(9, 27, 10, 28, 'k')
    c.line(12, 30, 15, 30, 'k')
    c.px(12, 26, 'q'); c.px(12, 27, 'q')                                                           # a tear for the forest
    blush(c, 8, 26); blush(c, 23, 26)


@sprite48('Fernfury', {'a': '#a87a48', 'd': '#704a20', 'b': '#f8e4c8', 'c': '#2ea82e'})
def fernfury(c):
    c.ell(29, 30, 13, 9, 'a')
    for x, col in [(19, 'd'), (37, 'd'), (23, 'a'), (40, 'a')]:
        c.rect(x - 2, 35, x + 1, 45, col)
    c.ell(14, 21, 10, 9, 'a')
    # big fern antlers
    for x0, y0, x1, y1 in [(10, 14, 1, 1), (18, 13, 28, 1), (8, 12, 3, 4), (20, 11, 24, 3)]:
        c.line(x0, y0, x1, y1, 'c', 2)
    for x, y in [(4, 5), (6, 9), (25, 4), (22, 8), (1, 2), (28, 2)]:
        c.ell(x, y, 1.5, 1.5, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.ell(9, 25, 5, 3, 'b')
    bigeye(c, 8, 18); bigeye(c, 16, 18, 3, 5)
    c.line(7, 17, 11, 18, 'k'); c.line(16, 18, 19, 17, 'k')
    c.line(5, 29, 11, 29, 'k')
    c.px(6, 30, 'w'); c.px(10, 30, 'w')                                                           # grew teeth
    c.rect(3, 23, 4, 24, 'k')
    for x, y in [(30, 24), (34, 27), (26, 27)]:
        c.px(x, y, 'L')                                                                            # moss


# ---------------------------------------------------------------- Clickdisk / Diskdrake
@sprite48('Clickdisk', {'a': '#3a7aff', 'd': '#1e4cc0', 'b': '#d8e8ff', 'c': '#c9ced8'})
def zapdisk(c):
    c.poly([(34, 34), (46, 30), (45, 36), (36, 40)], 'a')
    c.ell(25, 33, 12, 8, 'a')
    for x in (16, 22, 30, 35):
        c.ell(x, 41, 2.5, 2, 'a')
    c.ell(13, 25, 9, 8, 'a')
    # thick zip disk on its back
    c.rect(20, 22, 36, 32, 'd')
    c.outline()
    c.shadow('a', 'd')
    c.rect(24, 22, 31, 26, 'c'); c.rect(27, 23, 28, 25, 'k')
    c.rect(22, 29, 34, 31, 'w')
    for x, y in [(4, 14), (40, 18), (8, 40)]:
        spark(c, x, y)
    bigeye(c, 9, 22); bigeye(c, 16, 22, 3, 5)
    c.line(8, 29, 12, 29, 'k')
    blush(c, 6, 27)
    c.px(38, 24, 'k'); c.px(40, 22, 'k')                                                           # click... click...


@sprite48('Diskdrake', {'a': '#3a6aff', 'd': '#1e3cb0', 'b': '#d8e6ff', 'c': '#c9ced8'})
def diskdrake(c):
    # hoard of empty disks
    for x in (6, 14, 30, 40):
        c.rect(x, 40, x + 7, 46, 'n')
    # wings like disk shutters
    c.poly([(20, 16), (4, 4), (8, 20), (18, 26)], 'c'); c.poly([(32, 16), (46, 4), (42, 20), (32, 26)], 'c')
    c.ell(26, 31, 13, 10, 'a')
    c.ell(14, 18, 9, 8, 'a')
    c.poly([(9, 12), (6, 3), (13, 9)], 'd'); c.poly([(16, 11), (19, 2), (21, 10)], 'd')
    c.poly([(36, 36), (47, 30), (46, 38)], 'a')
    c.outline()
    c.shadow('a', 'd')
    for x in (6, 14, 30, 40):
        c.rect(x + 2, 40, x + 5, 42, 'c')
    # scale plates = labels
    for x, y in [(22, 27), (30, 27), (26, 33)]:
        c.rect(x - 2, y - 1, x + 2, y + 1, 'w')
    c.line(8, 12, 14, 8, 'k'); c.line(36, 12, 42, 8, 'k')
    c.ell(24, 34, 6, 4, 'b')
    bigeye(c, 9, 15); bigeye(c, 17, 15, 3, 5)
    c.line(8, 14, 12, 14, 'k')
    c.line(6, 23, 12, 23, 'k'); c.px(7, 24, 'w')
    soft_flame(c, 3, 22, 4, -1, 'q', 'w')                                                         # a puff of blue static


# ---------------------------------------------------------------- Roboruff / Robowoof: robot puppies
@sprite48('Roboruff', {'a': '#e8ecf4', 'd': '#a8b0c4', 'b': '#ffffff', 'c': '#ff3f5f'})
def roboruff(c):
    c.rect(18, 28, 38, 38, 'a')
    for x in (20, 26, 31, 36):
        c.rect(x - 1, 38, x + 1, 44, 'd')
    c.rect(38, 26, 41, 29, 'a')                                                                       # stub tail
    c.rect(8, 16, 26, 30, 'a')
    c.rect(6, 14, 10, 22, 'd'); c.rect(22, 12, 26, 20, 'd')                                           # ears
    c.outline()
    c.shadow('a', 'd')
    # battery meter: one bar left
    c.rect(26, 31, 36, 35, 'k'); c.rect(27, 32, 28, 34, 'c'); c.px(37, 33, 'k')
    c.rect(10, 18, 24, 25, 'n')
    c.rect(12, 20, 14, 23, 'q'); c.rect(19, 20, 21, 23, 'q')                                          # LED eyes
    c.px(12, 20, 'w'); c.px(19, 20, 'w')
    c.line(14, 28, 18, 28, 'k')
    c.rect(4, 26, 7, 28, 'k')
    blush(c, 8, 26) if False else None
    for x, y in [(42, 18), (44, 16)]:
        c.px(x, y, 'k')                                                                                # zzz... power save


@sprite48('Robowoof', {'a': '#d8dce8', 'd': '#8a92a8', 'b': '#ffffff', 'c': '#ffcf3a'})
def robowoof(c):
    c.rect(16, 24, 40, 36, 'a')
    for x, col in [(18, 'd'), (38, 'd'), (22, 'a'), (35, 'a')]:
        c.rect(x - 2, 36, x + 1, 45, col)
    # lightning antenna tail, angled and short
    c.line(40, 26, 44, 20, 'c', 2); c.line(44, 20, 42, 18, 'c', 2); c.line(42, 18, 46, 13, 'c', 2)
    c.rect(4, 12, 24, 28, 'a')
    c.rect(2, 9, 7, 18, 'd'); c.rect(20, 7, 25, 16, 'd')
    c.outline()
    c.shadow('a', 'd')
    c.rect(6, 15, 22, 23, 'n')
    c.rect(8, 17, 11, 21, 'c'); c.rect(16, 17, 19, 21, 'c')
    c.line(7, 16, 11, 17, 'q'); c.line(16, 17, 20, 16, 'q')                                            # mischievous brows
    c.rect(18, 28, 38, 30, 'c')
    c.line(8, 26, 14, 26, 'k'); c.px(15, 25, 'k')
    for x, y in [(0, 24), (2, 30), (44, 30)]:
        spark(c, x, y, 'c')


# ---------------------------------------------------------------- Laserpouncer: a black cat after the red dot
@sprite48('Laserpouncer', {'a': '#3a3a4a', 'd': '#1e1e28', 'b': '#8a8aa0', 'c': '#ff3f3f'})
def laserpouncer(c):
    # crouched mid-pounce, butt up, tail wiggling
    c.poly([(36, 24), (42, 14), (46, 18), (40, 28)], 'a')
    c.ell(28, 30, 12, 8, 'a')
    c.ell(14, 32, 9, 8, 'a')
    c.poly([(8, 27), (6, 18), (13, 24)], 'a'); c.poly([(17, 24), (20, 16), (22, 26)], 'a')
    for x in (10, 18, 30, 37):
        c.ell(x, 40, 3, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.ell(11, 36, 4, 3, 'b')
    # huge pupils locked on
    c.ell(10, 31, 3, 3, 'z'); c.ell(17, 31, 3, 3, 'z')
    c.ell(10, 31, 2, 2.5, 'k'); c.ell(17, 31, 2, 2.5, 'k'); c.px(9, 30, 'w'); c.px(16, 30, 'w')
    c.line(12, 37, 15, 37, 'k')
    # the dot, glowing, uncatchable
    c.ell(2, 44, 1.5, 1.5, 'c'); c.ring(2, 44, 3, 3, 1, 'm')


# ---------------------------------------------------------------- Staticling / Statickle: frizzy static creatures
@sprite48('Staticling', {'a': '#d8c4ff', 'd': '#9a7ad8', 'b': '#f4eeff', 'c': '#ff5aa8'})
def staticling(c):
    # stuck to the ceiling, upside down, hair standing straight down
    c.rect(0, 0, 47, 3, 'n')
    c.ell(24, 18, 11, 10, 'a')
    for i in range(10):
        x = 14 + i * 2
        c.line(x, 26, x + (i % 3 - 1), 34 + (i % 2) * 3, 'a')
    c.ell(13, 9, 3, 4, 'a'); c.ell(35, 9, 3, 4, 'a')                                                    # feet on the ceiling
    # the balloon it was rubbed on
    c.ell(40, 30, 6, 7, 'c'); c.line(40, 37, 38, 44, 'k')
    c.outline()
    c.shadow('a', 'd')
    c.px(37, 27, 'w'); c.px(38, 26, 'w')
    bigeye(c, 17, 16); bigeye(c, 27, 16)
    c.line(22, 13, 26, 13, 'k')                                                                         # upside-down smile
    c.px(21, 14, 'k'); c.px(27, 14, 'k')
    blush(c, 14, 20); blush(c, 30, 20)
    for x, y in [(6, 16), (8, 24)]:
        spark(c, x, y, 'y')


@sprite48('Statickle', {'a': '#9ae0ff', 'd': '#4aa0d0', 'b': '#e8f8ff', 'c': '#ffcf3a'})
def statickle(c):
    # frizz-ball porcupine, every hair a spike of static
    for i in range(22):
        a = math.pi + i * math.pi / 21
        c.line(24 + math.cos(a) * 10, 28 + math.sin(a) * 10, 24 + math.cos(a) * 20, 28 + math.sin(a) * 19, 'a', 2)
    c.ell(24, 30, 14, 12, 'a')
    c.ell(16, 43, 3, 2, 'd'); c.ell(32, 43, 3, 2, 'd')
    # paw out toward a doorknob
    c.ell(6, 34, 3, 3, 'a')
    c.ell(1, 34, 2, 2, 'y')
    c.outline()
    c.shadow('a', 'd')
    c.ell(22, 33, 8, 6, 'b')
    bigeye(c, 16, 26); bigeye(c, 26, 26)
    c.line(20, 35, 24, 35, 'k'); c.px(25, 34, 'k')                                                         # mischief
    blush(c, 13, 32); blush(c, 30, 32)
    for x, y in [(2, 30), (4, 27), (1, 39)]:
        spark(c, x, y, 'c')


# ---------------------------------------------------------------- Spellbot: a robot parrot with a keypad belly
@sprite48('Spellbot', {'a': '#2ad1c4', 'd': '#16948a', 'b': '#d8fff8', 'c': '#2a2a38'})
def spellbot(c):
    c.poly([(30, 38), (44, 44), (40, 46), (28, 44)], 'd')                                                   # tail feathers
    c.rect(14, 20, 34, 42, 'a')
    c.ell(22, 14, 10, 9, 'a')
    c.ring(22, 4, 4, 2, 1, 'c')                                                                              # carry handle
    c.poly([(8, 13), (13, 10), (13, 18)], 'y')                                                               # beak
    c.ell(16, 44, 3, 1.5, 'y'); c.ell(30, 44, 3, 1.5, 'y')
    c.outline()
    c.shadow('a', 'd')
    # display reading a confident misspelling
    c.rect(16, 22, 32, 26, 'c')
    for x in (18, 21, 24, 27, 30):
        c.rect(x, 23, x + 1, 25, 'r')
    # keypad
    for y in (29, 32, 35, 38):
        for x in (17, 21, 25, 29):
            c.rect(x, y, x + 2, y + 1, 'w')
    bigeye(c, 16, 11, 3, 4); bigeye(c, 24, 11, 3, 4)
    c.ell(19, 18, 1, 1, 'k')
    blush(c, 28, 16)


# ---------------------------------------------------------------- Glowpeg: a jellyfish made of glowing pegs
@sprite48('Glowpeg', {'a': '#2a2a3a', 'd': '#16161f', 'b': '#4a4a5e', 'c': '#ff3fa4'})
def glowpeg(c):
    c.ell(24, 18, 15, 12, 'a')
    c.clear(0, 20, 47, 47)
    c.rect(9, 18, 39, 22, 'a')
    for x in (12, 18, 24, 30, 36):
        c.rect(x - 1, 22, x + 1, 36 + (x % 7) % 4, 'a')
    c.outline()
    # glowing pegs in the dark
    cols = 'cyqzfm'
    k = 0
    for y in range(9, 21, 3):
        for x in range(12, 37, 3):
            if ((x - 24) / 15) ** 2 + ((y - 18) / 12) ** 2 < .8:
                c.px(x, y, cols[k % 6]); k += 1
    for x in (12, 18, 24, 30, 36):
        for y in range(25, 36, 3):
            c.px(x, y, cols[(x + y) % 6])
    bigeye(c, 17, 12, 3, 4); bigeye(c, 28, 12, 3, 4)
    c.ell(17, 12, 1, 1, 'w') if False else None
    c.line(21, 18, 26, 18, 'w')
    blush(c, 14, 17); blush(c, 31, 17)
