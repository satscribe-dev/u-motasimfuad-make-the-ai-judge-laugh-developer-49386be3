# Make the AI Judge Laugh: Developer Excuses

Entry for the make.fun bounty
`u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`.

## What it does

`main.py` writes one funny single-line excuse a developer gives when
code breaks in production to `/output/entry.txt` (65 characters, UTF-8,
no trailing newline — inside the gate of 1–200 characters).

## The entry

> The tests passed. I wrote them after the code, like a good alibi.

## Why this line

Judged pairwise (positions swapped) against five other candidate lines
using the judge brief published in the kit's `competition.yaml`. This
line won because it turns the most recognised developer excuse ("the
tests passed") with a twist that reveals what really happened — the
tests were written after the code, like a good alibi — in one short
sentence where every word earns its place. See `results/log.md` in the
bounty work folder for the full candidate list, pairwise results, and
the reasons the losing lines lost.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py /tmp/out.txt  # writes to a custom path (local testing)
```

## License

MIT — see `LICENSE`.
