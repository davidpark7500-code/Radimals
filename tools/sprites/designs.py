"""Hand-designed Radimal sprites. Each function composes one creature around its pun.
Run tools/sprites/build.py to inject them into www/index.html."""
import math
from lib import sprite


def star(c, cx, cy, n, r1, r2, col, rot=-math.pi / 2):
    pts = []
    for i in range(n * 2):
        r = r1 if i % 2 == 0 else r2
        a = rot + i * math.pi / n
        pts.append((cx + 0.5 + r * math.cos(a), cy + 0.5 + r * math.sin(a)))
    c.poly(pts, col)


def sparkle(c, x, y, col='F', core='w'):
    c.stamp(x, y, ['.' + col + '.', col + core + col, '.' + col + '.'])


# ============================== FIRE ==============================
@sprite('Sparklerp')
def _(c):
    c.rect(11, 13, 12, 20, 'n')
    for y in (14, 17):
        c.line(10, y, 7, y + 3, 'n')
        c.line(13, y, 16, y + 3, 'n')
    c.rect(11, 20, 12, 22, 't')
    star(c, 11, 7, 8, 7.5, 4.5, 'a', rot=-math.pi / 2 + math.pi / 8)
    c.ell(11.5, 7.5, 4, 3.5, 'b')
    c.outline()
    for x, y in [(0, 1), (19, 0), (0, 11), (20, 11), (2, 16), (19, 16)]:
        sparkle(c, x, y)
    c.eye(8, 6, 'big').eye(14, 6, 'big')
    c.brow(7, 4, 'L').brow(14, 4, 'R')
    c.stamp(9, 9, ['k....k', '.kkkk.'])


@sprite('Fizzlerp')
def _(c):
    c.rect(11, 17, 12, 22, 'n')
    c.rect(11, 17, 12, 18, 'f')
    c.line(10, 19, 6, 21, 'n')
    c.line(13, 19, 17, 21, 'n')
    star(c, 11, 9, 12, 9.5, 6, 'a')
    c.ell(11.5, 9.5, 5.5, 5, 'b')
    c.outline()
    c.stamp(1, 0, ['.w.', 'www', '.w.'])
    c.stamp(19, 1, ['w.', 'ww'])
    for x, y in [(1, 17), (20, 16), (3, 21), (19, 20)]:
        c.px(x, y, 'f')
    c.stamp(7, 8, ['kkk', 'wkk'])
    c.stamp(14, 8, ['kkk', 'kkw'])
    c.stamp(9, 12, ['.kkkk.', 'k....k'])
    c.px(17, 11, 'q')


@sprite('Flaminhawk')
def _(c):
    c.poly([(15, 13), (22, 9), (21, 13), (23, 15), (20, 19), (15, 17)], 'c')
    c.ell(12, 14, 7, 6, 'a')
    c.ell(11, 16.5, 5, 3, 'b')
    c.ell(7.5, 8, 4.5, 4, 'a')
    c.poly([(5, 6), (0.5, 8), (1.5, 11), (3, 10), (4, 11), (5, 10)], 'y')
    c.poly([(5, 5), (6, 0), (8, 3), (10, 0), (11, 4), (14, 2), (12, 6)], 'f')
    c.poly([(7, 4), (8, 2), (9, 4), (10, 2), (11, 5)], 'F')
    c.poly([(9, 11), (17, 9), (20, 12), (17, 14), (19, 16), (14, 17), (10, 14)], 'c')
    c.rect(9, 19, 10, 22, 'y')
    c.rect(14, 19, 15, 22, 'y')
    c.outline()
    for x, y in [(12, 11), (15, 12), (11, 13), (16, 15), (13, 15)]:
        c.px(x, y, 'r')
    c.stamp(8, 22, ['kk.kk']).stamp(13, 22, ['kk.kk'])
    c.eye(5, 7, 'big', look=-1)
    c.brow(5, 5, 'R', 3)
    c.px(2, 9, 'k')


@sprite('Crimpede')
def _(c):
    path = [(9, 9), (12, 12), (15, 10), (18, 13), (19, 17), (16, 20), (12, 19)]
    for i, (x, y) in enumerate(path):
        c.ell(x, y, 2.6, 2.6, 'a' if i % 2 == 0 else 'b')
    c.ell(5.5, 6, 4, 3.6, 'a')
    c.outline()
    for x, y in path:
        c.px(x - 2, y + 3, 'k')
        c.px(x + 2, y + 3, 'k')
    # crimped hair
    c.stamp(2, 0, ['c.c.c.c', 'ccccccc', '.c.c.c.'])
    c.px(1, 1, '#').px(9, 1, '#')
    c.eye(3, 5, 'big', look=-1).eye(7, 5, 'big')
    c.brow(2, 3, 'L').brow(7, 3, 'R')
    c.stamp(4, 8, ['kwwk'])
    c.px(11, 20, 'c').px(10, 21, 'c')


@sprite('Curlironx')
def _(c):
    c.line(15, 19, 20, 5, 'n', 2)
    c.line(18, 11, 21, 4, 'k')
    c.rect(19, 2, 21, 4, 'f')
    c.ell(10, 16, 6, 5, 'a')
    c.ell(7, 9, 5, 4.2, 'a')
    c.poly([(2.5, 7), (2.5, 1), (6.5, 5)], 'a')
    c.poly([(8, 5), (11, 1), (11.5, 7)], 'a')
    c.rect(5, 19, 6, 22, 'a')
    c.rect(9, 19, 10, 22, 'a')
    c.ell(9.5, 17, 3, 3, 'b')
    c.ell(5, 11.5, 2.3, 1.5, 'b')
    c.outline()
    c.px(2, 0, 'k').px(11, 0, 'k')
    c.px(4, 4, 'b').px(10, 4, 'b')
    c.eye(4, 8, 'big', look=-1).eye(8, 8, 'big', look=-1)
    c.brow(3, 6, 'R').brow(8, 6, 'R')
    c.stamp(4, 11, ['k.k'])
    c.stamp(3, 12, ['.kk'])
    for x, y in [(22, 1), (18, 0), (22, 6)]:
        c.px(x, y, 'F')
    c.line(16, 22, 22, 22, 'k')
    c.stamp(21, 20, ['c', 'c'])


@sprite('Orangeglug')
def _(c):
    c.ring(18.5, 13, 3.5, 4.5, 2, 'a')
    c.poly([(7, 8), (16, 8), (17.5, 10), (17.5, 21), (16, 22), (7, 22), (5.5, 21), (5.5, 10)], 'a')
    c.rect(9, 5, 14, 7, 'a')
    c.rect(8, 2, 15, 4, 'c')
    c.rect(6, 12, 17, 18, 'b')
    c.outline()
    c.stamp(8, 2, ['.k.k.k.k'])
    c.shine('a', 'b')
    c.eye(8, 13, 'big').eye(13, 13, 'big')
    c.stamp(9, 16, ['kwwwk', '.kkk.'])
    c.px(10, 9, 'w').px(11, 9, 'w').px(7, 11, 'w')


@sprite('Glugdeluxe')
def _(c):
    c.poly([(6, 12), (2, 13), (1, 9), (3, 8), (4, 10), (6, 10)], 'a')
    c.poly([(17, 12), (21, 13), (22, 9), (20, 8), (19, 10), (17, 10)], 'a')
    c.poly([(7, 7), (16, 7), (17.5, 9), (17.5, 20), (5.5, 20), (5.5, 9)], 'a')
    c.rect(8, 21, 9, 22, 'a')
    c.rect(14, 21, 15, 22, 'a')
    c.poly([(6.5, 6), (14, 2.5), (15.5, 5), (8, 8.5)], 'c')
    c.rect(14, 0, 15, 4, 'r')
    c.rect(16, 0, 18, 1, 'r')
    c.rect(6, 11, 17, 17, 'b')
    c.outline()
    c.px(14, 1, 'w').px(14, 3, 'w').px(17, 0, 'w')
    c.shades(8, 12, 8)
    c.stamp(10, 15, ['....k', 'kkkk.'])
    c.px(1, 9, 'b').px(22, 9, 'b')


@sprite('Sourbomb')
def _(c):
    c.ell(11.5, 13.5, 8.5, 8.5, 'a')
    c.rect(10, 3, 13, 5, 'n')
    c.line(13, 2, 16, 0, 't')
    c.outline()
    sparkle(c, 16, 0, 'F', 'w')
    for x, y in [(6, 8), (16, 9), (5, 15), (18, 16), (9, 19), (14, 20), (17, 12), (11, 7)]:
        c.px(x, y, 'w')
    c.stamp(14, 17, ['cc', '.cc'])
    c.stamp(6, 11, ['kk..', '..kk', 'kk..'])
    c.stamp(14, 11, ['..kk', 'kk..', '..kk'])
    c.stamp(10, 15, ['.kk.', 'kmmk', '.kk.'])
    c.px(7, 15, 'm').px(16, 15, 'm')


@sprite('Kerosnail')
def _(c):
    c.poly([(1, 22), (3, 18), (19, 18), (22.5, 22)], 'a')
    c.ell(5, 15, 3.2, 4, 'a')
    c.line(3, 11, 2, 6, 'a')
    c.line(6, 11, 7, 6, 'a')
    c.poly([(9, 6), (14.5, 1.5), (20, 6)], 'n')
    c.rect(9, 6, 20, 18, 'n')
    c.rect(10, 8, 19, 16, 'F')
    c.ell(14.5, 12.5, 2.4, 3.4, 'f')
    c.ell(14.5, 13.5, 1, 1.6, 'y')
    c.outline()
    c.rect(14, 0, 15, 0, 'k')
    for x in (12, 17):
        c.line(x, 8, x, 16, 'n')
    c.stamp(1, 5, ['wk']).stamp(7, 5, ['wk'])
    c.stamp(3, 15, ['kk'])
    c.stamp(3, 16, ['.kk'])
    c.px(4, 19, 'b').px(8, 20, 'b').px(13, 20, 'b')
    c.px(20, 23, 'k').px(11, 23, 'k')


@sprite('Minibagel')
def _(c):
    c.rect(6, 19, 8, 22, 'a')
    c.rect(15, 19, 17, 22, 'a')
    c.ell(11.5, 11.5, 10, 8.5, 'a')
    c.poly([(2, 10), (5, 4), (11.5, 3), (18, 4), (21, 10), (19, 12), (18, 10), (16, 13), (14, 10), (11, 12), (8, 10), (6, 13), (4, 10)], 'y')
    c.ell(11.5, 15, 2.6, 1.8, '.')
    c.outline()
    for x, y in [(4, 7), (17, 6), (15, 9)]:
        c.stamp(x, y, ['rr', 'rr'])
    c.eye(7, 7, 'big').eye(12, 7, 'big')
    c.stamp(8, 10, ['kwwk', '.kk.'])
    c.px(4, 14, 'b').px(18, 15, 'b').px(6, 17, 'b')


@sprite('Pizzarolla')
def _(c):
    c.rect(0, 11, 2, 14, 'a')
    c.rect(21, 11, 23, 14, 'a')
    c.poly([(3, 6), (20, 6), (21.5, 8), (21.5, 18), (20, 20), (3, 20), (1.5, 18), (1.5, 8)], 'a')
    c.rect(5, 20, 7, 22, 'a')
    c.rect(16, 20, 18, 22, 'a')
    c.poly([(15, 20), (17, 20), (16.5, 23), (15.5, 23)], 'f')
    c.outline()
    for x in range(3, 21, 2):
        c.px(x, 6, 'b').px(x, 20, 'b')
    c.line(16, 8, 19, 12, 'f')
    c.line(17, 8, 20, 12, 'F')
    c.line(4, 15, 6, 18, 'f')
    c.stamp(7, 0, ['.w..w.', 'w..w..', '.w..w.', '..w..w'])
    c.brow(5, 9, 'L', 3).brow(13, 9, 'R', 3)
    c.eye(6, 11, 'big').eye(14, 11, 'big')
    c.stamp(7, 15, ['kkkkkkkk', 'kwkwkwkk', '.kkkkkk.'])


