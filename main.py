# A news-summary-01 entry (Python 3.13, standard library only): the summary of
# 11 November 2026's world news is the summary.txt beside this file, and the
# program copies it to /output/entry.txt, byte for byte, so the two grader
# runs write identical bytes. The gate takes UTF-8 text of 1 to 2,000
# characters (Unicode code points) that is not only white space.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

source = Path(__file__).resolve().parent / "summary.txt"
target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
target.parent.mkdir(parents=True, exist_ok=True)

# Guard the gate before copying: the grader wants 1-2000 Unicode code
# points of non-blank text. Fail loudly instead of silently shipping an
# entry that cannot score.
text = source.read_text(encoding="utf-8")
if not text.strip():
    raise SystemExit("summary.txt is blank; refusing to write an empty entry")
if len(text) > 2000:
    raise SystemExit(f"summary.txt is {len(text)} code points; gate allows at most 2000")
shutil.copyfile(source, target)
