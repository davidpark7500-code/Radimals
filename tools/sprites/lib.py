"""Tiny pixel-art authoring kit for 24x24 Radimal sprites.

Shapes fill palette letters; outline() adds the '#' silhouette around everything drawn so far;
glow()/stamp after outline() adds detail that should NOT be outlined (sparks, shine, faces).
Palette letters: a/b/c are per-species; the rest are global (see PAL in www/index.html).
"""
import math

W = H = 24


class C:
    def __init__(self):
        self.g = [['.'] * W for _ in range(H)]

    # --- primitives -------------------------------------------------------
    def px(self, x, y, c):
        x, y = int(round(x)), int(round(y))
        if 0 <= x < W and 0 <= y < H:
            self.g[y][x] = c
        return self

    def get(self, x, y):
        return self.g[y][x] if 0 <= x < W and 0 <= y < H else '.'

    def rect(self, x0, y0, x1, y1, c):
        for y in range(min(y0, y1), max(y0, y1) + 1):
            for x in range(min(x0, x1), max(x0, x1) + 1):
                self.px(x, y, c)
        return self

    def ell(self, cx, cy, rx, ry, c):
        for y in range(H):
            for x in range(W):
                if ((x - cx) / (rx + 0.35)) ** 2 + ((y - cy) / (ry + 0.35)) ** 2 <= 1:
                    self.px(x, y, c)
        return self

    def ring(self, cx, cy, rx, ry, w, c):
        for y in range(H):
            for x in range(W):
                d = ((x - cx) / (rx + 0.35)) ** 2 + ((y - cy) / (ry + 0.35)) ** 2
                d2 = ((x - cx) / max(0.5, rx - w + 0.35)) ** 2 + ((y - cy) / max(0.5, ry - w + 0.35)) ** 2
                if d <= 1 and d2 > 1:
                    self.px(x, y, c)
        return self

    def poly(self, pts, c):
        for y in range(H):
            for x in range(W):
                px, py = x + 0.5, y + 0.5
                inside = False
                j = len(pts) - 1
                for i in range(len(pts)):
                    xi, yi = pts[i]
                    xj, yj = pts[j]
                    if (yi > py) != (yj > py) and px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                        inside = not inside
                    j = i
                if inside:
                    self.px(x, y, c)
        return self

    def line(self, x0, y0, x1, y1, c, w=1):
        n = max(abs(x1 - x0), abs(y1 - y0), 1)
        for i in range(int(n) + 1):
            x = x0 + (x1 - x0) * i / n
            y = y0 + (y1 - y0) * i / n
            for dx in range(w):
                for dy in range(w):
                    self.px(x + dx, y + dy, c)
        return self

    def stamp(self, x, y, rows):
        for j, r in enumerate(rows):
            for i, ch in enumerate(r):
                if ch != '.':
                    self.px(x + i, y + j, ch)
        return self

    def clear(self, x0, y0, x1, y1):
        return self.rect(x0, y0, x1, y1, '.')

    def mirror(self):
        """Copy the left half onto the right half (symmetric creatures)."""
        for y in range(H):
            for x in range(12):
                self.g[y][23 - x] = self.g[y][x]
        return self

    def recolor(self, frm, to, region=None):
        x0, y0, x1, y1 = region or (0, 0, 23, 23)
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if self.g[y][x] == frm:
                    self.g[y][x] = to
        return self

    def outline(self, diag=False):
        add = []
        nb = [(1, 0), (-1, 0), (0, 1), (0, -1)] + ([(1, 1), (1, -1), (-1, 1), (-1, -1)] if diag else [])
        for y in range(H):
            for x in range(W):
                if self.g[y][x] != '.':
                    continue
                for dx, dy in nb:
                    v = self.get(x + dx, y + dy)
                    if v not in ('.', '#'):
                        add.append((x, y))
                        break
        for x, y in add:
            self.g[y][x] = '#'
        return self

    def shadow(self, frm, to):
        """Darken the bottom/right inner edge of a fill (gives volume)."""
        pts = []
        for y in range(H):
            for x in range(W):
                if self.g[y][x] == frm and (self.get(x, y + 1) == '#' or self.get(x + 1, y) == '#'):
                    pts.append((x, y))
        for x, y in pts:
            self.g[y][x] = to
        return self

    def shine(self, frm, to):
        """Lighten the top/left inner edge of a fill."""
        pts = []
        for y in range(H):
            for x in range(W):
                if self.g[y][x] == frm and (self.get(x, y - 1) == '#' or self.get(x - 1, y) == '#'):
                    pts.append((x, y))
        for x, y in pts:
            self.g[y][x] = to
        return self

    # --- faces --------------------------------------------------------------
    def eye(self, x, y, kind='big', look=1):
        """kind: big (2x2 w/ highlight), dot, wide (3x2), sleepy, angry (with brow),
        shut (^), x (dizzy), star, shades handled separately."""
        if kind == 'dot':
            self.px(x, y, 'k')
        elif kind == 'big':
            self.stamp(x, y, ['wk', 'kk'] if look > 0 else ['kw', 'kk'])
        elif kind == 'wide':
            self.stamp(x, y, ['wwk', 'wkk'] if look > 0 else ['kww', 'kkw'])
        elif kind == 'tall':
            self.stamp(x, y, ['wk', 'kk', 'kk'] if look > 0 else ['kw', 'kk', 'kk'])
        elif kind == 'sleepy':
            self.stamp(x, y, ['kk', 'wk'] if look > 0 else ['kk', 'kw'])
        elif kind == 'shut':
            self.stamp(x, y, ['k.k', '.k.'][::-1])
        elif kind == 'x':
            self.stamp(x, y, ['k.k', '.k.', 'k.k'])
        elif kind == 'line':
            self.stamp(x, y, ['kk'])
        return self

    def brow(self, x, y, side, n=2):
        """Angry brow ending above an eye. side='L' slants down to the right, 'R' down to the left."""
        for i in range(n):
            self.px(x + i, y + (i if side == 'L' else n - 1 - i), 'k')
        return self

    def shades(self, x, y, w):
        self.rect(x, y, x + w - 1, y + 1, 'k')
        self.px(x + 1, y, 'q')
        self.px(x + w - 3, y, 'q')
        return self


SPRITES = {}


def sprite(name):
    def deco(fn):
        SPRITES[name] = fn
        return fn
    return deco


def render(name):
    c = C()
    SPRITES[name](c)
    rows = [''.join(r) for r in c.g]
    assert len(rows) == 24 and all(len(r) == 24 for r in rows), name
    return rows
