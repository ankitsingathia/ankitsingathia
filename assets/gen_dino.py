"""Generate assets/offline-dino.svg, and verify it numerically.

Sprites are ASCII grids ('#' = pixel). Pixel runs are merged into rectangles so
the SVG stays compact. This is the slim-strip layout: long and short, so the
dino reads as a divider rather than a hero banner.

The jump is phase-locked to the obstacles: the apex lands when a cactus is
centred under the dino, and the airborne window is derived to be wider than the
whole time that cactus overlaps the dino horizontally. check_clearance() proves
it by walking a full cycle.

Vertical budget is the binding constraint on a strip this short:

    dino height + APEX + headroom  <=  GROUND_Y

Raising APEX or a cactus without raising GROUND_Y pushes the dino off the top of
the canvas, so the asserts at the bottom fail loudly if that ever happens.

Run:  python assets/gen_dino.py
"""
import pathlib

PX = 1.5                 # sprite pixel size in user units
W, H = 1000, 84          # long and short
GROUND_Y = 74
DINO_X = 70

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
# tucked pose, held while airborne, like the real game
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
CLOUD = [
    "....######....", "..##########..", ".#############",
    "##############", ".############.",
]
# No pterodactyl in this layout: the dino's apex reaches the top of the canvas,
# so there is no altitude band left for one to cross without colliding.

# ------------------------------------------------------------------ timing --
START_X, END_X = W + 40, -40
TRAVEL = START_X - END_X
T = 3.4                             # seconds for one obstacle to cross
SPEED = TRAVEL / T
JUMP = T / 2                        # obstacles alternate every half cycle

APEX = 34                           # px of lift at the top of the arc
AIRTIME = 0.50                      # seconds off the ground

TILE = 200                          # ground tile width; scroll shifts exactly one

dino_w = 24 * PX
dino_h = (len(DINO_BODY) + len(DINO_LEGS_A)) * PX
dino_top = GROUND_Y - dino_h
cs_h, cl_h = len(CACTUS_SMALL) * PX, len(CACTUS_LARGE) * PX
cs_w, cl_w = len(CACTUS_SMALL[0]) * PX, len(CACTUS_LARGE[0]) * PX
cs_top, cl_top = GROUND_Y - cs_h, GROUND_Y - cl_h

apex_x = DINO_X + dino_w / 2 - cl_w / 2
apex_t = (START_X - apex_x) / SPEED
apex_pct = (apex_t % JUMP) / JUMP
half = (AIRTIME / JUMP) / 2
lo, hi = apex_pct - half, apex_pct + half


def arc(p):
    """Vertical offset (negative = up) at phase p of the jump cycle."""
    if not (lo <= p <= hi):
        return 0.0
    u = (p - apex_pct) / half
    return -APEX * (1 - u * u)


