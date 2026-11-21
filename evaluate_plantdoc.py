"""Measure the deployed model on real field photos: the PlantDoc test split (CC BY 4.0).

  git clone --depth 1 --filter=blob:none --sparse https://github.com/pratikkayal/PlantDoc-Dataset plantdoc
  git -C plantdoc sparse-checkout set test
  python evaluate_plantdoc.py plantdoc/test            # writes evaluation.json

PlantDoc's 27 classes are a subset of the model's 38 labels; FOLDER_TO_LABEL maps them. The model was trained on the PlantDoc
TRAIN split only, so the test split is held out. The test split has a few duplicates the model's author removed, so counts
differ slightly from the model card (236 photos here, 228 there).
"""
import json
import math
import os
import sys

from PIL import Image

import classifier as c

FOLDER_TO_LABEL = {
    "Apple Scab Leaf": "Apple___Apple_scab", "Apple leaf": "Apple___healthy", "Apple rust leaf": "Apple___Cedar_apple_rust",
    "Bell_pepper leaf": "Pepper,_bell___healthy", "Bell_pepper leaf spot": "Pepper,_bell___Bacterial_spot",
    "Blueberry leaf": "Blueberry___healthy", "Cherry leaf": "Cherry_(including_sour)___healthy",
    "Corn Gray leaf spot": "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn leaf blight": "Corn_(maize)___Northern_Leaf_Blight",
    "Corn rust leaf": "Corn_(maize)___Common_rust_", "Peach leaf": "Peach___healthy",
    "Potato leaf early blight": "Potato___Early_blight", "Potato leaf late blight": "Potato___Late_blight",
    "Raspberry leaf": "Raspberry___healthy", "Soyabean leaf": "Soybean___healthy", "Squash Powdery mildew leaf": "Squash___Powdery_mildew",
    "Strawberry leaf": "Strawberry___healthy", "Tomato Early blight leaf": "Tomato___Early_blight",
    "Tomato Septoria leaf spot": "Tomato___Septoria_leaf_spot", "Tomato leaf": "Tomato___healthy",
    "Tomato leaf bacterial spot": "Tomato___Bacterial_spot", "Tomato leaf late blight": "Tomato___Late_blight",
    "Tomato leaf mosaic virus": "Tomato___Tomato_mosaic_virus", "Tomato leaf yellow virus": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato mold leaf": "Tomato___Leaf_Mold", "grape leaf": "Grape___healthy", "grape leaf black rot": "Grape___Black_rot",
    "Tomato two spotted spider mites leaf": "Tomato___Spider_mites Two-spotted_spider_mite",
}


def wilson(k, n, z=1.96):
    if not n:
        return [0.0, 0.0, 0.0]
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(p * 100, 1), round(max(0, centre - half) * 100, 1), round(min(1, centre + half) * 100, 1)]


def main(root, out="evaluation.json"):
    idx = {v: k for k, v in c.LABELS.items()}
    rows = []
    for folder in sorted(os.listdir(root)):
        if folder not in FOLDER_TO_LABEL:
            print("skipping unmapped folder:", folder)
            continue
        for fn in sorted(os.listdir(os.path.join(root, folder))):
            try:
                img = Image.open(os.path.join(root, folder, fn))
                img.load()
            except Exception:
                continue
            probs = c.probabilities(img)
            rows.append((idx[FOLDER_TO_LABEL[folder]], int(probs.argmax()), float(probs.max()), folder))
    n = len(rows)
    plant = lambda i: c.LABELS[i].split("___")[0]
    healthy = lambda i: c.LABELS[i].endswith("healthy")
    right = sum(t == p for t, p, _, _ in rows)
    answered = [r for r in rows if r[2] >= c.CONF_HIGH]
    answered_right = sum(t == p for t, p, _, _ in answered)
    per = {}
    for t, p, _, f in rows:
        d = per.setdefault(f, [0, 0])
        d[0] += 1
        d[1] += t == p
    result = {
        "dataset": "PlantDoc test split (real field photos, CC BY 4.0), held out from training",
        "model": "LeafScan ConvNeXt-T int8 (Marconcini, CC BY-SA 4.0)",
        "preprocess": c.PREPROCESS,
        "photos": n,
        "accuracy": wilson(right, n),
        "right_crop_pct": wilson(sum(plant(t) == plant(p) for t, p, _, _ in rows), n),
        "healthy_vs_diseased_pct": wilson(sum(healthy(t) == healthy(p) for t, p, _, _ in rows), n),
        "threshold": c.CONF_HIGH,
        "answered": wilson(len(answered), n),
        "right_when_answered": wilson(answered_right, len(answered)),
        "per_class": {k: {"photos": v[0], "correct": v[1]} for k, v in sorted(per.items())},
        "note": "Values are [percent, lower, upper] with 95% Wilson intervals. The 'Tomato two spotted spider mites leaf' folder is mapped but may be absent.",
        "published_by_model_author": "int8 on 228 PlantDoc test photos: 71.9% accuracy; answers 66%, 84.7% of those right",
    }
    with open(out, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps({k: v for k, v in result.items() if k != "per_class"}, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
