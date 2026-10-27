# Batch Work on Folders

By the end of this chapter a folder of
page images will become a folder of text
files in one loop, you will know the
stdin/stdout trick that makes Tesseract
a pipeline citizen, and your batch will
leave the evidence (TSV, logs) that
chapter 9's checking needs.

## The loop is the feature

Tesseract reads one image per
invocation, deliberately: it is a
building block, and the loop is yours.
The working pattern (lab transcript
`t08-batch-and-pipes.txt`):

```bash
for f in batch-demo/*.png; do
  tesseract "$f" "${f%.png}"
done
```

Each `page.png` gains a sibling
`page.txt`. The lab's demo folder —
the notice, the bakery receipt, the
two-column article — came through in one
pass, each text beside its image. For a
searchable-PDF archive instead, put the
config name inside the loop:

```bash
for f in scans/*.png; do
  tesseract "$f" "pdfs/$(basename "${f%.png}")" pdf
done
```

## Doing it at scale, honestly

- **Keep the pairing.** Output base name
  derived from the image name, always.
  A thousand pages in, `IMG_412.txt`
  beside `IMG_412.png` is the only
  filing system that never lies.
- **Save the evidence with the text.**
  A second pass with `tsv` costs seconds
  and buys chapter 9's whole checking
  workflow. Disk is cheaper than
  re-scanning.
- **Log per page.** Redirect Tesseract's
  working messages per run
  (`2> logs/page.log`) so a sick page in
  the middle of five hundred leaves a
  note instead of scrolling away.
- **Sort your inputs.** The shell's glob
  order is alphabetical; pad page
  numbers (`page-007`, not `page-7`) so
  book order survives.
- **Expect the failures to be a
  minority with names.** A batch this
  guide trusts is one where, at the
  end, you can list which pages scored
  badly (from the TSVs) rather than
  discovering it later by hand.

A **list file** is the other built-in
shape: give Tesseract a plain text file
with one image path per line, and it
reads them all in order:

```bash
printf 'images/one-line.png\nimages/receipt.png\n' > pages.txt
tesseract pages.txt combined
```

The difference from the loop matters:
the list form produces *one* combined
output, the pages separated by form
feeds — right for turning a chapter's
worth of scans into a single text. The
loop produces one output *per page* —
right for archives, where each text must
stay paired with its own page. The lab
ran the list form on two images to be
sure (its output opens with the one-line
fragment, then the receipt).

## stdin and stdout: the pipe form

Both ends can be streams:

```bash
cat images/notice-clean.png | tesseract stdin stdout | head -3
```

The literal names `stdin` and `stdout`
stand in for the file arguments. This is
how other programs drive the engine
without temp files (chapter 11), and
how you OCR the output of a scanner
command, an image converter, or a
screenshot tool in one breath. Note it
inherits the same rules: format comes
from the bytes, not a filename, so feed
it real PNG/JPEG/TIFF bytes.

## Throughput, without folklore

On the lab's small machine each
full-page read took a few seconds; a
receipt, about one. Tesseract is
single-page-at-a-time but uses several
threads within a page (its `--version`
banner mentions OpenMP). For bulk work
the practical lever is parallel pages,
not a faster engine: run a few loops at
once with a tool such as GNU Parallel
over separate folders, and stop at about
your core count. Measure on twenty of
*your* pages before promising anyone a
finish time for twenty thousand.
