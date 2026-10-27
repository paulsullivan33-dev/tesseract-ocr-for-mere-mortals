# Tesseract OCR for Mere Mortals

A scanned page is a picture, and a
picture cannot be searched, copied, or
read aloud. **Tesseract** is the free
**OCR** engine — optical character
recognition — that turns those pictures
back into text: it finds the lines,
reads the letter shapes with a neural
network, and writes out words a program
can use, entirely on your own machine.
This guide explains how that works, how
to get a first perfect read, and — the
part most OCR advice skips — what to do
with the imperfect ones: the tilted, the
speckled, the faint, the tiny, the
upside-down, and the confidently wrong.

The method throughout is measurement.
Because the lab's test pages are pages
it printed itself as images, it knows
their true text character for character,
so every claim in this guide carries a
number: the clean notice at 100%
character accuracy, the same notice at
eight degrees of tilt at 38%, rescued to
100% again by deskewing. Where the
engine surprised the lab — pale print
and lopsided lighting barely hurt it; a
repair for the shadowed page scored
*worse* than the damage — the surprise
is in the text with its numbers, not
smoothed over.

The lab behind this guide ran the real
thing: **Tesseract 5.3.4** (Leptonica
1.82.0) on a small Linux machine,
reading a shelf of generated fixtures —
a community-hall notice, a bakery
receipt, a two-column article, a German
reading-circle notice — and twelve
damaged variants of the notice, each
hurt in one measured way. Against those
pages the lab verified the install
checks, the first read, deskew,
denoise, upscaling and background
normalisation repairs, six page
segmentation modes including the
orientation report and the automatic
uprighting of a flipped page, three
language settings on the German notice
(plus the error the wrong one makes),
four output formats — plain text, TSV,
hOCR, and a searchable PDF whose text
layer was extracted and measured
independently — word-level confidence
scores including the one wrong word
they catch and the right word they
falsely accuse, a folder batch, a list
file, and the stdin/stdout pipe form.

What the lab could not do, it did not
fake. Its pages are synthetic — rendered
type, not photographs of real paper — so
real-world grime (folds, bleed-through,
a thumb over the lens) is discussed from
the engine's documented behaviour and
the shape of the lab's results, and
chapter 14 says where that leaves you.
The macOS and Windows install routes are
described from the project's
documentation rather than demonstrated.
Handwriting was not tested because the
engine makes no claim to read it.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What Tesseract OCR is**](what-tesseract-ocr-is.md) —
  pictures of text versus text, what the
  engine hands back, and the rule for
  other people's pages
- [**The moving parts**](the-moving-parts.md) —
  the image, the preprocessing, the
  engine, the language data and page
  segmentation, and which part fails how
- [**Installing Tesseract**](installing-tesseract.md) —
  the program plus its language files,
  and the two commands that prove the
  install
- [**Your first OCR**](your-first-ocr.md) —
  one clean page read to screen and to
  file, and how to prove the read with a
  character error rate
- [**Getting a clean image**](getting-a-clean-image.md) —
  tilt, speckle, faint print, shadows and
  low resolution, each damaged on purpose
  and measured, and the repairs that
  rescue them — plus the repair that lost
- [**Page segmentation modes**](page-segmentation-modes.md) —
  the layout assumption inside every
  read, the two-column trap, single lines
  and words, and the orientation modes
- [**Languages and traineddata**](languages-and-traineddata.md) —
  how the engine knows a language, the
  German notice under three settings,
  and adding languages of your own
- [**Output formats**](output-formats.md) —
  plain text, TSV, hOCR and the
  searchable PDF, all switched by one
  small mechanism
- [**Confidence and checking the result**](confidence-and-checking.md) —
  word scores as a triage tool, the
  wrong word they catch, the right word
  they accuse, and a checking workflow
- [**Batch work on folders**](batch-work.md) —
  the loop, the list file, keeping the
  evidence, and the stdin/stdout pipe
- [**OCR in a pipeline**](ocr-in-a-pipeline.md) —
  repair before, checking after, and the
  rules that keep a production line
  honest
- [**Recipes**](recipes.md) — a
  searchable shoebox, a tilted batch
  rescued, a receipt into a spreadsheet,
  the wrong-language fix, mixed
  orientations, figures only
- [**The neighbours**](the-neighbours.md) —
  other engines, the cloud services,
  OCRmyPDF and scanner software: what
  each does that Tesseract doesn't
- [**Limits**](limits.md) — print only,
  shapes not meaning, the confident
  error, damage floors and layout edges,
  stated plainly
- [**Troubleshooting**](troubleshooting.md) —
  the empty read, the interleaved
  columns, the one character always
  wrong, missing language data, and the
  fix that made it worse
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Handwriting recognition — the engine
does not claim it and this guide does
not pretend otherwise. Reading text in
photographs of the world (signs,
whiteboards, shopfronts) belongs to a
different family of tools, named in
chapter 13. Building a document
management system — storage, indexing,
retention — is likewise beyond the
engine and the guide; chapter 11 shows
where OCR hands over to such systems.
And reading other people's documents
without permission is not a harder
chapter of this book; chapter 1 explains
the line.

## How to use this guide

Read chapters 1 and 2 for the model —
five parts, five failure shapes — then
install (chapter 3) and take the first
read (chapter 4) in the same sitting.
Make a known-truth page of your own
early: one page typed by hand and kept,
because without it you cannot measure
anything and chapters 5 and 9 lose
their teeth. Read chapter 9 before
trusting any output you care about.
The lab's images are in
`tesseract-lab/images/` with their true
texts beside them; its scripts are
`tesseract-lab/make-images.py`,
`make-images-hard.py`, `fix-images.py`
and `measure.py`; its transcripts and
the full accuracy ledger are in
`tesseract-lab/transcripts/`; its notes
are `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Pandoc for Mere Mortals](https://paulsullivan33-dev.github.io/pandoc-for-mere-mortals/)
- [Stirling PDF for Mere Mortals](https://paulsullivan33-dev.github.io/stirling-pdf-for-mere-mortals/)
- [ExifTool for Mere Mortals](https://paulsullivan33-dev.github.io/exiftool-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/tesseract-ocr-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/tesseract-ocr-for-mere-mortals/blob/main/LICENSE-CODE).
