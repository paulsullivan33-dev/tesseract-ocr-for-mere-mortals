# Page Segmentation Modes

By the end of this chapter you will know
what **page segmentation** assumes about
your page, how the wrong assumption
scrambles a read, and which of the modes
are worth your time. All experiments are
in lab transcript `t04-page-segmentation.txt`.

## The assumption inside every read

Before reading a single letter, Tesseract
must decide how the page is laid out:
one column or two, paragraphs or
captions, a page or a fragment. The
**--psm** option (page segmentation mode)
is how you state that assumption. The
default, `--psm 3`, means *analyse the
layout yourself* — no OSD, no help, just
decide. For ordinary pages it is right,
and this guide's advice is to leave it
alone until a read's *shape* goes wrong:
letters fine, arrangement nonsense.

## The two-column trap

The lab's article (`columns.png`) is a
short gardening piece in two columns.
Under the default mode the columns are
found and read in order — left column
top to bottom, then the right.

Under `--psm 6` (assume one uniform
block of text) the engine reads *across*
the gutter, stitching half-lines from
both columns together:

```text
Planting Tomatoes Move the young plants out
Tomatoes want sun, steady mild. Dig a deep hole, set
water, and patience. Start the stem low in the soil,
```

Every word is a real word from the page;
the sentences are nonsense. `--psm 4`
(one column of variable-size text) did
the same here. Neither mode is broken —
each did exactly what it was told. The
page simply was not the shape they
assume. When a read comes back
interleaved like this, the letters were
never the problem: the layout assumption
was.

## Small fragments: lines and words

For clippings — one line off a form, one
word off a sign — specialised modes
exist: `--psm 7` treats the image as a
single text line, `--psm 8` as a single
word. The lab's results counsel humility:

- The single line ("The meeting starts
  at seven in the hall.") read perfectly
  under both the default and `--psm 7`.
- The single word ("Cleanup") read
  perfectly under the **default** — and
  failed under `--psm 8` twice, trimmed
  and bordered, the mode latching onto a
  fragment of the word.

Specialised modes are promises about the
image, and a promise that is even
slightly off (a tight crop, an uneven
margin) can cost more than the general
mode's caution. Use them when the
default visibly misreads a fragment;
keep the default's output to compare.

## Orientation: modes 0 and 1

`--psm 0` does not read at all. It
reports orientation and script, using
the `osd` data file:

```text
$ tesseract images/notice-upside-down.png stdout --psm 0
Orientation in degrees: 180
Rotate: 180
Orientation confidence: 19.54
Script: Latin
```

`--psm 1` goes further: detect
orientation, rotate the page upright,
*then* read. The lab's upside-down
notice scored **14.7%** read as-is and
**100.0%** under `--psm 1`. If your
scanner or camera sometimes flips pages,
a `--psm 1` pass on a folder
(chapter 10) settles them wholesale.
Note the confidence figures in the
report: orientation detection on a
sparse or unusual page can be unsure of
itself, which is why `--psm 0`'s report
is worth reading before trusting
`--psm 1` blindly on thousands of pages.

## The modes, in practice

| Mode | Assumes | Reach for it when |
|---|---|---|
| 3 | Nothing — analyse layout | Default; ordinary pages |
| 0 | — | You only want orientation/script |
| 1 | Page may be rotated | Mixed-orientation scans |
| 4 | One column, varied sizes | Single-column clippings |
| 6 | One uniform block | A paragraph cut from a page |
| 7 | One line | A single-line fragment |
| 8 | One word | A single-word fragment — and check it |
| 11 | Sparse text | Words scattered on a form or sign |

Modes 2, 5, 9, 10, 12 and 13 exist for
specialised and historical cases; the
project documentation lists them all.
Ninety percent of real work is modes 3
and 1 and occasionally 7 — and the
discipline of suspecting the *layout*
when the letters look right but the text
reads wrong.
