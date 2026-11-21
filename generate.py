"""Generate news.png v2 for make.fun news-image-20261121 (21 Nov 2026).
Illustrated front page. Deterministic: fixed text, fixed colours, fixed
layout, fixed asset files, no network, no time. Run once locally; the
submitted main.py only copies the generated PNG.

Stories (same six facts as v1, verified 2026-11-21 via AP / Reuters):
 - Russian Kh-101 missiles + drone crash in Poland, Tusk: intentional
   provocation, NATO Rutte: grave violation, no injuries reported.
 - Russia's overnight bombardment of Ukraine: 400+ drones, 110+ missiles,
   8+ killed.
 - COP31 Antalya: draft drops fossil fuels, talks stall / into overtime.
 - Wall Street AI rout: Nasdaq erases 2026 gains, S&P 500 into correction.
 - Denmark expels Russian envoy / alleged assassination plot.
 - Saudi forces intercept a Houthi missile; debris in Riyadh.

v2 fixes vs v1 (user feedback): hero photo illustration instead of a weak
target graphic; every sub-story has a filled illustration (3 AI images,
1 Pillow-drawn night-skyline panel) instead of empty white boxes;
no white text on light colours (POLAND label removed entirely);
headline hierarchy is masthead > lead headline > title bars > body.
Geometry was measured so every body line fits inside its box: thumbnail
100 + title bar 34 + body 82 = 216 per grid row, body 19pt / 24px line
height, 3 lines max. Hero is cropped with centering (0.5, 0.32) so the
missile, drone and jets are all inside the frame.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
W = H = 1024
CREAM = (247, 243, 232)
INK = (17, 24, 39)
DARKRED = (185, 28, 28)
GOLD = (253, 203, 88)
WHITE = (255, 255, 255)
BODY = (31, 41, 55)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(p, s):
    return ImageFont.truetype(p, s)


def wrap_px(d, text, f, max_w):
    """Greedy word wrap measured in pixels, so no line ever overflows."""
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if d.textlength(trial, font=f) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur or not lines:
            lines.append(cur)
    return lines


def draw_lines(d, x, y, text, f, fill, max_w, lh):
    for line in wrap_px(d, text, f, max_w):
        d.text((x, y), line, font=f, fill=fill)
        y += lh
    return y


def fit(path, w, h, cy=0.45):
    im = Image.open(path).convert("RGB")
    return ImageOps.fit(im, (w, h), method=Image.LANCZOS, centering=(0.5, cy))


def draw_riyadh_panel(w, h):
    """Pillow-drawn thumbnail for Denmark + Riyadh: night desert skyline,
    a missile streak crossing the sky and an interception burst.
    Fully filled, no text, no empty area."""
    im = Image.new("RGB", (w, h), (10, 22, 48))
    d = ImageDraw.Draw(im)
    for y in range(h):
        t = y / max(h - 1, 1)
        d.line([(0, y), (w, y)], fill=(
            int(10 + 40 * t), int(22 + 30 * t), int(48 + 55 * t)))
    for sx, sy in [(28, 14), (70, 30), (120, 10), (180, 26), (240, 12),
                   (300, 32), (360, 14), (420, 28), (52, 44), (330, 48)]:
        d.ellipse([sx, sy, sx + 3, sy + 3], fill=(255, 244, 200))
    # interception streak + burst, kept inside the panel
    d.line([(40, 88), (400, 30)], fill=(255, 190, 80), width=5)
    d.line([(40, 88), (400, 30)], fill=(255, 255, 255), width=2)
    bx, by = 400, 30
    for r, col in [(24, (255, 190, 80)), (14, (255, 230, 150)), (7, (255, 255, 255))]:
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=col)
    for dx, dy in [(-30, -8), (-24, 14), (-34, 4), (-18, -16)]:
        d.line([(bx, by), (bx + dx, by + dy)], fill=(255, 210, 110), width=2)
    buildings = [(0, 62, 58, 100), (52, 48, 96, 100), (92, 70, 150, 100),
                 (146, 40, 186, 100), (182, 66, 240, 100), (236, 52, 282, 100),
                 (278, 72, 330, 100), (326, 46, 368, 100), (364, 68, 420, 100),
                 (416, 56, 476, 100)]
    for x0, y0, x1, y1 in buildings:
        d.rectangle([x0, y0, x1, y1], fill=(6, 14, 32))
        for wy in range(y0 + 8, y1 - 6, 12):
            for wx in range(x0 + 7, x1 - 7, 14):
                if (wx * 7 + wy * 3) % 5 < 2:
                    d.rectangle([wx, wy, wx + 4, wy + 5], fill=(255, 200, 90))
    return im


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 92], fill=INK)
d.text((24, 10), "THE WORLD TODAY", font=font(SERIFB, 58), fill=WHITE)
d.text((24, 70), "SATURDAY  •  21 NOVEMBER 2026  •  ONE IMAGE, SIX STORIES",
       font=font(BOLD, 17), fill=GOLD)
d.rectangle([0, 92, W, 98], fill=DARKRED)

# ---- lead: hero image, kicker, headline, deck, quote strip ----
LX0, LX1 = 24, 1000
img.paste(fit(os.path.join(ASSETS,
    "media-generation-hero-poland-0-a4288991-eda5-49a9-80ff-3aa2ce7c1d84.png"),
    LX1 - LX0, 200, cy=0.32), (LX0, 106))
d.rectangle([LX0, 306, LX1, 338], fill=DARKRED)
d.text((LX0 + 16, 313), "LEAD  •  NATO ON ALERT", font=font(BOLD, 21), fill=WHITE)
d.text((LX0 + 16, 348), "RUSSIAN MISSILES", font=font(SERIFB, 44), fill=INK)
d.text((LX0 + 16, 396), "LAND IN POLAND", font=font(SERIFB, 44), fill=INK)
draw_lines(d, LX0 + 16, 444,
           "Two Kh-101 missiles and a drone crash in Poland during a huge "
           "attack on Ukraine. NATO jets scrambled.",
           font(REG, 20), BODY, LX1 - LX0 - 32, 25)
d.rectangle([LX0, 494, LX1, 526], fill=INK)
d.text((LX0 + 16, 501),
       "Tusk: “intentional provocation”  •  Rutte: “grave violation”  •  No injuries",
       font=font(BOLD, 18), fill=WHITE)

# ---- 2x2 grid: thumbnail 100 + title bar 34 + body 82 = 216 per row ----
stories = [
    ("UKRAINE UNDER FIRE", DARKRED,
     os.path.join(ASSETS,
        "media-generation-thumb-ukraine-0-aa5a3c18-d26d-4721-a299-6d832ba026a8.png"),
     "400+ drones and 110+ missiles\nin a single night. 8+ killed;\nbridges hit, power cut."),
    ("COP31 STALLS", (4, 120, 87),
     os.path.join(ASSETS,
        "media-generation-thumb-cop31-0-59b73f3f-7b35-4655-8570-5e4d22d40e2a.png"),
     "Climate talks in Antalya\nstall into overtime. Draft\ndrops fossil fuels."),
    ("WALL ST. AI ROUT", (120, 53, 15),
     os.path.join(ASSETS,
        "media-generation-thumb-markets-0-a8ee4c8c-0466-4d1f-85ca-77f9a7cd2c3a.png"),
     "Nasdaq erases all its 2026\ngains. S&P 500 sinks into\ncorrection, down 10%."),
    ("DENMARK  •  RIYADH", (30, 64, 175),
     None,
     "Denmark expels Russia's\nenvoy. Saudi forces intercept\na Houthi missile over Riyadh."),
]
boxes = [(24, 538, 500, 754), (524, 538, 1000, 754),
         (24, 766, 500, 982), (524, 766, 1000, 982)]
for (x0, y0, x1, y1), (title, col, thumb, body) in zip(boxes, stories):
    bw = x1 - x0
    d.rectangle([x0, y0, x1, y1], fill=WHITE)
    if thumb:
        img.paste(fit(thumb, bw, 100), (x0, y0))
    else:
        img.paste(draw_riyadh_panel(bw, 100), (x0, y0))
    d.rectangle([x0, y0 + 100, x1, y0 + 134], fill=col)
    d.text((x0 + 12, y0 + 107), title, font=font(BOLD, 22), fill=WHITE)
    draw_lines(d, x0 + 12, y0 + 142, body, font(REG, 19), BODY, bw - 24, 24)
    d.rectangle([x0, y0, x1, y1], outline=INK, width=3)

# ---- footer ----
d.rectangle([0, 990, W, 1024], fill=INK)
d.text((24, 998),
       "Sources: AP / Reuters, 21 Nov 2026  •  All six stories happened on 20–21 Nov 2026",
       font=font(REG, 15), fill=WHITE)

img.save(os.path.join(HERE, "news.png"), format="PNG", optimize=True, compress_level=9)
print("saved")
