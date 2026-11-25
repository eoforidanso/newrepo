"""Original abstract artwork for the site, drawn as SVG (no stock licences needed).

Each piece is a theme for one part of the business:
  network     routes and outlets          (homepage hero, distribution, services)
  growth      rising bars and a trend     (sales strategy, how we work)
  people      linked circles              (sales training, contact)
  compass     rings, ticks and a heading  (part-time leadership, about)
  grid        isometric tiles and stock   (retail operations, privacy)

Run by build.py; files go to site/assets/art/.
"""
import math
import random
from pathlib import Path

TEAL, TEAL_D, BLUE, WHITE = "#5ed6cf", "#1f8a86", "#7aa6f5", "#ffffff"
W, H = 800, 600


def _wrap(body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" fill="none">'
            f'<defs>{defs}'
            f'<radialGradient id="orb" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{TEAL}" stop-opacity=".35"/>'
            f'<stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="orb2" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{BLUE}" stop-opacity=".28"/>'
            f'<stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{TEAL}" stop-opacity=".55"/>'
            f'<stop offset="1" stop-color="{TEAL}" stop-opacity=".04"/></linearGradient>'
            f'</defs>{body}</svg>')


def network(seed=7):
    rnd = random.Random(seed)
    pts = []
    for gx in range(6):
        for gy in range(4):
            pts.append((70 + gx * 135 + rnd.uniform(-40, 40), 70 + gy * 150 + rnd.uniform(-40, 40)))
    out = [f'<circle cx="560" cy="250" r="260" fill="url(#orb)"/>',
           f'<circle cx="170" cy="470" r="200" fill="url(#orb2)"/>']
    seen = set()
    for i, (x, y) in enumerate(pts):
        near = sorted(range(len(pts)), key=lambda j: (pts[j][0] - x) ** 2 + (pts[j][1] - y) ** 2)[1:3]
        for j in near:
            key = tuple(sorted((i, j)))
            if key in seen:
                continue
            seen.add(key)
            x2, y2 = pts[j]
            mx, my = (x + x2) / 2 + rnd.uniform(-30, 30), (y + y2) / 2 + rnd.uniform(-30, 30)
            flow = rnd.random() < .3
            dash = (' stroke-dasharray="4 10"><animate attributeName="stroke-dashoffset" from="0" to="-28" '
                    'dur="2.4s" repeatCount="indefinite"/></path>') if flow else '/>'
            out.append(f'<path d="M{x:.0f} {y:.0f}Q{mx:.0f} {my:.0f} {x2:.0f} {y2:.0f}" '
                       f'stroke="{TEAL if flow else WHITE}" stroke-opacity="{.7 if flow else .16}" stroke-width="1.5"{dash}')
    for x, y in pts:
        big = rnd.random() < .25
        if big:
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="16" fill="{TEAL}" fill-opacity=".14"/>')
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{5 if big else 3}" fill="{TEAL if big else WHITE}" '
                   f'fill-opacity="{.95 if big else .5}"/>')
    return _wrap("".join(out))