def keyframes():
    stops = [(apex_pct + (-1 + i * 0.25) * half,
              round(-APEX * (1 - (-1 + i * 0.25) ** 2), 1)) for i in range(9)]
    body = [f"  0%, {stops[0][0] * 100:.1f}% {{ transform: translateY(0); }}"]
    for pct, dy in stops[1:-1]:
        body.append(f"  {pct * 100:.1f}% {{ transform: translateY({dy:g}px); }}")
    body.append(f"  {stops[-1][0] * 100:.1f}%, 100% {{ transform: translateY(0); }}")
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
n_tiles = -(-(W + TILE) // TILE)     # enough tiles that the shift stays seamless
ground = "".join(
    f'<rect x="{i * TILE}" y="{GROUND_Y}" width="{TILE}" height="1.5"/>'
    + "".join(
        f'<rect x="{i * TILE + sx}" y="{GROUND_Y + 3.5}" width="{sw}" height="1.5"/>'
        for sx, sw in speckles)
    for i in range(n_tiles)
)
scroll_dur = TILE / SPEED

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Pixel-art dinosaur running and jumping over cacti, like the Chrome offline game">
<title>Offline dino runner</title>
<style>
  .ink   {{ fill: #5f6368; }}
  .faint {{ fill: #c4c7c5; }}
  @media (prefers-color-scheme: dark) {{
    .ink   {{ fill: #9aa0a6; }}
    .faint {{ fill: #4a4e52; }}
  }}
  .scroll {{ animation: scroll {scroll_dur:.3f}s linear infinite; }}
  .obs    {{ animation: obs {T}s linear infinite; }}
  .obs2   {{ animation-delay: {-T / 2}s; }}
  .dino   {{ animation: jump {JUMP}s linear infinite; }}
  .legA   {{ animation: alt .2s steps(1, end) infinite; }}
  .legB   {{ animation: alt .2s steps(1, end) infinite; animation-delay: -.1s; }}
  .run    {{ animation: onGround {JUMP}s steps(1, end) infinite; }}
  .tuck   {{ animation: airborne {JUMP}s steps(1, end) infinite; }}
  .cloudA {{ animation: cloud 24s linear infinite; }}
  .cloudB {{ animation: cloud 33s linear infinite; animation-delay: -15s; }}

  @keyframes scroll {{ from {{ transform: translateX(0); }}
                      to   {{ transform: translateX(-{TILE}px); }} }}
  @keyframes obs    {{ from {{ transform: translateX({START_X}px); }}
                      to   {{ transform: translateX({END_X}px); }} }}
  @keyframes cloud  {{ from {{ transform: translateX({W + 30}px); }}
                      to   {{ transform: translateX(-70px); }} }}
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
    .cloudA, .cloudB {{ animation: none; }}
    .legB, .tuck {{ opacity: 0; }}
  }}
</style>

<g class="faint">
  <g class="cloudA">{svg_rects(CLOUD, 0, 9, 1.5)}</g>
  <g class="cloudB">{svg_rects(CLOUD, 0, 26, 1.5)}</g>
</g>

<g class="ink scroll">{ground}</g>

<g class="ink">
  <g class="obs">{svg_rects(CACTUS_SMALL, 0, cs_top)}</g>
  <g class="obs obs2">{svg_rects(CACTUS_LARGE, 0, cl_top)}</g>
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

out = pathlib.Path(__file__).with_name("offline-dino.svg")
out.write_text(svg, encoding="utf-8")


# ------------------------------------------------------------ verification --
def obstacle_x(t, phase):
    return START_X - TRAVEL * (((t + phase) % T) / T)


def check_clearance(steps=20000):
    """Walk a full cycle; fail if the dino's feet are ever inside a cactus."""
    worst, fails = {}, []
    for i in range(steps):
        t = T * i / steps
        feet = GROUND_Y + arc((t % JUMP) / JUMP)
        for name, phase, w, top in (("small", 0.0, cs_w, cs_top),
                                    ("large", T / 2, cl_w, cl_top)):
            x = obstacle_x(t, phase)
            if x < DINO_X + dino_w and x + w > DINO_X:
                gap = top - feet
                if name not in worst or gap < worst[name][0]:
                    worst[name] = (gap, t, x)
                if gap <= 0:
                    fails.append((name, round(t, 3), round(gap, 1)))
    return worst, fails


if __name__ == "__main__":
    worst, fails = check_clearance()
    apex_top = dino_top - APEX
    print(f"wrote {out.name}  ({len(svg)} bytes)")
    print(f"canvas {W}x{H} (ratio {W / H:.1f}:1) | speed {SPEED:.0f} px/s | "
          f"obstacle {T}s | jump {JUMP}s")
    print(f"dino {dino_w:g}x{dino_h:g} at y{dino_top:g} | "
          f"cactus {cs_w:g}x{cs_h:g} and {cl_w:g}x{cl_h:g}")
    print(f"apex {apex_pct * 100:.1f}% of cycle, "
          f"airborne {lo * 100:.1f}%-{hi * 100:.1f}%")
    for name, (gap, t, x) in worst.items():
        print(f"  tightest {name}: {gap:+.1f}px clearance at t={t:.3f}s")
    print("COLLISIONS:",
          "none - clears every obstacle" if not fails else fails[:6])
    print(f"headroom: dino apex reaches y{apex_top:g} -> "
          f"{'OK, %gpx spare' % apex_top if apex_top >= 0 else 'CLIPPED'}")
    assert not fails, "dino collides with an obstacle"
    assert apex_top >= 0, "dino jumps off the top of the canvas"
