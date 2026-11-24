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


def main() -> None:
    import os
    import sys

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
