"""Generate the animated offline-dino runner SVG, and verify it numerically.

Sprites are ASCII grids ('#' = pixel). Pixel runs are merged into rectangles so
the SVG stays compact. Proportions follow the real Chrome game: a 600x150 stage
with a ~48px dino.

The jump is phase-locked to the obstacles: apex lands when a cactus is centred
under the dino, and the airborne window is wide enough to cover the whole time
the cactus overlaps the dino horizontally. check_clearance() proves it.
"""
import pathlib

PX = 2
W, H = 600, 150
GROUND_Y = 127
DINO_X = 54

# ---------------------------------------------------------------- sprites --
DINO_BODY = [
    "...............######...",
    "..............#########.",
    "..............#########.",
    "..............##.#######",
    "..............#########.",
    "..............#########.",
    ".............##########.",
    ".............######.....",
    "#............#####......",
    "##...........######.....",
    "###.........#######.....",
    ".####......########.....",
    "..##################....",   # small forward arm nub
    "...################.....",
    "....##############......",
    ".....#############......",
    "......############......",
    ".......###########......",
    ".......##########.......",
    ".......#########........",
]
DINO_LEGS_A = [
    ".......##...##..........",
    ".......##...##..........",
    ".......##...............",
    "......####..............",
]
DINO_LEGS_B = [
    ".......##...##..........",
    ".......##...##..........",
    "............##..........",
    "...........####.........",
]
# tucked pose held while airborne, like the real game
DINO_LEGS_JUMP = [
    ".......##...##..........",
    "......###...###.........",
    "........................",
    "........................",
]

CACTUS_SMALL = [
    "..###..", "..###..", "#.###..", "#.###.#",
    "#####.#", "#####.#", "..###.#", "..#####",
    "..###..", "..###..", "..###..", "..###..",
]
CACTUS_LARGE = [
    "...####...", "...####...", "...####...", "#..####...",
    "#..####..#", "#..####..#", "#######..#", "#######..#",
    "...####..#", "...####..#", "...#######", "...####...",
    "...####...", "...####...", "...####...", "...####...",
    "...####...",
]

BIRD_UP = [
    "..##........", ".####.......", "..######....",
    "...#########", "..######....", "............", "............",
]
BIRD_DOWN = [
    "............", "............", "..######....",
    "...#########", "..######....", ".####.......", "..##........",
]
CLOUD = [
    "....######....", "..##########..", ".#############",
    "##############", ".############.",
]

# ------------------------------------------------------------------ timing --
START_X, END_X = 640, -60
TRAVEL = START_X - END_X            # 700 px
T = 2.2                             # seconds for one obstacle to cross
SPEED = TRAVEL / T                  # ~318 px/s
JUMP = T / 2                        # obstacles alternate every half cycle

APEX = 46                           # px of lift at the top of the arc
AIRTIME = 0.56                      # seconds off the ground
BIRD_Y = 12                         # kept above the dino's apex, see check below

dino_w = 24 * PX
dino_h = (len(DINO_BODY) + len(DINO_LEGS_A)) * PX
dino_top = GROUND_Y - dino_h
cs_h, cl_h = len(CACTUS_SMALL) * PX, len(CACTUS_LARGE) * PX
cs_w, cl_w = len(CACTUS_SMALL[0]) * PX, len(CACTUS_LARGE[0]) * PX
cs_top, cl_top = GROUND_Y - cs_h, GROUND_Y - cl_h

# apex when the (larger) cactus is centred under the dino
apex_x = DINO_X + dino_w / 2 - cl_w / 2
apex_t = (START_X - apex_x) / SPEED          # obstacle-local time of apex
apex_pct = (apex_t % JUMP) / JUMP            # phase within the jump cycle
half = (AIRTIME / JUMP) / 2
lo, hi = apex_pct - half, apex_pct + half


