"""Dex 106-120: the rest of the bug zoo and the first of the garden."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Rantasaurus: the elected (regretted) queen ant
@sprite48('Rantasaurus', {'a': '#d8302a', 'd': '#8e1a14', 'b': '#ffd0c8', 'c': '#ffcf3a'})
def rantzilla(c):
    c.ell(35, 35, 11, 9, 'a')
    c.ell(22, 31, 6, 6, 'a')
    c.ell(14, 21, 10, 9, 'a')
    for x0, x1 in [(18, 12), (22, 22), (27, 32), (32, 40)]:
        c.line(x0, 37, x1, 46, 'd', 2)
    c.ell(8, 30, 3, 3, 'a')
    c.poly([(6, 13), (8, 6), (11, 10), (14, 4), (17, 10), (20, 6), (21, 13)], 'c')            # crown
    c.outline()
    c.shadow('a', 'd')
    c.line(17, 25, 30, 38, 'q', 2)                                                               # "ELECTED" sash
    c.px(13, 6, 'r')
    # megaphone in hand, pointed away from the body
    c.poly([(2, 26), (7, 28), (7, 32), (2, 34)], 'w'); c.px(1, 30, 'k')
    c.line(10, 13, 5, 3, 'k'); c.line(17, 13, 20, 2, 'k')
    bigeye(c, 8, 18); bigeye(c, 17, 18, 3, 5)
    c.line(7, 17, 11, 18, 'k'); c.line(17, 18, 20, 17, 'k')
    c.line(10, 26, 15, 26, 'k')
    c.px(38, 31, 'b'); c.px(42, 35, 'b')


# ---------------------------------------------------------------- Butterclip / Flutterclip: butterflies made of hair clips
@sprite48('Butterclip', {'a': '#ff8ad8', 'd': '#d04aa0', 'b': '#ffe6f6', 'c': '#7ae0ff'})
def butterclip(c):
    # translucent glitter-plastic wings
    c.poly([(22, 22), (4, 6), (2, 22), (10, 28), (22, 26)], 'a'); c.poly([(22, 26), (6, 30), (8, 42), (22, 32)], 'c')
    c.poly([(26, 22), (44, 6), (46, 22), (38, 28), (26, 26)], 'a'); c.poly([(26, 26), (42, 30), (40, 42), (26, 32)], 'c')
    c.ell(24, 27, 4, 10, 'd')
    c.ell(24, 16, 6, 5, 'd')
    c.outline()
    for x, y in [(8, 14), (13, 18), (38, 12), (40, 18), (12, 36), (36, 37)]:
        c.px(x, y, 'w')                                                                             # glitter
    # clip teeth along the body
    for y in range(22, 37, 3):
        c.px(22, y, 'w'); c.px(26, y, 'w')
    c.line(22, 12, 18, 5, 'k'); c.line(26, 12, 30, 5, 'k')
    bigeye(c, 20, 14, 3, 4); bigeye(c, 25, 14, 3, 4)
    c.line(22, 19, 25, 19, 'k')
    blush(c, 18, 18); blush(c, 28, 18)


@sprite48('Flutterclip', {'a': '#ff5ac0', 'd': '#b8208a', 'b': '#ffe0f4', 'c': '#a04cff'})
def flutterclip(c):
    c.poly([(22, 20), (1, 2), (0, 22), (10, 30), (22, 26)], 'a'); c.poly([(22, 26), (2, 32), (6, 46), (22, 34)], 'c')
    c.poly([(26, 20), (47, 2), (47, 22), (38, 30), (26, 26)], 'a'); c.poly([(26, 26), (46, 32), (42, 46), (26, 34)], 'c')
    c.ell(24, 26, 5, 12, 'd')
    c.ell(24, 14, 7, 6, 'd')
    c.outline()
    # snapping clip teeth on the wing edges (the grudge)
    for x in range(4, 20, 3):
        c.px(x, 30 - (x // 6), 'w')
    for x in range(28, 44, 3):
        c.px(x, 28 + (x // 12), 'w')
    for x, y in [(6, 10), (12, 16), (40, 10), (36, 16), (10, 40), (38, 40), (24, 40)]:
        c.px(x, y, 'y')
    c.line(21, 9, 15, 1, 'k'); c.line(27, 9, 33, 1, 'k')
    bigeye(c, 19, 12, 3, 4); bigeye(c, 26, 12, 3, 4)
    c.line(18, 11, 22, 12, 'k'); c.line(26, 12, 29, 11, 'k')
    c.line(22, 18, 26, 17, 'k')


# ---------------------------------------------------------------- Ladybugsy: a playground racketeer ladybug
@sprite48('Ladybugsy', {'a': '#ff3f3f', 'd': '#b01e1e', 'b': '#ffd8d8', 'c': '#2a2a38'})
def ladybugsy(c):
    c.ell(26, 32, 15, 11, 'a')
    c.ell(12, 28, 8, 7, 'c')
    for x0, x1 in [(18, 15), (24, 24), (32, 34)]:
        c.line(x0, 40, x1, 45, 'c', 2)
    # fedora
    c.rect(4, 17, 20, 19, 'c'); c.rect(7, 12, 17, 17, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.line(26, 21, 26, 43, 'c')
    for x, y in [(19, 27), (32, 25), (21, 36), (35, 35), (29, 31)]:
        c.ell(x, y, 2, 2, 'c')
    c.line(7, 16, 17, 16, 'r')                                                                          # hat band
    # gummy worm "payment" in its claw
    c.line(1, 34, 5, 32, 'z', 2); c.line(5, 32, 8, 34, 'y', 2)
    c.ell(10, 27, 2, 1.5, 'w'); c.ell(15, 27, 2, 1.5, 'w')
    c.rect(10, 27, 11, 28, 'k'); c.rect(15, 27, 16, 28, 'k')
    c.line(9, 25, 12, 26, 'w'); c.line(14, 26, 17, 25, 'w')
    c.line(10, 32, 14, 32, 'w'); c.px(15, 31, 'w')


# ---------------------------------------------------------------- Beeperbee: a bee whose stripes are a pager display
@sprite48('Beeperbee', {'a': '#ffd23a', 'd': '#d89a10', 'b': '#fff6cc', 'c': '#2a2a38'})
def beeperbee(c):
    c.ell(16, 16, 7, 5, 'q'); c.ell(30, 14, 7, 5, 'q')
    c.ell(28, 30, 12, 10, 'a')
    c.ell(14, 26, 9, 8, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.ring(16, 16, 7, 5, 1, 'w'); c.ring(30, 14, 7, 5, 1, 'w')
    # stripes = a pager screen reading 911
    c.rect(22, 26, 38, 33, 'c'); c.rect(23, 27, 37, 32, 'g')
    for x in (25, 30, 33):
        c.line(x + 1, 28, x + 1, 31, 'k')
    c.ring(25, 29, 1, 1, 1, 'k')
    c.line(24, 36, 36, 36, 'c')
    c.poly([(40, 30), (45, 31), (40, 33)], 'c')                                                           # tiny stinger
    c.line(10, 19, 7, 11, 'k'); c.line(15, 18, 16, 10, 'k')
    bigeye(c, 9, 23); bigeye(c, 16, 23, 3, 5)
    c.line(10, 30, 14, 30, 'k')
    blush(c, 7, 28); blush(c, 19, 28)
    for x, y in [(44, 22), (46, 25), (44, 28)]:
        c.line(x, y, x + 1, y, 'k')


# ---------------------------------------------------------------- Spicearachnid: a spider with five different hairdos
@sprite48('Spicearachnid', {'a': '#3a2a4a', 'd': '#1e1428', 'b': '#e8dcf0', 'c': '#ff3fa4'})
def spicearachnid(c):
    for x0, x1, y1 in [(16, 4, 42), (19, 10, 46), (29, 38, 46), (32, 44, 42), (16, 3, 32), (32, 45, 32), (18, 8, 24), (30, 40, 24)]:
        c.line(x0, 32, x1, y1, 'a', 2)
    c.ell(24, 32, 11, 9, 'a')
    c.ell(24, 21, 9, 8, 'a')
    # five hair puffs, five colors, each one the leader
    for x, y, col in [(15, 12, 'c'), (20, 9, 'y'), (25, 8, 'q'), (30, 10, 'z'), (34, 14, 'f')]:
        c.ell(x, y, 3.5, 3.5, col)
    c.outline()
    # platform sneakers on the front feet
    for x, y in [(2, 42), (42, 42)]:
        c.rect(x, y, x + 4, y + 3, 'w'); c.line(x, y + 3, x + 4, y + 3, 'c')
    bigeye(c, 18, 19); bigeye(c, 26, 19)
    c.line(21, 26, 26, 26, 'k'); c.px(20, 25, 'k'); c.px(27, 25, 'k')
    blush(c, 16, 24); blush(c, 30, 24)
    c.poly([(22, 31), (26, 31), (24, 35)], 'c')                                                            # star mark


# ---------------------------------------------------------------- Cicadaboom: a cicada with speakers for wings
@sprite48('Cicadaboom', {'a': '#6a9a3a', 'd': '#3e6a1e', 'b': '#d8f0c0', 'c': '#2a2a38', 'e': '#c9ced8'})
def cicadaboom(c):
    # speaker-cone wings
    c.ell(12, 20, 9, 8, 'c'); c.ell(36, 20, 9, 8, 'c')
    c.ell(24, 30, 10, 12, 'a')
    c.ell(24, 18, 9, 7, 'a')
    for x0, x1 in [(17, 12), (22, 20), (27, 29), (31, 36)]:
        c.line(x0, 40, x1, 45, 'd', 2)
    c.outline()
    c.shadow('a', 'd')
    c.ring(12, 20, 6, 5, 1, 'e'); c.ell(12, 20, 2, 2, 'e'); c.ring(36, 20, 6, 5, 1, 'e'); c.ell(36, 20, 2, 2, 'e')
    for y in range(26, 40, 3):
        c.line(18, y, 30, y, 'd')
    # cool shades, finally awake after seventeen years
    c.rect(16, 15, 32, 18, 'k'); c.px(18, 15, 'q'); c.px(27, 15, 'q')
    c.line(21, 22, 27, 22, 'k'); c.px(28, 21, 'k')
    for x, y in [(1, 8), (3, 5), (45, 8), (43, 5)]:
        c.rect(x, y, x + 1, y + 1, 'k')


# ---------------------------------------------------------------- Sproutpup / Sprouthound: terracotta dogs that grow sprouts
@sprite48('Sproutpup', {'a': '#d8784a', 'd': '#a44c24', 'b': '#f8d0b0', 'c': '#5cd64a'})
def sproutpup(c):
    c.ell(28, 34, 11, 8, 'a')
    for x in (20, 26, 33, 37):
        c.ell(x, 43, 2.5, 2, 'a')
    c.ell(16, 24, 11, 10, 'a')
    c.ell(7, 20, 3, 6, 'd')                                                                                 # floppy ear
    # thin, patchy sprouts (mild disappointment)
    for x, y in [(12, 13), (17, 12), (22, 14), (30, 26), (34, 27), (38, 30)]:
        c.line(x, y + 2, x, y - 1, 'c', 1); c.px(x - 1, y - 1, 'c'); c.px(x + 1, y - 2, 'c')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(26, 37), (32, 36), (21, 30)]:
        c.px(x, y, 'd')                                                                                     # clay texture
    bigeye(c, 11, 21); bigeye(c, 20, 21, 3, 5)
    c.rect(6, 27, 7, 28, 'k')
    c.line(9, 30, 13, 30, 'k')
    blush(c, 14, 28)
    c.px(2, 40, 'q'); c.px(3, 42, 'q')                                                                     # just add water


@sprite48('Sprouthound', {'a': '#c8683a', 'd': '#8e3e1a', 'b': '#f4c8a4', 'c': '#3ab83a'})
def sprouthound(c):
    c.ell(28, 31, 14, 10, 'a')
    for x, col in [(17, 'd'), (37, 'd'), (21, 'a'), (40, 'a')]:
        c.rect(x - 2, 36, x + 1, 45, col)
    c.ell(13, 20, 11, 10, 'a')
    c.ell(5, 16, 3, 7, 'd')
    # lush green coat along the back
    for x in range(14, 44, 4):
        c.ell(x, 20 if x < 22 else 22, 3, 4, 'c')
    c.outline()
    c.shadow('a', 'd')
    for x in range(14, 44, 4):
        c.px(x, 19 if x < 22 else 21, 'l')
    bigeye(c, 8, 18); bigeye(c, 16, 18, 3, 5)
    c.line(7, 17, 11, 17, 'k'); c.line(16, 17, 19, 17, 'k')
    c.rect(2, 24, 3, 25, 'k')
    # sneeze: a burst of sprouts
    for x, y in [(0, 30), (2, 33), (5, 31)]:
        c.px(x, y, 'c'); c.px(x, y - 1, 'l')
    c.ell(6, 29, 1.5, 1, 'k')


# ---------------------------------------------------------------- Footbaggle / Footbagsquatch: knitted bigfoot kids
@sprite48('Footbaggle', {'a': '#8a6a4a', 'd': '#5a4028', 'b': '#e8d0b0', 'c': '#ff8a1a'})
def footbaggle(c):
    # a round knitted ball of a creature with BIG feet
    c.ell(24, 26, 14, 14, 'c')
    c.ell(13, 43, 6, 3, 'a'); c.ell(35, 43, 6, 3, 'a')
    c.ell(9, 26, 3, 4, 'a'); c.ell(39, 26, 3, 4, 'a')
    c.outline()
    # knit pattern panels
    c.poly([(12, 18), (24, 13), (24, 27), (12, 30)], 'g'); c.poly([(24, 27), (36, 30), (34, 38), (24, 40)], 'v')
    for y in range(14, 40, 3):
        c.line(11, y, 37, y, 'd' if y % 2 else 'c')
    c.ell(24, 25, 8, 6, 'b')
    bigeye(c, 18, 22); bigeye(c, 26, 22)
    c.line(22, 28, 26, 28, 'k')
    blush(c, 16, 27); blush(c, 30, 27)


@sprite48('Footbagsquatch', {'a': '#7a5a3a', 'd': '#4a3018', 'b': '#e0c8a8', 'c': '#ff8a1a'})
def footbagsquatch(c):
    # shaggy sasquatch mid-kick, footbag in the air
    c.ell(24, 26, 12, 14, 'a')
    c.ell(24, 10, 9, 8, 'a')
    c.ell(10, 24, 4, 9, 'a'); c.ell(38, 22, 4, 9, 'a')
    c.rect(16, 36, 21, 45, 'a'); c.ell(17, 45, 6, 2, 'a')
    c.poly([(27, 36), (32, 34), (44, 38), (42, 42)], 'a'); c.ell(44, 40, 3, 3, 'a')                         # kicking leg
    c.ell(40, 30, 3, 3, 'c')                                                                                 # the footbag
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(15, 18), (30, 22), (20, 30), (28, 33), (12, 30)]:
        c.line(x, y, x + 1, y + 3, 'd')                                                                      # shag
    c.ell(24, 12, 5, 4, 'b')
    bigeye(c, 19, 8); bigeye(c, 26, 8)
    c.line(21, 15, 26, 15, 'k')
    # blurry-photo motion lines
    for x, y in [(1, 14), (2, 20), (1, 26), (46, 10)]:
        c.line(x, y, x + 3, y, 'd')
    c.px(40, 27, 'g'); c.px(41, 31, 'v')


# ---------------------------------------------------------------- Fuzzpuff / Fuzznado: rubber-strand puffballs
@sprite48('Fuzzpuff', {'a': '#5cd64a', 'd': '#2e962a', 'b': '#e0ffd0', 'c': '#ff3fa4'})
def fuzzpuff(c):
    # radiating rubber strands
    import math
    for i in range(28):
        ang = i * math.pi * 2 / 28
        col = 'a' if i % 3 else ('c' if i % 2 else 'y')
        c.line(24 + math.cos(ang) * 8, 25 + math.sin(ang) * 8, 24 + math.cos(ang) * 17, 25 + math.sin(ang) * 16, col)
    c.ell(24, 25, 10, 9, 'a')
    c.outline()
    c.ell(24, 26, 7, 6, 'b')
    bigeye(c, 19, 22); bigeye(c, 26, 22)
    c.line(22, 29, 25, 29, 'k')
    blush(c, 16, 27); blush(c, 30, 27)


@sprite48('Fuzznado', {'a': '#3ab83a', 'd': '#1a7a1a', 'b': '#d0f8c0', 'c': '#ff3fa4'})
def fuzznado(c):
    import math
    # spinning: strands swirl in a spiral
    for i in range(36):
        ang = i * math.pi * 2 / 36
        col = 'a' if i % 3 else ('c' if i % 2 else 'q')
        r0, r1 = 10, 22
        c.line(24 + math.cos(ang) * r0, 24 + math.sin(ang) * r0 * .9,
               24 + math.cos(ang + .5) * r1, 24 + math.sin(ang + .5) * r1 * .9, col)
    c.ell(24, 24, 11, 10, 'a')
    c.outline()
    c.ell(24, 25, 8, 7, 'b')
    bigeye(c, 18, 21); bigeye(c, 27, 21)
    c.line(17, 20, 22, 21, 'k'); c.line(27, 21, 31, 20, 'k')
    c.line(21, 28, 27, 28, 'k'); c.px(20, 27, 'k'); c.px(28, 27, 'k')


# ---------------------------------------------------------------- Cabbagebaby / Cabbagelord: leafy sprout babies
@sprite48('Cabbagebaby', {'a': '#ffd8b8', 'd': '#e0a07a', 'b': '#fff0e0', 'c': '#8ae05a'})
def cabbagebaby(c):
    # wrapped in a cabbage leaf like a bonnet and blanket
    c.ell(24, 36, 12, 9, 'c')
    c.ell(24, 22, 11, 10, 'a')
    c.poly([(10, 22), (14, 8), (24, 4), (34, 8), (38, 22), (33, 14), (24, 11), (15, 14)], 'c')
    c.outline()
    c.shadow('a', 'd')
    for x0, y0, x1, y1 in [(24, 5, 24, 11), (24, 30, 24, 43), (16, 33, 20, 40), (32, 33, 28, 40)]:
        c.line(x0, y0, x1, y1, 'L')
    bigeye(c, 17, 21); bigeye(c, 27, 21)
    c.ell(24, 28, 1.2, 1, 'k')
    blush(c, 14, 26); blush(c, 31, 26)
    # adoption papers tucked in the blanket
    c.rect(32, 36, 40, 43, 'w'); c.line(33, 38, 39, 38, 'd'); c.line(33, 40, 37, 40, 'd'); c.px(38, 42, 'r')


@sprite48('Cabbagelord', {'a': '#6ac83a', 'd': '#3a8a1a', 'b': '#d8ffc0', 'c': '#ffcf3a'})
def cabbagelord(c):
    # a huge round cabbage king, leaves as a royal robe
    c.ell(24, 30, 18, 15, 'a')
    for x, y, rx, ry in [(10, 28, 7, 10), (38, 28, 7, 10), (24, 38, 12, 6)]:
        c.ell(x, y, rx, ry, 'L')
    c.poly([(14, 14), (16, 6), (20, 11), (24, 4), (28, 11), (32, 6), (34, 14)], 'c')
    c.ell(14, 45, 4, 2, 'L'); c.ell(34, 45, 4, 2, 'L')
    c.outline()
    c.shadow('a', 'd')
    for x0, y0, x1, y1 in [(24, 16, 24, 40), (10, 20, 14, 36), (38, 20, 34, 36)]:
        c.line(x0, y0, x1, y1, 'b')
    c.px(24, 6, 'r')
    bigeye(c, 16, 21); bigeye(c, 28, 21)
    c.line(15, 20, 20, 21, 'k'); c.line(28, 21, 32, 20, 'k')
    c.line(20, 28, 28, 28, 'k'); c.px(19, 27, 'k'); c.px(29, 27, 'k')
    # the smell
    for x, y in [(3, 10), (5, 7), (43, 10), (41, 7)]:
        c.line(x, y, x + 1, y - 2, 'g')
