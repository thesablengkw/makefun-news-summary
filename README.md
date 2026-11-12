# news-summary-01 entry

A one-day world news summary for make.fun's news-summary-01 competition:
the events of Wednesday 11 November 2026, written in English, ordered by
importance, with the reporting outlet named for the main stories.

- `main.py` (Python 3.13, standard library only) copies `summary.txt` to
  `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
  variable is set — byte for byte, so repeated runs are identical.
- `summary.txt` is the summary itself: UTF-8, under the competition's
  2,000-character limit.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
