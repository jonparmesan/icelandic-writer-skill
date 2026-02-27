#!/usr/bin/env python3
"""GreynirCorrect verification for Icelandic text.

Usage:
    python3 check_icelandic.py <file>
    python3 check_icelandic.py --help
"""

import argparse
import re
import sys

from reynir_correct import check_single


# Known project terms to ignore (add as needed)
IGNORE_WORDS = {
    "Ókind", "ensímvinnuð", "keratínefni", "keratínprótein",
    "keratínlífplast", "keratínfilmur", "keratínsameindum",
}


def check_file(filepath: str) -> int:
    """Check an Icelandic text file. Returns number of errors found."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    error_count = 0
    lines = text.split("\n")

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        # Skip empty lines, headings, tables, horizontal rules, list markers
        if (not stripped or stripped.startswith("#") or stripped.startswith("|")
                or stripped.startswith("---") or stripped.startswith("*")):
            continue

        clean = re.sub(r'\*\*', '', stripped)
        clean = re.sub(r'^- ', '', clean)
        if len(clean) < 5:
            continue

        try:
            sent = check_single(clean)
            for a in sent.annotations:
                if a.code and a.code.startswith("E006"):
                    continue  # Skip abbreviation warnings
                if a.code and a.code.startswith("U001"):
                    if a.text and any(w in a.text for w in IGNORE_WORDS):
                        continue
                if a.code and a.code.startswith("W001"):
                    if any(w in (a.text or "") for w in IGNORE_WORDS):
                        continue
                print(f"L{i} [{a.code}]: {a.text}")
                if a.suggest:
                    print(f"  → {a.suggest}")
                print(f"  context: {clean[:80]}")
                print()
                error_count += 1
        except Exception:
            pass

    if error_count == 0:
        print("✓ No errors found.")
    else:
        print(f"Found {error_count} issue(s).")

    return error_count


def main():
    parser = argparse.ArgumentParser(
        description="Check Icelandic text for spelling and grammar errors using GreynirCorrect."
    )
    parser.add_argument("file", help="Path to the Icelandic text file to check")
    args = parser.parse_args()

    try:
        errors = check_file(args.file)
        sys.exit(1 if errors > 0 else 0)
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
