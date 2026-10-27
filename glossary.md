# Glossary

**Adaptive thresholding** — binarising
with a level chosen locally, region by
region, instead of one level for the
whole page; the reason unevenly lit
pages often read well (chapter 5).

**Binarise** — convert an image to pure
black on pure white by choosing a
brightness threshold; Tesseract does
this internally, and preprocessing
sometimes does it first (chapter 5).

**Bounding box** — the rectangle
(`left`, `top`, `width`, `height`, in
pixels) around a word or line, reported
in TSV and hOCR output (chapter 8).

**CER** — character error rate: edits
needed to turn the OCR output into the
known truth, divided by the truth's
length. The lab's measuring ruler
(chapter 4).

**Confidence** — Tesseract's 0–100
score per word: its own estimate of a
read's reliability. A triage tool, not
a verdict (chapter 9).

**Deskew** — rotating a page by the
negative of its tilt so text lines run
level (chapter 5).

**DPI** — dots (pixels) per inch: an
image's stated resolution. Around 300
is OCR's comfort zone (chapter 2).

**hOCR** — an XHTML output format
carrying each word with its bounding
box and confidence (chapter 8).

**Leptonica** — the image-processing
library Tesseract reads pictures
through; named in `tesseract --version`
(chapter 3).

**LSTM** — long short-term memory: the
kind of neural network, built for
sequences, that modern Tesseract reads
lines with (chapter 2).

**Median filter** — a denoise that
replaces each pixel with the middle
value of its neighbours, killing lone
specks while keeping edges (chapter 5).

**OCR** — optical character
recognition: turning pictures of text
into text (chapter 1).

**OEM** — OCR engine mode, chosen with
`--oem`; the default (1) is the LSTM
engine (chapter 9).

**OSD** — orientation and script
detection, performed by
`osd.traineddata`; reports which way up
a page is and in what script
(chapter 6).

**Preprocessing** — repairing an image
before the engine reads it: deskew,
denoise, threshold, upscale
(chapters 5 and 11).

**PSM** — page segmentation mode,
chosen with `--psm`: the assumption
about how a page is laid out
(chapter 6).

**Segmentation** — dividing a page into
regions, lines and words before (and
while) reading them (chapter 2).

**Traineddata** — the per-language data
file that teaches the engine a
language's shapes and habits
(chapters 3 and 7).

**TSV** — tab-separated values output:
one row per word with position and
confidence (chapter 8).

**Whitelist** — a setting
(`tessedit_char_whitelist`) restricting
which characters the engine may output
at all (chapter 9).