# ============================== WATER ==============================
@sprite('Slipslug')
def _(c):
    c.rect(0, 18, 23, 21, 'c')
    c.ell(13, 15, 9, 3.6, 'a')
    c.ell(5, 12.5, 4, 4, 'a')
    c.line(3, 9, 2, 4, 'a')
    c.line(7, 9, 8, 4, 'a')
    c.ell(13, 17, 8, 1.4, 'b')
    c.outline()
    for x in range(1, 23, 4):
        c.rect(x, 20, x + 1, 20, 'w')
    c.stamp(1, 3, ['wk']).stamp(8, 3, ['wk'])
    c.stamp(3, 13, ['kwwwk', '.kkk.'])
    c.px(3, 11, 'k').px(6, 11, 'k')
    c.stamp(0, 14, ['q', '.', 'q'])
    c.px(22, 13, 'q').px(20, 11, 'q')
    c.px(10, 12, 'w').px(14, 12, 'w')


@sprite('Slidemander')
def _(c):
    c.line(17, 13, 21, 9, 'a', 2)
    c.line(21, 9, 21, 4, 'a', 2)
    c.ell(11, 13, 7.5, 3.4, 'a')
    c.ell(4, 12, 3.6, 3, 'a')
    c.line(7, 15, 4, 19, 'a', 2)
    c.line(7, 10, 5, 6, 'a', 2)
    c.line(14, 15, 16, 19, 'a', 2)
    c.line(14, 10, 16, 6, 'a', 2)
    c.ell(11, 14.5, 6, 1.2, 'b')
    c.outline()
    for x, y in [(3, 20), (6, 20), (15, 20), (18, 20), (4, 5), (6, 5), (16, 5), (18, 5)]:
        c.px(x, y, 'b')
    c.stamp(1, 10, ['ckkck', 'kqkqk'])
    c.line(5, 10, 9, 10, 'c')
    for x, y in [(10, 12), (13, 11), (16, 13)]:
        c.px(x, y, 'c')
    c.stamp(2, 13, ['kww'])
    c.stamp(0, 16, ['q.q', '.q.'])
    c.px(0, 8, 'q')


@sprite('Bubbletapir')
def _(c):
    c.ell(15.5, 8, 7, 7, 'b')
    c.line(3, 12, 8, 9, 'a', 2)
    c.ell(8, 17, 6.5, 4, 'a')
    c.ell(4.5, 13.5, 3.6, 3.2, 'a')
    c.poly([(6, 11), (7, 8), (9, 11)], 'a')
    c.rect(4, 20, 5, 22, 'a')
    c.rect(11, 20, 12, 22, 'a')
    c.outline()
    c.stamp(11, 3, ['.ww', 'w..', 'w..'])
    c.px(19, 12, 'w')
    c.eye(3, 13, 'big', look=-1)
    c.px(6, 15, 'm').px(2, 16, 'k')
    c.px(8, 16, 'b').px(11, 18, 'b')


@sprite('Bubblewrapir')
def _(c):
    c.ell(13, 15, 9.5, 6, 'a')
    c.ell(5, 10, 4.6, 4.2, 'a')
    c.line(1, 11, 1, 16, 'a', 2)
    c.poly([(7, 7), (8, 3), (10, 7)], 'a')
    for x in (6, 10, 16, 20):
        c.rect(x, 19, x + 1, 22, 'a')
    c.outline()
    for y in range(11, 20, 3):
        for x in range(8 + (y % 2), 22, 3):
            if c.get(x, y) == 'a' and c.get(x + 1, y + 1) == 'a':
                c.stamp(x, y, ['wb', 'bb'])
    c.px(0, 17, 'a').px(1, 18, 'k')
    for x, y in [(12, 5), (20, 6), (16, 4), (22, 10)]:
        c.px(x, y, 'w')
    c.stamp(17, 6, ['w.w', '.w.', 'w.w'])
    c.eye(3, 9, 'big', look=-1).eye(6, 9, 'big')
    c.brow(3, 7, 'R').brow(6, 7, 'R')
    c.stamp(2, 12, ['kwk'])


@sprite('Dunktank')
def _(c):
    c.line(17, 13, 20, 9, 'n', 2)
    c.ell(20, 6, 3, 3, 'c')
    c.rect(1, 4, 16, 21, 'a')
    c.rect(3, 7, 14, 20, 'b')
    c.rect(4, 22, 5, 22, 'a')
    c.rect(12, 22, 13, 22, 'a')
    c.outline()
    c.rect(4, 9, 13, 9, 't')
    c.ell(20, 6, 2, 2, 'r')
    c.ell(20, 6, 1, 1, 'w')
    c.px(20, 6, 'r')
    for x in range(3, 15, 3):
        c.px(x, 11, 'w').px(x + 1, 11, 'w')
    c.eye(5, 13, 'wide').eye(10, 13, 'wide')
    c.brow(5, 12, 'L', 2)
    c.stamp(7, 17, ['.kk.', 'k..k', '.kk.'])
    c.px(12, 16, 'w').px(13, 14, 'w')
    c.rect(1, 4, 16, 5, 'n')


@sprite('Brineape')
def _(c):
    cx, cy, r = 11, 12.5, 6.5
    n = 12
    for i in range(n):
        th = math.radians(-55 - i * (220 / (n - 1)))
        c.ell(cx + r * math.cos(th), cy + r * math.sin(th), 2.8 - i * 0.08, 2.8 - i * 0.08, 'a' if i % 2 else 'b')
    c.ell(15, 6.5, 3.8, 3.4, 'a')
    c.poly([(12, 17), (19, 15), (21, 20), (16, 22)], 'a')
    c.outline()
    c.stamp(12, 1, ['y.y.y', 'yyyyy'])
    c.line(18, 5, 23, 1, 'k')
    c.line(17, 3, 20, 0, 'k')
    c.eye(15, 6, 'big')
    c.brow(14, 4, 'L', 3)
    c.stamp(12, 9, ['kk.'])
    for i in range(5):
        c.px(7 + i, 11 + i, 'k')
    c.px(18, 18, 'c').px(17, 19, 'c')


@sprite('Fishtankamari')
def _(c):
    c.poly([(16, 12), (22.5, 6), (21, 12), (22.5, 18)], 'a')
    c.ell(10, 12, 7.5, 5, 'a')
    c.poly([(8, 7), (12, 3), (13, 8)], 'c')
    c.poly([(9, 17), (12, 21), (13, 16)], 'c')
    c.outline()
    for x in (9, 11, 13):
        c.line(x, 9, x, 15, 'b')
    c.line(8, 12, 15, 12, 'b')
    c.eye(4, 10, 'wide', look=-1)
    c.stamp(1, 13, ['.k', 'k.', '.k'])
    c.ring(5, 3, 1.5, 1.5, 1, 'q')
    c.px(2, 6, 'q').px(8, 1, 'q')


@sprite('Hangryhippo')
def _(c):
    c.ell(4, 2.5, 2, 2, 'a')
    c.ell(19, 2.5, 2, 2, 'a')
    c.ell(11.5, 7.5, 9, 5.5, 'a')
    c.ell(11.5, 18, 10, 4.5, 'a')
    c.rect(3, 11, 20, 16, 'R')
    c.outline()
    c.rect(3, 11, 20, 11, 'k')
    for x in (4, 18):
        c.rect(x, 12, x + 1, 13, 'w')
        c.rect(x, 15, x + 1, 16, 'w')
    c.ell(9, 14.5, 1.2, 1.2, 'q').ell(14, 14, 1.2, 1.2, 'y')
    c.px(11, 16, 'm').px(12, 16, 'm')
    c.px(4, 2, 'b').px(19, 2, 'b')
    c.eye(6, 5, 'big').eye(15, 5, 'big', look=-1)
    c.brow(5, 3, 'L', 3).brow(15, 3, 'R', 3)
    c.px(9, 9, 'k').px(14, 9, 'k')
    c.stamp(6, 19, ['b..........b'])


@sprite('Snorkelord')
def _(c):
    c.poly([(3, 21), (6, 17), (8, 22)], 'a')
    c.poly([(20, 21), (17, 17), (15, 22)], 'a')
    c.ell(11.5, 15, 7, 7, 'a')
    c.ell(11.5, 8, 5.6, 5, 'a')
    c.ell(11.5, 17, 4.5, 4.5, 'b')
    c.rect(19, 2, 20, 9, 'c')
    c.rect(17, 8, 20, 9, 'c')
    c.ell(11.5, 15.5, 10.5, 2.4, 'r')
    c.outline()
    c.stamp(7, 0, ['y.y.y.y.y', 'yyyyyyyyy'])
    c.px(6, 1, '#').px(16, 1, '#')
    c.rect(6, 6, 17, 9, 'k')
    c.rect(7, 7, 10, 8, 'q')
    c.rect(13, 7, 16, 8, 'q')
    c.px(9, 8, 'k').px(15, 8, 'k')
    c.px(19, 2, 'r').px(20, 2, 'r')
    c.stamp(9, 11, ['k...k', '.kkk.'])
    for x in range(2, 22, 3):
        c.px(x, 15, 'w').px(x, 16, 'w')


# ============================== BASIC ==============================
@sprite('Yakkity')
def _(c):
    c.ell(13.5, 14, 8, 5.5, 'a')
    c.poly([(6, 17), (8, 21), (10, 18), (12, 21), (14, 18), (16, 21), (18, 18), (20, 21), (21.5, 16)], 'a')
    for x in (7, 11, 16, 19):
        c.rect(x, 19, x + 1, 22, 'a')
    c.ell(5, 11, 4.2, 4, 'a')
    c.poly([(3, 8), (0.5, 6), (1, 2), (2.5, 5), (5, 7)], 'w')
    c.poly([(6, 7), (8, 4), (10, 1), (9.5, 5), (8, 8)], 'w')
    c.rect(11, 11, 18, 16, 'b')
    c.outline()
    for y in (12, 14):
        for x in range(12, 18, 2):
            c.px(x, y, 'k')
    c.px(17, 15, 'r')
    c.eye(3, 10, 'big', look=-1)
    c.brow(3, 8, 'R')
    c.stamp(2, 13, ['kkk', 'krk'])
    c.stamp(0, 12, ['k', '.', 'k'])


@sprite('Sockpup')
def _(c):
    c.rect(10, 10, 17, 22, 'a')
    c.ell(9.5, 7, 7.5, 4.6, 'a')
    c.outline()
    c.line(2, 8, 11, 8, 'k')
    c.stamp(3, 9, ['rrrr'])
    c.rect(10, 17, 17, 17, 'c')
    c.rect(10, 19, 17, 19, 'c')
    c.rect(10, 21, 17, 21, 'c')
    c.stamp(6, 4, ['nn', 'nw']).stamp(11, 4, ['nn', 'nw'])
    c.px(14, 12, 'b').px(15, 13, 'b')


@sprite('Puppetmaster')
def _(c):
    c.line(8, 12, 4, 4, 'a', 2)
    c.line(15, 12, 19, 4, 'a', 2)
    c.rect(8, 11, 15, 19, 'a')
    c.ell(11.5, 8, 5, 4, 'a')
    c.rect(9, 20, 10, 22, 'a')
    c.rect(13, 20, 14, 22, 'a')
    c.rect(3, 1, 20, 2, 't')
    c.rect(11, 0, 12, 4, 't')
    c.outline()
    c.line(4, 3, 9, 20, 'n')
    c.line(19, 3, 14, 20, 'n')
    for y in (14, 16, 18):
        c.rect(8, y, 15, y, 'c')
    c.stamp(8, 7, ['nn..nn', 'nw..nw'])
    c.stamp(9, 10, ['....kk', 'kkkk..'])


@sprite('Hamsterjam')
def _(c):
    c.line(6, 13, 2, 8, 'a', 2)
    c.line(17, 13, 21, 9, 'a', 2)
    c.ell(11.5, 14, 6.5, 6.5, 'a')
    c.ell(11.5, 8, 6, 5, 'a')
    c.ell(6, 3, 1.8, 1.8, 'a')
    c.ell(17, 3, 1.8, 1.8, 'a')
    c.rect(8, 20, 9, 22, 'a')
    c.line(15, 19, 19, 21, 'a', 2)
    c.ell(11.5, 16, 4, 4, 'b')
    c.ell(5.5, 8, 2, 2.4, 'c')
    c.ell(17.5, 8, 2, 2.4, 'c')
    c.outline()
    c.ring(11.5, 8, 6.5, 6, 1, 'k')
    c.recolor('k', 'a', (0, 7, 23, 23))
    c.eye(8, 7, 'big').eye(13, 7, 'big')
    c.stamp(10, 10, ['kwwk', '.kk.'])
    c.px(7, 10, 'm').px(16, 10, 'm')
    c.stamp(0, 0, ['.kk', '.k.', 'kk.'])
    c.stamp(20, 15, ['.kk', '.k.', 'kk.'])


