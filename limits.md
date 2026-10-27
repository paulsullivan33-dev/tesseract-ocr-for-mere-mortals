# Limits

By the end of this chapter you will know
where Tesseract's competence ends —
stated plainly, so that the documents
you care about are never the ones that
teach you.

## Print only, really

The engine reads machine print and good
typewriting. Handwriting is outside the
design: joined script defeats it
entirely, and even careful block
capitals come back unreliable. If the
page is handwritten and the words
matter, the honest tools are a human, a
handwriting specialist service, or a
transcription project — not persistence
with modes and filters.

## It reads shapes, not meaning

Tesseract has no idea what a document
is. It will read a total and a subtotal
with equal serenity and no arithmetic;
it cannot notice that 2 + 2 has been
read off a page where the answer printed
is 5 — or that its own read of the
figures is internally impossible.
Semantic checking — totals that must
sum, dates that must exist, names that
must match a register — is your
pipeline's job (chapter 11), and the
reason chapter 9 insists the output is
a draft with evidence, not a result.

## The confident error is the product

Most OCR errors are not noisy. They are
clean, plausible, wrong words — *moming*
for *morning* — produced without any
visible hesitation in the text itself.
Confidence scores help triage
(chapter 9) but the engine can be
highly confident and wrong, and the
characters most often substituted
(`rn`/`m`, `0`/`O`, `1`/`l`/`I`, `5`/`S`)
haunt exactly the reference numbers and
names that identify things. Any workflow
that pipes OCR output into action —
payments, records, citations — without
a checking stage has automated the
errors along with the reading.

## Damage has a floor

Preprocessing rescues a great deal
(chapter 5), but not everything:
characters physically destroyed by
blotches, folds, bleed-through or
cropping are gone, and the engine will
fill the gap with its best guess rather
than admit a hole. A line may come back
smoothly readable and quietly invented.
Where the original is unique and the
passage matters, compare against the
image, always — the text is a witness
with a known habit of polishing its
testimony.

## Layout has edges

Ordinary columns, headings and
paragraphs are handled well. Beyond
that: tables lose their grid (you get
words, roughly ordered), forms scatter
their labels from their values,
mathematics and music notation are not
text to this engine, and text printed
*inside* pictures — captions burned into
photographs, signs in scenes — is
another field's problem (chapter 13).
Rotated *within* a page — a sideways
table in an upright report — needs the
region cropped and read separately.

## Languages and scripts have edges

A language reads well when its
traineddata is strong, which is
unevenly true across the hundred-plus
files: major European languages are
excellent; smaller languages and
historical scripts vary, and historical
*print* (Fraktur, long-s typography)
needs its own models. Mixed-script
pages can need per-region reads. The
wrong-language failure of chapter 7 —
silent, plausible, localised — is the
standing warning.

## And the standing limit

OCR converts private paper into
searchable text at scale. The limit
from chapter 1 is not technical and has
no workaround: read what is yours, or
what you have permission to read.
Everything in this chapter can be
engineered around except that.
