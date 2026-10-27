# Installing Tesseract

By the end of this chapter Tesseract will
be installed on your machine, you will
know which version you have, and you will
know where its language files live — the
three facts every later chapter leans on.

## The shape of an install

Tesseract is two things: the **program**
(`tesseract`, one command) and the
**traineddata** files, one per language,
which the program cannot work without.
Installers bundle the program with at
least English (`eng`). Every other
language is a separate small package or
file, added the same way (chapter 7).

## Linux

On Debian and Ubuntu:

```bash
sudo apt install tesseract-ocr
```

Add languages by package name —
`tesseract-ocr-deu` for German,
`tesseract-ocr-fra` for French, and so on:

```bash
sudo apt install tesseract-ocr-deu tesseract-ocr-fra
```

On Fedora the same shape:
`sudo dnf install tesseract`. On Arch:
`sudo pacman -S tesseract tesseract-data-eng`.
Your distribution's package is the right
first choice everywhere: it puts the
program and its tessdata in the places
the system expects.

## macOS and Windows

With Homebrew on a Mac:
`brew install tesseract` (and
`tesseract-lang` for all languages).
Windows has an installer maintained by
the Mannheim University Library (UB
Mannheim), linked from the project's
documentation; it offers extra languages
during setup. This guide's lab ran on
Linux, so the macOS and Windows routes
are described from the project's
documentation, not demonstrated —
`criteria.md` says so plainly. The
commands after installation are the
same on every system.

## The two checks

Whatever the route, prove the install
with the same two commands:

```bash
tesseract --version
tesseract --list-langs
```

The lab's run of the first (transcript
`tesseract-lab/transcripts/t00-version-and-languages.txt`):

```text
tesseract 5.3.4
 leptonica-1.82.0
```

The second line names **Leptonica**, the
image library Tesseract reads pictures
through — worth knowing because some
"the engine can't open my file" problems
are Leptonica not knowing that file
format. The language list should show at
least `eng` and `osd`. If `--list-langs`
shows nothing, the program cannot find
its tessdata folder; that is an install
problem, not an OCR problem, and
chapter 15 has the remedy.

An honest note about this guide's own
lab: the build machine's package manager
was busy with other work for the whole
build, so the lab ran the *same* Ubuntu
package (`tesseract-ocr` 5.3.4) unpacked
into a scratch folder and run from there.
Same binary, same version, same results —
and every transcript in the lab was
produced by exactly the program the
command above installs.

## Where things live

On a packaged Linux install:

- the program: `/usr/bin/tesseract`
- the language data:
  `/usr/share/tesseract-ocr/5/tessdata/`
  (the `5` is the major version)
- inside that folder, a `configs`
  subfolder whose small files — `tsv`,
  `hocr`, `pdf`, `digits` — are how
  chapter 8's output formats are switched
  on.

If you ever download a traineddata file
by hand (chapter 7 does), it goes in
that tessdata folder, or in a folder you
name with the `TESSDATA_PREFIX`
environment variable or the
`--tessdata-dir` option.
