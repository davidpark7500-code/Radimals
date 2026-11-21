"""Early routes: what players meet in the first 30 minutes (plus their evolutions)."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ---------------------------------------------------------------- Milkwog: a pollywog-frog that IS a milk cap
@sprite48('Milkwog', {'a': '#ffd86a', 'd': '#e0a83a', 'b': '#fff6d6', 'c': '#ff5aa8'})
def milkwog(c):
    # little tadpole tail swish
    c.poly([(34, 34), (44, 28), (46, 33), (40, 38)], 'a')
    # body: one fat round cap, seen 3/4
    c.ell(24, 32, 14, 11, 'a')
    c.ell(24, 31, 11, 8, 'b')
    # frog eye bumps on top
    c.ell(16, 20, 5, 5, 'a'); c.ell(29, 20, 5, 5, 'a')
    # stubby front feet
    c.ell(15, 43, 3, 2, 'a'); c.ell(30, 43, 3, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    # printed cap art: a pink swirl, the bit kids traded for
    c.ring(24, 33, 5, 4, 1, 'c'); c.rect(23, 32, 25, 33, 'c'); c.px(26, 31, 'c')
    c.ring(24, 31, 11, 8, 1, 'd')
    bigeye(c, 14, 18); bigeye(c, 27, 18)
    c.line(20, 26, 23, 27, 'k'); c.line(23, 27, 26, 26, 'k')
    blush(c, 11, 25); blush(c, 33, 25)


@sprite48('Slammerog', {'a': '#9aa3b5', 'd': '#5d6578', 'b': '#e6ebf3', 'c': '#ff3f5f'})
def slammerog(c):
    # heavy toad body
    c.ell(26, 34, 16, 11, 'a')
    # back is a thick steel slammer disc, worn like a shell
    c.ell(30, 27, 13, 8, 'd')
    c.ell(30, 26, 11, 6, 'a')
    # big strong legs
    c.ell(13, 41, 5, 4, 'a'); c.ell(38, 42, 6, 4, 'a')
    c.rect(8, 44, 18, 46, 'b'); c.rect(33, 44, 44, 46, 'b')
    # head
    c.ell(13, 30, 10, 8, 'a')
    c.ell(9, 22, 4, 4, 'a'); c.ell(18, 21, 4, 4, 'a')
    c.outline()
    c.shadow('a', 'd')
    # slammer face: red flame print + rivets
    c.poly([(26, 26), (34, 22), (32, 26), (37, 25), (30, 30)], 'c')
    for x, y in [(21, 25), (39, 25), (30, 21), (30, 31)]:
        c.px(x, y, 'w')
    c.ell(13, 36, 7, 3, 'b')
    bigeye(c, 7, 20, 4, 4); bigeye(c, 16, 19, 4, 4)
    c.line(5, 19, 10, 19, 'k'); c.line(15, 18, 20, 18, 'k')
    c.line(5, 32, 13, 32, 'k'); c.px(14, 31, 'k')        # smug wide mouth
    blush(c, 18, 28)


# ---------------------------------------------------------------- Slapbrace: neon inchworm curled like a bracelet
@sprite48('Slapbrace', {'a': '#2ee6c8', 'd': '#159c88', 'b': '#e8fff9', 'c': '#ff3fa4'})
def slapbrace(c):
    # body curled into a C (the bracelet), thick segments
    c.ring(26, 30, 15, 13, 7, 'a')
    c.clear(6, 30, 18, 46)
    c.rect(11, 25, 18, 33, 'a')
    # head on the open end
    c.ell(13, 34, 9, 8, 'a')
    # tiny feet under the segments
    for x in (24, 31, 37):
        c.ell(x, 44, 2, 1, 'd')
    c.outline()
    c.shadow('a', 'd')
    # neon zebra print stripes across the band
    for x0, y0, x1, y1 in [(20, 17, 22, 23), (28, 16, 29, 22), (35, 18, 33, 24), (40, 25, 35, 27), (40, 33, 35, 32), (36, 39, 32, 36), (28, 42, 27, 37)]:
        c.line(x0, y0, x1, y1, 'c', 2)
    c.ell(13, 37, 5, 3, 'b')
    bigeye(c, 8, 30); bigeye(c, 16, 30)
    c.line(11, 38, 14, 38, 'k')
    blush(c, 5, 36); blush(c, 19, 36)
    # antenna nubs
    c.px(9, 25, 'k'); c.px(8, 24, 'c'); c.px(16, 25, 'k'); c.px(17, 24, 'c')


@sprite48('Snapviper', {'a': '#28d6b8', 'd': '#127a6c', 'b': '#e8fff9', 'c': '#ff3fa4'})
def snapviper(c):
    # coiled tail base
    c.ell(30, 40, 14, 5, 'a')
    c.ell(32, 35, 10, 4, 'a')
    # upright body
    c.poly([(17, 38), (27, 38), (25, 18), (19, 18)], 'a')
    # hood: a slap bracelet snapped open behind the head
    c.ell(22, 15, 12, 9, 'd')
    c.ell(22, 15, 10, 7, 'a')
    # head
    c.ell(19, 15, 7, 6, 'a')
    c.outline()
    c.shadow('a', 'd')
    # hood print
    for x0, y0, x1, y1 in [(13, 9, 15, 13), (29, 9, 27, 13), (12, 17, 14, 20), (31, 17, 29, 20)]:
        c.line(x0, y0, x1, y1, 'c', 2)
    # belly scales + bug legs (it's still a bug)
    c.rect(20, 24, 23, 37, 'b')
    for y in (26, 30, 34):
        c.line(20, y, 23, y, 'd')
        c.px(16, y, 'k'); c.px(27, y, 'k')
    bigeye(c, 14, 13); bigeye(c, 21, 13)
    c.line(13, 12, 17, 12, 'k'); c.line(21, 12, 25, 12, 'k')
    c.line(15, 19, 21, 19, 'k'); c.px(14, 18, 'k')
    c.px(13, 20, 'r'); c.px(12, 21, 'r'); c.px(14, 21, 'r')   # flicked tongue
    blush(c, 11, 17)


# ---------------------------------------------------------------- Beanbuddy: a floppy bean-bag bear with its tag
@sprite48('Beanbuddy', {'a': '#c08a5a', 'd': '#8e5f38', 'b': '#f2d6b4', 'c': '#ff3f5f'})
def beanbuddy(c):
    # floppy sitting bean bag body
    c.ell(25, 36, 11, 9, 'a')
    c.ell(25, 38, 7, 6, 'b')
    # legs splayed forward (sits on any shelf)
    c.ell(16, 43, 5, 3, 'a'); c.ell(34, 43, 5, 3, 'a')
    c.ell(14, 44, 2, 2, 'b'); c.ell(36, 44, 2, 2, 'b')
    # arms floppy
    c.ell(13, 34, 3, 4, 'a'); c.ell(37, 34, 3, 4, 'a')
    # big head
    c.ell(24, 20, 13, 11, 'a')
    c.ell(13, 10, 4, 4, 'a'); c.ell(35, 10, 4, 4, 'a')
    c.ell(13, 10, 2, 2, 'b'); c.ell(35, 10, 2, 2, 'b')
    c.ell(20, 25, 6, 4, 'b')
    c.outline()
    c.shadow('a', 'd')
    # THE TAG: a red heart tag hanging off the ear (keep it on!)
    c.rect(39, 11, 39, 14, 'k')
    c.poly([(36, 15), (42, 15), (42, 20), (39, 22), (36, 20)], 'c')
    c.px(38, 17, 'w'); c.px(40, 17, 'w')
    # face
    bigeye(c, 15, 18); bigeye(c, 27, 18)
    c.rect(18, 23, 20, 24, 'k')
    c.line(19, 25, 19, 26, 'k'); c.line(17, 27, 19, 26, 'k'); c.line(19, 26, 21, 27, 'k')
    blush(c, 12, 24); blush(c, 30, 24)
    # stitch seam down the belly
    for y in range(32, 44, 2):
        c.px(25, y, 'd')


# ---------------------------------------------------------------- Fuzzbeak: an owlet with a speaker belly and a useless switch
@sprite48('Fuzzbeak', {'a': '#9b6cff', 'd': '#6a3ed0', 'b': '#efe4ff', 'c': '#ffb02e'})
def fuzzbeak(c):
    # round fluffy body = head + body in one
    c.ell(24, 28, 15, 15, 'a')
    # tufts (short, soft)
    c.ell(12, 13, 4, 5, 'a'); c.ell(35, 13, 4, 5, 'a')
    # wings
    c.ell(9, 31, 4, 7, 'd'); c.ell(39, 31, 4, 7, 'd')
    # feet
    c.ell(18, 44, 3, 1, 'c'); c.ell(29, 44, 3, 1, 'c')
    c.outline()
    c.shadow('a', 'd')
    # face disc
    c.ell(18, 23, 7, 6, 'b'); c.ell(30, 23, 7, 6, 'b')
    # speaker grille belly (it talks. always.)
    c.ell(24, 36, 7, 5, 'b')
    for y in (33, 35, 37, 39):
        c.line(20, y, 28, y, 'd')
    bigeye(c, 15, 20); bigeye(c, 28, 20)
    c.poly([(22, 26), (26, 26), (24, 30)], 'c')
    blush(c, 12, 27); blush(c, 33, 27)
    # tiny on/off switch on the side, stuck ON
    c.rect(40, 22, 42, 25, 'k'); c.rect(41, 22, 41, 23, 'z')
    # "hello" sound marks at 3 AM
    c.px(4, 14, 'k'); c.px(3, 16, 'k'); c.px(5, 12, 'k')


# ---------------------------------------------------------------- Pagerpup / Beeperhound: dogs with a pager built in
@sprite48('Pagerpup', {'a': '#56606f', 'd': '#353c48', 'b': '#c9d2dd', 'c': '#b6ff3b'})
def pagerpup(c):
    # stubby antenna tail
    c.rect(38, 24, 40, 31, 'a'); c.ell(39, 23, 2, 2, 'c')
    # body: a little rectangular pager-bodied pup, softened
    c.ell(29, 35, 10, 7, 'a')
    # legs
    for x in (21, 27, 33, 37):
        c.ell(x, 43, 2, 2, 'a')
    # big head
    c.ell(16, 24, 12, 11, 'a')
    # floppy ears
    c.ell(7, 20, 4, 7, 'd'); c.ell(25, 16, 4, 6, 'd')
    c.ell(9, 30, 5, 4, 'b')
    c.outline()
    c.shadow('a', 'd')
    # LCD on its side reading 143
    c.rect(24, 31, 36, 37, 'k'); c.rect(25, 32, 35, 36, 'c')
    for x0 in (26, 29, 33):
        pass
    c.line(26, 32, 26, 36, 'k')                                  # 1
    c.line(28, 32, 28, 34, 'k'); c.line(28, 34, 30, 34, 'k'); c.line(30, 32, 30, 36, 'k')   # 4
    c.line(32, 32, 34, 32, 'k'); c.line(33, 34, 34, 34, 'k'); c.line(32, 36, 34, 36, 'k'); c.line(34, 32, 34, 36, 'k')  # 3
    bigeye(c, 10, 21); bigeye(c, 20, 21)
    c.rect(4, 28, 5, 29, 'k')
    c.line(7, 33, 10, 33, 'k'); c.px(6, 32, 'k')
    c.px(8, 34, 'r'); c.px(9, 34, 'r'); c.px(8, 35, 'r')
    blush(c, 13, 28)
    # beep marks
    c.px(41, 18, 'c'); c.px(43, 17, 'c'); c.px(44, 20, 'c')


@sprite48('Beeperhound', {'a': '#4a5262', 'd': '#2a303c', 'b': '#c9d2dd', 'c': '#b6ff3b'})
def beeperhound(c):
    # tall lean hound standing proud
    c.rect(39, 18, 41, 28, 'a'); c.ell(40, 16, 2, 2, 'c')     # antenna tail
    c.ell(29, 30, 12, 8, 'a')
    c.ell(25, 33, 7, 5, 'b')
    for x, col in [(19, 'd'), (35, 'd'), (23, 'a'), (38, 'a')]:
        c.rect(x - 2, 35, x + 1, 44, col)
        c.rect(x - 3, 43, x + 2, 45, 'b')
    # long head forward
    c.ell(15, 19, 10, 8, 'a')
    c.ell(5, 23, 6, 4, 'a')
    c.ell(18, 12, 4, 8, 'd')                                     # long ear
    c.outline()
    c.shadow('a', 'd')
    # belt-clip collar with the screen
    c.rect(22, 22, 32, 26, 'k'); c.rect(23, 23, 31, 25, 'c')
    c.line(24, 24, 30, 24, 'k')
    c.rect(0, 22, 1, 23, 'k')
    bigeye(c, 9, 16); bigeye(c, 17, 16, 3, 5)
    c.line(8, 15, 12, 15, 'k'); c.line(17, 15, 20, 15, 'k')
    c.line(2, 27, 8, 27, 'k')
    blush(c, 11, 22)
    # vibrating lines
    for x, y in [(44, 26), (45, 29), (44, 32)]:
        c.line(x, y, x + 2, y, 'k')


# ---------------------------------------------------------------- Y2Kroach: a roach with the blinking 12:00 on its back
@sprite48('Y2Kroach', {'a': '#a0603a', 'd': '#6a3a20', 'b': '#e8c29a', 'c': '#ff3f5f'})
def y2kroach(c):
    # legs first (6, chunky)
    for x0, y0, x1, y1 in [(14, 34, 9, 43), (22, 36, 20, 45), (31, 36, 33, 45), (38, 34, 43, 42), (12, 30, 6, 33), (40, 29, 46, 31)]:
        c.line(x0, y0, x1, y1, 'd', 2)
    # shell body
    c.ell(27, 30, 15, 9, 'a')
    # head
    c.ell(13, 26, 8, 7, 'a')
    # antennae (thick, curled at the tips)
    c.line(8, 20, 3, 8, 'd', 2); c.ell(3, 7, 2, 2, 'd')
    c.line(15, 19, 17, 6, 'd', 2); c.ell(17, 5, 2, 2, 'd')
    c.outline()
    c.shadow('a', 'd')
    # digital clock on the shell: 12:00
    c.rect(22, 24, 38, 31, 'k')
    c.line(24, 26, 24, 29, 'c')                                     # 1
    c.line(26, 26, 28, 26, 'c'); c.line(28, 26, 28, 27, 'c'); c.line(26, 28, 28, 27, 'c'); c.line(26, 29, 28, 29, 'c')   # 2
    c.px(30, 26, 'c'); c.px(30, 28, 'c')
    c.ring(33, 27, 1, 1.6, 1, 'c'); c.ring(36, 27, 1, 1.6, 1, 'c')
    c.ell(12, 30, 4, 2, 'b')
    bigeye(c, 7, 23); bigeye(c, 14, 23, 3, 5)
    c.line(9, 30, 12, 30, 'k'); c.px(13, 29, 'k')
    blush(c, 5, 28)


# ---------------------------------------------------------------- Grungehog: a hedgehog in flannel with a messy quill fringe
@sprite48('Grungehog', {'a': '#c2402e', 'd': '#7c2418', 'b': '#f2dcc0', 'c': '#3a2c24'})
def grungehog(c):
    # messy quills (dark, soft points)
    c.poly([(8, 22), (12, 8), (16, 16), (20, 4), (25, 13), (30, 5), (33, 15), (39, 9), (38, 20), (44, 18), (40, 30), (12, 30)], 'c')
    # round body in flannel
    c.ell(27, 32, 14, 11, 'a')
    c.ell(15, 26, 10, 9, 'b')                                        # face
    c.ell(18, 44, 3, 2, 'c'); c.ell(32, 44, 3, 2, 'c')
    c.outline()
    c.shadow('a', 'd')
    # flannel plaid
    for x in range(20, 42, 5):
        c.line(x, 23, x, 42, 'd')
    for y in range(26, 43, 5):
        c.line(16, y, 40, y, 'd')
    for x in range(22, 42, 5):
        for y in range(28, 42, 5):
            c.px(x, y, 'y')
    # quill fringe over one eye (refuses to comb it)
    c.poly([(12, 16), (22, 17), (17, 24)], 'c')
    bigeye(c, 9, 23); bigeye(c, 19, 24, 3, 4)
    c.rect(5, 29, 6, 30, 'k')
    c.line(9, 31, 13, 31, 'k')
    blush(c, 11, 28)


# ---------------------------------------------------------------- Frostedtip: a blue-jay chick with bleached spiky tips
@sprite48('Frostedtip', {'a': '#3a8cff', 'd': '#2058c0', 'b': '#e6f2ff', 'c': '#fff6a8'})
def frostedtip(c):
    # spiky gelled crest, tips bleached
    c.poly([(12, 16), (10, 4), (16, 11), (18, 1), (22, 10), (27, 2), (28, 12), (34, 8), (31, 17)], 'a')
    # round body
    c.ell(24, 30, 13, 13, 'a')
    c.ell(21, 34, 8, 8, 'b')
    # wing doing a "whatever" gesture
    c.ell(35, 30, 5, 8, 'd')
    # tail
    c.poly([(36, 38), (46, 40), (44, 44), (34, 42)], 'd')
    c.ell(19, 44, 3, 1, 'y'); c.ell(28, 44, 3, 1, 'y')
    c.outline()
    c.shadow('a', 'd')
    # bleached tips
    for x, y in [(10, 4), (11, 5), (18, 1), (18, 2), (27, 2), (27, 3), (34, 8), (33, 9)]:
        c.px(x, y, 'c')
    # beak + face
    c.poly([(6, 25), (12, 23), (12, 28)], 'y')
    bigeye(c, 13, 20); bigeye(c, 23, 20)
    c.line(12, 19, 16, 18, 'k')                                       # one raised brow: cool
    blush(c, 11, 27); blush(c, 25, 27)
    # puka-shell necklace
    for x in range(14, 30, 3):
        c.px(x, 33 + (1 if 18 < x < 26 else 0), 'w')


# ---------------------------------------------------------------- Boppurr: a cat with a twist-knob tail and a big button
@sprite48('Boppurr', {'a': '#8a5cff', 'd': '#5a34c4', 'b': '#efe6ff', 'c': '#ffd23a'})
def boppurr(c):
    # tail ends in a twist knob
    c.ell(40, 37, 5, 3, 'a'); c.ell(44, 33, 3, 3, 'a')
    c.ell(44, 28, 4, 4, 'c'); c.line(42, 28, 46, 28, 'd')            # round twist knob, curled low
    # body sitting
    c.ell(26, 36, 11, 8, 'a')
    c.ell(25, 39, 6, 5, 'b')
    c.ell(18, 44, 3, 2, 'b'); c.ell(31, 44, 3, 2, 'b')
    # paw up: yelling an instruction
    c.ell(13, 30, 3, 3, 'a')
    # head
    c.ell(22, 21, 12, 10, 'a')
    # pull-handle ears
    c.poly([(11, 15), (10, 3), (19, 11)], 'a'); c.poly([(26, 11), (33, 2), (34, 15)], 'a')
    c.outline()
    c.shadow('a', 'd')
    # THE BUTTON on its forehead
    c.ell(22, 13, 3, 2, 'c'); c.px(21, 12, 'w')
    # stripes
    c.rect(29, 31, 33, 34, 'c'); c.rect(30, 32, 32, 33, 'd')        # pull-handle on its side
    bigeye(c, 14, 19); bigeye(c, 25, 19)
    c.ell(20, 26, 2, 2, 'k'); c.px(20, 27, 'r')                         # yelling "o"
    for x, y in [(3, 20), (2, 23), (4, 17)]:
        c.px(x, y, 'k')
