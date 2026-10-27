# The Moving Parts

By the end of this chapter you will be
able to name the five parts that decide
whether an OCR read succeeds: **the
image**, **the preprocessing**, **the
engine**, **the language data**, and
**page segmentation**. Almost every bad
read you will ever meet is one of these
five failing, and each fails in its own
recognisable way.

## The image

Everything starts as pixels. Tesseract
wants what a careful human reader wants:
letters that are dark against a light
background (or the reverse, which it
detects), an upright page, and enough
**resolution** — enough pixels per letter
— to tell an `e` from a `c`. Print shops
measure resolution in **DPI**, dots per
inch; OCR works best around 300 DPI and
gets steadily worse below about 150.

A sharp 300-DPI scan of a clean page is
nearly a solved problem: the lab's clean
notice scored 100% character accuracy.
The same page skewed by three degrees,
peppered with speckle, printed faint, or
shrunk to 100 DPI each failed in a
different way (chapter 5 fixes all four).
The engine cannot invent pixels that are
not there, which is why so much of this
guide is about the picture, not the
program.

## The preprocessing

Few real scans arrive perfect, so before
recognition the image is usually
**preprocessed**: straightened
(**deskewed**), cleaned of speckles
(**denoised**), and converted to pure
black on pure white (**binarised**, also
called thresholding). Tesseract does some
of this itself — it converts your image
to black and white internally and can
correct small tilts — but heavy damage is
better repaired before the engine sees
the page, by an image tool working under
your control (chapters 5 and 11). The
dividing rule of this guide: light touch
inside Tesseract, real surgery outside
it, where you can see what the surgery
did.

## The engine

The recogniser itself. Modern Tesseract
(version 4 and later, including the 5.x
series this guide uses) reads with a
**neural network** — specifically an
**LSTM**, a kind of network built for
sequences — trained on lines of text. It
does not match letter templates the way
1980s OCR did; it reads a whole line at
once and judges the letter shapes in
context, which is why it can be very good
on clean print and oddly wrong on damaged
print: a smeared word is read as the
nearest *plausible* word, sometimes a
different real word, which is the hardest
kind of error to spot.

The engine is chosen with **--oem** (OCR
engine mode). The default, `--oem 1`, is
the LSTM engine and is right for nearly
everything. You will meet the option in
chapter 9 and mostly leave it alone.

## The language data

The engine knows shapes; the
**traineddata** files teach it a
language: which letter combinations are
likely, what the vocabulary looks like,
how `ß` differs from `B`. One file per
language — `eng.traineddata`,
`deu.traineddata`, `fra.traineddata` —
kept in a folder Tesseract calls its
**tessdata** directory. You name the
languages per run with `-l`:

```bash
tesseract brief.png brief -l deu
tesseract notice.png notice -l eng+deu
```

The second form reads with two languages'
knowledge at once, for pages that mix
them. Picking the wrong language is a
quiet catastrophe — the lab's German
notice read with English data loses
characters throughout (chapter 7) — and
a special file, `osd.traineddata`, is
not a language at all but the
**orientation and script** detector,
which works out which way up a page is.

## Page segmentation

Before reading, Tesseract must decide how
the page is *arranged*: where the columns
are, whether a block is a paragraph or a
caption, whether the whole image is one
line. That layout decision is **page
segmentation**, chosen with **--psm**
(page segmentation mode). The default,
`--psm 3`, analyses the layout
automatically and is right for ordinary
pages. Other modes tell the engine
"this is a single line" (`--psm 7`), "a
single word" (`--psm 8`), or "just tell
me the orientation" (`--psm 0`). A wrong
assumption here scrambles reading order
or merges columns — the lab's two-column
article read under the wrong mode comes
out interleaved (chapter 6).

## How the five parts fail, in one table

| Symptom | Likely part |
|---|---|
| Every word slightly wrong | The image (resolution, blur) |
| Gibberish in patches | The image or preprocessing (speckle, stains) |
| Right letters, wrong language's quirks | The language data |
| Columns interleaved, order scrambled | Page segmentation |
| One word read as another real word | The engine, guessing — check confidence |
| Page read as mirror nonsense | Orientation (segmentation/OSD) |

Keep this table. Chapter 15
(Troubleshooting) is mostly this table
with the fixes attached.