@sprite('Binderling')
def _(c):
    c.rect(3, 4, 21, 11, 'a')
    c.rect(3, 14, 21, 19, 'a')
    c.rect(2, 4, 4, 19, 'L')
    c.rect(5, 12, 21, 13, 'k')
    for x in (7, 12, 17):
        c.rect(x, 11, x + 1, 14, 'w')
    c.rect(5, 20, 6, 22, 'a')
    c.rect(17, 20, 18, 22, 'a')
    c.outline()
    c.rect(17, 5, 21, 9, 'c')
    c.px(18, 6, 'b').px(20, 8, 'b')
    c.eye(7, 6, 'big').eye(12, 6, 'big')
    c.brow(6, 4, 'L', 3).brow(12, 4, 'R', 3)
    c.rect(6, 16, 15, 16, 'b')


@sprite('Fannypacker')
def _(c):
    c.poly([(16, 18), (21, 16), (22.5, 21), (19, 21)], 'a')
    c.ell(11.5, 14, 5.6, 7, 'a')
    c.ell(11.5, 6, 4.6, 4, 'a')
    c.poly([(8, 4), (7, 0), (10, 3)], 'a')
    c.poly([(15, 4), (16, 0), (13, 3)], 'a')
    c.poly([(5, 22), (6, 19), (11, 20), (10, 22.5)], 'a')
    c.poly([(18, 22), (17, 19), (12, 20), (13, 22.5)], 'a')
    c.ell(11.5, 16, 3.5, 4, 'b')
    c.rect(6, 14, 17, 17, 'c')
    c.outline()
    c.line(6, 13, 17, 13, 'k')
    c.line(7, 15, 16, 15, 'k')
    c.px(15, 16, 'w')
    c.rect(6, 3, 17, 3, 'm')
    c.rect(4, 4, 9, 4, 'm')
    c.eye(8, 5, 'sleepy').eye(13, 5, 'sleepy')
    c.stamp(10, 8, ['k..k', '.kk.'])
    c.line(6, 10, 4, 13, 'a', 1)
    c.line(17, 10, 19, 13, 'a', 1)


@sprite('Goofyputt')
def _(c):
    c.line(6, 11, 1, 7, 'a', 2)
    c.ell(1, 6, 1.4, 1.4, 'a')
    c.line(17, 11, 21, 8, 'a', 2)
    c.ell(22, 7, 1.4, 1.4, 'a')
    c.ell(11.5, 11, 6, 6.5, 'a')
    c.poly([(5, 15), (6.5, 13), (8, 15), (10, 13), (12, 15), (14, 13), (16, 15), (17.5, 13), (19, 15), (18, 21), (12, 23), (6, 21)], 'c')
    c.poly([(7, 4), (10, 1), (15, 0.5), (19, 3), (17, 5), (9, 5.5)], 'c')
    c.outline()
    c.eye(8, 9, 'wide').eye(13, 9, 'wide', look=-1)
    c.stamp(9, 12, ['kmmmk', '.kkk.'])
    c.stamp(14, 12, ['k.k', '.k.'][::-1])
    c.rect(6, 17, 17, 17, 'b')
    c.px(4, 3, 'k').px(3, 4, 'k')


@sprite('Goofypuddle')
def _(c):
    c.ell(11.5, 18.5, 11, 4, 'a')
    c.ell(11.5, 13, 5.5, 5.5, 'a')
    c.ell(11.5, 18.5, 8, 2, 'b')
    c.outline()
    c.ell(20, 3, 2.2, 2.2, 'y')
    for x, y in [(20, 0), (23, 3), (17, 3), (20, 6)]:
        c.px(x, y, 'F')
    c.line(8, 9, 8, 17, 'b')
    c.line(15, 11, 15, 17, 'b')
    c.stamp(8, 11, ['kk..kk', 'wk..wk', '.k...k'])
    c.stamp(9, 15, ['.kkk.', 'k...k'])
    c.px(17, 9, 'q').px(17, 10, 'q')


@sprite('Springee')
def _(c):
    c.rect(0, 16, 7, 22, 't')
    c.rect(16, 20, 23, 22, 't')
    pts = []
    for i in range(14):
        t = i / 13
        pts.append((3.5 + 16 * t, 14.5 - 12 * math.sin(math.pi * t) + 4.5 * t))
    for x, y in pts:
        c.ell(x, y, 1.4, 3.3, 'a')
    c.outline()
    for i, (x, y) in enumerate(pts[1:], 1):
        for dy in range(-3, 4):
            if c.get(int(x), int(y + dy)) == 'a':
                c.px(int(x), int(y + dy), 'k' if i % 2 else 'b')
    x, y = pts[0]
    c.ell(x, y, 2.4, 2.4, 'b')
    c.stamp(int(x) - 2, int(y) - 1, ['wk.wk'])
    c.stamp(int(x) - 1, int(y) + 1, ['kkk'])
    c.rect(0, 16, 7, 16, 'k')
    c.rect(16, 20, 23, 20, 'k')


@sprite('Springstretch')
def _(c):
    c.ring(11.5, 12, 9.5, 5, 2, 'a')
    c.ring(11.5, 12, 5, 9.5, 2, 'b')
    c.line(3, 20, 7, 16, 'a', 2)
    c.line(20, 3, 16, 7, 'b', 2)
    c.ell(11.5, 12, 3.6, 3.2, 'a')
    c.outline()
    for i in range(0, 24, 2):
        for y in range(24):
            if c.get(i, y) in 'ab' and (y + i) % 4 == 0:
                c.px(i, y, 'w')
    c.eye(9, 11, 'big').eye(13, 11, 'big', look=-1)
    c.brow(8, 9, 'L').brow(13, 9, 'R')
    c.stamp(10, 14, ['kkkk'])


@sprite('Mallrat')
def _(c):
    c.line(18, 20, 22, 17, 'm')
    c.line(22, 17, 22, 13, 'm')
    c.ell(13, 15, 6, 5, 'a')
    c.ell(7, 10, 4.6, 3.8, 'a')
    c.poly([(3, 9), (0, 11), (3, 12)], 'a')
    c.ell(8, 5, 2.2, 2.2, 'a')
    c.ell(12, 6, 2.2, 2.2, 'a')
    c.rect(9, 20, 10, 22, 'a')
    c.rect(15, 20, 16, 22, 'a')
    c.rect(17, 9, 20, 15, 'w')
    c.rect(17, 8, 20, 8, 'c')
    c.line(19, 7, 21, 3, 'r')
    c.ell(13, 16, 3.5, 3, 'b')
    c.outline()
    c.stamp(5, 5, ['cccc', 'ccccccc'])
    c.px(8, 5, 'b').px(12, 6, 'b')
    c.px(0, 11, 'k')
    c.eye(5, 9, 'sleepy', look=-1)
    c.stamp(2, 12, ['kkk.'])
    c.px(16, 12, 'a').px(16, 13, 'a')
    c.rect(18, 11, 19, 12, 'r')


@sprite('Mallratking')
def _(c):
    c.poly([(5, 9), (2, 21), (11, 22), (12, 10)], 'v')
    c.poly([(18, 9), (21, 21), (12, 22), (11, 10)], 'v')
    c.line(17, 20, 22, 18, 'm')
    c.ell(12, 15, 5.6, 6.5, 'a')
    c.ell(12, 8, 4.6, 4, 'a')
    c.ell(7, 4.5, 2.6, 2.6, 'a')
    c.ell(17, 4.5, 2.6, 2.6, 'a')
    c.rect(9, 20, 10, 22, 'a')
    c.rect(14, 20, 15, 22, 'a')
    c.ell(12, 16, 3.5, 4, 'b')
    c.outline()
    c.stamp(8, 0, ['y.y.y.y.y', 'yyyyyyyyy'])
    c.px(7, 4, 'b').px(17, 4, 'b')
    c.shades(8, 7, 8)
    c.stamp(10, 10, ['....k', 'kkkk.'])
    c.stamp(0, 20, ['yy', 'yy']).stamp(19, 21, ['yyy'])
    c.stamp(16, 13, ['yy', 'yy', '.y', 'yy'])


@sprite('Couchpotato')
def _(c):
    c.rect(2, 8, 21, 14, 'c')
    c.rect(1, 14, 22, 20, 'c')
    c.rect(0, 11, 3, 20, 'c')
    c.rect(20, 11, 23, 20, 'c')
    c.ell(11.5, 12, 5.6, 6, 'a')
    c.outline()
    c.rect(2, 21, 3, 22, 'k').rect(20, 21, 21, 22, 'k')
    c.rect(4, 17, 19, 17, 'G')
    c.stamp(10, 4, ['.L.', 'LLL'])
    for x, y in [(8, 9), (15, 14), (9, 16)]:
        c.px(x, y, 't')
    c.eye(8, 11, 'sleepy').eye(13, 11, 'sleepy')
    c.stamp(10, 14, ['kkkk'])
    c.px(13, 15, 'q')
    c.rect(16, 13, 18, 16, 'k')
    c.px(17, 14, 'r')


@sprite('Gooshpod')
def _(c):
    c.poly([(11.5, 3), (18, 8), (19, 16), (14, 22), (9, 22), (4, 16), (5, 8)], 'a')
    c.poly([(9, 3), (11.5, 0), (14, 3), (11.5, 5)], 'L')
    c.outline()
    c.stamp(0, 4, ['c.', '.c', 'cc', '.c'])
    c.stamp(21, 3, ['.c', 'c.', 'cc', 'c.'])
    c.stamp(17, 10, ['c', 'c'])
    c.line(17, 9, 15, 13, 'k')
    c.px(15, 22, 'c').px(15, 23, 'c')
    c.eye(7, 10, 'wide').eye(13, 10, 'wide')
    c.stamp(9, 15, ['.kk.', 'k..k'])
    c.px(7, 6, 'b').px(8, 5, 'b')


@sprite('Freshprints')
def _(c):
    c.ell(13, 14, 7, 5, 'a')
    c.ell(7, 9, 4.6, 4.2, 'a')
    c.poly([(3, 9), (0.5, 11), (3, 12.5)], 'a')
    c.rect(4, 3, 10, 5, 'k')
    c.poly([(11, 8), (13, 5), (13, 10)], 'a')
    c.line(19, 12, 22, 8, 'a', 2)
    c.rect(8, 18, 9, 21, 'a')
    c.rect(16, 18, 17, 21, 'a')
    c.line(11, 18, 13, 16, 'a', 2)
    c.rect(7, 21, 10, 22, 'w')
    c.rect(15, 21, 18, 22, 'w')
    c.outline()
    c.px(0, 11, 'k')
    c.eye(5, 8, 'big', look=-1)
    c.brow(4, 6, 'R', 3)
    c.stamp(2, 12, ['kk.k'])
    c.ell(12, 15, 4, 2.5, 'b')
    for x, y in [(1, 20), (4, 22)]:
        c.stamp(x, y, ['n.n', '.n.'])
    c.rect(7, 22, 10, 22, 'c').rect(15, 22, 18, 22, 'c')


@sprite('Freshroyal')
def _(c):
    c.ell(11.5, 15, 6, 6.5, 'a')
    c.ell(11.5, 7, 4.6, 4.2, 'a')
    c.rect(7, 0, 16, 4, 'k')
    c.rect(8, 20, 10, 22, 'w')
    c.rect(13, 20, 15, 22, 'w')
    c.rect(5, 12, 18, 15, 'a')
    c.outline()
    c.stamp(10, 0, ['y.y.y', 'yyyyy'])
    c.rect(7, 4, 16, 4, 'k')
    c.shades(8, 6, 8)
    c.stamp(10, 9, ['...k', 'kkk.'])
    c.line(6, 13, 17, 13, 'k')
    c.ring(11.5, 15, 4, 2.5, 1, 'y')
    c.recolor('y', 'a', (0, 12, 23, 14))
    c.px(11, 17, 'y').px(12, 17, 'y')
    c.rect(8, 22, 10, 22, 'c').rect(13, 22, 15, 22, 'c')


