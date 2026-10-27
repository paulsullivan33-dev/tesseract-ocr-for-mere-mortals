# Languages and Traineddata

By the end of this chapter you will know
how Tesseract knows a language, how to
add one, how to read a mixed-language
page — and what the wrong language
quietly does to a read.

## Data, not dictionaries alone

A **traineddata** file is the trained
model for one language: the letter
shapes it expects, the combinations it
finds likely, the characters it knows
exist. `eng.traineddata` knows no `ß`
and treats `ü` as a stranger;
`deu.traineddata` expects both. The
files live in the **tessdata** folder
(chapter 3), one per language, named by
a three-letter code: `eng`, `deu`,
`fra`, `spa`, `ita`, `jpn`, `chi_sim`,
and more than a hundred others.

See what you have:

```bash
tesseract --list-langs
```

## The lab's German notice

`tesseract-lab/images/letter-deu.png` is
a short fictional notice from a reading
circle — ordinary German prose. Read
three ways (transcript
`t05-languages.txt`):

```bash
tesseract images/letter-deu.png out -l eng
tesseract images/letter-deu.png out -l deu
tesseract images/letter-deu.png out -l eng+deu
```

| Language setting | Accuracy |
|---|---|
| `-l eng` | 99.2% |
| `-l deu` | 100.0% |
| `-l eng+deu` | 99.2% |

The English read is *nearly* perfect —
this page's German is mostly letters
English also has. The single error is
the tell: *darüber* came back as
*dariiber*. Faced with `ü`, a character
its data does not contain, the engine
split it into the nearest shapes it
knows. No warning is printed; one word
is simply, silently wrong. On a page
dense with umlauts or accents the same
effect multiplies. This is the wrong
language's signature: not gibberish, but
a scatter of small, plausible errors in
exactly the characters the chosen
language lacks.

Two languages at once (`eng+deu`) reads
with both models side by side and is the
right tool for genuinely mixed pages —
a German letter quoting an English
slogan. On this purely German page it
did not beat plain `deu`, and still
tripped on the same `ü`: more data is
not automatically better data. Match
the language to the page; combine only
when the page itself is combined.

## Adding a language

Two honest routes:

1. **Your package manager** (chapter 3):
   `sudo apt install tesseract-ocr-deu`
   on Debian/Ubuntu; equivalents exist on
   other systems. Preferred — versions
   stay consistent with your engine.
2. **By hand**: download the
   `.traineddata` file from the project's
   `tessdata` (or the smaller, faster
   `tessdata_fast`) repository and place
   it in the tessdata folder, or point
   Tesseract at a folder of your own:

   ```bash
   tesseract page.png page -l deu --tessdata-dir ~/my-tessdata
   ```

   The `TESSDATA_PREFIX` environment
   variable does the same for every run.

Choose the model flavour knowingly:
`tessdata_fast` files (the packaged
default in most distributions) are
smaller and quicker with a small
accuracy cost; the full `tessdata`
models are the most accurate; and
`tessdata_best` trades speed again for
the last fraction. For one engine
version, keep the files from one family.

## Scripts and special cases

Some traineddata files are not languages
but *jobs*: `osd` (orientation and
script detection, chapter 6), `equ`
(equation detection). Vertical text and
right-to-left scripts have their own
files (`jpn_vert`, for instance). And
Fraktur — the blackletter print of older
German books — needs its own historical
model; modern `deu` data reads it
poorly. Knowing the family exists is
enough for most readers; the point is
that "add the data for the page you
actually have" is nearly always the fix
when characters come back consistently
wrong in one specific way.
