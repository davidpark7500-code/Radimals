"""Starter lines (fire / water / grass)."""
from kit48 import sprite48, bigeye, blush, soft_flame, coil, plug  # noqa: F401


# ================================================================ FIRE
@sprite48('Dialupine', {'a': '#ff6a2e', 'd': '#c8461f', 'b': '#ffe6bf', 'c': '#33384a', 'e': '#8a93ab'})
def dialupine(c):
    # small round body, stubby legs
    c.ell(25, 37, 9, 7, 'a')
    c.ell(18, 43, 3, 2, 'b'); c.ell(26, 44, 3, 2, 'b'); c.ell(33, 43, 3, 2, 'b')
    c.ell(24, 39, 5, 4, 'b')
    # BIG head (half the sprite)
    c.ell(21, 21, 13, 12, 'a')
    # big soft ears
    c.poly([(9, 15), (7, 2), (17, 10)], 'a')
    c.poly([(26, 10), (33, 0), (34, 14)], 'a')
    c.poly([(10, 12), (9, 5), (15, 10)], 'b')
    # flame cowlick: three soft curls
    soft_flame(c, 18, 11, 10, -1); soft_flame(c, 23, 10, 12, 1); soft_flame(c, 13, 12, 7, -1)
    # muzzle bump
    c.ell(11, 27, 5, 4, 'b')
    c.outline()
    c.shadow('a', 'd')
    # face: eyes LOW and WIDE, tiny screaming "o" mouth, blush
    bigeye(c, 11, 19); bigeye(c, 24, 19)
    c.rect(7, 25, 8, 26, 'k')                      # little nose
    c.ell(12, 29, 1.2, 1.2, 'k'); c.px(12, 30, 'r')  # tiny screech
    blush(c, 9, 25); blush(c, 27, 25)
    # coiled cord tail trailing along the ground, plug resting at the end
    coil(c, [(35, 40), (38, 41), (41, 41), (44, 40)])
    plug(c, 42, 34)
    c.line(44, 38, 44, 38, 'c')
    # status LEDs as freckles on the shoulder
    for x, y in [(28, 33), (31, 34), (34, 36)]:
        c.px(x, y, 'z')
    # screech lines
    c.line(1, 27, 3, 27, 'k'); c.line(1, 31, 3, 30, 'k'); c.line(2, 24, 3, 25, 'k')


@sprite48('Modemauler', {'a': '#f2512a', 'd': '#a8301a', 'b': '#ffdcae', 'c': '#33384a', 'e': '#8a93ab'})
def modemauler(c):
    # chunky stump legs (stands up as a figure)
    for x, y, col in [(36, 41, 'd'), (21, 41, 'd'), (16, 42, 'a'), (41, 41, 'a')]:
        c.ell(x, y, 4, 4, col)
    c.rect(11, 44, 21, 46, 'b'); c.rect(36, 44, 46, 46, 'b')
    # long low prowling body
    c.ell(29, 33, 14, 8, 'a')
    c.ell(25, 37, 9, 4, 'b')
    # soft flame mane along the spine
    for x, y, h, ln in [(19, 27, 9, 0), (24, 26, 11, 1), (29, 26, 11, 1), (34, 26, 10, 1), (39, 28, 7, 1)]:
        soft_flame(c, x, y, h, ln)
    # big head, ears up
    c.ell(13, 24, 10, 9, 'a')
    c.poly([(7, 18), (6, 5), (15, 14)], 'a'); c.poly([(8, 15), (8, 8), (12, 14)], 'b')
    c.poly([(16, 16), (22, 6), (23, 18)], 'd')
    soft_flame(c, 12, 16, 8, -1)
    c.ell(5, 28, 5, 3.5, 'b')
    c.outline()
    c.shadow('a', 'd')
    # face: confident not mean; one goofy fang
    bigeye(c, 8, 21); bigeye(c, 16, 21, 3, 5)
    c.line(7, 20, 11, 20, 'k'); c.line(16, 20, 19, 20, 'k')
    c.rect(0, 26, 1, 27, 'k')
    c.line(3, 31, 9, 31, 'k'); c.px(2, 30, 'k'); c.px(10, 30, 'k')
    c.rect(5, 32, 5, 33, 'w')
    c.rect(11, 28, 13, 28, 'm')
    # coiled cord tail: a loose spiral sweeping back and down to the plug on the ground
    coil(c, [(42, 31), (44, 34), (45, 37), (44, 40)])
    plug(c, 42, 43)
    # LED strip on the flank (line signature, grown up)
    c.rect(26, 33, 39, 34, 'k')
    for i, col in enumerate('zzgzyz'):
        c.px(27 + i * 2, 33, col)


