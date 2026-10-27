# Getting a Clean Image

By the end of this chapter you will know
which kinds of damage actually hurt OCR,
which ones barely matter — the lab
measured both, and the answers are not
the ones intuition predicts — and the
standard repairs that rescue a bad page.

Every page below is the clean notice
from chapter 4 (100.0% character
accuracy), damaged in exactly one way
and re-measured with the same ruler
(transcripts `t02`, `t02b` and `t03` in
the lab; the full ledger is
`t90-accuracy-ledger.txt`).

## What barely hurt

Modern Tesseract is tougher than its
reputation:

- **A slight tilt.** At 3 degrees the
  read scored 99.6%. The only casualty
  was *morning*, read as *moming* — the
  classic `rn`→`m` confusion.
- **Pale print.** The notice reprinted
  in light grey, then in paler grey with
  a slight blur: 100.0% both times. The
  engine **binarises** — converts to pure
  black and white — intelligently, and
  uniform pale ink still separates
  cleanly from the paper.
- **Uneven light.** A page "photographed"
  with a smooth fall from bright to dim
  across it: 100.0%. Even a hard shadow
  edge — dark on one side of a sharp line
  — cost only 2.1% (97.9%), losing the
  tail of the bold heading.
- **Missing resolution data.** An image
  saved with no DPI information at all:
  100.0%. Tesseract noticed, said
  `Estimating resolution as 402`, and
  carried on. (Feed it a *wrong* DPI,
  though, and it will believe you —
  chapter 15.)

Do not conclude damage never matters.
Conclude that *these* damages, at *these*
levels, are inside what the engine's own
preprocessing can absorb.

## What genuinely hurt

- **A real tilt.** The same notice at 8
  degrees: **38.0%**. Lines slope enough
  that the reader's line-finding fails,
  and the text comes back shredded.
- **Heavy speckle.** Dense black dust
  plus grey blotches, like a dirty
  photocopier: **83.8%**. Speckle becomes
  fake punctuation and phantom words;
  blotches eat real letters.
- **Genuinely low resolution.** The
  notice rendered at about 70 DPI:
  **87.5%**. Letters are only a few
  pixels tall; `e`, `c` and `o` blur
  into one another and no reader can
  separate what was never distinct.

## The repairs, measured

Each repair is one classic image
operation, done in the lab with a small
script (`tesseract-lab/fix-images.py`)
and available in every image editor and
in command-line image tools under
similar names.

**Deskew the tilted page.** Measure the
tilt (or search for the angle whose
text rows line up sharpest), rotate by
the opposite amount. The lab's search
found exactly −8.00 degrees on the 8°
page: **38.0% → 100.0%**. A complete
rescue, and always worth trying first,
because tilt poisons every later step.

**Denoise the speckled page.** A
**median filter** — replace each pixel
with the middle value of its
neighbourhood — kills lone black specks
while keeping letter edges. Followed by
a threshold to pure black and white:
**83.8% → 93.2%**. Better, not perfect:
speckle can be removed, but letters the
blotches swallowed are gone for good,
and no filter invents them back.

**Upscale the tiny page.** Enlarge three
times with a good resampling filter and
tell the file it is 300 DPI:
**87.5% → 99.2%**. Upscaling invents no
detail, but it gives the engine letters
at the size it was trained on, and it
separates nearly-touching shapes.

**The repair that lost.** The shadowed
page seemed to call for **background
normalisation** — divide the page by a
blurred copy of itself to cancel the
lighting, then threshold. Result:
**97.9% → 95.8%**, worse. The division
amplified murk in the dark half and the
threshold then misjudged letters the
engine's own subtler binarisation had
read fine. Keep the lesson, it is worth
more than the technique: *measure after
every fix, keep the version that scores
best, and be ready for "help" to hurt.*
That is why this guide measures
everything twice.

## Working rules

1. Scan flat and square at 300 DPI if
   you control the scan; most later pain
   is prevented here.
2. Fix tilt before anything else.
3. Remove speckle before thresholding;
   threshold after denoising, not
   before.
4. Upscale small images rather than
   feeding them tiny.
5. Keep the original untouched, work on
   copies, and measure each candidate
   against your known-truth page before
   trusting a pipeline on real pages.
