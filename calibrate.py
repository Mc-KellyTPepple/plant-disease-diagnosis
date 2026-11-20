"""Pick confidence thresholds from real labelled photos.

Usage: python calibrate.py <folder>
<folder> must contain one sub-folder per class, named exactly like the labels in
model/labels.json (e.g. Tomato___Early_blight/). Use YOUR OWN field photos if you
can: the public dataset is lab-style and will make the model look better than it
will be in practice.
"""
import os
import sys

import numpy as np
from PIL import Image

from classifier import LABELS, probabilities

root = sys.argv[1]
name_to_idx = {v: k for k, v in LABELS.items()}
conf, correct = [], []
for cls in sorted(os.listdir(root)):
    if cls not in name_to_idx:
        print(f"skipping unknown folder: {cls}")
        continue
    for fn in os.listdir(os.path.join(root, cls)):
        try:
            img = Image.open(os.path.join(root, cls, fn))
        except Exception:
            continue
        p = probabilities(img)
        conf.append(p.max())
        correct.append(int(p.argmax()) == name_to_idx[cls])
conf, correct = np.array(conf), np.array(correct)
if len(conf) == 0:
    sys.exit("No images found.")
print(f"\n{len(conf)} images, overall accuracy {correct.mean():.1%}\n")
print("confidence bin   images   accuracy")
for lo, hi in [(0, .3), (.3, .4), (.4, .5), (.5, .6), (.6, .7), (.7, .8), (.8, .9), (.9, 1.01)]:
    m = (conf >= lo) & (conf < hi)
    if m.any():
        print(f"{lo:.1f}-{min(hi, 1):.1f}        {m.sum():6d}   {correct[m].mean():.1%}")
print("\nSuggested thresholds (lowest confidence at which accuracy of everything above it meets the target):")
for target in (0.99, 0.95, 0.90):
    ok = [t for t in np.arange(0.05, 1.0, 0.01)
          if (conf >= t).sum() >= 10 and correct[conf >= t].mean() >= target]
    if ok:
        t = ok[0]
        print(f"  {target:.0%} accurate -> CONF_HIGH={t:.2f} (answers {np.mean(conf >= t):.0%} of photos)")
    else:
        print(f"  {target:.0%} accurate -> not reachable with this data")
