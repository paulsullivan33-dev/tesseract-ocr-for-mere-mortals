# Output Formats

By the end of this chapter you will be
able to get four things out of one page
— plain text, a table of words with
positions and confidences, a web-page
format that preserves layout, and a
searchable PDF — and you will understand
the small mechanism that switches them.

## One mechanism: config names

Chapter 3 pointed at the `configs`
folder inside tessdata. Each file there
is a ready-made bundle of settings, and
naming one as the last argument turns
it on:

```bash
tesseract images/notice-clean.png out txt
tesseract images/notice-clean.png out tsv
tesseract images/notice-clean.png out hocr
tesseract images/notice-clean.png out pdf
```

The output file gains the matching
extension (`.txt`, `.tsv`, `.hocr`,
`.pdf`). Plain text is the default when
no config is named. Settings can also be
set one by one with `-c`, for example
`-c tessedit_create_pdf=1` — the config
files are simply the convenient bundles.
(Lab transcript `t06-output-formats.txt`
has the runs and sizes: from one page,
527 bytes of text, 5 KB of TSV, 13.5 KB
of hOCR, 144 KB of PDF.)

## Plain text

The working format of the earlier
chapters: reading order, blank lines
between paragraphs, nothing else. Right
for searching, diffing, feeding other
programs, and measuring accuracy.

## TSV: every word, placed and scored

**TSV** is tab-separated values — a
spreadsheet in a text file. One row per
word, with its page, block, paragraph
and line numbers, its bounding box
(`left`, `top`, `width`, `height`, in
pixels), its **confidence**, and the
word itself:

```text
level  page_num  block_num  par_num  line_num  word_num  left  top  width  height  conf      text
5      1         3          1        1        8         785   531  155    38      59.613350 moming
```

That row is the one wrong word from
chapter 5's tilted page, with its
coordinates and its mediocre confidence.
Chapter 9 is built on this format; even
if you never open it in a spreadsheet,
knowing the read *has* this detail
underneath changes how you trust the
plain text.

## hOCR: layout as HTML

**hOCR** is XHTML: the page as nested
divisions (`ocr_page`, `ocr_par`,
`ocr_line`, `ocrx_word`), each carrying
its bounding box in a `title` attribute
and each word its confidence
(`x_wconf`). It is the interchange
format of the OCR world — archive
software and book-digitising pipelines
consume it to rebuild pages that look
like the original and search like text.
If you need the words *and* where they
stood, in a format other tools already
speak, this is the one.

## PDF: the searchable scan

The `pdf` config produces the most
useful artefact of all for most people:
a PDF that *shows* your original page
image and *hides* the recognised text
behind it, each word positioned over
its picture. Open it in any reader and
it looks like a scan — but search works,
copy works, screen readers work.

The lab verified the text layer rather
than admiring it: `pdftotext` pulled the
text back out of the lab's PDF, and it
measured 98.1% against the truth —
against 100.0% for the plain-text run of
the same page. The missing fraction is
the *extractor's* doing, not the OCR's:
the heading's last word sits in the PDF
in an order the extractor presented
oddly. A lesson worth keeping: a
searchable PDF holds positioned words,
and different tools reassemble them
slightly differently. Search and copy
will feel perfect; a character-exact
audit should use the plain text.

## Choosing

- Just the words: plain text.
- Words with evidence: TSV (checking,
  chapter 9) or hOCR (interchange).
- A document to hand to a human who
  will search it: searchable PDF.
- Frequently both of the last two:
  the PDF to keep, the TSV to audit.
