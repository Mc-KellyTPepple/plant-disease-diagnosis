"""Model loading, preprocessing and confidence assessment (no UI dependencies).

Model: LeafScan ConvNeXt-T (int8 ONNX) by Marconcini, https://huggingface.co/Marconcini/leafscan-convnext-tiny
Fine-tuned on PlantVillage and then PlantDoc field photos. CC BY-SA 4.0.
"""
import json
import os

import numpy as np
import onnxruntime as ort

CONFIG_PATH = "model/config.json"

with open(CONFIG_PATH, "r") as f:
    _cfg = json.load(f)

_variant = _cfg["onnx_int8"]
MODEL_PATH = os.path.join("model", _variant["file"])
IMG_SIZE = int(_cfg["img_size"])

# Temperature and threshold were fitted by the model's author on held-out FIELD photos
# (threshold targets ~90% accuracy on the photos it answers). Use the int8 values: this
# file is the int8 export, which has its own calibration.
TEMPERATURE = float(_variant["temperature"])
CONF_HIGH = float(os.environ.get("LEAFSCAN_THRESHOLD", _variant["threshold"]))
# Below this, the app says it can't tell. Between the two it shows "possible" candidates.
# 0.40 is my own untuned choice; adjust with LEAFSCAN_LOW after testing on your photos.
CONF_LOW = float(os.environ.get("LEAFSCAN_LOW", 0.40))

# Preprocessing: the model card does not state it. The backbone's default (timm convnext_tiny.fb_in22k_ft_in1k) is
# resize shorter side to 224/0.875 = 256, centre-crop 224, ImageNet normalisation. On the 236 PlantDoc test photos this
# reproduces the author's published int8 numbers (71.9% accuracy, 66% answered, 84.7% right) better than a plain
# 224x224 squash (see evaluation.json). Change PREPROCESS to "squash" to compare.
PREPROCESS = os.environ.get("LEAFSCAN_PREPROCESS", "crop")
CROP_PCT = 0.875
MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)

LABELS = {i: name for i, name in enumerate(_cfg["classes"])}

_session = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])
_input_name = _session.get_inputs()[0].name


def preprocess(img):
    from PIL import Image

    img = img.convert("RGB")
    if PREPROCESS == "squash":
        img = img.resize((IMG_SIZE, IMG_SIZE), Image.BICUBIC)
    else:
        w, h = img.size
        scale = round(IMG_SIZE / CROP_PCT) / min(w, h)
        img = img.resize((max(IMG_SIZE, round(w * scale)), max(IMG_SIZE, round(h * scale))), Image.BICUBIC)
        w, h = img.size
        left, top = (w - IMG_SIZE) // 2, (h - IMG_SIZE) // 2
        img = img.crop((left, top, left + IMG_SIZE, top + IMG_SIZE))
    x = np.asarray(img).astype(np.float32) / 255.0
    x = (x - MEAN) / STD
    return np.expand_dims(np.transpose(x, (2, 0, 1)), 0).astype(np.float32)


def probabilities(img):
    """Temperature-calibrated class probabilities."""
    out = _session.run(None, {_input_name: preprocess(img)})[0][0].astype(np.float64)
    # Guard: if the export already applies softmax, go back to log-space first.
    if out.min() >= 0 and abs(out.sum() - 1.0) < 1e-3:
        out = np.log(np.clip(out, 1e-12, 1.0))
    z = out / TEMPERATURE
    e = np.exp(z - z.max())
    return e / e.sum()


def plant_of(label):
    return label.split("___")[0]


def assess(probs):
    """Turn a probability vector into a decision with a confidence tier."""
    order = np.argsort(probs)[::-1]
    top = [(int(i), LABELS[int(i)], float(probs[i])) for i in order[:3]]
    p1 = top[0][2]
    level = "high" if p1 >= CONF_HIGH else "medium" if p1 >= CONF_LOW else "low"

    # Even when the disease is unclear, the crop is often clear.
    plant_probs = {}
    for i, lab in LABELS.items():
        plant_probs[plant_of(lab)] = plant_probs.get(plant_of(lab), 0.0) + float(probs[i])
    plant, plant_p = max(plant_probs.items(), key=lambda kv: kv[1])
    return {
        "level": level,
        "top": top,
        "plant": plant if plant_p >= 0.80 else None,
    }


def supported_plants():
    return sorted({plant_of(v).replace("_", " ").replace(",", "") for v in LABELS.values()})