# ============================== AIR ==============================
@sprite('Goosebumpy')
def _(c):
    c.ell(13.5, 15, 7.5, 5, 'a')
    c.poly([(19, 13), (23, 10), (22, 15)], 'a')
    c.line(9, 14, 6, 6, 'a', 2)
    c.ell(6, 4.5, 3, 2.6, 'a')
    c.poly([(3, 4), (0, 5.5), (3, 6.5)], 'f')
    c.rect(11, 20, 11, 22, 'f')
    c.rect(16, 20, 16, 22, 'f')
    c.outline()
    for x, y in [(11, 12), (14, 13), (17, 12), (12, 16), (15, 16), (18, 15), (7, 9), (8, 12)]:
        c.px(x, y, 'b')
    c.stamp(13, 13, ['.yy.', 'yyyy'][::-1])
    c.px(14, 13, 'k')
    c.eye(5, 3, 'wide', look=-1)
    c.stamp(10, 22, ['kkk']).stamp(15, 22, ['kkk'])
    c.stamp(0, 12, ['k', '.', 'k', '.', 'k'])
    c.stamp(23, 4, ['k', '.', 'k'])


@sprite('Papairplane')
def _(c):
    c.poly([(1, 7), (22.5, 12), (6, 13)], 'a')
    c.poly([(6, 13), (22.5, 12), (3, 19)], 'b')
    c.outline()
    c.line(6, 13, 22, 12, 'k')
    for y in (9, 11):
        c.line(3, y, 15, y + 1, 'q')
    c.line(5, 16, 14, 14, 'q')
    c.line(4, 8, 6, 18, 'r')
    c.eye(15, 11, 'big').eye(18, 11, 'big')
    c.stamp(1, 21, ['k.k.k'])


