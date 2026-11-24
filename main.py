#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — entry program.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (or to the path given as argv[1]).

The entry was chosen by pairwise judging (positions swapped) among six
candidate lines against the judge brief in the kit's competition.yaml:
the winning line turns a recognised excuse ("the tests passed") with a
twist that reveals what really happened (the tests were written after
the code), in one short sentence where every word earns its place.
"""

ENTRY = "The tests passed. I wrote them after the code, like a good alibi."

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from the kit (competition.yaml / RULES.txt, "The gate"):
# /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
# white space, and a single line.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200


def validate_entry(entry: str) -> None:
    """Check an entry against the competition gate.

    Raises ValueError with a clear reason when the entry would be
    refused by the sealed gate scorer.
    """
    # Must be encodable as UTF-8 (rejects lone surrogates and the like).
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"entry is not valid UTF-8: {exc}") from exc
    if not (MIN_ENTRY_CHARS <= len(entry) <= MAX_ENTRY_CHARS):
        raise ValueError(
            f"entry is {len(entry)} characters, outside the gate "
            f"of {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} characters"
        )
    if not entry.strip():
        raise ValueError("entry is only white space")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line (no newline characters)")


def main() -> None:
    import os
    import sys

    # Refuse to write an entry the gate would reject: fail loudly
    # (non-zero exit) instead of producing an invalid /output/entry.txt.
    try:
        validate_entry(ENTRY)
    except ValueError as exc:
        print(f"error: invalid entry: {exc}", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # No trailing newline: the gate counts characters (1-200), so the
    # file holds exactly the entry text and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
