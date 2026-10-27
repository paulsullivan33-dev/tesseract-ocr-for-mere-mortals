# Troubleshooting

By the end of this chapter the failures
this guide met — and the ones every OCR
user meets — will each have a name, a
cause, and a check. The table in
chapter 2 is the map; this is the same
country with roads drawn in.

## The read is empty or nearly empty

**Check the orientation first.** An
upside-down page scored 14.7% in the
lab — near-empty reads with strange
characters are rotation until proven
otherwise. `--psm 0` reports; `--psm 1`
repairs (chapter 6). Then check the
image is what you think it is: open it.
A "scan" that is actually a thumbnail,
or a page photographed mostly as
tabletop, reads exactly as well as it
deserves.

## Everything is slightly wrong

Uniform low-grade error — every third
word bruised — is an image problem, not
a settings problem. In the lab's order
of likelihood: resolution (a 70-DPI page
scored 87.5%; rescan at 300 or upscale,
chapter 5), blur (a soft focus no filter
fully reverses), and heavy compression
(JPEG artefacts around letters; ask for
PNG or TIFF from the scanner). Verify
with your known-truth page: if it also
drops, your pipeline changed, not the
engine.

## One region is gibberish

Local damage: a blotch, a fold, coffee.
The engine reads around damage and
guesses through it (chapter 14). Crop
the region, repair it alone (denoise,
threshold), read it alone, and splice —
or accept a human transcription for
those lines. A whole-page re-run with
stronger medicine usually makes the
healthy regions worse.

## The columns are interleaved

Letters right, order wrong: page
segmentation. You (or an earlier
command) set a block mode over a
multi-column page. Return to the
default `--psm 3` and compare
(chapter 6's stitched sentences are the
reference specimen).

## Specific characters are always wrong

One character family mangled the same
way throughout — every `ü` split, every
accent stripped — is the wrong language
data. `--list-langs`, then `-l` the
page's real language (chapter 7).
Consistent substitution of one *pair*
(`0` for `O` in codes) is a job for
chapter 9's whitelists or a dictionary
check, not more preprocessing.

## The engine cannot find its data

`tesseract --list-langs` shows nothing,
or a run dies with an error about
`eng.traineddata`. The tessdata folder
is missing, moved, or the environment
steers elsewhere. Check, in order: the
package actually installed its data
(chapter 3's locations); `TESSDATA_PREFIX`
if set — one stale export poisons every
run in that shell; and `--tessdata-dir`
pointed explicitly as a test.

## Resolution warnings

`Estimating resolution as 402` on the
lab's DPI-less image was benign — the
estimate was sane and the read perfect.
The dangerous case is the reverse: an
image whose DPI metadata *lies* (a
300-DPI page re-saved as 72 by an
editor) gets read at the wrong assumed
scale. When a page should work and
doesn't, force the truth:
`--dpi 300`. Conversely, a page that
reads badly despite a clean look is
often small: check its pixel dimensions
before its DPI claims.

## It is slow

Seconds per page on a small machine is
normal (the lab's pages took roughly
one to ten seconds by size and damage).
Minutes per page is not: suspect a huge
image (downscale photographs to page
size — a 50-megapixel page buys
nothing), `--psm 0` left off a batch
that needs orientation per page (fine)
or on one that doesn't (waste), and the
full `tessdata_best` models where the
fast ones would do. Parallel pages
(chapter 10) beat a faster single page
nearly every time.

## The fix made it worse

It happens in print, in this very
guide: the shadowed page lost 2.1
points to its own rescue (95.8% after
normalise-and-threshold, 97.9% raw).
The defence is procedural, and it is
the guide's whole method: keep the
original, measure before and after on a
known-truth page, keep the better
version, and write down what the
numbers were. Intuition about images is
a fine servant and a poor auditor.