def arc(p):
    """Vertical offset (negative = up) at phase p of the jump cycle."""
    if not (lo <= p <= hi):
        return 0.0
    u = (p - apex_pct) / half
    return -APEX * (1 - u * u)


def keyframes():
    stops = []
    for i in range(9):
        u = -1 + i * 0.25
        pct = apex_pct + u * half
        stops.append((pct * 100, round(-APEX * (1 - u * u))))
    body = [f"  0%, {stops[0][0]:.1f}% {{ transform: translateY(0); }}"]
    for pct, dy in stops[1:-1]:
        body.append(f"  {pct:.1f}% {{ transform: translateY({dy}px); }}")
    body.append(f"  {stops[-1][0]:.1f}%, 100% {{ transform: translateY(0); }}")
    return "\n".join(body)


# ---------------------------------------------------------------- emitting --
def runs(grid):
    rects = []
    for y, row in enumerate(grid):
        x = 0
        while x < len(row):
            if row[x] == "#":
                s = x
                while x < len(row) and row[x] == "#":
                    x += 1
                rects.append([s, y, x - s, 1])
            else:
                x += 1
    merged = []
    for r in rects:
        for m in merged:
            if m[0] == r[0] and m[2] == r[2] and m[1] + m[3] == r[1]:
                m[3] += 1
                break
        else:
            merged.append(r)
    return merged


def svg_rects(grid, ox, oy, px=PX):
    return "".join(
        f'<rect x="{ox + x * px:g}" y="{oy + y * px:g}" '
        f'width="{w * px:g}" height="{h * px:g}"/>'
        for x, y, w, h in runs(grid)
    )


speckles = [(7, 4), (31, 7), (58, 3), (77, 9), (104, 5),
            (129, 8), (151, 3), (172, 6), (191, 4)]


def ground_tile(ox):
    out = [f'<rect x="{ox}" y="{GROUND_Y}" width="200" height="2"/>']
    for sx, sw in speckles:
        out.append(f'<rect x="{ox + sx}" y="{GROUND_Y + 4}" width="{sw}" height="2"/>')
    return "".join(out)


