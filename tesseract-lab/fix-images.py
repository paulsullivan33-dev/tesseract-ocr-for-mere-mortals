#!/usr/bin/env python3
"""Repair the lab's damaged pages, one classic operation each:

- notice-skewed8.png  -> deskew (projection-profile search)
- notice-noisy2.png   -> median filter, then threshold
- notice-uneven.png   -> background normalisation, then threshold
- notice-lowres2.png  -> upscale 3x, save at 300 dpi

Each repair writes images/<name>-fixed.png. The operations are
the standard ones every image tool offers under some name; they
are done here with PIL and numpy so the lab needs nothing else.
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

HERE = Path(__file__).resolve().parent
IMG = HERE / "images"


def deskew(img, limit=10.0):
    """Find the rotation that makes text rows line up: try small
    angles on a shrunk binary copy and keep the one whose row
    projections vary the most (sharp lines beat smears)."""
    small = img.convert("L").resize((img.width // 4, img.height // 4))
    binary = small.point(lambda v: 0 if v < 128 else 255)
    best_angle, best_score = 0.0, -1.0
    angle = -limit
    while angle <= limit:
        rot = binary.rotate(angle, resample=Image.NEAREST, fillcolor=255)
        rows = (255 - np.asarray(rot, dtype=np.int64)).sum(axis=1)
        score = float((rows ** 2).sum())
        if score > best_score:
            best_angle, best_score = angle, score
        angle += 0.25
    print(f"deskew: best angle {best_angle:+.2f} degrees")
    return img.rotate(best_angle, resample=Image.BICUBIC, fillcolor="white")


def threshold(img, level=160):
    return img.convert("L").point(lambda v: 255 if v > level else 0).convert("RGB")


def normalise_background(img):
    """Divide the page by a blurred copy of itself. The blur holds
    only the lighting; dividing cancels slow brightness changes
    and leaves the letters at full contrast everywhere."""
    gray = np.asarray(img.convert("L"), dtype=np.float64)
    bg = np.asarray(
        img.convert("L").filter(ImageFilter.GaussianBlur(40)), dtype=np.float64)
    bg[bg == 0] = 1.0
    fixed = np.clip(gray / bg * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(fixed, mode="L").convert("RGB")


def main():
    skewed = Image.open(IMG / "notice-skewed8.png")
    deskew(skewed).save(IMG / "notice-skewed8-fixed.png", dpi=(300, 300))
    print("wrote notice-skewed8-fixed.png")

    noisy = Image.open(IMG / "notice-noisy2.png")
    threshold(noisy.filter(ImageFilter.MedianFilter(3)), 150).save(
        IMG / "notice-noisy2-fixed.png", dpi=(300, 300))
    print("wrote notice-noisy2-fixed.png")

    uneven = Image.open(IMG / "notice-uneven.png")
    threshold(normalise_background(uneven), 170).save(
        IMG / "notice-uneven-fixed.png", dpi=(300, 300))
    print("wrote notice-uneven-fixed.png")

    lowres = Image.open(IMG / "notice-lowres2.png")
    big = lowres.resize((lowres.width * 3, lowres.height * 3), Image.LANCZOS)
    big.save(IMG / "notice-lowres2-fixed.png", dpi=(300, 300))
    print("wrote notice-lowres2-fixed.png")


if __name__ == "__main__":
    main()
