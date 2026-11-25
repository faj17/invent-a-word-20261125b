#!/usr/bin/env python3
"""Invent a Word We Need entry: "escalurch".

Coinage: escalator + lurch. The entry is one invented English word
with a one-line definition, written to /output/entry.txt. The gate
is 1-140 characters of UTF-8 text, a single line, more than
whitespace. Standard library only; no network, no input, no
randomness, no clock: two runs produce byte-identical output.
"""

from pathlib import Path

WORD = "escalurch"
DEFINITION = (
    "the small jolt you feel when you step onto a stopped "
    "escalator as if it were moving."
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 140
SEPARATOR = " \u2014 "


def assemble(word: str, definition: str) -> str:
    """Join the coined word and its definition into the entry line."""
    return f"{word} (n.){SEPARATOR}{definition}"


def validate(line: str) -> str:
    """Check the entry line against the competition gate.

    Must be 1-MAX_CHARS characters, one line, more than whitespace,
    and UTF-8-encodable; it must also open with the coined word and
    carry the word/definition separator, so a truncated or mangled
    line can never pass. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not line.startswith(WORD):
        raise ValueError("entry must open with the coined word")
    if SEPARATOR not in line:
        raise ValueError("entry must carry the word/definition separator")
    if not line.endswith(DEFINITION):
        raise ValueError("entry must end with the full definition")
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate(assemble(WORD, DEFINITION))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