ground = "".join(ground_tile(i * 200) for i in range(6))
scroll_dur = 600 / SPEED

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Pixel-art dinosaur running and jumping over cacti, like the Chrome offline game">
<title>Offline dino runner</title>
<style>
  .ink   {{ fill: #5f6368; }}
  .faint {{ fill: #b7b7b7; }}
  @media (prefers-color-scheme: dark) {{
    .ink   {{ fill: #9aa0a6; }}
    .faint {{ fill: #5f6368; }}
  }}
  .scroll {{ animation: scroll {scroll_dur:.3f}s linear infinite; }}
  .obs    {{ animation: obs {T}s linear infinite; }}
  .obs2   {{ animation-delay: {-T / 2}s; }}
  .dino   {{ animation: jump {JUMP}s linear infinite; }}
  .legA   {{ animation: alt .22s steps(1, end) infinite; }}
  .legB   {{ animation: alt .22s steps(1, end) infinite; animation-delay: -.11s; }}
  .run    {{ animation: onGround {JUMP}s steps(1, end) infinite; }}
  .tuck   {{ animation: airborne {JUMP}s steps(1, end) infinite; }}
  .bird   {{ animation: bird 7s linear infinite; }}
  .wingU  {{ animation: alt .3s steps(1, end) infinite; }}
  .wingD  {{ animation: alt .3s steps(1, end) infinite; animation-delay: -.15s; }}
  .cloudA {{ animation: cloud 22s linear infinite; }}
  .cloudB {{ animation: cloud 31s linear infinite; animation-delay: -14s; }}

  @keyframes scroll {{ from {{ transform: translateX(0); }}
                      to   {{ transform: translateX(-600px); }} }}
  @keyframes obs    {{ from {{ transform: translateX({START_X}px); }}
                      to   {{ transform: translateX({END_X}px); }} }}
  @keyframes bird   {{ from {{ transform: translateX(660px); }}
                      to   {{ transform: translateX(-60px); }} }}
  @keyframes cloud  {{ from {{ transform: translateX(620px); }}
                      to   {{ transform: translateX(-90px); }} }}
  @keyframes alt    {{ 0% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
  /* legs cycle only while the feet are down, freeze in a tuck while airborne */
  @keyframes onGround {{ 0% {{ opacity: 1; }}
                         {lo * 100:.1f}% {{ opacity: 0; }}
                         {hi * 100:.1f}%, 100% {{ opacity: 1; }} }}
  @keyframes airborne {{ 0% {{ opacity: 0; }}
                         {lo * 100:.1f}% {{ opacity: 1; }}
                         {hi * 100:.1f}%, 100% {{ opacity: 0; }} }}
  /* parabolic hop, phase-locked so the apex lands on the cactus */
  @keyframes jump {{
{keyframes()}
  }}
  @media (prefers-reduced-motion: reduce) {{
    .scroll, .obs, .dino, .legA, .legB, .run, .tuck,
    .bird, .wingU, .wingD, .cloudA, .cloudB {{ animation: none; }}
    .legB, .wingD, .tuck {{ opacity: 0; }}
  }}
</style>

<g class="faint">
  <g class="cloudA">{svg_rects(CLOUD, 0, 32, 2)}</g>
  <g class="cloudB">{svg_rects(CLOUD, 0, 54, 2)}</g>
</g>

<g class="ink scroll">{ground}</g>

<g class="ink">
  <g class="obs">{svg_rects(CACTUS_SMALL, 0, cs_top)}</g>
  <g class="obs obs2">{svg_rects(CACTUS_LARGE, 0, cl_top)}</g>
  <g class="bird" transform="translate(0,{BIRD_Y})">
    <g class="wingU">{svg_rects(BIRD_UP, 0, 0)}</g>
    <g class="wingD">{svg_rects(BIRD_DOWN, 0, 0)}</g>
  </g>
</g>

<g class="ink dino">
  {svg_rects(DINO_BODY, DINO_X, dino_top)}
  <g class="run">
    <g class="legA">{svg_rects(DINO_LEGS_A, DINO_X, dino_top + len(DINO_BODY) * PX)}</g>
    <g class="legB">{svg_rects(DINO_LEGS_B, DINO_X, dino_top + len(DINO_BODY) * PX)}</g>
  </g>
  <g class="tuck">{svg_rects(DINO_LEGS_JUMP, DINO_X, dino_top + len(DINO_BODY) * PX)}</g>
</g>
</svg>
'''

out = pathlib.Path(r"C:\Users\ankit\Downloads\ankitsingathia\assets\offline-dino.svg")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(svg, encoding="utf-8")


# ------------------------------------------------------- numeric collision --
def obstacle_x(t, phase):
    return START_X - TRAVEL * (((t + phase) % T) / T)


def check_clearance(steps=20000):
    """Walk a full cycle; fail if the dino's feet are ever inside a cactus."""
    worst = {}
    fails = []
    for i in range(steps):
        t = T * i / steps
        feet = GROUND_Y + arc((t % JUMP) / JUMP)
        for name, phase, w, top in (
            ("small", 0.0, cs_w, cs_top),
            ("large", T / 2, cl_w, cl_top),
        ):
            x = obstacle_x(t, phase)
            overlaps_x = (x < DINO_X + dino_w) and (x + w > DINO_X)
            if overlaps_x:
                gap = top - feet          # >0 means feet are above the cactus top
                if name not in worst or gap < worst[name][0]:
                    worst[name] = (gap, t, x)
                if gap <= 0:
                    fails.append((name, round(t, 3), round(x, 1), round(gap, 1)))
    return worst, fails


worst, fails = check_clearance()
print(f"wrote {out}  ({len(svg)} bytes)")
print(f"speed {SPEED:.1f} px/s | obstacle cycle {T}s | jump cycle {JUMP}s")
print(f"apex at {apex_pct * 100:.1f}% of jump cycle, airborne {lo * 100:.1f}%-{hi * 100:.1f}%")
print(f"dino {dino_w}x{dino_h} at y{dino_top}  cactus small {cs_w}x{cs_h} large {cl_w}x{cl_h}")
for name, (gap, t, x) in worst.items():
    print(f"  tightest {name}: {gap:+.1f}px clearance at t={t:.3f}s (cactus x={x:.0f})")
print("COLLISIONS:", "none - clears every obstacle" if not fails else fails[:6])
bird_bottom = BIRD_Y + len(BIRD_UP) * PX
dino_apex_top = dino_top - APEX
print(f"bird occupies y{BIRD_Y}-{bird_bottom}, dino apex top y{dino_apex_top} "
      f"-> {'OK, gap %dpx' % (dino_apex_top - bird_bottom) if dino_apex_top >= bird_bottom else 'OVERLAP'}")

# ------------------------------------------------------------ PNG contact --
from PIL import Image, ImageDraw
SC = 2


def draw(d, grid, ox, oy, colour, px=PX):
    for x, y, w, h in runs(grid):
        d.rectangle([((ox + x * px) * SC, (oy + y * px) * SC),
                     ((ox + (x + w) * px) * SC - 1, (oy + (y + h) * px) * SC - 1)],
                    fill=colour)


def frame(t, bg, ink, faint):
    img = Image.new("RGB", (W * SC, H * SC), bg)
    d = ImageDraw.Draw(img)
    sc = -(t % scroll_dur) * SPEED
    for i in range(6):
        ox = i * 200 + sc
        d.rectangle([(ox * SC, GROUND_Y * SC), ((ox + 200) * SC, (GROUND_Y + 2) * SC)], fill=ink)
        for sx, sw in speckles:
            d.rectangle([((ox + sx) * SC, (GROUND_Y + 4) * SC),
                         ((ox + sx + sw) * SC, (GROUND_Y + 6) * SC)], fill=ink)
    draw(d, CLOUD, 620 - 710 * ((t % 22) / 22), 32, faint, px=2)
    draw(d, CLOUD, 620 - 710 * (((t + 14) % 31) / 31), 54, faint, px=2)
    bx = 660 - 720 * ((t % 7) / 7)
    draw(d, BIRD_UP if int(t / .3) % 2 == 0 else BIRD_DOWN, bx, BIRD_Y, ink)
    draw(d, CACTUS_SMALL, obstacle_x(t, 0), cs_top, ink)
    draw(d, CACTUS_LARGE, obstacle_x(t, T / 2), cl_top, ink)
    p = (t % JUMP) / JUMP
    dy = arc(p)
    draw(d, DINO_BODY, DINO_X, dino_top + dy, ink)
    legs = DINO_LEGS_JUMP if lo <= p <= hi else (DINO_LEGS_A if int(t / .22) % 2 == 0 else DINO_LEGS_B)
    draw(d, legs, DINO_X, dino_top + dy + len(DINO_BODY) * PX, ink)
    return img


times = [0.0, 0.45, 0.62, 0.69, 0.80, 1.35, 1.79]
rows = [frame(t, "#ffffff", "#535353", "#b7b7b7") for t in times]
rows.append(frame(1.79, "#0d1117", "#9aa0a6", "#5f6368"))
sheet = Image.new("RGB", (W * SC, H * SC * len(rows)), "white")
for i, r in enumerate(rows):
    sheet.paste(r, (0, i * H * SC))
p = pathlib.Path(r"C:\Users\ankit\AppData\Local\Temp\claude\C--Users-ankit-Downloads-msds\105be561-e68f-444d-ac4b-9e4f9a7c7637\scratchpad\dino_frames.png")
sheet.save(p)
print("preview ->", p, sheet.size, "| frames at t =", times, "+ dark")
