# The Neighbours

By the end of this chapter you will know
the tools that sit next to Tesseract —
what each does that it cannot, and the
jobs where reaching past it is the right
move. These tools are characterised
from their documentation and general
practice, not benchmarked in this lab;
`criteria.md` says so.

## Other OCR engines

- **EasyOCR and PaddleOCR** — younger,
  deep-learning OCR systems, driven from
  Python. They handle scene text —
  signs, labels, photographs of the
  world — more gracefully than
  Tesseract, and are heavier to install
  and run. For documents, the contest is
  close; for a photo of a shopfront,
  they are the natural reach.
- **ABBYY FineReader** — the commercial
  benchmark for document OCR: superb
  layout retention, document-compare
  tools, a price to match. Organisations
  digitising at scale with audit needs
  buy it for the workflow as much as the
  accuracy.
- **Cloud OCR** (Google Cloud Vision,
  Azure AI Vision, Amazon Textract) —
  someone else's very large computers.
  Accuracy on ugly real-world pages is
  excellent and forms/tables support is
  strong; the costs are money, latency,
  and the fact that your documents leave
  your building. For a hospital's archive
  or a private diary, that last one
  decides it.
- **Your phone and OS** — Apple and
  Google ship OCR inside their photo and
  notes apps (Live Text, Lens), and
  Windows/macOS have it in places. For
  one page, once, they are unbeatable
  for convenience; they are not
  scriptable batch citizens like
  chapter 10's loop.

## The tools around the engine

- **Scanners' own software** — the
  honest first resort: if your scanner
  already makes searchable PDFs you
  like, an engine swap needs a reason.
- **OCRmyPDF** — a well-known wrapper
  that drives Tesseract (and image
  tools) over whole PDFs: existing scans
  in, searchable PDFs out, with deskew
  and cleanup built in. If your input is
  PDFs rather than page images, start
  there rather than splitting pages
  yourself.
- **Scan front-ends** (gscan2pdf,
  NAPS2) — friendly scanning programs
  that call OCR engines, Tesseract
  included, behind a window. The same
  engine with a face.
- **Image editors and converters** —
  not neighbours so much as the repair
  bench of chapters 5 and 11: any tool
  that deskews, denoises, thresholds and
  scales can feed the engine. The
  operations matter, not the brand.

## When Tesseract is the wrong reach

Handwriting: specialised recognisers
(and the cloud services) do meaningfully
better, and even they are modest.
Photographs of scenes rather than pages:
the deep-learning engines above.
Heavily structured forms where the
*boxes* carry meaning — claims, tax
tables — want the commercial or cloud
tools' layout machinery, or a template
built for the one form. For clean print,
in bulk, on your own machine, for free,
with the evidence kept: that square is
Tesseract's, and it is a large square.
