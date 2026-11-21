"""Dex 76-90: things that fly out of classrooms and things that live in game consoles."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Papairplane / Paperjet: folded-paper birds
@sprite48('Papairplane', {'a': '#f8f8f0', 'd': '#c8ccd8', 'b': '#ffffff', 'c': '#7ab0ff'})
def papairplane(c):
    # folded wings: crisp triangles
    c.poly([(8, 26), (40, 14), (30, 30)], 'a')
    c.poly([(10, 28), (42, 34), (28, 31)], 'd')
    c.ell(16, 27, 8, 7, 'a')
    c.outline()
    # ruled notebook lines + red margin
    for y in (20, 24):
        c.line(22, y + 1, 36, y - 4, 'c')
    c.line(28, 18, 30, 29, 'r')
    c.line(30, 30, 40, 33, 'd')
    bigeye(c, 10, 24, 3, 4); bigeye(c, 17, 24, 3, 4)
    c.poly([(4, 29), (9, 27), (9, 31)], 'y')
    blush(c, 13, 31)
    # whoosh lines
    for y in (38, 41):
        c.line(32, y, 44, y, 'q')


@sprite48('Paperjet', {'a': '#ffffff', 'd': '#b8c0d0', 'b': '#ffffff', 'c': '#ff3f5f'})
def paperjet(c):
    c.poly([(2, 24), (44, 8), (30, 26)], 'a')
    c.poly([(4, 26), (46, 40), (28, 30)], 'd')
    c.poly([(28, 26), (40, 22), (36, 30)], 'a')
    c.ell(13, 25, 9, 7, 'a')
    c.outline()
    c.line(4, 25, 38, 13, 'c'); c.line(6, 27, 40, 37, 'c')                             # racing stripes
    for y in (16, 20):
        c.line(18, y + 4, 34, y - 2, 'q')
    bigeye(c, 7, 22, 3, 4); bigeye(c, 14, 22, 3, 4)
    c.line(6, 21, 10, 22, 'k'); c.line(14, 22, 17, 21, 'k')
    c.poly([(0, 27), (5, 25), (5, 29)], 'y')
    c.line(9, 29, 13, 29, 'k')
    for y in (36, 40, 44):
        c.line(30, y, 46, y, 'q')


# ---------------------------------------------------------------- Balloonatic: a balloon-animal poodle that floats off
@sprite48('Balloonatic', {'a': '#ff5aa8', 'd': '#d02c7a', 'b': '#ffd0e8', 'c': '#ffffff'})
def balloonatic(c):
    # twisted balloon segments
    for x, y, rx, ry in [(20, 14, 8, 8), (24, 26, 9, 6), (12, 30, 3, 6), (34, 30, 3, 6), (16, 36, 3, 5), (30, 36, 3, 5),
                         (37, 21, 4, 3), (12, 7, 3, 4), (26, 7, 3, 4)]:
        c.ell(x, y, rx, ry, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(16, 10), (21, 23), (10, 27), (32, 27), (35, 19)]:
        c.px(x, y, 'b'); c.px(x + 1, y, 'b')                                              # shine
    # string it let go of, trailing DOWN and away
    c.line(24, 32, 28, 40, 'k'); c.line(28, 40, 25, 46, 'k')
    bigeye(c, 14, 13, 3, 4); bigeye(c, 22, 13, 3, 4)
    c.line(17, 19, 21, 19, 'k')
    blush(c, 12, 18); blush(c, 25, 18)
    c.px(44, 6, 'k'); c.px(42, 4, 'k')                                                    # wheee


# ---------------------------------------------------------------- Foamfalcon: foam-dart beak, still hurts
@sprite48('Foamfalcon', {'a': '#2e7dff', 'd': '#1a4cb0', 'b': '#e0ecff', 'c': '#ff8a1a'})
def foamfalcon(c):
    c.poly([(30, 22), (46, 14), (44, 30), (34, 34)], 'd')                                    # wing raised
    c.ell(26, 32, 11, 10, 'a')
    c.ell(24, 35, 7, 6, 'b')
    c.ell(20, 44, 3, 1.5, 'y'); c.ell(30, 44, 3, 1.5, 'y')
    c.ell(18, 20, 10, 9, 'a')
    # foam dart beak with a suction-cup tip
    c.rect(2, 19, 10, 23, 'c'); c.ell(2, 21, 2, 3, 'r')
    c.outline()
    c.shadow('a', 'd')
    for x in (4, 7):
        c.px(x, 20, 'y')
    c.line(34, 20, 42, 17, 'c'); c.line(36, 26, 43, 24, 'c')                                 # foam stripes
    bigeye(c, 12, 16); bigeye(c, 21, 16, 3, 5)
    c.line(11, 15, 15, 15, 'k'); c.line(21, 15, 24, 15, 'k')
    blush(c, 14, 24)


# ---------------------------------------------------------------- Kitedelic: a tie-dye kite bat, string tangled with bows
@sprite48('Kitedelic', {'a': '#ff3fa4', 'd': '#a04cff', 'b': '#ffe0f0', 'c': '#3ae0ff'})
def kitedelic(c):
    c.poly([(24, 2), (44, 20), (24, 36), (4, 20)], 'a')
    c.outline()
    # tie-dye quarters
    c.poly([(24, 4), (42, 20), (24, 20)], 'c')
    c.poly([(24, 20), (42, 20), (24, 34)], 'y')
    c.poly([(6, 20), (24, 20), (24, 34)], 'd')
    c.ring(24, 20, 6, 6, 1, 'w')
    c.line(24, 3, 24, 35, 't'); c.line(5, 20, 43, 20, 't')
    # face in the centre
    c.ell(24, 20, 5, 5, 'b')
    bigeye(c, 21, 18, 2, 3); bigeye(c, 26, 18, 2, 3)
    c.line(23, 23, 25, 23, 'k')
    # wavy string with bows, tangled into a little loop
    for i, (x, y) in enumerate([(24, 37), (21, 40), (24, 43), (28, 41), (26, 38)]):
        c.px(x, y, 'k')
    c.line(26, 38, 32, 44, 'k')
    for x, y in [(22, 41), (30, 42)]:
        c.poly([(x - 2, y - 1), (x, y), (x - 2, y + 1)], 'm'); c.poly([(x + 2, y - 1), (x, y), (x + 2, y + 1)], 'm')
    c.rect(34, 42, 44, 46, 'G'); c.ell(39, 41, 4, 2, 'L')                                    # the tree it's stuck in


# ---------------------------------------------------------------- Dustbunnie / Dustbeast: under-the-bed rabbits
@sprite48('Dustbunnie', {'a': '#b8b8c4', 'd': '#7e7e8e', 'b': '#e8e8f0', 'c': '#8a8a9a'})
def dustbunnie(c):
    c.ell(24, 32, 13, 11, 'a')
    c.ell(18, 12, 3, 9, 'a'); c.ell(29, 12, 3, 9, 'a')
    c.ell(16, 44, 4, 1.5, 'a'); c.ell(31, 44, 4, 1.5, 'a')
    c.outline(diag=True)
    c.shadow('a', 'd')
    # fluffy fringe: jagged dust on the outline
    for x, y in [(11, 28), (10, 34), (13, 40), (37, 28), (38, 34), (35, 40), (24, 20)]:
        c.px(x, y, 'a'); c.px(x - 1, y + 1, '#')
    c.ell(18, 12, 1, 6, 'b'); c.ell(29, 12, 1, 6, 'b')
    bigeye(c, 17, 28); bigeye(c, 27, 28)
    c.rect(23, 33, 24, 33, 'm')
    c.line(22, 35, 25, 35, 'k')
    blush(c, 14, 33); blush(c, 30, 33)
    for x, y in [(4, 40), (6, 37), (42, 38), (44, 41)]:
        c.px(x, y, 'c')                                                                      # floating dust


@sprite48('Dustbeast', {'a': '#9a9aa8', 'd': '#62626e', 'b': '#dcdce6', 'c': '#ff3f5f'})
def dustbeast(c):
    c.ell(24, 30, 18, 15, 'a')
    c.ell(14, 9, 4, 9, 'a'); c.ell(33, 8, 4, 9, 'a')
    c.ell(10, 44, 6, 2, 'a'); c.ell(37, 44, 6, 2, 'a')
    c.outline(diag=True)
    c.shadow('a', 'd')
    # stuff it absorbed: a sock, a coin, a toy brick
    c.poly([(34, 30), (41, 30), (41, 38), (37, 38), (37, 34), (34, 34)], 'w'); c.line(34, 31, 41, 31, 'c')
    c.ell(10, 36, 2.5, 2.5, 'y')
    c.rect(28, 38, 33, 41, 'c'); c.px(29, 37, 'c'); c.px(32, 37, 'c')
    bigeye(c, 14, 24); bigeye(c, 29, 24)
    c.line(13, 23, 18, 23, 'k'); c.line(29, 23, 34, 23, 'k')
    c.line(19, 32, 28, 32, 'k'); c.px(18, 31, 'k'); c.px(29, 31, 'k')
    c.px(21, 33, 'w'); c.px(26, 33, 'w')


# ---------------------------------------------------------------- Cloudsurf: a cloud otter on an airbrushed board
@sprite48('Cloudsurf', {'a': '#ffffff', 'd': '#c8d4e8', 'b': '#ffffff', 'c': '#ff7a3a'})
def cloudsurf(c):
    # surfboard with an airbrushed sunset
    c.ell(24, 41, 21, 4, 'c')
    for x, y, r in [(16, 28, 7), (24, 24, 8), (32, 28, 7), (24, 32, 9)]:
        c.ell(x, y, r, r - 1, 'a')
    c.ell(10, 34, 3, 2, 'a'); c.ell(38, 30, 3, 2, 'a')                                         # arms out, balancing
    c.outline()
    c.shadow('a', 'd')
    c.line(5, 41, 43, 41, 'y'); c.line(8, 43, 40, 43, 'm')
    bigeye(c, 18, 24); bigeye(c, 27, 24)
    c.line(21, 30, 25, 30, 'k'); c.px(20, 29, 'k'); c.px(26, 29, 'k')
    blush(c, 15, 29); blush(c, 30, 29)
    for x, y in [(2, 46), (6, 45), (44, 46)]:
        c.px(x, y, 'q')


# ---------------------------------------------------------------- Aquanetta: a cockatoo whose hair does not move. Ever.
@sprite48('Aquanetta', {'a': '#ffd0e8', 'd': '#e090b8', 'b': '#fff4fa', 'c': '#a04cff'})
def aquanetta(c):
    # enormous teased bouffant
    c.ell(24, 13, 16, 12, 'c')
    c.ell(24, 32, 11, 11, 'a')
    c.ell(24, 36, 7, 6, 'b')
    c.ell(12, 33, 3, 6, 'a'); c.ell(36, 33, 3, 6, 'a')
    c.ell(19, 44, 3, 1.5, 'y'); c.ell(29, 44, 3, 1.5, 'y')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(14, 8), (22, 4), (32, 6), (36, 14), (12, 16)]:
        c.ring(x, y, 2, 2, 1, 'v')                                                                # perm curls
    c.px(30, 10, 'w'); c.px(31, 9, 'w')                                                            # lacquer shine
    c.poly([(21, 29), (27, 29), (24, 33)], 'y')
    bigeye(c, 17, 24); bigeye(c, 27, 24)
    c.line(16, 23, 20, 22, 'k'); c.line(27, 22, 31, 23, 'k')                                       # lashes
    blush(c, 14, 29); blush(c, 31, 29)
    # spray mist
    for x, y in [(42, 6), (44, 9), (41, 11)]:
        c.px(x, y, 'q')


# ---------------------------------------------------------------- Parachutie / Parachuteor: flying squirrels in parachute pants
@sprite48('Parachutie', {'a': '#c08050', 'd': '#8a5430', 'b': '#fff0dc', 'c': '#3ae0ff'})
def parachutie(c):
    c.ell(38, 22, 5, 8, 'a')                                                                       # fluffy tail
    # glide membrane = shiny baggy pants
    c.poly([(8, 26), (40, 26), (44, 40), (4, 40)], 'c')
    c.ell(24, 26, 10, 8, 'a')
    c.ell(24, 15, 10, 9, 'a')
    c.ell(15, 7, 3, 3, 'a'); c.ell(33, 7, 3, 3, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x in (12, 20, 28, 36):
        c.line(x, 29, x - 1, 39, 'o')                                                              # pant pleats
    for x, y in [(10, 34), (37, 34)]:
        c.rect(x, y, x + 3, y + 2, 'k'); c.px(x + 1, y + 1, 'e' if False else 'w')                  # zipper pockets
    c.ell(24, 19, 5, 3, 'b')
    bigeye(c, 18, 12); bigeye(c, 27, 12)
    c.line(22, 20, 26, 20, 'k')
    blush(c, 15, 17); blush(c, 31, 17)


@sprite48('Parachuteor', {'a': '#a86a40', 'd': '#704420', 'b': '#fff0dc', 'c': '#ffcf3a'})
def parachuteor(c):
    c.ell(40, 18, 6, 9, 'a')
    c.poly([(4, 24), (44, 24), (47, 42), (1, 42)], 'c')
    c.ell(24, 24, 11, 9, 'a')
    # hands out: the "you can't touch this" stop pose
    c.ell(5, 18, 4, 4, 'a'); c.ell(43, 18, 4, 4, 'a')
    c.ell(24, 12, 10, 9, 'a')
    c.ell(15, 4, 3, 3, 'a'); c.ell(33, 4, 3, 3, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x in (9, 17, 25, 33, 41):
        c.line(x, 27, x - 1, 41, 'f')
    c.ell(24, 16, 5, 3, 'b')
    c.rect(16, 9, 32, 11, 'k'); c.px(18, 9, 'q'); c.px(28, 9, 'q')                                  # shades
    c.line(21, 18, 27, 18, 'k'); c.px(28, 17, 'k')
    for x, y in [(2, 12), (46, 12)]:
        c.line(x, y, x, y - 3, 'k')                                                                # motion


# ---------------------------------------------------------------- Twistorm: a little whirlwind full of colored dots
@sprite48('Twistorm', {'a': '#e0f0ff', 'd': '#a8c4e0', 'b': '#ffffff', 'c': '#ff3f5f'})
def twistorm(c):
    c.poly([(6, 6), (42, 6), (34, 22), (28, 36), (24, 44), (20, 36), (14, 22)], 'a')
    c.outline()
    c.shadow('a', 'd')
    for y in (11, 18, 26, 33):
        c.line(14 + (y - 11) // 3, y, 34 - (y - 11) // 3, y - 2, 'd')
    # spinner dots in the four colors
    for x, y, col in [(10, 8, 'r'), (38, 9, 'b' if False else 'q'), (34, 20, 'y'), (16, 24, 'g')]:
        c.ell(x, y, 2, 2, col)
    bigeye(c, 18, 12, 3, 4); bigeye(c, 26, 12, 3, 4)
    c.line(20, 18, 25, 19, 'k')                                                                    # dizzy grin
    blush(c, 15, 17); blush(c, 29, 17)
    c.ell(24, 46, 8, 1, 'd')


# ---------------------------------------------------------------- Moonbootle: a rock beetle in springy moon shoes
@sprite48('Moonbootle', {'a': '#8a93ab', 'd': '#5a6278', 'b': '#d8dce8', 'c': '#3a6cff'})
def moonbootle(c):
    c.ell(25, 25, 15, 11, 'a')
    c.line(24, 14, 24, 35, 'd')
    c.ell(11, 27, 7, 6, 'a')
    # moon-shoe trampolines on its feet
    for x in (14, 34):
        c.line(x, 34, x, 39, 'k')
        c.ell(x, 41, 6, 2.5, 'c')
    c.outline()
    c.shadow('a', 'd')
    for x in (14, 34):
        c.line(x - 5, 41, x + 5, 41, 'k')
        for dx in (-4, 0, 4):
            c.line(x + dx, 42, x + dx, 44, 'e' if False else 'k')
    for x, y in [(30, 18), (34, 24), (20, 20)]:
        c.ell(x, y, 1.5, 1.5, 'b')                                                                   # moon craters
    bigeye(c, 6, 24, 3, 4); bigeye(c, 12, 24, 3, 4)
    c.line(7, 31, 11, 31, 'k')
    blush(c, 4, 29)
    c.line(6, 21, 3, 16, 'k'); c.line(11, 21, 12, 15, 'k')
    for x, y in [(2, 44), (44, 46)]:
        c.px(x, y, 'k')


# ---------------------------------------------------------------- Blowcart / Cartrolith: game-cartridge rock creatures
@sprite48('Blowcart', {'a': '#a0a0a8', 'd': '#6a6a74', 'b': '#e8e8ec', 'c': '#ff3f5f'})
def blowcart(c):
    # a marmot whose body is a cartridge
    c.rect(14, 18, 36, 42, 'a')
    c.ell(25, 18, 11, 9, 'a')
    c.ell(16, 10, 3, 3, 'a'); c.ell(34, 10, 3, 3, 'a')
    c.ell(18, 44, 3, 1.5, 'd'); c.ell(32, 44, 3, 1.5, 'd')
    c.outline()
    c.shadow('a', 'd')
    c.rect(17, 26, 33, 36, 'c'); c.line(19, 29, 31, 29, 'w'); c.line(19, 32, 28, 32, 'y')            # label
    for x in range(16, 35, 2):
        c.px(x, 40, 'd')                                                                              # contacts
    bigeye(c, 18, 14); bigeye(c, 28, 14)
    c.ring(25, 21, 1.5, 1.5, 1, 'k')                                                                   # blowing
    blush(c, 15, 19); blush(c, 32, 19)
    for x, y in [(7, 21), (4, 19), (6, 24), (2, 22)]:
        c.px(x, y, 'd')                                                                               # the dust it blew off


@sprite48('Cartrolith', {'a': '#8a8a94', 'd': '#55555e', 'b': '#dcdce2', 'c': '#3a6cff'})
def cartrolith(c):
    # a stone gorilla built from a giant cartridge
    c.rect(12, 12, 36, 40, 'a')
    c.ell(24, 10, 9, 7, 'a')
    c.ell(7, 28, 5, 10, 'a'); c.ell(41, 28, 5, 10, 'a')
    c.ell(7, 40, 5, 4, 'd'); c.ell(41, 40, 5, 4, 'd')
    c.rect(14, 40, 21, 46, 'a'); c.rect(27, 40, 34, 46, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.rect(15, 18, 33, 30, 'c'); c.line(17, 21, 31, 21, 'w'); c.line(17, 25, 26, 25, 'y')
    # glowing save battery heart
    c.ell(24, 35, 3, 2, 'z'); c.px(23, 34, 'w')
    for x in range(14, 35, 3):
        c.px(x, 38, 'd')
    for x, y in [(9, 18), (40, 22), (20, 44)]:
        c.line(x, y, x + 2, y + 2, 'd')                                                                # cracks
    bigeye(c, 18, 7); bigeye(c, 27, 7)
    c.line(17, 6, 22, 7, 'k'); c.line(27, 7, 32, 6, 'k')
    c.line(21, 13, 27, 13, 'k')
