#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt.
Deterministic: no network, no randomness, no input, no files
outside the repository are read.
"""

from pathlib import Path

ENTRY = (
    "The committee writing the AI safety bill spent forty minutes "
    "asking IT how to save a Word file as a PDF \u2014 then voted to "
    "regulate the machines."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
