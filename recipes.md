# Recipes

Small jobs, whole. Each assumes the
install of chapter 3 and pages that are
yours to read (chapter 1's rule). Every
recipe here was run in the lab in some
form; the transcripts are named so you
can check.

## Make a shoebox of scans searchable

The archive job, whole: a folder of page
images becomes a folder of searchable
PDFs, with TSVs kept for checking.

```bash
mkdir -p pdfs audit
for f in scans/*.png; do
  b=$(basename "${f%.png}")
  tesseract "$f" "pdfs/$b" pdf 2> "audit/$b.log"
  tesseract "$f" "audit/$b" tsv 2>/dev/null
done
```

Then chapter 9's awk line over the TSVs
lists the pages a human should eyeball.

## Rescue the tilted batch

A scanner feeder that skews everything
by roughly the same angle: deskew with
your image tool's rotate or `-deskew`,
then re-read. The lab's 8° page went
from 38.0% to 100.0% on this alone
(transcript `t03`). If angles vary page
to page, deskew must be measured per
page — the lab's `fix-images.py` shows
one honest way (a projection-profile
search), and chapter 5 explains it.

## Read the receipt into a spreadsheet

Receipts and other narrow print read
best as TSV, whose columns *are*
spreadsheet-shaped:

```bash
tesseract receipt.png receipt tsv
```

Open the `.tsv` in any spreadsheet and
the words arrive with coordinates, so
sorting by `top` then `left` rebuilds
the lines. Mind the lesson of the lab's
receipt: decorative rules and heavy
spacing vanish from the text, while the
figures — the part you actually want —
came through exactly.

## A page in the wrong language

Symptoms: text mostly fine, one
character family consistently mangled.
Fix: install the language, name it.

```bash
tesseract letter.png letter -l deu
```

Measured on the lab's German notice:
99.2% under English data (the `ü` in
*darüber* destroyed), 100.0% under
German. For mixed pages, `-l eng+deu`
(chapter 7) — and read the result,
because combined data is not a promise.

## Mixed-orientation scans

```bash
for f in scans/*.png; do
  tesseract "$f" "${f%.png}" --psm 1
done
```

Mode 1 detects each page's orientation
and rotates before reading. The lab's
upside-down page: 14.7% unaided, 100.0%
this way (transcript `t04`). Check
`--psm 0`'s report on a sample page
first if a batch matters; detection
confidence is printed and is usually
honest.

## OCR a screenshot or a pipe

```bash
screenshot-tool -o shot.png
tesseract shot.png stdout
```

or, with no file at all, any program
that emits image bytes can feed
`tesseract stdin stdout` directly
(chapter 10 ran it off `cat`). Small
on-screen text is low-resolution text:
expect chapter 5's low-DPI behaviour,
and upscale first if the words matter.

## Numbers only, from a form

For a column of figures where letters
would be errors:

```bash
tesseract figures.png figures -c tessedit_char_whitelist=0123456789.,
```

The whitelist forbids everything else.
Verify on one known form before
trusting it on fifty — chapter 9's
warning applies: a whitelist on prose
will turn every `S` into a `5` without
a flicker of doubt.
