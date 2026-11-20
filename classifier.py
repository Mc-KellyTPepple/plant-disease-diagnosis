"""Model loading, preprocessing and confidence assessment (no UI dependencies)."""
import json
import os

import numpy as np
import onnxruntime as ort

MODEL_PATH = "model/plant_disease_classifier.onnx"
LABELS_PATH = "model/labels.json"

# Confidence tiers. These are STARTING POINTS, not calibrated values:
# run `python calibrate.py <validation_dir>` on real labelled photos and adjust.
# Override without editing code via environment variables.
CONF_HIGH = float(os.environ.get("CONF_HIGH", 0.70))  # at/above: confident
CONF_LOW = float(os.environ.get("CONF_LOW", 0.40))    # below: "can't tell"

MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)

with open(LABELS_PATH, "r") as f:
    LABELS = {int(k): v for k, v in json.load(f).items()}

_session = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])
_input_name = _session.get_inputs()[0].name


def preprocess(img):
    # Must match training preprocessing; do not change independently of the model.
    img = img.convert("RGB").resize((224, 224))
    x = np.asarray(img).astype(np.float32) / 255.0
    x = (x - MEAN) / STD
    return np.expand_dims(np.transpose(x, (2, 0, 1)), 0).astype(np.float32)


def probabilities(img):
    logits = _session.run(None, {_input_name: preprocess(img)})[0][0]
    e = np.exp(logits - np.max(logits))
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
