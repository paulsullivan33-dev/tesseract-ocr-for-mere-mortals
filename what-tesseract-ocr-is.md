# What Tesseract OCR Is

A scanned page is a picture. Your
computer can show it to you, store it,
and send it — but it cannot search it,
copy a sentence out of it, or read it
aloud, because as far as the computer is
concerned there is no text in it. There
are only pixels: dark ones shaped like
letters, arranged in lines.

**OCR** — optical character recognition —
is the job of turning those pixels back
into text: real characters a program can
search, copy, index, translate or speak.
**Tesseract** is a free, open-source OCR
**engine**: a program that takes an image
in at one end and puts text out at the
other. You run it from the command line,
it works entirely on your own machine,
and it has been doing this job, in one
form or another, since the 1980s.

By the end of this chapter you will know
what Tesseract does with a page, what it
hands back, and what kind of work it is
honestly good at.

## The one-paragraph version

You give Tesseract an image of printed or
typewritten text:

```bash
tesseract page.png page
```

It studies the shapes, works out where
the lines and words are, decides which
letter each shape most likely is, and
writes its best reading into `page.txt`.
That is the whole transaction. Everything
else in this guide — cleaning the image,
choosing languages, checking confidence —
is about making that one transaction go
well more often.

## What it hands back

Plain text is the headline output, but
not the only one (chapter 8 has the
rest). From one image Tesseract can
produce:

- **Plain text**, laid out in reading
  order, paragraphs separated by blank
  lines.
- **A searchable PDF** — your original
  page image with an invisible text layer
  over it, so the PDF *looks* like a scan
  but can be searched and copied.
- **Positioned text** (hOCR or TSV): every
  word with its place on the page and a
  **confidence** score — how sure the
  engine is about that word. Chapter 9
  lives on this.

## What it is good at

- Clean scans and photographs of printed
  pages: letters, notices, forms, book
  pages, receipts. The lab's clean test
  page — a fictional community-hall
  notice — came back **character-perfect**:
  every one of its 518 characters right
  (chapter 4).
- Batch work. It is a command-line tool
  with no window to babysit, so a folder
  of five hundred scans is one loop away
  from five hundred text files
  (chapter 10).
- Many languages. The engine is driven by
  data files called **traineddata**, one
  per language; chapter 7 shows a German
  notice failing under English rules and
  succeeding under German ones.
- Being a component. Because it reads
  files and writes files, other programs
  — scanners' software, archive tools,
  your own scripts — can drive it
  (chapter 11).

## What it is not

Tesseract reads *print*. It does not read
handwriting beyond the most cooperative
block capitals, it does not understand
what a page means, and it will not tell
you a document is important, forged, or
about to expire. It is not a document
management system: it keeps nothing,
indexes nothing, files nothing. And it
makes mistakes — confidently, silently,
and usually on exactly the words that
matter, like names, dates and totals.
Chapter 14 (Limits) is blunt about this,
and chapter 9 exists because of it: the
professional habit is never *OCR and
trust*, it is *OCR and check*.

## The rule for other people's pages

OCR makes private paper searchable, which
is a power worth one honest paragraph.
Run it on your own documents, your
organisation's archive with permission,
the public-domain book you are restoring:
yes. Run it over a photograph of someone
else's mail, a colleague's desk, a form a
stranger filled in: the fact that the
text came from a picture rather than a
keyboard changes nothing about whose
words they are. This guide's lab used
only pages it invented for the purpose.

## Where we go from here

Chapter 2 takes the engine apart into
five moving parts — the image, the
preprocessing, the engine itself,
languages, and page segmentation — so
that when a read goes wrong you can name
*which* part failed. Chapter 3 installs
it. Chapter 4 makes the first perfect
read, and the chapters after it spend
their time on the imperfect ones, which
are the ones you will actually meet.