# ================================================================ WATER
@sprite48('Floppuss', {'a': '#3e86ff', 'd': '#2758c4', 'b': '#bfe6ff', 'c': '#2a2a38', 'e': '#d3d8e0'})
def floppuss(c):
    # flat paddle tail
    c.ell(39, 38, 7, 4, 'd')
    # one chubby egg: head+body (plush-shaped)
    c.ell(25, 30, 13, 14, 'a')
    c.ell(25, 36, 9, 7, 'b')
    # stubby flippers and webbed feet
    c.ell(13, 34, 3, 2, 'a'); c.ell(36, 32, 2, 3, 'a')
    c.ell(19, 44, 4, 2, 'c'); c.ell(31, 44, 4, 2, 'c')
    # FLOPPY BILL: a soft square pillow, corner bent (the flaw: "do not bend")
    c.rect(1, 22, 15, 34, 'c')
    c.clear(1, 22, 2, 23)
    c.outline()
    c.shadow('a', 'd')
    c.rect(5, 22, 11, 26, 'e'); c.rect(8, 23, 9, 25, 'c')       # shutter + window
    c.rect(4, 29, 13, 33, 'w'); c.line(5, 30, 12, 30, 'b')        # label
    c.px(3, 24, 'e'); c.px(2, 24, '#')                            # bent corner
    # face: big low eyes, smug little smile, blush
    bigeye(c, 17, 23); bigeye(c, 27, 23)
    c.line(21, 31, 24, 31, 'k'); c.px(25, 30, 'k')
    blush(c, 16, 29); blush(c, 31, 29)
    # bubbles
    c.ell(42, 12, 2, 2, 'q'); c.px(41, 11, 'w'); c.ell(45, 6, 1, 1, 'q')


@sprite48('CDRompuss', {'a': '#2f72f0', 'd': '#1d47a8', 'b': '#b0dcff', 'c': '#2a2a38', 'e': '#d3d8e0'})
def cdrompuss(c):
    # CD tail worn like a shield
    c.ell(35, 27, 12, 12, 'e')
    # chunky standing body, chest out, fists on hips
    c.ell(23, 33, 12, 11, 'a')
    c.ell(22, 36, 8, 7, 'b')
    c.ell(11, 34, 3, 3, 'a'); c.ell(35, 34, 3, 3, 'a')
    c.ell(17, 42, 4, 3, 'a'); c.ell(29, 42, 4, 3, 'a')
    c.ell(17, 45, 5, 1.5, 'c'); c.ell(30, 45, 5, 1.5, 'c')
    # head
    c.ell(22, 18, 11, 9, 'a')
    # CD-drive bill growing out of the face, tray slid out
    c.rect(3, 17, 15, 23, 'c'); c.rect(1, 23, 13, 27, 'e')
    c.outline()
    c.shadow('a', 'd')
    c.ell(7, 25, 4, 1.5, 'w'); c.px(7, 25, 'e'); c.px(5, 24, 'm'); c.px(9, 26, 'q')
    c.rect(5, 19, 7, 20, 'z'); c.rect(12, 19, 14, 20, 'e')
    # shades pushed up on top of its head
    c.rect(16, 9, 21, 11, 'k'); c.rect(24, 9, 29, 11, 'k'); c.line(21, 10, 24, 10, 'k')
    c.rect(17, 9, 18, 9, 'q'); c.rect(25, 9, 26, 9, 'q')
    # face
    bigeye(c, 17, 14); bigeye(c, 26, 14)
    c.line(20, 22, 24, 22, 'k'); c.px(25, 21, 'k')
    c.rect(14, 20, 16, 20, 'm'); c.rect(30, 20, 32, 20, 'm')
    # rainbow sheen + hub
    for (x, y), col in zip([(41, 18), (44, 22), (45, 27), (44, 32), (41, 36)], 'myqgy'):
        c.px(x, y, col); c.px(x - 1, y, col)
    c.ell(40, 27, 2, 2, 'w'); c.px(40, 27, 'k')


