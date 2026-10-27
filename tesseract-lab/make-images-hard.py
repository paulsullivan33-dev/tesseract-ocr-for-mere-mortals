#!/usr/bin/env python3
"""Second fixture set: the same fictional notice, damaged harder.

The first set (make-images.py) turned out to be gentle damage
that Tesseract 5 shrugs off. These are the heavier, still common
cases: an 8-degree skew, heavy speckle with blotches, very pale
ink with blur, and a genuinely low-resolution rendering.
Ground truth is the notice text, unchanged.
"""
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
IMG = HERE / "images"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

truth = (IMG / "notice-clean.txt").read_text(encoding="utf-8")


def notice(ink=(0, 0, 0), scale=1.0):
    img = Image.new("RGB", (int(2200 * scale), int(2800 * scale)), "white")
    d = ImageDraw.Draw(img)
    m, y = int(220 * scale), int(190 * scale)
    d.text((m, y), "MAPLE STREET COMMUNITY HALL", fill=ink,
           font=ImageFont.truetype(SANS_B, int(88 * scale)))
    y += int(170 * scale)
    d.text((m, y), "Spring Cleanup Day", fill=ink,
           font=ImageFont.truetype(SERIF_B, int(64 * scale)))
    y += int(150 * scale)
    body = ImageFont.truetype(SERIF, int(46 * scale))
    lines = [ln for ln in truth.splitlines()[2:] if ln]
    # Rebuild the paragraph layout exactly as make-images.py did:
    paras = [lines[0:4], lines[4:7], lines[7:9], lines[9:12]]
    for para in paras:
        for line in para:
            d.text((m, y), line, fill=ink, font=body)
            y += int(78 * scale)
        y += int(58 * scale)
    return img


clean = notice()

# Skewed hard: 8 degrees.
clean.rotate(8, resample=Image.BICUBIC, fillcolor="white").save(
    IMG / "notice-skewed8.png", dpi=(300, 300))

# Noisy hard: dense speckle plus bigger blotches, slight blur.
random.seed(7)
noisy = clean.filter(ImageFilter.GaussianBlur(0.9))
px = noisy.load()
W, H = noisy.size
for _ in range(120000):
    px[random.randrange(W), random.randrange(H)] = (0, 0, 0)
nd = ImageDraw.Draw(noisy)
for _ in range(70):
    x, y = random.randrange(W - 120), random.randrange(H - 60)
    nd.ellipse([x, y, x + random.randrange(20, 110), y + random.randrange(8, 40)],
               fill=(60, 60, 60))
noisy.save(IMG / "notice-noisy2.png", dpi=(300, 300))

# Faint hard: very pale ink plus blur.
faint = notice(ink=(198, 198, 198)).filter(ImageFilter.GaussianBlur(1.0))
faint.save(IMG / "notice-faint2.png", dpi=(300, 300))

# Low resolution hard: about 70 dpi.
small = notice(scale=0.23)
small.save(IMG / "notice-lowres2.png", dpi=(72, 72))

# Uneven light: the page is photographed, not scanned. The
# background falls off from white at the top left to mid grey at
# the bottom right, while the ink is a flat dark grey, so in the
# dim corner letters and background are nearly the same shade.
import numpy as np

base = np.asarray(notice(ink=(80, 80, 80)).convert("L"), dtype=np.float64)
H, W = base.shape
cols = np.linspace(0.0, 0.5, W)[None, :]
rows = np.linspace(0.0, 0.5, H)[:, None]
field = 1.0 - 0.62 * (cols + rows)  # 1.00 top left -> 0.38 bottom right
uneven = np.clip(base * field, 0, 255).astype("uint8")
Image.fromarray(uneven, mode="L").convert("RGB").save(
    IMG / "notice-uneven.png", dpi=(300, 300))

for name in ("notice-skewed8", "notice-noisy2", "notice-faint2",
             "notice-lowres2", "notice-uneven"):
    (IMG / f"{name}.txt").write_text(truth, encoding="utf-8")
    print("wrote", name + ".png")
