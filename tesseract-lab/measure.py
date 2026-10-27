#!/usr/bin/env python3
"""Measure OCR accuracy as a character error rate (CER).

Usage: measure.py TRUTH.txt OCR.txt

Both texts are normalised the same way before comparing: every
run of whitespace becomes one space, and the ends are trimmed.
The error rate is the Levenshtein edit distance (characters to
insert, delete or substitute) divided by the number of
characters in the truth. 0.00 is a perfect read; 1.00 means as
many edits as there are characters.
"""
import sys


def normalise(text):
    return " ".join(text.split())


def levenshtein(a, b):
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def main():
    truth = normalise(open(sys.argv[1], encoding="utf-8").read())
    ocr = normalise(open(sys.argv[2], encoding="utf-8").read())
    dist = levenshtein(truth, ocr)
    cer = dist / len(truth) if truth else 0.0
    print(f"truth {len(truth)} chars | ocr {len(ocr)} chars | "
          f"edits {dist} | CER {cer:.3f} | accuracy {1 - cer:.1%}")


if __name__ == "__main__":
    main()
