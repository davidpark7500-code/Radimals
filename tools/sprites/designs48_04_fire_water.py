"""Dex 30-44: the snack-and-summer Fire types and the backyard Water types."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Flaminhawk: hawk chick dusted in red snack powder
@sprite48('Flaminhawk', {'a': '#e8402a', 'd': '#a42418', 'b': '#ffe0c8', 'c': '#ffb02e'})
def flaminhawk(c):
    c.poly([(34, 34), (46, 30), (46, 37), (36, 40)], 'd')           # tail feathers
    c.ell(25, 31, 12, 11, 'a')
    c.ell(22, 35, 7, 6, 'b')
    c.ell(35, 30, 5, 8, 'd')                                         # wing
    c.ell(19, 44, 3, 1, 'c'); c.ell(29, 44, 3, 1, 'c')
    # crest of crunchy curled snack puffs
    for x, y in [(14, 11), (19, 8), (24, 9), (29, 12)]:
        c.ell(x, y, 3, 3, 'c')
    c.ell(20, 19, 10, 9, 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(14, 11), (19, 8), (24, 9), (29, 12)]:
        c.px(x - 1, y - 1, 'F'); c.px(x + 1, y + 1, 'f')
    c.poly([(5, 21), (12, 18), (12, 24)], 'y')                       # beak
    bigeye(c, 13, 16); bigeye(c, 22, 16)
    # red dust on its cheeks that never washes off
    for x, y in [(11, 23), (13, 24), (24, 23), (26, 24), (12, 25)]:
        c.px(x, y, 'R')
    c.line(30, 24, 32, 22, 'k')                                       # licking-fingers wing
    for x, y in [(36, 20), (39, 22), (37, 24)]:
        c.px(x, y, 'R')


# ---------------------------------------------------------------- Inflamingo: an inflatable pool flamingo, one leg on fire
@sprite48('Inflamingo', {'a': '#ff6ab4', 'd': '#d8408a', 'b': '#ffe0f0', 'c': '#ffcf3a'})
def inflamingo(c):
    # body: a pool float ring
    c.ring(28, 31, 13, 8, 6, 'a')
    # S-neck and head
    c.line(18, 26, 13, 16, 'a', 4); c.line(13, 16, 16, 8, 'a', 4)
    c.ell(16, 8, 6, 5, 'a')
    # one standing leg + one folded leg on fire
    c.rect(27, 38, 28, 46, 'c'); c.rect(25, 45, 31, 46, 'c')
    c.line(33, 37, 38, 41, 'c', 2)
    c.outline()
    c.shadow('a', 'd')
    soft_flame(c, 39, 42, 7, 1)
    # valve + seam lines (it's inflatable)
    c.rect(39, 27, 40, 28, 'w'); c.px(39, 26, 'k')
    c.line(17, 31, 39, 31, 'b')
    c.poly([(5, 9), (11, 7), (11, 11)], 'k'); c.poly([(8, 8), (11, 7), (11, 9)], 'w')   # beak
    bigeye(c, 14, 5, 3, 4); bigeye(c, 19, 5, 3, 4)
    c.line(14, 12, 17, 12, 'k')                                        # "it's fine" smile
    blush(c, 12, 10); blush(c, 21, 10)
    c.px(43, 34, 'k'); c.px(44, 32, 'k')                               # sweat


# ---------------------------------------------------------------- Crimpede / Curlironx: hair-tool Fire types
@sprite48('Crimpede', {'a': '#c06aff', 'd': '#8640d0', 'b': '#f2e4ff', 'c': '#ffcf3a'})
def crimpede(c):
    # segmented body arching
    for i, (x, y) in enumerate([(36, 38), (31, 37), (26, 36), (21, 34)]):
        c.ell(x, y, 5, 5, 'a')
    for x in (20, 25, 30, 35, 39):
        c.line(x, 40, x - 1, 45, 'd', 2)
    c.ell(14, 26, 10, 9, 'a')                                          # head
    # CRIMPED hair: zigzag mane
    c.poly([(5, 20), (8, 8), (11, 14), (14, 5), (17, 13), (21, 6), (23, 15), (27, 10), (26, 22)], 'c')
    c.outline()
    c.shadow('a', 'd')
    for x0, y0 in [(8, 10), (14, 7), (21, 8)]:
        c.line(x0, y0, x0 + 1, y0 + 3, 'f')
    bigeye(c, 8, 24); bigeye(c, 17, 24)
    c.line(10, 31, 14, 31, 'k')
    blush(c, 5, 29); blush(c, 21, 29)
    for x, y in [(35, 32), (30, 31), (25, 30)]:
        c.px(x, y, 'b')


@sprite48('Curlironx', {'a': '#b04aff', 'd': '#6e24b8', 'b': '#f0e0ff', 'c': '#ffcf3a', 'e': '#c9ced8'})
def curlironx(c):
    # coiled power cord lying behind (low, coiled)
    c.ell(28, 34, 13, 9, 'a')
    c.ell(25, 37, 8, 5, 'b')
    for x, col in [(18, 'd'), (36, 'd'), (22, 'a'), (39, 'a')]:
        c.ell(x, 42, 4, 3, col)
    c.ell(16, 21, 11, 10, 'a')
    # ear tufts are curling-iron barrels with ringlets
    c.rect(7, 4, 10, 13, 'e'); c.rect(21, 3, 24, 12, 'e')
    c.ell(28, 30, 6, 6, 'c')                                            # curly mane puff
    c.ell(24, 26, 4, 4, 'c')
    c.outline()
    c.shadow('a', 'd')
    coil(c, [(41, 40), (44, 38), (46, 35)], 'k', 'e')
    for x, y in [(8, 6), (8, 9), (22, 5), (22, 8)]:
        c.line(x, y, x + 2, y + 1, 'f')
    for x, y in [(26, 28), (29, 31), (24, 25)]:
        c.ring(x, y, 1.6, 1.6, 1, 'f')
    bigeye(c, 9, 19); bigeye(c, 19, 19, 3, 5)
    c.line(8, 18, 12, 18, 'k'); c.line(19, 18, 22, 18, 'k')
    c.line(9, 27, 14, 27, 'k'); c.px(15, 26, 'k')
    blush(c, 6, 25)
    soft_flame(c, 9, 4, 4, 0, 'w', 'w'); soft_flame(c, 23, 3, 4, 0, 'w', 'w')   # steam


# ---------------------------------------------------------------- Orangeglug / Glugdeluxe: fizzy drink-mix newts
@sprite48('Orangeglug', {'a': '#ff8a1a', 'd': '#d05a08', 'b': '#fff0d0', 'c': '#ff3f5f'})
def orangeglug(c):
    # a squat, round drink-mix toad (no tail): one chubby blob with frog legs
    c.ell(24, 32, 15, 12, 'a')
    c.ell(24, 37, 10, 6, 'b')
    c.ell(10, 42, 5, 3, 'a'); c.ell(38, 42, 5, 3, 'a')                       # frog legs
    c.ell(16, 21, 5, 5, 'a'); c.ell(31, 21, 5, 5, 'a')                       # eye bumps
    # bendy straw stuck in its head, bent over (no upright shaft)
    c.line(24, 20, 26, 11, 'c', 2); c.line(26, 11, 33, 9, 'c', 2)
    c.outline()
    c.shadow('a', 'd')
    c.line(25, 15, 26, 15, 'w')
    # fizz dots all over: a drink, not a lizard
    for x, y in [(12, 30), (36, 29), (15, 36), (34, 35), (30, 26)]:
        c.ring(x, y, 1, 1, 1, 'F')
    bigeye(c, 14, 19); bigeye(c, 29, 19)
    c.line(19, 29, 28, 29, 'k'); c.px(18, 28, 'k'); c.px(29, 28, 'k')
    c.rect(20, 30, 27, 30, 'f')                                              # orange mustache
    blush(c, 11, 26); blush(c, 34, 26)


@sprite48('Glugdeluxe', {'a': '#ff7a0a', 'd': '#b84a04', 'b': '#fff0d0', 'c': '#ff3f5f'})
def glugdeluxe(c):
    # big bullfrog, chest puffed, fizz crown
    c.ell(24, 31, 18, 13, 'a')
    c.ell(24, 36, 12, 7, 'b')
    c.ell(7, 42, 6, 4, 'a'); c.ell(41, 42, 6, 4, 'a')
    c.ell(13, 18, 6, 6, 'a'); c.ell(34, 18, 6, 6, 'a')
    for x, y, h in [(19, 20, 8), (24, 19, 10), (29, 20, 8)]:
        soft_flame(c, x, y, h, 0)
    # twin bendy straws, bent outward
    c.line(9, 22, 4, 14, 'c', 2); c.line(4, 14, 1, 16, 'c', 2)
    c.line(39, 22, 44, 14, 'y', 2); c.line(44, 14, 47, 16, 'y', 2)
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(10, 30), (38, 29), (14, 37), (35, 36)]:
        c.ring(x, y, 1, 1, 1, 'F')
    bigeye(c, 10, 16); bigeye(c, 32, 16)
    c.line(9, 15, 14, 15, 'k'); c.line(32, 15, 37, 15, 'k')
    c.line(15, 28, 33, 28, 'k'); c.px(14, 27, 'k'); c.px(34, 26, 'k'); c.px(33, 27, 'k')   # wide smirk
    c.rect(17, 29, 31, 29, 'f')
    blush(c, 8, 24); blush(c, 37, 24)


# ---------------------------------------------------------------- Sourbomb: a sour-candy bomb, face folded in half
@sprite48('Sourbomb', {'a': '#b6ff3b', 'd': '#7ac416', 'b': '#f4ffd6', 'c': '#8a93ab'})
def sourbomb(c):
    c.ell(24, 30, 15, 14, 'a')
    c.rect(21, 13, 27, 17, 'c')                                           # fuse cap
    c.line(25, 13, 30, 7, 'k', 1)
    c.ell(16, 44, 3, 1, 'd'); c.ell(32, 44, 3, 1, 'd')
    c.outline()
    c.shadow('a', 'd')
    soft_flame(c, 31, 7, 6, 1)
    # sugar crystals
    for x, y in [(14, 22), (30, 20), (35, 31), (12, 34), (24, 39), (33, 38)]:
        c.px(x, y, 'w'); c.px(x + 1, y + 1, 'b')
    # PUCKER: eyes squeezed, mouth a tiny knot
    c.line(15, 27, 19, 29, 'k'); c.line(15, 31, 19, 29, 'k')
    c.line(32, 27, 28, 29, 'k'); c.line(32, 31, 28, 29, 'k')
    c.ring(24, 34, 1.6, 1.6, 1, 'k')
    blush(c, 12, 32); blush(c, 33, 32)
    c.px(39, 20, 'q'); c.px(40, 22, 'q')                                  # tear


# ---------------------------------------------------------------- Kerosnail: a snail with a lantern for a shell
@sprite48('Kerosnail', {'a': '#8ad0a0', 'd': '#4e9466', 'b': '#e4f8ea', 'c': '#c89a3a', 'e': '#ffe66a'})
def kerosnail(c):
    c.poly([(4, 44), (40, 44), (38, 38), (8, 36)], 'a')                    # foot
    c.ell(10, 30, 7, 8, 'a')                                               # head
    c.line(8, 23, 6, 15, 'a', 2); c.line(13, 23, 15, 15, 'a', 2)            # eye stalks
    # lantern shell
    c.rect(20, 18, 38, 38, 'c')
    c.rect(23, 21, 35, 35, 'e')
    c.ell(29, 15, 6, 3, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.ring(29, 11, 3, 3, 1, 'k')                                            # handle
    soft_flame(c, 29, 33, 10, 0)
    c.line(23, 28, 35, 28, 'c')
    c.ell(6, 14, 2, 2, 'w'); c.ell(15, 14, 2, 2, 'w')
    c.rect(6, 14, 7, 15, 'k'); c.rect(15, 14, 16, 15, 'k')
    c.px(6, 14, 'w'); c.px(15, 14, 'w')
    c.line(7, 33, 11, 33, 'k')
    blush(c, 5, 31)
    for x in range(10, 38, 4):
        c.px(x, 45, 'n')                                                    # greasy trail


# ---------------------------------------------------------------- Minibagel / Pizzarolla: pizza-snack rollers
@sprite48('Minibagel', {'a': '#e8b46a', 'd': '#b8823a', 'b': '#fff0c8', 'c': '#ff5a3a'})
def minibagel(c):
    # a little hamster curled into a bagel ring
    c.ell(24, 30, 15, 13, 'a')
    c.ell(29, 29, 4, 3, '.')                                                # the hole
    c.ell(13, 23, 4, 4, 'a'); c.ell(20, 17, 4, 4, 'a')                       # ears
    c.ell(18, 44, 3, 1, 'd'); c.ell(31, 44, 3, 1, 'd')
    c.outline()
    c.shadow('a', 'd')
    # pizza topping on top: sauce, cheese, pepperoni
    c.ell(30, 22, 8, 4, 'c'); c.ell(31, 21, 6, 3, 'y')
    for x, y in [(28, 21), (33, 22), (31, 19)]:
        c.ell(x, y, 1, 1, 'R')
    c.ell(16, 32, 6, 5, 'b')
    bigeye(c, 11, 26); bigeye(c, 19, 26)
    c.line(14, 34, 17, 34, 'k')
    blush(c, 8, 31); blush(c, 22, 31)


@sprite48('Pizzarolla', {'a': '#e0a050', 'd': '#a86a24', 'b': '#fff0c8', 'c': '#ff5a3a'})
def pizzarolla(c):
    # armadillo whose plates are pizza rolls
    c.ell(27, 30, 16, 12, 'a')
    for x, col in [(16, 'd'), (36, 'd'), (21, 'a'), (39, 'a')]:
        c.ell(x, 42, 4, 3, col)
    c.ell(11, 31, 8, 7, 'b')
    c.ell(16, 22, 3, 4, 'b')
    c.outline()
    c.shadow('a', 'd')
    for x in (19, 26, 33, 40):
        c.line(x, 19, x - 2, 41, 'd')
    # molten cheese bursting from the seams
    for x, y in [(20, 25), (27, 22), (34, 24), (41, 29), (26, 34)]:
        c.ell(x, y, 2, 1, 'y'); c.px(x, y + 2, 'y')
    soft_flame(c, 25, 18, 6, 0, 'w', 'w'); soft_flame(c, 35, 19, 6, 1, 'w', 'w')
    bigeye(c, 6, 27); bigeye(c, 13, 27, 3, 5)
    c.line(5, 26, 9, 26, 'k'); c.line(13, 26, 16, 26, 'k')
    c.line(5, 35, 11, 35, 'k')
    c.px(3, 32, 'k')
    blush(c, 15, 33)


# ---------------------------------------------------------------- Pumpsoakra / Hydrosoakra: orcas with water guns built in
@sprite48('Pumpsoakra', {'a': '#2a2f45', 'd': '#151a2a', 'b': '#ffffff', 'c': '#ffcf3a', 'e': '#3ae0ff'})
def pumpsoakra(c):
    c.poly([(34, 30), (46, 22), (44, 32), (46, 40), (36, 36)], 'a')      # tail
    c.ell(24, 31, 14, 11, 'a')
    c.ell(21, 36, 9, 6, 'b')
    c.poly([(24, 20), (28, 10), (31, 21)], 'a')                              # dorsal fin
    c.ell(14, 41, 4, 2, 'a')                                                 # flipper
    # pump grip under its chin + nozzle snout
    c.rect(2, 26, 10, 29, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.ell(18, 24, 4, 2, 'b')                                                 # eye patch
    bigeye(c, 16, 23, 3, 4); bigeye(c, 26, 24, 3, 4)
    c.line(11, 31, 15, 31, 'k')
    blush(c, 13, 28)
    c.rect(4, 27, 8, 28, 'd')
    for x in range(0, 3):
        c.px(x, 27, 'e')                                                     # squirt
    c.px(0, 24, 'e'); c.px(1, 31, 'e')


@sprite48('Hydrosoakra', {'a': '#262b40', 'd': '#12162a', 'b': '#ffffff', 'c': '#ffcf3a', 'e': '#3ae0ff'})
def hydrosoakra(c):
    c.poly([(38, 32), (47, 24), (46, 34), (47, 42), (40, 38)], 'a')
    c.ell(25, 32, 16, 12, 'a')
    c.ell(22, 37, 10, 6, 'b')
    # backpack water tank
    c.ell(30, 17, 9, 7, 'e')
    c.rect(26, 22, 34, 24, 'c')
    c.ell(13, 43, 5, 2, 'a'); c.ell(33, 43, 5, 2, 'a')
    c.rect(0, 25, 9, 29, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.line(24, 14, 34, 14, 'w'); c.ell(30, 19, 6, 3, 'q')
    c.ell(17, 24, 4, 2, 'b')
    bigeye(c, 15, 23, 3, 4); bigeye(c, 25, 23, 3, 4)
    c.line(14, 22, 18, 22, 'k'); c.line(24, 22, 28, 22, 'k')
    c.line(10, 31, 16, 31, 'k'); c.px(17, 30, 'k')
    for x, y in [(0, 23), (2, 21), (1, 31), (3, 33)]:
        c.px(x, y, 'e')


# ---------------------------------------------------------------- Slipslug / Slidemander: backyard slide creatures
@sprite48('Slipslug', {'a': '#ffe03a', 'd': '#d8a810', 'b': '#fff8c8', 'c': '#3ae0ff'})
def slipslug(c):
    # long flat slug body = the slide mat
    c.poly([(4, 42), (44, 42), (46, 38), (14, 30)], 'a')
    c.ell(13, 30, 9, 8, 'a')
    c.line(9, 23, 7, 16, 'a', 2); c.line(15, 23, 17, 16, 'a', 2)
    c.outline()
    c.shadow('a', 'd')
    # water stripe down the middle + puddle
    c.line(16, 38, 44, 39, 'c', 2)
    for x in range(4, 44, 5):
        c.px(x, 43, 'c')
    c.ell(7, 15, 2, 2, 'w'); c.ell(17, 15, 2, 2, 'w')
    c.rect(7, 15, 8, 16, 'k'); c.rect(17, 15, 18, 16, 'k')
    c.px(7, 15, 'w'); c.px(17, 15, 'w')
    c.line(10, 33, 15, 33, 'k'); c.px(9, 32, 'k'); c.px(16, 32, 'k')
    blush(c, 6, 31); blush(c, 18, 31)
    c.px(30, 34, 'w'); c.px(36, 36, 'w')                                     # splash


@sprite48('Slidemander', {'a': '#ffd21a', 'd': '#c89400', 'b': '#fff4b0', 'c': '#3ae0ff'})
def slidemander(c):
    # belly-sliding salamander, arms out, tail flicking up behind
    c.poly([(34, 36), (46, 28), (46, 33), (38, 40)], 'a')
    c.ell(24, 36, 15, 6, 'a')
    c.ell(9, 30, 8, 7, 'a')
    c.ell(14, 41, 3, 2, 'a'); c.ell(31, 41, 3, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    # spray wake
    for x, y in [(2, 40), (1, 37), (4, 43), (0, 34)]:
        c.px(x, y, 'c'); c.px(x + 1, y, 'c')
    c.line(12, 40, 40, 40, 'c')
    # scuffed knees (hits every rock)
    c.px(14, 41, 'R'); c.px(31, 41, 'R')
    for x, y in [(22, 33), (28, 33), (34, 34)]:
        c.px(x, y, 'f')
    bigeye(c, 5, 27, 3, 4); bigeye(c, 12, 27, 3, 4)
    c.line(4, 34, 10, 34, 'k'); c.px(3, 33, 'k'); c.px(11, 33, 'k')
    c.rect(5, 35, 9, 35, 'r')                                                 # "WHEEE" open grin
    blush(c, 14, 31)


# ---------------------------------------------------------------- Slurpeel: an eel coiled in a blue-raspberry slushie
@sprite48('Slurpeel', {'a': '#3a6cff', 'd': '#2244b0', 'b': '#c8f0ff', 'c': '#e8eef8', 'e': '#ff3f5f'})
def slurpeel(c):
    # the cup
    c.poly([(12, 46), (36, 46), (39, 24), (9, 24)], 'c')
    c.ell(24, 24, 15, 4, 'b')                                                 # dome of slush
    # eel coiling out of the slush
    c.line(28, 22, 32, 14, 'a', 4)
    c.ell(28, 11, 8, 7, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.line(14, 28, 34, 28, 'e'); c.line(15, 33, 33, 33, 'e')                  # cup stripes
    c.line(20, 22, 18, 14, 'e', 2); c.line(18, 14, 15, 13, 'e', 2)             # bendy straw
    for x, y in [(15, 22), (22, 21), (31, 23)]:
        c.px(x, y, 'w')
    bigeye(c, 23, 8, 3, 4); bigeye(c, 30, 8, 3, 4)
    c.line(25, 15, 28, 15, 'k')
    blush(c, 21, 13); blush(c, 33, 13)
    # brain-freeze shiver
    for x, y in [(38, 6), (40, 9), (38, 12)]:
        c.line(x, y, x + 2, y, 'k')