def growth():
    out = ['<circle cx="600" cy="200" r="250" fill="url(#orb)"/>',
           '<circle cx="180" cy="520" r="180" fill="url(#orb2)"/>']
    for r in (140, 210, 280, 350):
        out.append(f'<circle cx="120" cy="560" r="{r}" stroke="{WHITE}" stroke-opacity=".08" stroke-width="1.5"/>')
    base = 520
    heights = [90, 130, 120, 190, 240, 300, 380]
    for i, h in enumerate(heights):
        x = 200 + i * 78
        out.append(f'<rect x="{x}" y="{base - h}" width="44" height="{h}" rx="12" fill="url(#fade)"/>')
    pts = [(222 + i * 78, base - h - 34) for i, h in enumerate(heights)]
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    out.append(f'<path d="{d}" stroke="{TEAL}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    for x, y in pts:
        out.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#0f2a47" stroke="{TEAL}" stroke-width="3"/>')
    x, y = pts[-1]
    out.append(f'<path d="M{x - 18} {y - 30} L{x + 14} {y - 44} L{x + 4} {y - 10}" stroke="{TEAL}" stroke-width="3" '
               'stroke-linecap="round" stroke-linejoin="round"/>')
    return _wrap("".join(out))


def people(seed=3):
    rnd = random.Random(seed)
    out = ['<circle cx="520" cy="300" r="270" fill="url(#orb)"/>',
           '<circle cx="200" cy="140" r="170" fill="url(#orb2)"/>']
    hubs = [(420, 260, 120), (560, 330, 105), (470, 410, 90)]
    for x, y, r in hubs:
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{TEAL}" fill-opacity=".08" stroke="{WHITE}" stroke-opacity=".18" stroke-width="1.5"/>')
    cx, cy = 480, 330
    for k in range(18):
        a = k / 18 * math.tau + rnd.uniform(-.1, .1)
        dist = rnd.uniform(200, 290)
        x, y = cx + math.cos(a) * dist, cy + math.sin(a) * dist * .8
        out.append(f'<path d="M{cx} {cy} L{x:.0f} {y:.0f}" stroke="{WHITE}" stroke-opacity=".10" stroke-width="1.2"/>')
        r = rnd.choice((5, 7, 9))
        out.append(f'<circle cx="{x:.0f}" cy="{y - r * 1.6:.0f}" r="{r * .7:.1f}" fill="{WHITE}" fill-opacity=".55"/>'
                   f'<path d="M{x - r:.0f} {y + r * .6:.0f}a{r} {r} 0 0 1 {2 * r} 0" stroke="{WHITE}" stroke-opacity=".55" stroke-width="2" stroke-linecap="round"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="{TEAL}"/><circle cx="{cx}" cy="{cy}" r="24" stroke="{TEAL}" stroke-opacity=".5" stroke-width="2">'
               '<animate attributeName="r" values="18;34;18" dur="4s" repeatCount="indefinite"/>'
               '<animate attributeName="stroke-opacity" values=".6;0;.6" dur="4s" repeatCount="indefinite"/></circle>')
    return _wrap("".join(out))


def compass():
    cx, cy = 520, 300
    out = [f'<circle cx="{cx}" cy="{cy}" r="280" fill="url(#orb)"/>',
           '<circle cx="160" cy="480" r="170" fill="url(#orb2)"/>']
    for r, op in ((250, .08), (190, .14), (130, .2), (70, .28)):
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{WHITE}" stroke-opacity="{op}" stroke-width="1.5"/>')
    for k in range(72):
        a = k / 72 * math.tau
        long = k % 6 == 0
        r1, r2 = 190, 190 + (18 if long else 8)
        out.append(f'<path d="M{cx + math.cos(a) * r1:.1f} {cy + math.sin(a) * r1:.1f}L{cx + math.cos(a) * r2:.1f} {cy + math.sin(a) * r2:.1f}" '
                   f'stroke="{TEAL if long else WHITE}" stroke-opacity="{.8 if long else .25}" stroke-width="{2 if long else 1.2}"/>')
    out.append(f'<g transform="rotate(38 {cx} {cy})"><path d="M{cx} {cy - 150} L{cx + 16} {cy} L{cx} {cy + 22} L{cx - 16} {cy}Z" fill="{TEAL}" fill-opacity=".9"/>'
               f'<path d="M{cx} {cy + 150} L{cx + 16} {cy} L{cx - 16} {cy}Z" fill="{WHITE}" fill-opacity=".25"/></g>'
               f'<circle cx="{cx}" cy="{cy}" r="7" fill="#0f2a47" stroke="{WHITE}" stroke-width="2"/>')
    out.append(f'<path d="M80 560 C 200 520, 220 420, 330 400 S 470 330, 610 150" stroke="{TEAL}" stroke-opacity=".7" stroke-width="2" stroke-dasharray="2 9" stroke-linecap="round"/>'
               f'<path d="M610 150 v-56 l40 14 l-40 14" stroke="{TEAL}" stroke-width="2.5" stroke-linejoin="round" fill="{TEAL}" fill-opacity=".25"/>')
    return _wrap("".join(out))


def grid(seed=11):
    rnd = random.Random(seed)
    out = ['<circle cx="540" cy="260" r="270" fill="url(#orb)"/>',
           '<circle cx="180" cy="480" r="170" fill="url(#orb2)"/>']
    s = 46  # tile half-width

    def tile(i, j, lift=0, fill=None, op=.0):
        x = 400 + (i - j) * s
        y = 120 + (i + j) * s * .55 - lift
        p = f"M{x} {y} l{s} {s * .55} l{-s} {s * .55} l{-s} {-s * .55}Z"
        if fill:
            return f'<path d="{p}" fill="{fill}" fill-opacity="{op}" stroke="{WHITE}" stroke-opacity=".35" stroke-width="1.2"/>'
        return f'<path d="{p}" stroke="{WHITE}" stroke-opacity=".14" stroke-width="1.2"/>'

    for i in range(7):
        for j in range(7):
            out.append(tile(i, j))
    for (i, j, h) in [(2, 1, 1), (2, 2, 2), (3, 1, 1), (4, 3, 3), (4, 4, 2), (1, 4, 1), (5, 2, 2)]:
        for k in range(h):
            x = 400 + (i - j) * s
            y = 120 + (i + j) * s * .55 - (k + 1) * 30
            out.append(f'<path d="M{x - s} {y + s * .55} v30 l{s} {s * .55} v-30Z" fill="{TEAL_D}" fill-opacity=".55" stroke="{WHITE}" stroke-opacity=".25"/>'
                       f'<path d="M{x + s} {y + s * .55} v30 l{-s} {s * .55} v-30Z" fill="{TEAL}" fill-opacity=".30" stroke="{WHITE}" stroke-opacity=".25"/>')
            out.append(tile(i, j, lift=(k + 1) * 30, fill=TEAL, op=.55 if k == h - 1 else .2))
    return _wrap("".join(out))


PIECES = {"network": network, "growth": growth, "people": people, "compass": compass, "grid": grid}


def generate(out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, fn in PIECES.items():
        (out_dir / f"{name}.svg").write_text(fn(), encoding="utf-8")
