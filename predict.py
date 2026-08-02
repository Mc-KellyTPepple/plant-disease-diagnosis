from speech import speak
import json
import numpy as np
import onnxruntime as ort
import gradio as gr
from PIL import Image

from disease_info import DISEASE_INFO


# ----------------------------------------------------
# Load model
# ----------------------------------------------------

MODEL = "model/plant_disease_classifier.onnx"

with open("model/labels.json", "r") as f:
    labels = json.load(f)

session = ort.InferenceSession(
    MODEL,
    providers=["CPUExecutionProvider"]
)

input_name = session.get_inputs()[0].name


# ----------------------------------------------------
# Image preprocessing
# ----------------------------------------------------

MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)


def preprocess(img):

    img = img.convert("RGB")
    img = img.resize((224, 224))

    x = np.array(img).astype(np.float32) / 255.0
    x = (x - MEAN) / STD

    x = np.transpose(x, (2, 0, 1))
    x = np.expand_dims(x, 0)

    return x.astype(np.float32)


# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

def predict(image):

    x = preprocess(image)

    logits = session.run(
        None,
        {input_name: x}
    )[0][0]

    logits = logits - np.max(logits)

    probs = np.exp(logits)
    probs /= np.sum(probs)

    # -------------------------
    # Top prediction
    # -------------------------

    idx = int(np.argmax(probs))

    disease = labels[str(idx)]

    confidence = float(probs[idx] * 100)

    info = DISEASE_INFO.get(
        disease,
        {
            "description": "Information unavailable.",
            "treatment": "N/A",
            "prevention": "N/A"
        }
    )

    # -------------------------
    # Top-3 predictions
    # -------------------------

    top3 = np.argsort(probs)[::-1][:3]

    top3_text = ""

    for i in top3:

        top3_text += (
            f"• {labels[str(int(i))]} "
            f"({probs[i]*100:.2f}%)\n"
        )

    result = f"""
🌿 Disease
{disease}

🎯 Confidence
{confidence:.2f}%

🏆 Top 3 Predictions
{top3_text}

📝 Description
{info['description']}

💊 Recommended Treatment
{info['treatment']}

🛡 Prevention
{info['prevention']}
"""

    return image, result


# ----------------------------------------------------
# Gradio UI
# ----------------------------------------------------

def create_demo():

    return gr.Interface(

        fn=predict,

        inputs=gr.Image(
            type="pil",
            label="Upload a Plant Leaf"
        ),

        outputs=[
            gr.Image(label="Uploaded Image"),
            gr.Textbox(
                label="Diagnosis",
                lines=22
            )
        ],

        title="🌿 Plant Disease Diagnosis",

        description="""
Upload a clear image of a plant leaf.

The AI model predicts the disease using a MobileNetV3-Large model exported to ONNX Runtime.

The application displays:

• Disease name

• Confidence score

• Top-3 predictions

• Disease description

• Recommended treatment

• Prevention tips
""",

        allow_flagging="never"
    )
