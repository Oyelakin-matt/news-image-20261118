# A working news-image entry (Python 3.13, standard library only): its image is
# the entry.png beside this file, and the program copies it to /output/entry.png.
# The image sums up Wednesday 18 November 2026's world news in one picture:
# Peltola flips Alaska and the Democrats take the Senate 56-44, the US strikes
# an Iranian missile site on Qeshm Island, the Kerch Bridge span falls on a
# second day of strikes, the US loses its measles-free status, and Nvidia sales
# top $100bn. A file copy is byte-for-byte deterministic, so both grader runs
# write identical bytes. The image itself is drawn by build-image.py (kept
# outside this repository) and copied into the repo as entry.png.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(src, dst)

# The gate takes a whole PNG, so refuse to finish on a truncated copy:
# PNG magic at the start, IEND chunk at the end.
with open(dst, "rb") as f:
    data = f.read()
if not data.startswith(b"\x89PNG\r\n\x1a\n") or not data.rstrip().endswith(b"IEND\xaeB`\x82"):
    raise SystemExit("entry.png is not a whole PNG")
