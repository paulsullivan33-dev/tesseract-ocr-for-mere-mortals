#!/usr/bin/env python3
"""Generate the lab's test pages: fictional notices, a receipt,
a two-column article and a short German letter, plus damaged
variants (skewed, noisy, faint, low resolution, upside down).

Every text is invented for this guide. Ground truth for each page
is written next to the image as a .txt file with the same stem.
"""
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
IMG = HERE / "images"
IMG.mkdir(parents=True, exist_ok=True)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"

from PIL import ImageFont


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_lines(draw, lines, x, y, leading):
    for line in lines:
        draw.text((x, y), line, fill=(0, 0, 0), font=line[1] if False else None) if False else None
        y += leading
    return y


def notice_page(ink=(0, 0, 0), scale=1.0, body=46, head=88):
    """The clean community-hall notice. Returns (image, truth lines)."""
    W, H = int(2200 * scale), int(2800 * scale)
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    m = int(220 * scale)
    y = int(190 * scale)
    head_f = font(SANS_B, int(head * scale))
    body_f = font(SERIF, int(body * scale))
    d.text((m, y), "MAPLE STREET COMMUNITY HALL", fill=ink, font=head_f)
    y += int(170 * scale)
    d.text((m, y), "Spring Cleanup Day", fill=ink, font=font(SERIF_B, int(64 * scale)))
    y += int(150 * scale)
    paras = [
        ["Saturday, April 18, from 9 in the morning",
         "until noon. Volunteers will sweep the hall,",
         "wash the windows, and clear the garden beds",
         "behind the building."],
        ["Please bring gloves and a bucket if you",
         "have them. Coffee, tea, and biscuits will",
         "be served in the kitchen at eleven."],
        ["Everyone is welcome. Children may help in",
         "the garden if an adult stays with them."],
        ["To sign up, write your name on the sheet",
         "by the front door, or call the hall office",
         "at 555-0142 before Thursday evening."],
    ]
    truth = ["MAPLE STREET COMMUNITY HALL", "Spring Cleanup Day"]
    for para in paras:
        for line in para:
            d.text((m, y), line, fill=ink, font=body_f)
            y += int(78 * scale)
            truth.append(line)
        y += int(58 * scale)
    return img, truth


def save(img, name, truth=None, dpi=(300, 300)):
    img.save(IMG / name, dpi=dpi)
    if truth is not None:
        (IMG / (Path(name).stem + ".txt")).write_text("\n".join(truth) + "\n", encoding="utf-8")
    print("wrote", name)


# 1. The clean notice.
img, truth = notice_page()
save(img, "notice-clean.png", truth)

# 2. The same notice, skewed by 3 degrees.
save(img.rotate(3, resample=Image.BICUBIC, fillcolor="white"),
     "notice-skewed.png", truth)

# 3. The same notice, upside down.
save(img.rotate(180), "notice-upside-down.png", truth)

# 4. The same notice, noisy: speckle plus a light blur.
random.seed(42)
noisy = img.filter(ImageFilter.GaussianBlur(0.7))
px = noisy.load()
W, H = noisy.size
for _ in range(26000):
    x, y = random.randrange(W), random.randrange(H)
    px[x, y] = (0, 0, 0)
nd = ImageDraw.Draw(noisy)
for _ in range(26):
    x, y = random.randrange(W - 60), random.randrange(H - 30)
    nd.ellipse([x, y, x + random.randrange(8, 46), y + random.randrange(5, 22)],
               fill=(70, 70, 70))
save(noisy, "notice-noisy.png", truth)

# 5. The same notice, faint: pale grey ink, as from a tired printer.
faint, _ = notice_page(ink=(168, 168, 168))
save(faint, "notice-faint.png", truth)

# 6. The same notice at low resolution (about 100 dpi).
small, _ = notice_page(scale=0.34, body=46, head=88)
save(small, "notice-lowres.png", truth, dpi=(100, 100))

# 7. The same notice saved with no resolution information at all.
img.save(IMG / "notice-nodpi.png")
(IMG / "notice-nodpi.txt").write_text("\n".join(truth) + "\n", encoding="utf-8")
print("wrote notice-nodpi.png")

# 8. A fictional bakery receipt, in a monospace face.
receipt_lines = [
    "CORNER BAKERY",
    "14 Willow Lane",
    "------------------------------",
    "2  Sourdough loaf      7.50",
    "1  Butter croissant    3.25",
    "3  Cheese roll         5.40",
    "1  Orange juice        2.95",
    "------------------------------",
    "TOTAL                 19.10",
    "Cash                  20.00",
    "Change                 0.90",
    "",
    "Thank you. See you soon.",
]
rimg = Image.new("RGB", (1080, 1240), "white")
rd = ImageDraw.Draw(rimg)
rf = font(MONO, 40)
y = 60
for line in receipt_lines:
    rd.text((60, y), line, fill=(0, 0, 0), font=rf)
    y += 84
save(rimg, "receipt.png", receipt_lines)

# 9. A two-column article, for the page-segmentation chapter.
col_left = [
    "Planting Tomatoes",
    "",
    "Tomatoes want sun, steady",
    "water, and patience. Start",
    "the seeds indoors six weeks",
    "before the last frost, in",
    "small pots by a bright",
    "window. Turn the pots a",
    "little each day so the",
    "seedlings grow straight.",
]
col_right = [
    "Move the young plants out",
    "only when the nights stay",
    "mild. Dig a deep hole, set",
    "the stem low in the soil,",
    "and water well. Roots will",
    "grow along the buried stem",
    "and the plant will stand",
    "firmer in the wind.",
]
cimg = Image.new("RGB", (2200, 1500), "white")
cd = ImageDraw.Draw(cimg)
bf = font(SERIF, 46)
tf = font(SERIF_B, 58)
y = 120
for line in col_left:
    cd.text((140, y), line, fill=(0, 0, 0),
            font=tf if line == "Planting Tomatoes" else bf)
    y += 82
y = 120
for line in col_right:
    cd.text((1180, y), line, fill=(0, 0, 0), font=bf)
    y += 82
save(cimg, "columns.png", col_left + col_right)

# 10. A short German notice, for the languages chapter.
deu_lines = [
    "GEMEINDEHAUS AHORNSTRASSE",
    "",
    "Der Lesekreis trifft sich jeden Dienstag",
    "um 19 Uhr im kleinen Saal. Im November",
    "lesen wir kurze Geschichten und sprechen",
    "dar\u00fcber bei Tee und Keksen.",
    "",
    "Neue Leserinnen und Leser sind herzlich",
    "willkommen. Die Teilnahme ist kostenlos.",
]
dimg = Image.new("RGB", (2200, 1600), "white")
dd = ImageDraw.Draw(dimg)
y = 160
for line in deu_lines:
    dd.text((180, y), line, fill=(0, 0, 0),
            font=font(SANS_B, 62) if line.startswith("GEMEINDE") else font(SERIF, 52))
    y += 104
save(dimg, "letter-deu.png", deu_lines)

# 11. A single line and a single word, for PSM 7 and PSM 8.
limg = Image.new("RGB", (1500, 220), "white")
ld = ImageDraw.Draw(limg)
ld.text((50, 60), "The meeting starts at seven in the hall.",
        fill=(0, 0, 0), font=font(SERIF, 54))
save(limg, "one-line.png", ["The meeting starts at seven in the hall."])

wimg = Image.new("RGB", (700, 220), "white")
wd = ImageDraw.Draw(wimg)
wd.text((50, 60), "Cleanup", fill=(0, 0, 0), font=font(SERIF_B, 72))
save(wimg, "one-word.png", ["Cleanup"])

print("done")
