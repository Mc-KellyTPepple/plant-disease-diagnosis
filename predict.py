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

    # ------------------------------------------------
    # Top prediction
    # ------------------------------------------------

    idx = int(np.argmax(probs))

    disease = labels[str(idx)]

    confidence = float(probs[idx] * 100)

    info = DISEASE_INFO.get(
        disease,
        {
            "name": disease,
            "cause": "Unknown",
            "description": "Information unavailable.",
            "symptoms": [],
            "treatment": [],
            "prevention": []
        }
    )
    cause = info["cause"]
    
    symptoms = "\n".join(
        f"• {item}"
        for item in info["symptoms"]
    )
    
    treatment = "\n".join(
        f"• {item}"
        for item in info["treatment"]
    )
    
    prevention = "\n".join(
        f"• {item}"
        for item in info["prevention"]
    )
    # ------------------------------------------------
    # Top 3 predictions
    # ------------------------------------------------

    top3 = np.argsort(probs)[::-1][:3]

    top3_text = ""

    for i in top3:

        top3_text += (
            f"• {labels[str(int(i))]} "
            f"({probs[i] * 100:.2f}%)\n"
        )

    # ------------------------------------------------
    # Text shown in the interface
    # ------------------------------------------------

    result = f"""🌿 Disease
    {info["name"]}
    
    🎯 Confidence
    {confidence:.2f}%
    
    🏆 Top 3 Predictions
    {top3_text}
    
    🦠 Cause
    {cause}
    
    📝 Description
    {info["description"]}
    
    ⚠ Symptoms
    {symptoms}
    
    💊 Recommended Treatment
    {treatment}
    
    🛡 Prevention
    {prevention}
    """

    # ------------------------------------------------
    # Text converted to speech
    # ------------------------------------------------

    speech = f"""The predicted disease is {info["name"]}.

    The confidence is {confidence:.1f} percent.
    
    Description.
    
    {info["description"]}
    
    Recommended treatment.
    
    {" ".join(info["treatment"])}
    
    Prevention tips.
    
    {" ".join(info["prevention"])}
    """

    # ------------------------------------------------
    # Generate speech
    # ------------------------------------------------
    try:
        audio = speak(speech)
    except Exception:
        audio = None

    # ------------------------------------------------
    # Return outputs
    # ------------------------------------------------

    return image, result, audio


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

            gr.Image(
                label="Uploaded Image"
            ),

            gr.Textbox(
                label="Diagnosis",
                lines=28
            ),

            gr.Audio(
                label="Voice Explanation",
                autoplay=True
            )

        ],

        title="🌿 AI Plant Disease Diagnosis System",

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

• Voice explanation
""",

        allow_flagging="never"
    )

demo = create_demo()

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
