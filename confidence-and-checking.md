# Confidence and Checking the Result

By the end of this chapter you will know
how to make Tesseract show its doubts,
how to use those doubts to check a read
efficiently — and the two ways confidence
will mislead you if you treat it as a
verdict instead of a triage tool.

## Every word has a score

The TSV output of chapter 8 scores every
word from 0 to 100. High means the
engine found the shapes clean and the
word plausible; low means it guessed.
Asking for the doubtful words in a read
is one line of shell over the TSV:

```bash
tesseract page.png page tsv
awk -F'\t' '$11 < 60 && $12 != "" {print $12, "("$11")"}' page.tsv
```

On the lab's heavily speckled page
(transcript `t07-confidence.txt`) that
list is a rogues' gallery: junk tokens
that are really dirt (`:`, `-`, a
"word" scored 0.0), chopped fragments,
and punctuation fused to words. If you
had time to check only twenty things on
that page, these are the twenty.

## The two honest case studies

**A wrong word, caught.** Chapter 5's
tilted page read *morning* as *moming*.
Its confidence was **59.6** — the lowest
real word on an otherwise clean page.
A threshold of "show me everything
under 60" puts the page's only error at
the top of your checking list.

**A right word, accused.** On the
speckled page, the word *morning* —
spelled correctly — scored **36.0**,
because speckle crowded its shapes.
Dirt near a word lowers the score
whether or not the word survived.

Together they state the rule:
**confidence ranks where to look first;
it does not decide what is wrong.** A
low score is a suspicion, not a
conviction, and — the dangerous half —
a high score is not an acquittal. The
engine can be serenely confident about
a plausible wrong word, especially a
real word substituted for another real
word. Names, numbers and dates, the
words a document usually matters for,
deserve eyeball checks whatever their
scores. Chapter 5's receipt makes the
point from the other side: it measured
73.6% character accuracy, yet a diff
showed every word and figure correct —
the entire "error" was two dashed
separator lines the engine skipped.
Read the diff before you mourn the
number.

## A checking workflow that scales

1. **OCR with TSV alongside text**
   (chapter 10's batch does both).
2. **Extract the low-confidence words**
   with their page and line, as above.
3. **Check those against the image**
   first. Most true errors live there.
4. **Spot-check the high-stakes words**
   regardless of score: names, dates,
   totals, reference numbers. A
   dictionary of expected terms, where
   you have one, catches substitutions
   no score will.
5. **Where the stakes justify it**,
   compare two reads: two engines, or
   the same engine after different
   preprocessing (chapter 5). Where two
   independent reads agree
   character-for-character, confidence is
   earned rather than asserted; where
   they differ, a human looks.

## Knobs that touch certainty

- **--oem** chooses the engine. The
  default (`--oem 1`, the LSTM reader)
  is the one this guide uses; the legacy
  engine is gone from Tesseract 5
  builds that ship LSTM only, so if
  `--oem 0` errors, that is why.
- **Dictionaries** can be switched off
  (`-c load_system_dawg=0
  -c load_freq_dawg=0`) for pages whose
  "words" are not English at all —
  codes, part numbers, names. A
  dictionary that keeps "correcting"
  your part numbers into words is a
  liability; off, the engine reads
  shapes only.
- **Character whitelists** constrain
  hard: `-c tessedit_char_whitelist=0123456789.`
  on a column of figures forbids letters
  outright. Powerful on forms and
  dangerous everywhere else — a
  whitelist applied to prose will
  dutifully turn every `S` into a `5`.

None of these replace the habit: OCR
produces a draft with evidence attached.
Your job is to read the evidence where
it points.
