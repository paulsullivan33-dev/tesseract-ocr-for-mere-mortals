# OCR in a Pipeline

By the end of this chapter Tesseract will
be sitting in the middle of a small
production line — image repair before it,
checking after it — and you will know the
rules that keep a pipeline honest.

## The shape

Real OCR work is rarely one command. It
is a chain:

```text
scan / photograph
      |
  repair the image     (chapter 5's operations)
      |
  tesseract            (the read)
      |
  check the evidence   (TSV, chapter 9)
      |
  text / searchable PDF / index
```

Each stage is a separate program doing
one job, passing files or streams along.
Tesseract is built for its seat in the
middle: it speaks files, `stdin` and
`stdout` (chapter 10), it sets nothing
global, and it keeps no state between
pages — which is why pipelines around it
stay simple and debuggable.

## The repair stage, with generic tools

Chapter 5's repairs were done with a
small Python script so the lab needed
nothing exotic. In production the same
four operations live in every serious
image tool. Described generically, so
you can find them under whatever names
your tool uses:

- **Deskew**: detect the page's tilt
  angle and rotate by its opposite.
  ImageMagick-style command lines expose
  this as a `-deskew` operation with a
  threshold; scan front-ends often offer
  "straighten" at scan time, which is
  the best place of all.
- **Denoise**: a median or
  speckle-reduction filter ("despeckle",
  "noise reduction") before any
  thresholding.
- **Threshold / binarise**: convert to
  black and white at a chosen level, or
  with an adaptive method that picks the
  level locally — the right choice for
  unevenly lit pages, and the reason
  chapter 5's pale pages survived.
- **Scale**: enlarge small images to
  roughly 300 DPI with a quality
  resampling filter, and set the DPI
  metadata while you are there.

Chain them in that order — straighten,
clean, then size, then threshold last if
at all. Remember the lab's warning: the
engine binarises internally anyway, so
an external threshold is the one step
most often worth *skipping*; the
shadowed page scored worse after an
enthusiastic normalise-and-threshold
(95.8%) than raw (97.9%). In a pipeline,
make each repair stage earn its place
by measuring the whole chain on your
known-truth pages with it in and out.

## A worked miniature

The lab's own chain, end to end:

```bash
python3 tesseract-lab/fix-images.py        # repair copies
tesseract images/notice-skewed8-fixed.png out   # read
python3 tesseract-lab/measure.py truth.txt out.txt  # judge
```

Three programs, three artefacts, every
stage inspectable. That is the entire
philosophy: when the final text is
wrong, you can open the repaired image
with your own eyes and learn whether the
repair or the read failed. A pipeline
whose middle stages you cannot inspect
will eventually make you guess, and
guessing is what the known-truth page
exists to prevent.

## Where the output goes

From the checking stage, the artefacts
of chapter 8 fan out to their consumers:
plain text to a full-text index or a
folder of `.txt` twins; searchable PDFs
to the archive; TSVs to a report that
lists the week's low-confidence pages
for a human's Friday hour. Orchestrating
that — schedules, watch folders, queues —
belongs to whatever automation you
already run; the OCR line itself stays
these same few commands, which is
precisely why it survives being
orchestrated.

## Pipeline rules

1. **Originals are sacred.** Repairs
   write new files; the scan as it
   arrived is never overwritten.
2. **One variable at a time.** Change
   one stage, re-measure the ledger.
3. **Keep the evidence.** TSV beside
   text, logs beside both.
4. **A stage that does not improve the
   measured score comes out**, however
   elegant it felt.
