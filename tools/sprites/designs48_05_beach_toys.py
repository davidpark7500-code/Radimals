"""Dex 45-60: boardwalk Water types and bedroom-toy Basics."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Bubbletapir / Bubblewrapir
@sprite48('Bubbletapir', {'a': '#ff9ac8', 'd': '#d8649a', 'b': '#ffe6f2', 'c': '#ff5aa8'})
def bubbletapir(c):
    c.ell(29, 34, 12, 8, 'a')
    c.ell(28, 37, 7, 4, 'b')
    for x in (21, 26, 33, 38):
        c.ell(x, 43, 2, 2, 'a')
    c.ell(18, 26, 10, 9, 'a')
    c.ell(13, 18, 3, 4, 'a')                                                  # ear
    c.ell(9, 31, 4, 3, 'a')                                                    # stubby trunk
    # giant bubblegum bubble out of the trunk
    c.ell(7, 17, 7, 7, 'c')
    c.outline()
    c.shadow('a', 'd')
    c.rect(4, 13, 5, 14, 'w'); c.px(6, 12, 'w')
    bigeye(c, 15, 22); bigeye(c, 23, 22, 3, 5)
    c.line(12, 33, 15, 34, 'k')
    blush(c, 18, 29)
    c.ring(13, 18, 1.5, 2, 1, 'd')


@sprite48('Bubblewrapir', {'a': '#c8e6ff', 'd': '#8ab4d8', 'b': '#ffffff', 'c': '#ff5aa8'})
def bubblewrapir(c):
    c.ell(29, 31, 16, 11, 'a')
    for x, col in [(18, 'd'), (38, 'd'), (22, 'a'), (41, 'a')]:
        c.ell(x, 42, 4, 3, col)
    c.ell(14, 24, 11, 10, 'a')
    c.ell(10, 15, 3, 4, 'a')
    c.ell(5, 30, 5, 4, 'a')
    c.outline()
    c.shadow('a', 'd')
    # bubble-wrap armor: grid of shiny bubbles, a few popped
    for y in range(24, 40, 4):
        for x in range(20 + (y // 4) % 2 * 2, 44, 4):
            if (x * 7 + y) % 11 == 0:
                c.px(x, y, 'd'); c.px(x + 1, y + 1, 'd')
            else:
                c.ring(x, y, 1.5, 1.5, 1, 'b'); c.px(x - 1, y - 1, 'w')
    bigeye(c, 9, 21); bigeye(c, 18, 21, 3, 5)
    c.line(8, 20, 12, 20, 'k'); c.line(18, 20, 21, 20, 'k')
    c.line(5, 33, 10, 34, 'k')
    blush(c, 14, 28)
    c.px(46, 20, 'k'); c.px(44, 18, 'k'); c.px(46, 16, 'k')                      # pop!


# ---------------------------------------------------------------- Goopopus: an octopus made of green goo
@sprite48('Goopopus', {'a': '#5ce65a', 'd': '#2ea82c', 'b': '#c8ffb8', 'c': '#2a8a2a'})
def goopopus(c):
    for x0, x1 in [(8, 4), (15, 13), (24, 24), (33, 35), (40, 44)]:
        c.line(x0, 30, x1, 42, 'a', 4)
        c.ell(x1 + 1, 44, 2.5, 1.5, 'a')
    c.ell(24, 22, 15, 14, 'a')
    c.outline()
    c.shadow('a', 'd')
    # drips + bubbles in the goo
    for x, y in [(12, 12), (33, 15), (28, 30), (17, 28)]:
        c.ring(x, y, 1.2, 1.2, 1, 'b')
    c.ell(20, 12, 4, 2, 'b')
    for x in (10, 22, 37):
        c.line(x, 35, x, 38, 'd')
    bigeye(c, 16, 19); bigeye(c, 28, 19)
    c.line(21, 27, 25, 28, 'k'); c.px(26, 27, 'k')
    blush(c, 13, 25); blush(c, 31, 25)


# ---------------------------------------------------------------- Dunktank / Dunkzilla: walruses with a target on the belly
@sprite48('Dunktank', {'a': '#8a6a5a', 'd': '#5e4438', 'b': '#e8d4c4', 'c': '#ff3f5f', 'e': '#9fd6ff'})
def dunktank(c):
    # water tank it sits in
    c.rect(6, 34, 42, 46, 'e')
    c.ell(24, 27, 13, 12, 'a')
    c.ell(13, 34, 3, 2, 'a'); c.ell(35, 34, 3, 2, 'a')                            # flippers on the rim
    c.outline()
    c.shadow('a', 'd')
    # target on its belly
    c.ring(24, 31, 5, 4, 1, 'c'); c.ell(24, 31, 1.5, 1.5, 'c')
    c.line(6, 37, 42, 37, 'w')
    for x in range(9, 42, 6):
        c.px(x, 40, 'w')
    c.ell(24, 22, 6, 3, 'b')
    c.rect(20, 24, 21, 28, 'w'); c.rect(27, 24, 28, 28, 'w')                       # tiny tusks
    bigeye(c, 16, 17); bigeye(c, 28, 17)
    c.rect(23, 20, 25, 21, 'k')
    blush(c, 12, 22); blush(c, 33, 22)


@sprite48('Dunkzilla', {'a': '#7a5a4a', 'd': '#4a3228', 'b': '#e4ccb8', 'c': '#ff3f5f', 'e': '#9fd6ff'})
def dunkzilla(c):
    c.ell(24, 30, 18, 15, 'a')
    c.ell(8, 44, 6, 2, 'a'); c.ell(40, 44, 6, 2, 'a')
    c.ell(4, 30, 4, 6, 'a'); c.ell(44, 30, 4, 6, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.ring(24, 35, 7, 6, 1, 'c'); c.ring(24, 35, 4, 3, 1, 'c'); c.ell(24, 35, 1.5, 1.5, 'c')
    c.ell(24, 22, 8, 4, 'b')
    c.rect(18, 24, 20, 32, 'w'); c.rect(28, 24, 30, 32, 'w')                         # big tusks
    bigeye(c, 13, 15); bigeye(c, 31, 15)
    c.line(12, 14, 17, 14, 'k'); c.line(31, 14, 36, 14, 'k')
    c.rect(23, 19, 25, 20, 'k')
    # big splash at its feet
    for x, y in [(1, 40), (3, 37), (45, 40), (43, 37), (12, 46), (36, 46)]:
        c.px(x, y, 'e'); c.px(x + 1, y - 1, 'e')


# ---------------------------------------------------------------- Brineape / Brinekong: sea-monkey shrimp, royal and angry
@sprite48('Brineape', {'a': '#ff9a7a', 'd': '#d8664a', 'b': '#ffe4d8', 'c': '#ffcf3a'})
def brineape(c):
    # curled shrimp tail
    for x, y, r in [(32, 34, 6), (37, 39, 5), (41, 43, 3)]:
        c.ell(x, y, r, r - 1, 'a')
    c.ell(22, 30, 10, 9, 'a')
    # little legs under
    for x in (17, 21, 25):
        c.line(x, 38, x - 1, 43, 'd', 1)
    c.ell(16, 21, 9, 8, 'a')
    c.ell(7, 20, 3, 3, 'a')                                                          # monkey ear
    # crown (advertised as royalty)
    c.poly([(11, 13), (12, 7), (15, 11), (17, 5), (19, 11), (22, 7), (22, 13)], 'c')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(30, 31), (35, 36), (39, 41)]:
        c.line(x - 2, y, x + 2, y, 'd')
    c.line(9, 16, 2, 6, 'k'); c.line(12, 15, 8, 4, 'k')                               # antennae
    c.ell(14, 24, 5, 3, 'b')
    bigeye(c, 11, 18); bigeye(c, 18, 18, 3, 5)
    c.line(10, 17, 14, 18, 'k'); c.line(18, 18, 21, 17, 'k')                           # angry shrimp
    c.line(12, 26, 16, 26, 'k')
    c.px(17, 11, 'r')


@sprite48('Brinekong', {'a': '#ff7a5a', 'd': '#c44a30', 'b': '#ffdccc', 'c': '#ffcf3a', 'e': '#8ae0ff'})
def brinekong(c):
    # plastic aquarium castle on its back
    c.rect(28, 8, 42, 22, 'e'); c.rect(28, 5, 31, 8, 'e'); c.rect(35, 5, 38, 8, 'e'); c.rect(40, 5, 42, 8, 'e')
    # gorilla-shrimp: huge arms, shrimp tail
    c.ell(42, 38, 5, 4, 'a')
    c.ell(26, 30, 14, 12, 'a')
    c.ell(9, 33, 6, 9, 'a'); c.ell(38, 33, 5, 8, 'a')
    c.ell(9, 43, 5, 3, 'd'); c.ell(36, 43, 5, 3, 'd')
    c.ell(20, 18, 9, 8, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.rect(32, 13, 34, 17, 'k'); c.rect(37, 13, 39, 16, 'k')                          # castle windows
    c.ell(25, 33, 8, 7, 'b')
    for y in (29, 33, 37):
        c.line(19, y, 31, y, 'd')
    c.line(14, 12, 8, 4, 'k'); c.line(18, 11, 16, 2, 'k')
    c.ell(18, 21, 6, 3, 'b')
    bigeye(c, 13, 15); bigeye(c, 22, 15, 3, 5)
    c.line(12, 14, 17, 15, 'k'); c.line(22, 15, 25, 14, 'k')
    c.line(14, 23, 20, 23, 'k')


# ---------------------------------------------------------------- Fishtankamari: a screensaver goldfish, slightly pixelated
@sprite48('Fishtankamari', {'a': '#ff8a2a', 'd': '#c85a10', 'b': '#ffe0b0', 'c': '#3ae0ff', 'e': '#8a93ab'})
def fishtankamari(c):
    # stepped (pixelated) fins: it's from a 1997 aquarium screensaver
    c.stamp(32, 14, ['aa......', 'aaaa....', 'aaaaaa..', 'aaaaaaaa'])
    c.stamp(36, 30, ['aaaaaaaa', 'aaaaaa..', 'aaaa....', 'aa......'])
    c.ell(22, 26, 15, 10, 'a')
    c.stamp(14, 35, ['aaaaaa', '.aaaa.', '..aa..'])
    c.outline()
    c.shadow('a', 'd')
    c.ell(18, 30, 9, 4, 'b')
    for x in (24, 29, 33):
        c.line(x, 19, x - 2, 32, 'd')
    bigeye(c, 10, 21); bigeye(c, 18, 21, 3, 5)
    c.ring(6, 28, 1.6, 1.6, 1, 'k')                                                     # "o" mouth
    blush(c, 12, 27)
    # bubbles + a tiny castle decoration
    for x, y in [(4, 18), (2, 12), (5, 7)]:
        c.ring(x, y, 1.2, 1.2, 1, 'c')
    c.rect(38, 41, 45, 46, 'e'); c.rect(38, 39, 39, 41, 'e'); c.rect(44, 39, 45, 41, 'e'); c.px(41, 44, 'k')


# ---------------------------------------------------------------- Hangryhippo: a purple hippo, mouth always open
@sprite48('Hangryhippo', {'a': '#9a6aff', 'd': '#6a3ed0', 'b': '#efe4ff', 'c': '#ff5a8a'})
def hangryhippo(c):
    c.ell(30, 32, 14, 11, 'a')
    for x in (22, 28, 35, 40):
        c.ell(x, 43, 3, 2, 'a')
    # huge open jaws
    c.ell(13, 19, 11, 7, 'a')
    c.ell(13, 33, 11, 5, 'a')
    c.ell(10, 9, 3, 2, 'a'); c.ell(20, 9, 3, 2, 'a')                                       # ears
    c.outline()
    c.shadow('a', 'd')
    c.rect(3, 24, 22, 29, 'c')
    c.rect(5, 23, 6, 24, 'w'); c.rect(18, 23, 19, 24, 'w'); c.rect(5, 29, 6, 30, 'w'); c.rect(18, 29, 19, 30, 'w')
    # marbles flying into its mouth
    for x, y, col in [(2, 18, 'q'), (5, 13, 'z'), (1, 35, 'y')]:
        c.ell(x, y, 1.2, 1.2, col); c.px(x, y - 1, 'w')
    bigeye(c, 11, 13, 3, 4); bigeye(c, 18, 13, 3, 4)
    c.line(10, 12, 14, 13, 'k'); c.line(18, 13, 21, 12, 'k')                                # hangry
    c.px(6, 19, 'k'); c.px(9, 19, 'k')                                                     # nostrils
    blush(c, 22, 17)


# ---------------------------------------------------------------- Snorkelot / Snorkelord: ocelots who do NOT do the deep end
@sprite48('Snorkelot', {'a': '#ffb24a', 'd': '#c87a1a', 'b': '#fff0d0', 'c': '#3ae0ff'})
def snorkelot(c):
    c.ell(30, 38, 4, 3, 'a'); c.ell(36, 35, 4, 3, 'a')                                      # curled tail
    c.ell(24, 35, 11, 8, 'a')
    c.ell(24, 38, 6, 5, 'b')
    c.ell(18, 44, 3, 2, 'b'); c.ell(29, 44, 3, 2, 'b')
    c.ell(22, 21, 12, 10, 'a')
    c.poly([(11, 15), (11, 5), (18, 12)], 'a'); c.poly([(27, 12), (34, 5), (33, 16)], 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(27, 32), (31, 35), (20, 30), (16, 34), (30, 18), (14, 18)]:
        c.ell(x, y, 1, 1, 'd')                                                               # spots
    # dive mask + short curved snorkel tube
    c.rect(11, 18, 31, 25, 'c'); c.rect(13, 19, 29, 24, 'q')
    c.line(32, 21, 37, 18, 'y', 2); c.line(37, 18, 37, 13, 'y', 2); c.line(37, 13, 35, 11, 'y', 2)
    bigeye(c, 15, 19); bigeye(c, 25, 19)
    c.line(19, 28, 23, 28, 'k')
    blush(c, 11, 27); blush(c, 29, 27)


@sprite48('Snorkelord', {'a': '#ffa030', 'd': '#b86a10', 'b': '#fff0d0', 'c': '#3ae0ff'})
def snorkelord(c):
    c.ell(25, 33, 14, 11, 'a')
    c.ell(24, 36, 8, 6, 'b')
    # swim fins
    c.poly([(10, 42), (20, 42), (22, 46), (6, 46)], 'c'); c.poly([(29, 42), (39, 42), (43, 46), (27, 46)], 'c')
    # arm floaties: scared of the deep end (the flaw)
    c.ell(9, 31, 5, 4, 'y'); c.ell(40, 31, 5, 4, 'y')
    c.ell(23, 17, 13, 11, 'a')
    c.poly([(11, 11), (12, 1), (18, 8)], 'a'); c.poly([(28, 8), (35, 1), (35, 12)], 'a')
    c.outline()
    c.shadow('a', 'd')
    for x, y in [(30, 29), (17, 30), (33, 36), (15, 37)]:
        c.ell(x, y, 1.2, 1.2, 'd')
    c.ring(9, 31, 5, 4, 1, 'f'); c.ring(40, 31, 5, 4, 1, 'f')
    # mask pushed up like a crown
    c.rect(14, 6, 32, 10, 'c'); c.rect(16, 7, 30, 9, 'q')
    bigeye(c, 15, 15); bigeye(c, 27, 15)
    c.line(14, 14, 19, 14, 'k'); c.line(27, 14, 32, 14, 'k')
    c.line(20, 24, 26, 24, 'k'); c.px(19, 23, 'k'); c.px(27, 23, 'k')
    blush(c, 11, 21); blush(c, 32, 21)


# ---------------------------------------------------------------- Yakkity: a yak calf with a tape recorder
@sprite48('Yakkity', {'a': '#a87a5a', 'd': '#6e4c34', 'b': '#e8d4c0', 'c': '#8a93ab', 'e': '#ff3f5f'})
def yakkity(c):
    # shaggy body
    c.ell(28, 33, 14, 10, 'a')
    for x in range(16, 42, 4):
        c.poly([(x, 40), (x + 4, 40), (x + 2, 45)], 'a')
    c.ell(16, 22, 11, 10, 'a')
    # horns, short and soft
    c.outline()
    c.shadow('a', 'd')
    for pts in ([(8, 15), (3, 12), (2, 6), (5, 8), (7, 12)], [(23, 14), (28, 11), (30, 5), (31, 10), (27, 15)]):
        c.poly(pts, 'e' if False else 'c')
    # handheld tape recorder slung on its chest, REC light on
    c.rect(22, 27, 34, 35, 'c'); c.ring(26, 31, 1.5, 1.5, 1, 'k'); c.ring(31, 31, 1.5, 1.5, 1, 'k')
    c.ell(33, 28, 1, 1, 'e')
    c.ell(11, 15, 6, 4, 'a')                                                                  # fringe over eyes
    for x in (8, 11, 14):
        c.line(x, 14, x, 18, 'd')
    bigeye(c, 10, 19, 3, 4); bigeye(c, 18, 19, 3, 4)
    c.ell(11, 27, 2, 1.5, 'k'); c.px(11, 28, 'r')                                             # talking
    blush(c, 7, 24); blush(c, 21, 24)
    for x, y in [(3, 24), (2, 27), (4, 30)]:
        c.px(x, y, 'k')


# ---------------------------------------------------------------- Sockpup / Puppetmaster: sock puppets that came alive
@sprite48('Sockpup', {'a': '#f4f4f0', 'd': '#c8c8c0', 'b': '#ff5a5a', 'c': '#3a6cff'})
def sockpup(c):
    # a sock: the foot is the head, the leg is the body
    c.rect(22, 22, 36, 44, 'a')
    c.ell(18, 21, 13, 9, 'a')
    c.outline()
    c.shadow('a', 'd')
    # stripes on the cuff + heel
    c.line(22, 40, 36, 40, 'b', 2); c.line(22, 36, 36, 36, 'c', 2)
    c.ell(34, 28, 3, 3, 'd')
    # mouth fold
    c.line(6, 24, 22, 26, 'k'); c.px(5, 23, 'k')
    c.rect(9, 25, 15, 26, 'b')                                                                  # felt tongue
    # mismatched button eyes
    c.ell(14, 17, 2.5, 2.5, 'c'); c.px(13, 16, 'w'); c.px(15, 18, 'w')
    c.ell(23, 16, 2, 2, 'b'); c.px(23, 16, 'k')
    # floppy felt ears
    c.ell(28, 13, 3, 4, 'b')
    blush(c, 18, 21)


@sprite48('Puppetmaster', {'a': '#e8e8e0', 'd': '#b4b4aa', 'b': '#a04cff', 'c': '#ffcf3a'})
def puppetmaster(c):
    # holds its own control bar (pulls its own strings)
    c.rect(8, 3, 40, 5, 'c')
    c.rect(22, 22, 36, 44, 'a')
    c.ell(20, 19, 13, 9, 'a')
    c.ell(39, 28, 3, 6, 'a')                                                                    # arm up to the bar
    c.outline()
    c.shadow('a', 'd')
    for x0, x1 in [(10, 14), (24, 24), (38, 34)]:
        c.line(x0, 6, x1, 13, 'k')
    c.line(40, 6, 40, 22, 'k')
    c.line(22, 40, 36, 40, 'b', 2); c.line(22, 36, 36, 36, 'c', 2)
    c.line(8, 22, 24, 24, 'k'); c.px(7, 21, 'k')
    c.rect(11, 23, 17, 24, 'b')
    # top hat and monocle button
    c.rect(14, 6, 24, 11, 'k'); c.rect(12, 11, 26, 12, 'k'); c.line(14, 10, 24, 10, 'b')
    c.ell(16, 16, 2.5, 2.5, 'c'); c.px(15, 15, 'w'); c.ring(16, 16, 3.5, 3.5, 1, 'k')
    c.ell(25, 15, 2, 2, 'b'); c.px(25, 15, 'k')
    c.line(17, 20, 20, 21, 'k')


# ---------------------------------------------------------------- Hamsterjam / Hamsterrave: dancing hamsters
@sprite48('Hamsterjam', {'a': '#f2c08a', 'd': '#c88a50', 'b': '#fff4e4', 'c': '#ff3fa4'})
def hamsterjam(c):
    # mid-dance: one foot up, arms out
    c.ell(24, 30, 12, 12, 'a')
    c.ell(24, 33, 8, 8, 'b')
    c.ell(16, 44, 3, 2, 'a'); c.ell(33, 40, 3, 2, 'a')
    c.ell(10, 26, 3, 3, 'a'); c.ell(38, 22, 3, 3, 'a')
    c.ell(15, 17, 4, 4, 'a'); c.ell(33, 17, 4, 4, 'a')
    c.outline()
    c.shadow('a', 'd')
    # headphones
    c.line(14, 15, 34, 15, 'k'); c.ell(12, 22, 2, 3, 'c'); c.ell(36, 22, 2, 3, 'c')
    bigeye(c, 17, 22); bigeye(c, 27, 22)
    c.ell(24, 28, 1.5, 1, 'k')
    c.rect(23, 30, 25, 31, 'w')                                                                   # buck teeth
    blush(c, 14, 27); blush(c, 31, 27)
    # music notes
    for x, y in [(4, 12), (42, 8)]:
        c.rect(x, y, x + 1, y + 1, 'k'); c.line(x + 1, y - 4, x + 1, y, 'k'); c.px(x + 2, y - 4, 'k')


@sprite48('Hamsterrave', {'a': '#e8a060', 'd': '#b86a30', 'b': '#fff0dc', 'c': '#b6ff3b'})
def hamsterrave(c):
    c.ell(24, 30, 15, 14, 'a')
    c.ell(24, 34, 10, 9, 'b')
    c.ell(14, 44, 4, 2, 'a'); c.ell(34, 44, 4, 2, 'a')
    c.ell(7, 20, 4, 4, 'a'); c.ell(41, 20, 4, 4, 'a')                                               # arms up
    c.ell(13, 14, 4, 4, 'a'); c.ell(35, 14, 4, 4, 'a')
    c.outline()
    c.shadow('a', 'd')
    # glow sticks in both fists (short, chunky, glowing)
    c.line(5, 16, 3, 10, 'c', 2); c.line(43, 16, 45, 10, 'm', 2)
    for x, y in [(1, 9), (46, 9)]:
        c.px(x, y, 'w')
    # rave shades
    c.rect(14, 20, 34, 24, 'k'); c.px(16, 21, 'm'); c.px(28, 21, 'q')
    c.ell(24, 28, 2, 1.5, 'k')
    c.rect(23, 30, 25, 31, 'w')
    blush(c, 12, 26); blush(c, 33, 26)
    # beaded bracelets
    for x in (8, 40):
        c.px(x - 1, 23, 'm'); c.px(x, 23, 'y'); c.px(x + 1, 23, 'q')
