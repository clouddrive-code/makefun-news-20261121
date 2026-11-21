"""Generate news.png for make.fun news-image-20261121 (21 Nov 2026).
Deterministic: fixed text, fixed colours, fixed layout, no network, no time.
Run once locally; the submitted main.py only copies the generated PNG.
Stories verified 2026-11-21 ~03:10 UTC via news search:
 - Russian Kh-101 missiles + drone crash in Poland, Tusk: intentional provocation,
   NATO Rutte: grave violation, NATO jets scrambled, no injuries reported.
 - Russia's overnight bombardment of Ukraine: 400+ drones, 110+ missiles, 8+ killed.
 - COP31 Antalya: draft drops fossil fuels, talks stall / into overtime.
 - Wall Street AI rout: Nasdaq erases 2026 gains, S&P 500 into correction (-10%).
 - Denmark expels Russian envoy / accuses Russian intelligence of assassination plot.
 - Saudi-led coalition intercepts Houthi missile; debris falls in Riyadh.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def font(p, s):
    return ImageFont.truetype(p, s)

def wrap(d, text, f, width):
    lines = []
    for para in text.split("\n"):
        lines += textwrap.wrap(para, width=width) or [""]
    return lines

def draw_wrapped(d, x, y, text, f, fill, width_chars, lh):
    for line in wrap(d, text, f, width_chars):
        d.text((x, y), line, font=f, fill=fill)
        y += lh
    return y

img = Image.new("RGB", (W, H), (247, 243, 232))  # newsprint cream
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 118], fill=(17, 24, 39))
d.text((32, 14), "THE WORLD TODAY", font=font(SERIFB, 72), fill=(255, 255, 255))
d.text((32, 88), "SATURDAY  •  21 NOVEMBER 2026  •  ONE IMAGE, SIX STORIES",
       font=font(BOLD, 20), fill=(253, 203, 88))
d.rectangle([0, 118, W, 124], fill=(185, 28, 28))

# ---- lead story: Poland ----
d.rectangle([24, 142, 1000, 470], outline=(17, 24, 39), width=4, fill=(255, 255, 255))
d.rectangle([24, 142, 1000, 188], fill=(185, 28, 28))
d.text((40, 150), "LEAD  •  NATO ON ALERT", font=font(BOLD, 26), fill=(255, 255, 255))
y = 200
y = draw_wrapped(d, 40, y, "RUSSIAN MISSILES", font(SERIFB, 54), (17, 24, 39), 22, 60)
y = draw_wrapped(d, 40, y, "LAND IN POLAND", font(SERIFB, 54), (17, 24, 39), 22, 60)
y = draw_wrapped(d, 40, y + 4,
    "Two Kh-101 missiles and a drone crash in Poland during a huge attack on Ukraine. Tusk: \"intentional provocation.\" Rutte: \"grave violation.\" No injuries.",
    font(REG, 24), (51, 51, 51), 40, 30)

# target graphic, top-right corner only — clear of the text column (x < 700)
cx, cy = 880, 260
for r, col in [(66, (254, 226, 226)), (44, (252, 165, 165)), (24, (220, 38, 38))]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col, outline=(127, 29, 29), width=3)
d.text((cx - 48, cy - 13), "POLAND", font=font(BOLD, 22), fill=(255, 255, 255))
d.text((700, 432), "Kh-101  •  ~50 km from border", font=font(BOLD, 17), fill=(127, 29, 29))

# ---- 2x2 grid of secondary stories ----
stories = [
    ("UKRAINE UNDER FIRE", (185, 28, 28),
     "Russia fires 400+ drones\nand 110+ missiles overnight.\nAt least 8 killed in Kyiv;\nbridges hit, power cut."),
    ("COP31 STALLS", (4, 120, 87),
     "Climate talks in Antalya,\nTurkiye run into overtime.\nDraft drops fossil fuels;\nno agreement in sight."),
    ("WALL ST. AI ROUT", (120, 53, 15),
     "Nasdaq erases all its\n2026 gains. S&P 500 sinks\ninto correction, down\n10% from its high."),
    ("DENMARK  •  RIYADH", (30, 64, 175),
     "Denmark expels Russia's\nenvoy over an alleged\nassassination plot. Saudi\nforces intercept a Houthi\nmissile; debris in Riyadh."),
]
boxes = [(24, 490, 500, 748), (524, 490, 1000, 748),
         (24, 768, 500, 1000), (524, 768, 1000, 1000)]
# note last row height trimmed by footer; adjust: use 768-1000 minus footer
for (x0, y0, x1, y1), (title, col, body) in zip(boxes, stories):
    d.rectangle([x0, y0, x1, y1], outline=(17, 24, 39), width=3, fill=(255, 255, 255))
    d.rectangle([x0, y0, x1, y0 + 46], fill=col)
    d.text((x0 + 14, y0 + 9), title, font=font(BOLD, 24), fill=(255, 255, 255))
    yy = y0 + 58
    for line in body.split("\n"):
        d.text((x0 + 14, yy), line, font=font(REG, 24), fill=(31, 41, 55))
        yy += 32

# footer strip over bottom edge of grid (drawn last, inside image)
d.rectangle([0, 1000, W, 1024], fill=(17, 24, 39))
d.text((32, 1004), "Sources: AP / Reuters reports, 21 Nov 2026  •  All six stories happened on 20–21 Nov 2026",
       font=font(REG, 16), fill=(255, 255, 255))

img.save("/home/hatch/workspace/makefun-news-20261121/news.png", format="PNG", optimize=True)
print("saved")