# ================================================================ GRASS
@sprite48('Trollsprout', {'a': '#ffbf94', 'd': '#d88a62', 'b': '#fff0de', 'c': '#ff3fa4'})
def trollsprout(c):
    # HAIR: tall soft leaf plume (rounded leaves, not spikes)
    for x, y, rx, ry, col in [(15, 11, 3, 7, 'L'), (21, 7, 3, 8, 'L'), (27, 6, 3, 8, 'L'), (33, 10, 3, 7, 'L'),
                              (18, 9, 2, 6, 'l'), (24, 5, 2, 6, 'l'), (30, 8, 2, 6, 'l'), (12, 15, 3, 4, 'L'), (36, 15, 3, 4, 'L')]:
        c.ell(x, y, rx, ry, col)
    # big round head
    c.ell(24, 24, 12, 9, 'a')
    # little round body + gem belly
    c.ell(24, 38, 8, 6, 'a')
    c.ell(19, 45, 3, 2, 'a'); c.ell(29, 45, 3, 2, 'a')
    # one arm waving, one on belly
    c.ell(13, 33, 2, 4, 'a'); c.ell(11, 28, 3, 3, 'a')
    c.ell(33, 39, 3, 2, 'a')
    # ears
    c.ell(11, 24, 3, 2, 'a'); c.ell(37, 24, 3, 2, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.shadow('L', 'G')
    c.ell(24, 39, 2, 2, 'c'); c.px(23, 38, 'w')
    bigeye(c, 16, 22); bigeye(c, 28, 22)
    c.line(22, 30, 26, 30, 'k'); c.px(21, 29, 'k'); c.px(27, 29, 'k')   # tiny grin
    blush(c, 14, 28); blush(c, 31, 28)
    # sparkle: it thinks it's lucky
    c.px(40, 3, 'y'); c.px(39, 4, 'y'); c.px(41, 4, 'y'); c.px(40, 5, 'y')


@sprite48('Trolltree', {'a': '#e6a676', 'd': '#a86c46', 'b': '#fff0de', 'c': '#ff3fa4'})
def trolltree(c):
    # cloud-puff canopy (huggable, reads as a tree)
    for x, y, rx, ry in [(13, 11, 8, 7), (24, 7, 10, 7), (35, 11, 8, 7), (18, 16, 8, 4), (30, 16, 8, 4)]:
        c.ell(x, y, rx, ry, 'L')
    for x, y, rx, ry in [(11, 9, 3, 2), (22, 4, 4, 2), (34, 8, 3, 2)]:
        c.ell(x, y, rx, ry, 'l')
    c.rect(21, 18, 27, 22, 't')
    # big soft body: gentle giant
    c.ell(24, 33, 15, 12, 'a')
    c.ell(24, 36, 9, 7, 'b')
    # stubby root feet
    c.ell(15, 45, 5, 2, 't'); c.ell(33, 45, 5, 2, 't')
    # stubby branch arms, one holding a little bird
    c.ell(8, 33, 3, 5, 'a'); c.ell(40, 31, 3, 4, 'a')
    c.outline()
    c.shadow('a', 'd')
    c.shadow('L', 'G')
    # the bird and its nest (the "load-bearing hair" joke, now a friend)
    c.ell(38, 3, 3, 1, 't'); c.ell(38, 1, 1.5, 1.2, 'y'); c.px(37, 1, 'k'); c.px(36, 1, 'f')
    # gem belly glowing
    c.ell(24, 37, 3, 3, 'c'); c.px(23, 36, 'w')
    for x, y in [(19, 37), (29, 37), (24, 32), (24, 42)]:
        c.px(x, y, 'm')
    # face: content, sleepy-happy (lovable flaw: it never moves)
    c.line(15, 27, 18, 26, 'k'); c.line(18, 26, 20, 27, 'k')
    c.line(28, 27, 30, 26, 'k'); c.line(30, 26, 33, 27, 'k')
    c.line(21, 30, 27, 30, 'k'); c.px(20, 29, 'k'); c.px(28, 29, 'k')
    blush(c, 13, 29); blush(c, 33, 29)
