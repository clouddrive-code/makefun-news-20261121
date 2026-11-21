"""make.fun news-image-20261121 entry.

Writes the pre-generated image to /output/entry.png.
Deterministic by design: no network, no clock, no randomness —
it copies the same bundled PNG every run, so two runs write
identical bytes. Stdlib only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
DST = "/output/entry.png"

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST)
