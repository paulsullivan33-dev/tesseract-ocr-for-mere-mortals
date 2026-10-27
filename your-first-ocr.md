# Your First OCR

By the end of this chapter you will have
turned a picture of a page into text,
twice — once to the screen, once to a
file — and you will know how to *prove*
the read was good, not just hope it was.

## The page

The lab's page is `notice-clean.png`, a
fictional community-hall notice the lab
printed itself as an image: black print
on white, upright, sharp, about 300 DPI.
Because the lab made the page, it knows
the true text character for character —
that is what makes measuring possible.
Your own first page should be the easiest
page you own: a flat, well-lit scan of
clean print.

## The command

```bash
tesseract images/notice-clean.png stdout
```

`tesseract` takes the image first and
the **output base name** second.
`stdout` is a special base name meaning
"print the text instead of writing a
file". The lab's run (transcript
`tesseract-lab/transcripts/t01-first-ocr.txt`)
begins:

```text
MAPLE STREET COMMUNITY HALL

Spring Cleanup Day

Saturday, April 18, from 9 in the morning
until noon. Volunteers will sweep the hall,
```

To keep the text, name a file instead.
Tesseract adds the `.txt` itself:

```bash
tesseract images/notice-clean.png results/notice-clean
cat results/notice-clean.txt
```

Two habits to form now. First, always
look at the messages Tesseract prints
while working — they go to a separate
stream (standard error), and lines like
`Estimating resolution as 402` are the
engine telling you something about your
image (chapter 15). Second, give output
files names that say which page and
which settings made them; OCR experiments
breed files fast.

## Proving it: measure, don't eyeball

A page of OCR *looks* right long before
it *is* right. The lab measures with a
**character error rate (CER)**: line the
read up against the known truth, count
the smallest number of character edits —
insertions, deletions, substitutions —
that turns one into the other, and divide
by the truth's length. The lab's little
`measure.py` does this after flattening
all whitespace, so line-break differences
do not count but letter differences do.

On the clean notice:

```text
truth 518 chars | ocr 518 chars | edits 0 | CER 0.000 | accuracy 100.0%
```

Five hundred and eighteen characters,
zero wrong. That is what a good page and
a modern engine do together, and it is
the benchmark the rest of this guide
falls away from: every damaged page in
chapter 5 is this same notice, hurt in
one specific way, and measured by this
same ruler. Without a known-truth page
of your own you cannot measure at all —
which is why, when accuracy matters, the
first step is always to type one page by
hand and keep it as your yardstick.

## What just happened, in moving parts

You met all five parts of chapter 2 in
one command: the **image** (sharp,
upright, 300 DPI), **preprocessing**
(the engine quietly binarised it),
the **engine** (the LSTM reader), the
**language** (English, the default), and
**segmentation** (automatic, `--psm 3`,
which found one column of paragraphs and
read them in order). Nothing needed
adjusting because nothing was wrong.
The rest of the guide is what to do when
something is.