@sprite('Paperjet')
def _(c):
    c.poly([(0.5, 11), (12, 9), (22.5, 12), (12, 15)], 'a')
    c.poly([(7, 11), (14, 2), (16, 11)], 'b')
    c.poly([(7, 13), (14, 22), (16, 13)], 'b')
    c.poly([(1, 11), (3, 6), (5, 11)], 'b')
    c.outline()
    for x in range(10, 15):
        c.px(x, 6 + (14 - x) // 2, 'q')
    c.line(1, 12, 21, 12, 'k')
    c.shades(15, 10, 5)
    c.stamp(0, 15, ['f.k', '.fk'])
    c.px(1, 9, 'f')


@sprite('Balloonatic')
def _(c):
    c.ell(11.5, 8.5, 7.5, 8, 'a')
    c.poly([(10, 16), (13, 16), (14, 19), (9, 19)], 'a')
    c.outline()
    for i, y in enumerate(range(20, 24)):
        c.px(11 + (1 if i % 2 else -1), y, 'k')
    c.stamp(14, 19, ['.k.', 'k.k'])
    c.stamp(6, 2, ['cc', 'c.', 'c.'])
    c.eye(7, 6, 'wide').eye(14, 7, 'big', look=-1)
    c.brow(7, 4, 'R', 3)
    c.stamp(8, 11, ['k......k', '.kwwwwk.', '..kkmk..'])


@sprite('Foamfalcon')
def _(c):
    c.poly([(16, 9), (22, 3), (22, 9)], 'c')
    c.poly([(16, 15), (22, 21), (22, 15)], 'c')
    c.poly([(8, 10), (11, 2), (16, 3), (14, 10)], 'a')
    c.rect(5, 9, 19, 15, 'a')
    c.ell(3, 12, 2.4, 3.6, 'c')
    c.poly([(8, 14), (12, 22), (16, 21), (14, 14)], 'a')
    c.outline()
    for x, y in [(9, 4), (12, 6), (14, 4), (11, 17), (13, 19), (8, 11), (17, 13), (15, 11)]:
        c.px(x, y, 'b')
    c.rect(16, 9, 16, 15, 'k')
    c.eye(7, 10, 'big', look=-1)
    c.brow(6, 9, 'R', 3)
    c.stamp(6, 13, ['kkk'])


@sprite('Kitedelic')
def _(c):
    c.poly([(11.5, 0.5), (20.5, 8), (11.5, 18.5), (2.5, 8)], 'a')
    c.poly([(11.5, 0.5), (20.5, 8), (11.5, 8)], 'b')
    c.poly([(2.5, 8), (11.5, 8), (11.5, 18.5)], 'c')
    c.outline()
    c.poly([(11.5, 8), (20.5, 8), (11.5, 18.5)], 'm')
    c.line(11, 1, 11, 18, 't').line(3, 8, 20, 8, 't')
    c.eye(7, 5, 'shut').eye(13, 5, 'shut')
    c.stamp(8, 10, ['k....k', '.kkkk.'])
    pts = [(12, 19), (14, 20), (16, 19), (18, 20), (19, 22), (21, 21), (22, 19), (21, 17), (19, 17)]
    for x, y in pts:
        c.px(x, y, 'k')
    c.stamp(15, 20, ['r.r', '.r.']).stamp(20, 22, ['y'])


@sprite('Dustbunnie')
def _(c):
    c.ell(8, 6, 1.8, 5, 'a')
    c.ell(15, 6, 1.8, 5, 'a')
    c.ell(11.5, 15, 7.5, 6.2, 'a')
    for a in range(0, 360, 30):
        x = 11.5 + 8.6 * math.cos(math.radians(a))
        y = 15 + 7.2 * math.sin(math.radians(a))
        if y < 21:
            c.px(x, y, 'a')
    c.outline()
    c.line(8, 3, 8, 8, 'b').line(15, 3, 15, 8, 'b')
    c.eye(8, 13, 'sleepy').eye(13, 13, 'sleepy')
    c.stamp(10, 16, ['.kk.'])
    c.px(6, 17, 'm').px(17, 17, 'm')
    c.px(15, 19, 'y').px(5, 12, 'b').px(18, 14, 'b')


@sprite('Dustbeast')
def _(c):
    c.line(3, 13, 0, 18, 'a', 2)
    c.line(20, 13, 23, 18, 'a', 2)
    c.ell(11.5, 13.5, 9.5, 8, 'a')
    for a in range(0, 360, 20):
        c.px(11.5 + 10.6 * math.cos(math.radians(a)), 13.5 + 9 * math.sin(math.radians(a)), 'a')
    c.outline()
    c.stamp(0, 19, ['k.k.']).stamp(20, 19, ['.k.k'])
    c.brow(5, 7, 'L', 4).brow(14, 7, 'R', 4)
    c.stamp(6, 9, ['rr', 'rk']).stamp(16, 9, ['rr', 'kr'])
    c.rect(6, 14, 17, 17, 'k')
    for x in (7, 9, 14, 16):
        c.px(x, 14, 'w')
        c.px(x + 1, 17, 'w')
    c.stamp(16, 15, ['ww', 'rr', 'ww'])
    c.px(4, 19, 'y').px(13, 21, 'y').px(19, 5, 'b')


@sprite('Cloudsurf')
def _(c):
    c.ell(19, 4, 3.5, 3.5, 'f')
    c.poly([(1, 20), (4, 17), (20, 15), (23, 16), (20, 19), (4, 21)], 'c')
    c.ell(7, 11, 4.5, 4, 'a')
    c.ell(12, 8, 5, 5, 'a')
    c.ell(17, 11.5, 4, 3.6, 'a')
    c.rect(5, 11, 19, 14, 'a')
    c.outline()
    c.line(5, 19, 20, 17, 'r')
    c.recolor('a', 'b', (0, 13, 23, 15))
    c.shades(8, 9, 9)
    c.stamp(11, 12, ['k..k', '.kk.'])
    c.stamp(0, 21, ['qq.q', '.qqq'])
    c.px(23, 18, 'q').px(22, 20, 'q')


@sprite('Aquanetta')
def _(c):
    c.poly([(4, 9), (2, 3), (5, 5), (6, 0), (9, 3), (12, 0), (14, 3), (17, 0), (18, 4), (21, 2), (20, 8)], 'c')
    c.ell(11.5, 10, 5.5, 4.5, 'a')
    c.ell(11.5, 17, 6, 5, 'a')
    c.poly([(4, 11), (0.5, 12), (4, 13)], 'f')
    c.rect(9, 21, 9, 22, 'f').rect(14, 21, 14, 22, 'f')
    c.rect(17, 13, 19, 18, 'w')
    c.outline()
    c.ell(11.5, 18, 3.5, 3, 'b')
    c.rect(17, 12, 19, 12, 'k')
    c.px(18, 14, 'r').px(18, 15, 'r')
    c.stamp(20, 10, ['q.q', '.q.', 'q.q'])
    c.eye(6, 9, 'big', look=-1).eye(10, 9, 'big', look=-1)
    c.stamp(6, 8, ['k.k', '...']).stamp(10, 8, ['k.k'])
    for x in range(4, 20, 3):
        c.px(x, 4, 'm')


@sprite('Parachutie')
def _(c):
    c.line(9, 10, 4, 4, 'b', 2)
    c.ell(11.5, 5, 3.5, 3.5, 'b')
    c.rect(9, 8, 14, 11, 'c')
    c.poly([(8, 11), (15, 11), (21, 16), (19, 22), (14, 21), (11.5, 18), (9, 21), (4, 22), (2, 16)], 'a')
    c.line(15, 10, 18, 12, 'b', 2)
    c.rect(4, 22, 7, 22, 'k').rect(16, 22, 19, 22, 'k')
    c.ell(8.5, 1.5, 1.6, 1.6, 'b').ell(14.5, 1.5, 1.6, 1.6, 'b')
    c.outline()
    c.px(8, 1, 'm').px(14, 1, 'm')
    c.eye(10, 4, 'big').eye(13, 4, 'big')
    c.stamp(11, 7, ['kk'])
    c.line(11, 12, 11, 17, 'k')
    c.stamp(4, 15, ['bbb', 'b.b']).stamp(17, 15, ['bbb', 'b.b'])
    c.rect(8, 11, 15, 11, 'm')


@sprite('Parachuteor')
def _(c):
    c.line(7, 9, 2, 6, 'b', 2)
    c.line(16, 9, 21, 6, 'b', 2)
    c.ell(1.5, 5.5, 1.4, 1.4, 'b').ell(22, 5.5, 1.4, 1.4, 'b')
    c.ell(11.5, 4.5, 3.8, 3.8, 'b')
    c.rect(8, 8, 15, 11, 'c')
    c.poly([(7, 11), (16, 11), (22, 17), (21, 22), (15, 21), (11.5, 16), (8, 21), (2, 22), (1, 17)], 'a')
    c.poly([(8, 2), (8, -1), (10.5, 1)], 'b').poly([(15, 2), (15, -1), (12.5, 1)], 'b')
    c.outline()
    c.shades(9, 3, 6)
    c.stamp(10, 6, ['...k', 'kkk.'])
    c.ring(11.5, 9, 3, 2, 1, 'y')
    c.recolor('y', 'c', (0, 0, 23, 8))
    c.rect(7, 11, 16, 11, 'm')
    for x, y in [(4, 15), (18, 15)]:
        c.stamp(x, y, ['bbb', 'b.b'])
    c.px(0, 4, 'k').px(23, 4, 'k')


@sprite('Twistorm')
def _(c):
    rows = [(1, 10), (4, 9), (7, 8), (10, 6.5), (13, 5), (16, 3.6), (19, 2.4), (21, 1.4)]
    for i, (y, rx) in enumerate(rows):
        c.ell(11.5 + (1.5 if i % 2 else -1.5) * (i / 7), y + 1, rx, 1.8, 'a')
    c.outline()
    for i, (y, rx) in enumerate(rows):
        c.line(11.5 - rx + 2, y + 2, 11.5 + rx - 3, y + 1, 'b')
    for x, y, col in [(4, 2, 'r'), (17, 2, 'q'), (8, 8, 'y'), (15, 11, 'g'), (11, 15, 'r'), (7, 5, 'g')]:
        c.stamp(x, y, [col + col, col + col])
    c.stamp(8, 4, ['k.k', '.k.', 'k.k']).stamp(13, 4, ['k.k', '.k.', 'k.k'])
    c.stamp(10, 8, ['.kk.', 'k..k'])
    c.px(1, 12, 'k').px(21, 14, 't').px(3, 18, 't')


# ============================== ROCK ==============================
@sprite('Moonbootle')
def _(c):
    c.poly([(5, 2), (14, 2), (14, 13), (21, 14), (22, 18), (4, 18)], 'a')
    c.rect(3, 18, 22, 21, 'c')
    c.outline()
    for y in (6, 10, 14):
        c.line(5, y, 13, y, 'b')
    c.line(15, 14, 15, 17, 'b').line(18, 15, 18, 17, 'b')
    for x in range(4, 22, 3):
        c.px(x, 21, 'k')
    c.rect(4, 2, 14, 2, 'w')
    c.stamp(7, 3, ['w.w.w'])
    c.eye(6, 7, 'big').eye(10, 7, 'big')
    c.brow(6, 5, 'R').brow(10, 5, 'R')
    c.stamp(7, 11, ['kwwk', '.kk.'])
    for x, y in [(19, 4), (22, 9), (17, 0)]:
        sparkle(c, x, y, 'y', 'w')
    c.px(0, 22, 'k').px(2, 23, 'k')


@sprite('Blowcart')
def _(c):
    c.rect(2, 9, 5, 12, 'a')
    c.rect(18, 9, 21, 12, 'a')
    c.rect(5, 1, 18, 18, 'a')
    c.rect(7, 18, 16, 19, 'a')
    c.rect(7, 20, 8, 22, 'a').rect(15, 20, 16, 22, 'a')
    c.outline()
    for x in range(6, 18, 2):
        c.px(x, 1, 'b')
    c.rect(7, 4, 16, 12, 'c')
    for x in range(8, 16, 2):
        c.px(x, 19, 'F')
    c.eye(8, 6, 'big').eye(13, 6, 'big')
    c.stamp(10, 9, ['.kk.', 'k..k', '.kk.'])
    c.px(8, 10, 'm').px(15, 10, 'm')
    c.stamp(9, 14, ['bbbbbb'])
    c.stamp(0, 15, ['w.w', '.ww', 'w..'])
    c.stamp(20, 15, ['w.w', 'ww.', '..w'])


@sprite('Boomboxer')
def _(c):
    c.ell(1.5, 13, 1.6, 2.2, 'c')
    c.ell(22, 13, 1.6, 2.2, 'c')
    c.line(3, 13, 5, 13, 'a', 2)
    c.line(18, 13, 20, 13, 'a', 2)
    c.rect(4, 6, 19, 19, 'a')
    c.rect(6, 2, 17, 3, 'b')
    c.rect(6, 2, 7, 6, 'b').rect(16, 2, 17, 6, 'b')
    c.rect(6, 20, 7, 22, 'a').rect(16, 20, 17, 22, 'a')
    c.outline()
    for cx in (8, 15):
        c.ell(cx, 12, 3, 3, 'b')
        c.ell(cx, 12, 1.5, 1.5, 'k')
        c.px(cx - 1, 11, 'w')
    c.rect(9, 7, 14, 8, 'q')
    c.rect(9, 16, 14, 18, 'k')
    c.px(10, 17, 'w').px(13, 17, 'w')
    c.brow(5, 8, 'L', 3).brow(16, 8, 'R', 3)
    c.stamp(0, 4, ['.k', 'k.', '.k'])


@sprite('Brickphone')
def _(c):
    c.rect(14, 0, 15, 5, 'a')
    c.line(7, 13, 3, 17, 'a', 2)
    c.line(16, 13, 20, 9, 'a', 2)
    c.rect(7, 5, 16, 21, 'a')
    c.rect(8, 22, 9, 22, 'a').rect(14, 22, 15, 22, 'a')
    c.outline()
    c.rect(14, 0, 15, 0, 'r')
    c.rect(8, 7, 15, 11, 'c')
    c.eye(9, 8, 'big').eye(13, 8, 'big')
    c.stamp(10, 10, ['kkk'])
    for y in range(13, 21, 2):
        for x in (9, 11, 13):
            c.rect(x, y, x + 1, y, 'b')
    c.px(21, 8, 'k').px(22, 7, 'k')


@sprite('Petrock')
def _(c):
    c.poly([(5, 12), (8, 6), (13, 5), (18, 8), (19, 13), (5, 13)], 'a')
    c.rect(2, 13, 21, 21, 't')
    c.outline()
    c.stamp(3, 12, ['F.FF.F..F.F.FF.F.F'])
    c.rect(3, 14, 20, 14, 'k')
    for x in (6, 11, 16):
        c.px(x, 17, 'k')
    c.stamp(7, 7, ['www.www', 'wkw.wwk', 'www.www'])
    c.px(15, 6, 'b').px(16, 7, 'b')
    c.stamp(9, 19, ['F.F'])


@sprite('Petrocksteady')
def _(c):
    c.poly([(3, 15), (5, 6), (11, 3), (18, 4), (21, 10), (20, 15)], 'a')
    c.rect(4, 17, 19, 22, 'v')
    c.outline()
    c.rect(4, 17, 19, 17, 'k')
    c.shades(6, 8, 13)
    c.stamp(10, 11, ['....k', 'kkkk.'])
    c.ring(12, 13, 5, 3, 1, 'y')
    c.recolor('y', 'a', (0, 0, 23, 12))
    c.px(12, 16, 'y')
    c.px(15, 5, 'b').px(17, 6, 'b').px(7, 13, 'b')
    c.stamp(5, 19, ['m.m.m.m.m.m.m.m'])


@sprite('Gargoylie')
def _(c):
    c.poly([(7, 9), (0.5, 3), (2, 10), (0.5, 14), (6, 13)], 'a')
    c.poly([(16, 9), (22.5, 3), (21, 10), (22.5, 14), (17, 13)], 'a')
    c.ell(11.5, 14.5, 5, 4.5, 'a')
    c.ell(11.5, 7.5, 4.5, 4, 'a')
    c.poly([(8, 5), (7, 0), (10, 4)], 'a')
    c.poly([(15, 5), (16, 0), (13, 4)], 'a')
    c.rect(1, 19, 22, 22, 'b')
    c.outline()
    c.line(1, 20, 22, 20, 'k')
    for x in range(3, 22, 5):
        c.px(x, 21, 'k')
    c.line(2, 6, 4, 11, 'b').line(21, 6, 19, 11, 'b')
    c.brow(8, 5, 'L', 3).brow(13, 5, 'R', 3)
    c.stamp(9, 7, ['c', 'k']).stamp(14, 7, ['c', 'k'])
    c.stamp(10, 10, ['kwwk'])
    c.stamp(8, 17, ['k.k...k.k'])


@sprite('Cassettle')
def _(c):
    c.rect(3, 5, 20, 18, 'a')
    c.poly([(6, 18), (17, 18), (16, 21), (7, 21)], 'a')
    c.rect(6, 22, 7, 22, 'a').rect(16, 22, 17, 22, 'a')
    c.outline()
    c.rect(4, 6, 19, 10, 'c')
    c.stamp(5, 7, ['kk.kkk.kk'])
    for cx in (8, 15):
        c.ell(cx, 14, 2.4, 2.4, 'b')
        c.ell(cx, 14, 0.9, 0.9, 'k')
        c.px(cx - 1, 13, 'w')
    c.rect(11, 13, 12, 15, 'k')
    c.brow(6, 11, 'L').brow(15, 11, 'R')
    c.px(9, 20, 'k').px(14, 20, 'k')


@sprite('Cassettitan')
def _(c):
    c.line(2, 18, 0, 22, 't', 1)
    c.line(4, 19, 3, 23, 't', 1)
    c.rect(1, 4, 22, 18, 'a')
    c.poly([(5, 18), (18, 18), (17, 21), (6, 21)], 'a')
    c.line(15, 13, 21, 1, 'y', 2)
    c.outline()
    c.rect(2, 5, 21, 9, 'c')
    for cx in (7, 16):
        c.ell(cx, 13, 3, 3, 'b')
        c.ell(cx, 13, 1, 1, 'k')
    c.rect(21, 0, 22, 1, 'm')
    c.brow(4, 10, 'L', 3).brow(17, 10, 'R', 3)
    c.stamp(9, 16, ['kkkkkk', 'kwkwkk'])
    c.line(20, 14, 23, 19, 't')
    c.line(19, 18, 22, 23, 't')
    c.line(1, 14, 0, 17, 't')


@sprite('Blockstack')
def _(c):
    cells = {(3, 1): 'c', (3, 2): 'c', (3, 3): 'c', (3, 4): 'c',
             (0, 3): 'b', (1, 3): 'b', (2, 3): 'b', (1, 2): 'b',
             (0, 4): 'a', (1, 4): 'a', (2, 4): 'a', (2, 5): 'a', (3, 5): 'a', (4, 5): 'a', (4, 4): 'a'}
    ox, oy = 2, 0
    for (gx, gy), col in cells.items():
        x, y = ox + gx * 4, oy + gy * 4 - 1
        c.rect(x, y, x + 3, y + 3, col)
    c.outline()
    for (gx, gy), col in cells.items():
        x, y = ox + gx * 4, oy + gy * 4 - 1
        c.line(x + 3, y, x + 3, y + 3, 'k').line(x, y + 3, x + 3, y + 3, 'k')
        c.px(x, y, 'w')
    c.stamp(4, 12, ['wk..wk', 'kk..kk'])
    c.stamp(5, 16, ['kwwk'])
    c.stamp(14, 7, ['k', 'k'])


# ============================== BUG ==============================
@sprite('Pixelpest')
def _(c):
    c.line(8, 4, 5, 0, 'a')
    c.line(15, 4, 18, 0, 'a')
    c.ell(11.5, 12.5, 8, 9.5, 'a')
    for y in (10, 14, 18):
        c.line(3, y, 0, y + 2, 'a').line(20, y, 23, y + 2, 'a')
    c.outline()
    c.ring(11.5, 1.5, 1.8, 1.8, 1, 'n')
    c.rect(6, 6, 17, 14, 'k')
    c.rect(7, 7, 16, 13, 'b')
    c.stamp(9, 8, ['k....k', '.kkkk.', 'kwkkwk', '.kkkk.', 'k.kk.k'])
    for x in (8, 11, 14):
        c.ell(x + 0.5, 17.5, 1, 1, 'c')
    c.px(4, 9, 'b').px(5, 7, 'b')


@sprite('Anklehop')
def _(c):
    c.ring(5, 19, 3.5, 2.5, 1.5, 'b')
    c.ell(14, 9, 7, 7, 'a')
    for i in range(3):
        c.line(9 + i * 4, 15, 8 + i * 4, 18, 'a')
    c.outline()
    c.line(8, 17, 12, 14, 'c')
    c.rect(9, 19, 13, 21, 'k')
    c.stamp(10, 20, ['zz.'])
    c.line(13, 19, 13, 16, 'c')
    c.eye(11, 7, 'big').eye(16, 7, 'big')
    c.stamp(12, 11, ['kwwk', '.kk.'])
    c.line(13, 2, 11, 0, 'k').line(16, 2, 18, 0, 'k')
    c.px(9, 4, 'b').px(10, 3, 'b')


@sprite('Anklehopper')
def _(c):
    c.ring(4.5, 19, 3.5, 2.6, 1.5, 'b')
    c.ell(14, 9.5, 8, 8, 'a')
    c.outline()
    c.line(7, 18, 11, 16, 'c').line(11, 16, 13, 18, 'c')
    c.rect(12, 18, 20, 22, 'k')
    c.stamp(13, 19, ['F.F.F', 'FFFFF', 'F.F.F'][1:2] + ['F.F.F'])
    c.eye(10, 7, 'big').eye(16, 7, 'big', look=-1)
    c.brow(9, 5, 'L', 3).brow(16, 5, 'R', 3)
    c.stamp(12, 12, ['kkkk', 'kwwk'])
    c.rect(16, 2, 19, 3, 'w').px(17, 2, 'r')
    for x, y in [(0, 6), (1, 4), (3, 2), (22, 14), (23, 11)]:
        c.px(x, y, 'k')
    c.line(13, 2, 11, 0, 'k')


@sprite('Mothballer')
def _(c):
    c.poly([(11, 8), (1, 2), (0.5, 12), (10, 13)], 'a')
    c.poly([(13, 8), (23, 2), (23.5, 12), (14, 13)], 'a')
    c.poly([(11, 13), (3, 14), (5, 21), (11, 17)], 'a')
    c.poly([(13, 13), (21, 14), (19, 21), (13, 17)], 'a')
    c.ell(12, 12, 2.4, 6, 'b')
    c.ell(12, 5, 2.6, 2.4, 'b')
    c.outline()
    for cx, cy in [(5, 7), (19, 7), (7, 16), (17, 16)]:
        c.stamp(cx - 1, cy - 1, ['.c.', 'ctc', '.c.'])
    c.line(10, 3, 7, 0, 't').line(14, 3, 17, 0, 't')
    c.px(6, 0, 't').px(18, 0, 't')
    c.stamp(10, 4, ['k.k', '...', '.k.'][:1])
    c.stamp(11, 6, ['k'])
    for x, y in [(1, 21), (21, 22), (3, 23)]:
        c.ring(x, y, 1, 1, 1, 'c')


@sprite('Captula')
def _(c):
    for s in (-1, 1):
        for i, (dx, dy) in enumerate([(4, -3), (5, 0), (5, 3), (4, 6)]):
            x0, y0 = 11.5 + s * 3, 12 + i - 1
            c.line(x0, y0, x0 + s * dx, y0 + dy - 3, 'a', 1)
            c.line(x0 + s * dx, y0 + dy - 3, x0 + s * (dx + 2), y0 + dy + 1, 'a', 1)
    c.ell(11.5, 12, 5, 5, 'a')
    c.ell(11.5, 6, 3.4, 3, 'a')
    c.ell(11.5, 20, 5, 1.6, 'b')
    c.ell(11.5, 18.5, 5, 1.6, 'b')
    c.outline()
    c.ring(11.5, 18.5, 4, 1, 1, 'k')
    for x, y in [(9, 10), (14, 11), (11, 14), (8, 13), (15, 14)]:
        c.px(x, y, 'b')
    c.eye(9, 5, 'big').eye(13, 5, 'big')
    c.brow(8, 3, 'L').brow(13, 3, 'R')
    c.stamp(10, 8, ['w..w'])


@sprite('Rantz')
def _(c):
    c.ell(18, 15, 4.5, 4, 'a')
    c.ell(12, 13, 2.6, 2.2, 'a')
    c.ell(7, 10, 3.6, 3.4, 'a')
    c.poly([(1, 7), (4, 9), (4, 13), (1, 15)], 'w')
    for x in (11, 13, 15):
        c.line(x, 15, x - 2, 21, 'a')
    c.outline()
    c.rect(0, 7, 0, 15, 'r')
    c.line(6, 7, 4, 1, 'k').line(8, 7, 10, 1, 'k')
    c.eye(6, 9, 'big', look=-1)
    c.brow(5, 7, 'R', 3)
    c.stamp(5, 12, ['kk'])
    for x, y in [(0, 3), (0, 19), (2, 21)]:
        c.px(x, y, 'k')
    c.stamp(20, 6, ['k.k', '.k.'])
    c.px(17, 13, 'b').px(19, 12, 'b')


@sprite('Butterclip')
def _(c):
    c.poly([(10, 11), (2, 2), (0.5, 9), (4, 13), (1, 18), (6, 21), (10, 14)], 'a')
    c.poly([(13, 11), (21, 2), (22.5, 9), (19, 13), (22, 18), (17, 21), (13, 14)], 'a')
    c.ell(11.5, 12, 2, 7, 'b')
    c.outline()
    for x, y in [(4, 6), (19, 6), (4, 16), (18, 17), (7, 10), (16, 10)]:
        c.px(x, y, 'c')
    for y in range(4, 20, 2):
        if c.get(2, y) == 'a':
            c.px(1, y, 'k')
        if c.get(21, y) == 'a':
            c.px(22, y, 'k')
    c.eye(10, 8, 'dot').eye(13, 8, 'dot')
    c.stamp(11, 10, ['kk'])
    c.line(10, 5, 8, 1, 'k').line(13, 5, 15, 1, 'k')
    c.line(0, 23, 23, 20, 't')


@sprite('Flutterclip')
def _(c):
    c.poly([(10, 12), (1, 1), (0.5, 12), (10, 15)], 'a')
    c.poly([(13, 12), (22, 1), (22.5, 12), (13, 15)], 'a')
    c.poly([(10, 15), (2, 15), (5, 22), (10, 18)], 'b')
    c.poly([(13, 15), (21, 15), (18, 22), (13, 18)], 'b')
    c.ell(11.5, 12, 2.2, 7, 'c')
    c.outline()
    for x in range(2, 10, 2):
        c.px(x, 13, 'w').px(23 - x, 13, 'w')
    c.line(1, 12, 9, 12, 'k').line(14, 12, 22, 12, 'k')
    c.eye(10, 7, 'dot').eye(13, 7, 'dot')
    c.brow(9, 5, 'L').brow(13, 5, 'R')
    c.stamp(10, 9, ['kwwk'])
    for x, y in [(4, 4), (18, 5), (6, 9), (17, 9)]:
        sparkle(c, x - 1, y - 1, 'y', 'w')


@sprite('Ladybugsy')
def _(c):
    c.ell(11.5, 15, 8.5, 7, 'a')
    c.ell(11.5, 8, 4.6, 3.2, 'k')
    c.rect(5, 2, 18, 4, 'k')
    c.rect(2, 5, 21, 5, 'k')
    for x in (6, 17):
        c.rect(x - 2, 20, x - 1, 22, 'k')
    c.outline()
    c.rect(6, 4, 17, 4, 'r')
    c.line(11.5, 10, 11.5, 22, 'k')
    for x, y in [(6, 13), (16, 12), (7, 18), (16, 18), (9, 15), (14, 15)]:
        c.stamp(x - 1, y - 1, ['kk', 'kk'])
    c.stamp(8, 7, ['wkw.wkw'][:1])
    c.stamp(8, 7, ['ww.ww'])
    c.px(9, 7, 'k').px(13, 7, 'k')
    c.line(12, 10, 16, 9, 'c')
    c.px(16, 9, 'F')


@sprite('Spicearachnid')
def _(c):
    for s in (-1, 1):
        for i in range(4):
            x0, y0 = 11.5 + s * 3, 11 + i
            c.line(x0, y0, x0 + s * 5, y0 - 3 + i, 'a')
            c.line(x0 + s * 5, y0 - 3 + i, x0 + s * 7, y0 + 4 + i // 2, 'a')
    c.ell(11.5, 15, 4.6, 4.2, 'a')
    c.ell(11.5, 8, 4, 3.6, 'a')
    c.ell(5.5, 6, 2, 2.4, 'c')
    c.ell(17.5, 6, 2, 2.4, 'c')
    c.rect(3, 19, 6, 22, 'b')
    c.rect(17, 19, 20, 22, 'b')
    c.outline()
    c.stamp(9, 7, ['wk.wk', 'kk.kk'])
    c.stamp(10, 10, ['kwk'])
    sparkle(c, 10, 13, 'y', 'w')
    c.rect(3, 22, 6, 22, 'v').rect(17, 22, 20, 22, 'v')
    c.px(10, 4, 'v').px(13, 4, 'v')


@sprite('Cicadaboom')
def _(c):
    c.poly([(11, 8), (3, 9), (1, 18), (9, 20)], 'b')
    c.poly([(13, 8), (21, 9), (23, 18), (15, 20)], 'b')
    c.ell(12, 14, 3.5, 7.5, 'a')
    c.ell(12, 5, 5, 3, 'a')
    c.outline()
    for cx, cy in [(6, 14), (18, 14)]:
        c.ell(cx, cy, 3, 3, 'n')
        c.ell(cx, cy, 1.5, 1.5, 'c')
        c.px(cx, cy, 'k')
    c.stamp(7, 4, ['rr', 'rk']).stamp(16, 4, ['rr', 'kr'])
    c.stamp(10, 6, ['kwwk'])
    for y in range(11, 20, 2):
        c.line(11, y, 13, y, 'L')
    c.stamp(0, 2, ['.k', 'k.', '.k']).stamp(22, 2, ['k.', '.k', 'k.'])


# ============================== GRASS ==============================
@sprite('Sproutpup')
def _(c):
    c.ell(12.5, 15, 6.5, 5, 'a')
    c.ell(7, 10, 4.6, 4, 'a')
    c.poly([(3, 10), (0.5, 12), (3, 13)], 'a')
    c.poly([(9, 7), (12, 3), (12, 9)], 'a')
    c.rect(7, 18, 8, 22, 'a').rect(16, 18, 17, 22, 'a')
    c.line(18, 13, 22, 9, 'a', 2)
    for x in range(8, 19, 2):
        c.poly([(x, 11), (x + 1, 6 + (x % 3)), (x + 2, 11)], 'b')
    c.outline()
    for x in range(8, 19, 3):
        c.px(x + 1, 9, 'c')
    c.px(0, 12, 'k')
    c.eye(5, 9, 'big', look=-1)
    c.stamp(2, 13, ['k.kk'])
    c.px(20, 3, 'q').px(21, 5, 'q').px(15, 2, 'q')
    c.px(11, 16, 't').px(14, 17, 't')


@sprite('Footbaggle')
def _(c):
    c.line(4, 10, 1, 6, 'a', 2)
    c.line(19, 10, 22, 6, 'a', 2)
    c.ell(11.5, 9, 7.5, 7.5, 'a')
    c.rect(8, 17, 9, 19, 'a').rect(14, 17, 15, 19, 'a')
    c.rect(6, 20, 10, 21, 'w').rect(13, 20, 17, 21, 'w')
    c.outline()
    for y in range(3, 16, 3):
        for x in range(5, 19, 3):
            if c.get(x, y) == 'a' and c.get(x + 1, y + 1) == 'a':
                c.stamp(x, y, ['b.', '.b'])
    c.ring(11.5, 9, 7.5, 7.5, 1, 'c')
    c.ring(11.5, 9, 5, 5, 1, 'y')
    c.eye(8, 7, 'sleepy').eye(13, 7, 'sleepy')
    c.stamp(10, 10, ['k..k', '.kk.'])
    c.rect(6, 21, 10, 21, 'r').rect(13, 21, 17, 21, 'r')
    c.stamp(16, 22, ['k.k.k'])


@sprite('Fuzzpuff')
def _(c):
    cols = 'abc'
    for i, a in enumerate(range(0, 360, 15)):
        r = 10.5 if i % 2 == 0 else 8.5
        x = 11.5 + r * math.cos(math.radians(a))
        y = 11.5 + r * math.sin(math.radians(a))
        c.line(11.5, 11.5, x, y, cols[i % 3])
    c.ell(11.5, 11.5, 4.5, 4.5, 'a')
    c.outline()
    c.eye(9, 10, 'big').eye(13, 10, 'big')
    c.stamp(10, 13, ['kwwk'])


@sprite('Fuzznado')
def _(c):
    cols = 'abc'
    for i in range(36):
        t = i / 36 * 2 * math.pi
        r = 3 + i * 0.22
        x = 11.5 + r * math.cos(t * 2)
        y = 11.5 + r * math.sin(t * 2) * 0.9
        x2 = 11.5 + (r + 2.5) * math.cos(t * 2 + 0.6)
        y2 = 11.5 + (r + 2.5) * math.sin(t * 2 + 0.6) * 0.9
        c.line(x, y, x2, y2, cols[i % 3])
    c.ell(11.5, 11.5, 4, 4, 'a')
    c.outline()
    c.eye(9, 10, 'x').eye(13, 10, 'x')
    c.stamp(10, 14, ['kkkk'])


@sprite('Cabbagebaby')
def _(c):
    c.ell(11.5, 7, 7.5, 6.5, 'a')
    for a in range(0, 360, 40):
        c.ell(11.5 + 6.5 * math.cos(math.radians(a)), 7 + 5.5 * math.sin(math.radians(a)), 2.4, 2.4, 'a')
    c.ell(11.5, 8.5, 4.5, 3.8, 'c')
    c.rect(7, 13, 16, 20, 'b')
    c.rect(8, 21, 10, 22, 'c').rect(13, 21, 15, 22, 'c')
    c.line(7, 15, 3, 17, 'c', 2)
    c.rect(16, 14, 20, 19, 'w')
    c.outline()
    for a in range(20, 360, 40):
        c.line(11.5 + 4 * math.cos(math.radians(a)), 7 + 3 * math.sin(math.radians(a)),
               11.5 + 7.5 * math.cos(math.radians(a)), 7 + 6.5 * math.sin(math.radians(a)), 'b')
    c.ell(11.5, 8.5, 4, 3.3, 'c')
    c.eye(9, 7, 'big').eye(13, 7, 'big')
    c.stamp(10, 10, ['.kk.'])
    c.px(8, 10, 'm').px(15, 10, 'm')
    c.line(17, 15, 19, 15, 'k').line(17, 17, 19, 17, 'k')
    c.px(11, 16, 'w').px(12, 16, 'w')


@sprite('Dandylion')
def _(c):
    c.line(18, 15, 22, 10, 'c', 1)
    c.ell(14, 16, 6.5, 4.5, 'a')
    c.rect(9, 19, 10, 22, 'a').rect(17, 19, 18, 22, 'a')
    c.ell(7, 9.5, 7, 7, 'w')
    c.ell(7, 10, 3.6, 3.4, 'a')
    c.outline()
    for a in range(0, 360, 30):
        c.px(7 + 5.5 * math.cos(math.radians(a)), 9.5 + 5.5 * math.sin(math.radians(a)), 'b')
    c.ell(22, 9, 1.2, 1.2, 'w')
    c.eye(5, 9, 'sleepy', look=-1).eye(8, 9, 'sleepy')
    c.stamp(6, 12, ['k..k', '.kk.'])
    for x, y in [(17, 2), (20, 4), (15, 0), (22, 1)]:
        c.stamp(x, y, ['w', 'k'])


@sprite('Fruityfoot')
def _(c):
    c.poly([(5, 2), (14, 2), (15, 12), (21, 14), (22, 19), (19, 21), (4, 21), (3, 14)], 'a')
    for i, x in enumerate((14, 16.5, 19, 21)):
        c.ell(x, 13 - (0 if i else 1), 1.4, 1.6, 'a')
    c.outline()
    for y in range(3, 21, 3):
        c.line(4, y, 15, y + 1, 'b')
    c.line(3, 15, 21, 17, 'b')
    c.stamp(12, 1, ['ccc', '.cc', '..c'])
    c.eye(6, 6, 'big').eye(10, 6, 'big')
    c.stamp(7, 9, ['k..k', '.kk.'])
    c.stamp(5, 22, ['a.a...a'])


@sprite('Slimeon')
def _(c):
    c.poly([(5, 1), (18, 1), (16, 7), (7, 7)], 'c')
    c.ell(11.5, 15, 7, 6.5, 'a')
    c.poly([(6, 7), (17, 7), (20, 15), (18, 18), (17, 13), (15, 19), (13, 12), (11, 20), (9, 13), (7, 18), (5, 14), (3, 16)], 'b')
    c.outline()
    c.rect(5, 1, 18, 1, 'k')
    c.line(6, 4, 17, 4, 'k')
    c.px(11, 21, 'b').px(11, 22, 'b').px(5, 17, 'b')
    c.stamp(8, 14, ['wk...wk', 'kk...kk'])
    c.stamp(10, 17, ['kkk'])


@sprite('Weedwhack')
def _(c):
    c.line(15, 5, 7, 18, 'a', 2)
    c.rect(13, 1, 21, 7, 'c')
    c.rect(20, 3, 22, 5, 'c')
    c.ell(6, 19, 3.6, 1.6, 'a')
    c.outline()
    c.ring(6, 19, 5.5, 3, 1, 'w')
    for x, y in [(1, 14), (11, 15), (0, 22), (12, 22), (3, 12)]:
        c.stamp(x, y, ['b', 'L'])
    c.eye(15, 3, 'big').eye(18, 3, 'big')
    c.brow(14, 2, 'L').brow(18, 2, 'R')
    c.stamp(15, 6, ['kwwk'][:1])
    c.stamp(16, 6, ['kkk'])
    c.rect(10, 9, 11, 10, 'k')


@sprite('Fernbaby')
def _(c):
    c.ring(11.5, 7.5, 6, 6, 2.2, 'a')
    c.ell(11.5, 7.5, 2.2, 2.2, 'a')
    c.ell(11.5, 17, 3.5, 4.5, 'a')
    for s in (-1, 1):
        for i, y in enumerate((14, 17, 20)):
            c.poly([(11.5 + s * 2, y), (11.5 + s * (7 - i), y - 2), (11.5 + s * (6 - i), y + 1)], 'b')
    c.outline()
    c.line(17, 6, 14, 9, 'b').line(6, 6, 9, 9, 'b')
    c.stamp(9, 15, ['wk.wk', 'kk.kk'])
    c.stamp(10, 18, ['.k.', 'k.k'])
    c.px(9, 17, 'q').px(9, 18, 'q').px(14, 17, 'q').px(14, 19, 'q')
    c.rect(10, 22, 13, 22, 'c')


@sprite('Fernfury')
def _(c):
    for x in range(3, 21, 3):
        c.poly([(x, 9), (x + 1.5, 0.5 + (x % 2) * 2), (x + 3, 9)], 'b')
    c.ell(11.5, 13, 10, 7, 'a')
    c.rect(2, 18, 21, 21, 'c')
    c.rect(3, 22, 6, 22, 'c').rect(17, 22, 20, 22, 'c')
    c.outline()
    for x in range(4, 21, 3):
        c.line(x, 19, x, 21, 't')
    c.brow(5, 9, 'L', 4).brow(15, 9, 'R', 4)
    c.eye(6, 11, 'big').eye(16, 11, 'big', look=-1)
    c.rect(7, 15, 16, 16, 'k')
    for x in range(7, 17, 2):
        c.px(x, 15, 'w')
        c.px(x + 1, 16, 'w')
    c.line(0, 13, 2, 11, 'b').line(23, 13, 21, 11, 'b')


# ============================== TECHNO ==============================
@sprite('Zapdisk')
def _(c):
    c.rect(4, 3, 19, 20, 'a')
    c.rect(6, 21, 7, 22, 'a').rect(16, 21, 17, 22, 'a')
    c.outline()
    c.px(19, 3, '.').px(19, 4, '#').px(18, 3, '#')
    c.rect(7, 3, 15, 9, 'b')
    c.rect(12, 4, 14, 8, 'n')
    c.rect(6, 12, 17, 19, 'w')
    c.stamp(7, 13, ['kkk..kkk', 'kck..kck', 'kkk..kkk'])
    c.stamp(9, 17, ['k.k.k.'])
    for x, y in [(0, 6), (21, 12)]:
        c.stamp(x, y, ['.c', 'c.', 'cc', '.c', 'c.'])


@sprite('Roboruff')
def _(c):
    c.rect(19, 7, 19, 11, 'a')
    c.rect(8, 11, 19, 17, 'a')
    c.rect(2, 6, 10, 12, 'a')
    c.rect(3, 3, 4, 5, 'a').rect(8, 3, 9, 5, 'a')
    c.rect(1, 9, 2, 11, 'a')
    for x in (9, 12, 15, 18):
        c.rect(x, 18, x, 21, 'n')
        c.rect(x - 1, 22, x + 1, 22, 'a')
    c.outline()
    c.px(19, 6, 'c')
    c.rect(3, 7, 9, 9, 'k')
    c.rect(4, 8, 5, 8, 'c').rect(7, 8, 8, 8, 'c')
    c.line(3, 11, 7, 11, 'k')
    c.rect(11, 13, 16, 15, 'k')
    c.rect(12, 14, 12, 14, 'r')
    c.px(13, 14, 'n').px(14, 14, 'n').px(15, 14, 'n')
    c.px(17, 13, 'k').px(17, 14, 'k')
    c.px(9, 12, 'b').px(14, 12, 'b')


@sprite('Robowoof')
def _(c):
    c.poly([(19, 9), (22, 4), (21, 10)], 'a')
    c.rect(7, 10, 20, 17, 'a')
    c.rect(1, 4, 11, 12, 'a')
    c.poly([(2, 4), (3, 0), (5, 4)], 'a').poly([(8, 4), (10, 0), (11, 4)], 'a')
    c.rect(0, 9, 2, 13, 'a')
    for x in (8, 12, 15, 19):
        c.rect(x, 18, x + 1, 21, 'n')
        c.rect(x - 1, 22, x + 2, 22, 'a')
    c.outline()
    c.rect(2, 6, 10, 8, 'k')
    c.rect(3, 7, 9, 7, 'r')
    c.rect(1, 11, 7, 13, 'k')
    for x in (2, 4, 6):
        c.px(x, 11, 'w').px(x + 1, 13, 'w')
    c.rect(7, 10, 20, 10, 'k')
    for x in range(8, 21, 3):
        c.px(x, 9, 'w')
    c.stamp(12, 12, ['..cc.', '.cc..', 'cccc.', '..cc.', '.cc..'])
    c.px(21, 3, 'y').px(23, 6, 'y').px(13, 1, 'y').px(14, 2, 'y')


@sprite('Laserpouncer')
def _(c):
    c.line(19, 11, 22, 4, 'a', 2)
    c.poly([(5, 15), (11, 12), (19, 9), (21, 13), (17, 17), (8, 18)], 'a')
    c.ell(5.5, 14, 4.2, 3.6, 'a')
    c.poly([(2, 12), (2, 7), (5, 11)], 'a').poly([(6, 11), (8, 7), (9, 12)], 'a')
    c.rect(4, 18, 5, 21, 'a').rect(8, 18, 9, 21, 'a')
    c.rect(16, 16, 17, 21, 'a').rect(19, 14, 20, 21, 'a')
    c.outline()
    c.px(3, 9, 'b').px(7, 9, 'b')
    c.stamp(2, 13, ['wkk.wkk'][:1])
    c.stamp(2, 13, ['wk..wk']).stamp(2, 14, ['kk..kk'])
    c.stamp(4, 16, ['k.k'])
    c.ell(1, 21.5, 1, 0.8, 'c')
    c.px(0, 20, 'z').px(2, 22, 'z')
    for x, y in [(12, 11), (15, 10), (13, 15)]:
        c.px(x, y, 'b')


@sprite('Staticling')
def _(c):
    c.ell(11.5, 3.5, 4, 3.5, 'm')
    c.poly([(11, 7), (12, 7), (12.5, 8.5), (10.5, 8.5)], 'm')
    for i in range(-5, 6):
        x = 11.5 + i * 1.6
        c.line(11.5 + i * 0.6, 13, x, 9 + abs(i) * 0.5, 'a')
    c.ell(11.5, 16.5, 6.5, 5.5, 'a')
    c.outline()
    c.px(9, 2, 'w').px(10, 1, 'w')
    c.eye(8, 15, 'wide').eye(13, 15, 'wide', look=-1)
    c.stamp(10, 19, ['.kk.', 'k..k'])
    for x, y in [(3, 10), (20, 9), (2, 18), (21, 19)]:
        c.stamp(x, y, ['c.', '.c'])


@sprite('Statickle')
def _(c):
    for i in range(-6, 7):
        c.line(10 + i * 0.5, 9, 10 + i * 1.5, 1 + abs(i) * 0.6, 'a')
    c.ell(10, 13, 7, 6.5, 'a')
    c.line(16, 13, 20, 13, 'a', 2)
    c.rect(4, 19, 5, 22, 'a').rect(13, 19, 14, 22, 'a')
    c.ell(22, 13.5, 1.6, 1.6, 'y')
    c.outline()
    c.stamp(20, 9, ['.c', 'c.', '.c']).stamp(20, 16, ['c.', '.c', 'c.'])
    c.px(22, 11, 'c')
    c.brow(5, 10, 'L', 3).brow(10, 10, 'R', 3)
    c.eye(6, 12, 'big').eye(10, 12, 'big')
    c.stamp(6, 16, ['k.....k', '.kwwwk.'])


@sprite('Spellbot')
def _(c):
    c.line(3, 12, 0, 16, 'a', 2)
    c.line(20, 12, 23, 9, 'a', 2)
    c.rect(3, 4, 20, 21, 'a')
    c.rect(8, 1, 15, 4, 'a')
    c.rect(6, 22, 7, 22, 'a').rect(16, 22, 17, 22, 'a')
    c.outline()
    c.rect(10, 2, 13, 3, '.')
    c.rect(9, 1, 14, 1, '#')
    c.rect(5, 6, 18, 11, 'k')
    c.stamp(6, 7, ['c.c.ccc.ccc', 'cc..c.c..c.', 'c.c.ccc..c.', 'c.c.c.c..c.'])
    for y in range(13, 21, 2):
        for x in range(5, 19, 2):
            c.px(x, y, 'b')
    c.rect(17, 19, 18, 20, 'r')


@sprite('Glowpeg')
def _(c):
    c.rect(2, 2, 21, 19, 'n')
    c.rect(4, 4, 19, 17, 'a')
    c.rect(5, 20, 6, 22, 'n').rect(17, 20, 18, 22, 'n')
    c.outline()
    pegs = {(7, 7): 'b', (8, 7): 'b', (15, 7): 'b', (16, 7): 'b', (7, 8): 'q', (16, 8): 'q',
            (11, 10): 'r', (12, 10): 'r', (11, 11): 'r', (12, 11): 'r',
            (6, 13): 'c', (7, 14): 'c', (8, 15): 'c', (9, 15): 'c', (10, 15): 'c', (13, 15): 'c', (14, 15): 'c', (15, 15): 'c', (16, 14): 'c', (17, 13): 'c',
            (5, 5): 'z', (18, 5): 'z', (5, 16): 'y', (18, 16): 'y'}
    for (x, y), col in pegs.items():
        c.px(x, y, col)


@sprite('Glowpegger')
def _(c):
    c.poly([(1, 4), (22, 4), (22, 19), (1, 19)], 'n')
    c.poly([(0, 1), (4, 4), (2, 6)], 'n').poly([(23, 1), (19, 4), (21, 6)], 'n')
    c.rect(3, 6, 20, 17, 'a')
    c.rect(4, 20, 6, 22, 'n').rect(17, 20, 19, 22, 'n')
    c.outline()
    for (x, y) in [(6, 8), (7, 9), (8, 10), (15, 10), (16, 9), (17, 8)]:
        c.px(x, y, 'c')
    for x, y in [(7, 11), (16, 11)]:
        c.stamp(x - 1, y - 1, ['.b.', 'bwb', '.b.'])
    for x in range(6, 18):
        c.px(x, 14, 'b' if x % 2 else 'c')
    for x in range(7, 17, 2):
        c.px(x, 15, 'w')
    for x, y in [(4, 7), (19, 7), (4, 16), (19, 16), (11, 7), (12, 7)]:
        c.px(x, y, 'm')


@sprite('Snakebyte')
def _(c):
    path = [(3, 19), (7, 19), (11, 19), (15, 19), (19, 19), (19, 15), (15, 15), (11, 15), (7, 15), (7, 11), (11, 11), (15, 11), (15, 7)]
    for x, y in path:
        c.rect(x, y, x + 3, y + 3, 'b')
    c.rect(13, 2, 18, 7, 'b')
    c.outline()
    for x, y in path:
        c.line(x + 3, y, x + 3, y + 3, 'G').line(x, y + 3, x + 3, y + 3, 'G')
    c.stamp(14, 3, ['wk.wk', 'kk.kk'])
    c.line(18, 6, 21, 6, 'r').px(22, 5, 'r').px(22, 7, 'r')
    c.rect(4, 4, 6, 6, 'k')
    c.rect(4, 4, 4, 4, 'r')


@sprite('Electricslide')
def _(c):
    c.line(15, 9, 20, 2, 'a', 2)
    c.line(8, 12, 3, 15, 'a', 2)
    c.ell(11.5, 13, 6, 7, 'a')
    c.poly([(14, 18), (19, 18), (17, 20), (21, 23), (14, 21)], 'c')
    c.rect(7, 19, 8, 22, 'a')
    c.rect(5, 21, 9, 22, 't')
    c.outline()
    c.ell(11.5, 15, 3.5, 3.5, 'b')
    c.shades(8, 10, 8)
    c.stamp(10, 13, ['k..k', '.kk.'])
    c.ell(20.5, 1.5, 1.2, 1.2, 'a')
    for x, y in [(0, 4), (22, 9), (2, 1)]:
        c.stamp(x, y, ['.c', 'cc', 'c.'])


@sprite('Walkiehawkie')
def _(c):
    c.rect(15, 0, 16, 5, 'k')
    c.poly([(6, 9), (1, 13), (3, 19), (6, 17)], 'a')
    c.poly([(17, 9), (22, 13), (20, 19), (17, 17)], 'a')
    c.rect(6, 5, 17, 20, 'a')
    c.poly([(3, 9), (6, 8), (6, 11)], 'f')
    c.rect(8, 21, 8, 22, 'f').rect(15, 21, 15, 22, 'f')
    c.outline()
    c.rect(15, 0, 16, 0, 'r')
    c.eye(7, 7, 'big', look=-1).eye(11, 7, 'big')
    c.brow(7, 5, 'R').brow(11, 5, 'L')
    c.rect(8, 11, 15, 17, 'b')
    for y in range(12, 17, 2):
        c.line(9, y, 14, y, 'k')
    c.rect(18, 11, 18, 14, 'c')
    c.stamp(7, 22, ['k.k']).stamp(14, 22, ['k.k'])


@sprite('Walkiehawker')
def _(c):
    c.rect(13, 0, 14, 4, 'k').rect(18, 1, 19, 5, 'k')
    c.poly([(5, 8), (0.5, 11), (1, 20), (5, 17)], 'a')
    c.poly([(18, 8), (22.5, 11), (22, 20), (18, 17)], 'a')
    c.rect(5, 4, 19, 20, 'a')
    c.poly([(5, 8), (0.5, 9), (5, 11.5)], 'f')
    c.poly([(5, 12), (1, 14), (5, 13.5)], 'f')
    c.rect(8, 21, 9, 22, 'f').rect(15, 21, 16, 22, 'f')
    c.outline()
    c.rect(13, 0, 14, 0, 'r').rect(18, 1, 19, 1, 'r')
    c.eye(7, 6, 'big', look=-1).eye(11, 6, 'big', look=-1)
    c.brow(6, 4, 'R', 3).brow(10, 4, 'R', 3)
    c.rect(8, 13, 16, 18, 'b')
    for y in range(14, 18, 2):
        c.line(9, y, 15, y, 'k')
    c.px(17, 6, 'r')
    c.stamp(0, 0, ['.k', 'k.', '.k'])


@sprite('Screensaurus')
def _(c):
    segs = [((3, 18), (9, 18)), ((9, 18), (9, 12)), ((9, 12), (16, 12)), ((16, 12), (16, 5)), ((16, 5), (21, 5)),
            ((9, 18), (9, 22)), ((14, 12), (14, 22)), ((3, 18), (1, 14))]
    for (x0, y0), (x1, y1) in segs:
        c.line(x0, y0, x1, y1, 'b', 2)
    c.rect(15, 2, 22, 8, 'b')
    c.outline()
    for (x0, y0), (x1, y1) in segs:
        for x, y in ((x0, y0), (x1, y1)):
            c.rect(x, y, x + 1, y + 1, 'c')
    c.line(15, 8, 22, 8, 'k')
    for x in range(16, 22, 2):
        c.px(x, 7, 'w')
    c.eye(17, 3, 'big')
    c.brow(16, 2, 'L', 3)
    c.px(10, 15, 'a').px(15, 9, 'a')


@sprite('Slushpuppy')
def _(c):
    c.poly([(5, 11), (18, 11), (16, 22), (7, 22)], 'b')
    c.ell(11.5, 9.5, 7, 5, 'a')
    c.poly([(5, 7), (4, 2), (8, 5)], 'a').poly([(18, 7), (19, 2), (15, 5)], 'a')
    c.rect(16, 0, 17, 7, 'r')
    c.outline()
    c.px(16, 1, 'w').px(16, 3, 'w').px(16, 5, 'w')
    for y in (14, 17, 20):
        c.line(6, y, 17, y, 'c')
    c.line(5, 11, 18, 11, 'k')
    c.eye(8, 8, 'big').eye(13, 8, 'big')
    c.stamp(10, 11, ['.kk.']).stamp(10, 12, ['..mm'])
    c.px(6, 13, 'a').px(6, 14, 'a').px(17, 13, 'a')


@sprite('Slushhound')
def _(c):
    c.poly([(3, 12), (20, 12), (18, 23), (5, 23)], 'b')
    c.ell(11.5, 9, 8.5, 5.5, 'a')
    c.poly([(4, 6), (2, 0), (8, 4)], 'a').poly([(19, 6), (21, 0), (15, 4)], 'a')
    c.poly([(9, 11), (14, 11), (11.5, 15)], 'a')
    c.rect(18, 0, 19, 8, 'r')
    c.outline()
    c.px(18, 2, 'w').px(18, 5, 'w')
    for y in (16, 19):
        c.line(5, y, 18, y, 'c')
    c.brow(6, 5, 'L', 3).brow(14, 5, 'R', 3)
    c.eye(7, 7, 'big').eye(14, 7, 'big', look=-1)
    c.stamp(10, 11, ['kkkk', 'w..w'])
    c.px(10, 13, 'q').px(13, 13, 'q').px(4, 13, 'a').px(19, 14, 'a')


@sprite('Chatbrat')
def _(c):
    c.poly([(2, 3), (21, 3), (22, 5), (22, 15), (21, 17), (10, 17), (5, 22), (6, 17), (2, 17), (1, 15), (1, 5)], 'a')
    c.outline()
    c.eye(7, 5, 'big').eye(14, 5, 'big', look=-1)
    c.stamp(4, 10, ['k..k....k.k..k', 'kkkk..k..k..k.', 'k..k.k..k.k.kkk'][:3])
    c.rect(18, 13, 19, 15, 'c')
    c.stamp(9, 8, ['.k.'])


@sprite('Chatroomer')
def _(c):
    c.poly([(3, 9), (20, 9), (20, 21), (17, 19), (14, 22), (11, 19), (8, 22), (5, 19), (3, 21)], 'a')
    c.rect(2, 2, 21, 9, 'b')
    c.rect(2, 2, 21, 4, 'n')
    c.outline()
    c.stamp(17, 3, ['rk', '..'][:1])
    c.px(19, 3, 'y').px(20, 3, 'r').px(18, 3, 'g')
    c.stamp(5, 6, ['kkkk.kkkk', 'kwk...kwk'][:1])
    c.stamp(5, 6, ['k..kk..k'])
    c.stamp(5, 7, ['.kk..kk.'])
    c.stamp(5, 12, ['c..ccc.c.', 'c..c.c.c.', 'cc.ccc.cc'])
    c.px(10, 15, 'w')


@sprite('Emailephant')
def _(c):
    c.ell(14, 14, 7.5, 6, 'a')
    c.ell(6, 9, 4.5, 4.2, 'a')
    c.line(3, 11, 1, 18, 'a', 2)
    c.rect(8, 3, 17, 11, 'w')
    for x in (9, 13, 17, 20):
        c.rect(x, 19, x + 1, 22, 'a')
    c.outline()
    c.line(8, 3, 12, 7, 'k').line(12, 7, 17, 3, 'k')
    c.ell(18, 3, 2.4, 2.4, 'r')
    c.px(18, 3, 'w')
    c.eye(4, 8, 'sleepy', look=-1)
    c.stamp(4, 13, ['c.', '.c'])
    c.stamp(13, 14, ['.kkk.', 'k.kkk', 'k.k.k', 'k.kk.', '.kk..'])
    c.px(0, 19, 'a').px(1, 20, 'k')


@sprite('Bufferfly')
def _(c):
    for cx in (5.5, 17.5):
        for i in range(8):
            a = math.radians(i * 45 - 90)
            col = 'a' if i < 4 else 'b'
            c.ell(cx + 3.8 * math.cos(a), 8 + 3.8 * math.sin(a), 1.4, 1.4, col)
    c.ell(5.5, 17, 3.5, 2.5, 'a').ell(17.5, 17, 3.5, 2.5, 'a')
    c.rect(10, 4, 13, 21, 'b')
    c.outline()
    c.rect(11, 12, 12, 20, 'c')
    c.rect(10, 4, 13, 4, '#')
    c.stamp(10, 6, ['k..k', '....', '.kk.'])
    c.line(10, 3, 8, 0, 'k').line(13, 3, 15, 0, 'k')
    c.px(3, 22, 'k').px(5, 22, 'k').px(7, 22, 'k')
