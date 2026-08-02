import json
import numpy as np
import onnxruntime as ort
import gradio as gr
from PIL import Image

MODEL="model/plant_disease_classifier.onnx"

with open("model/labels.json") as f:
    labels=json.load(f)

session=ort.InferenceSession(
    MODEL,
    providers=["CPUExecutionProvider"]
)

input_name=session.get_inputs()[0].name

MEAN=np.array([0.485,0.456,0.406],dtype=np.float32)
STD=np.array([0.229,0.224,0.225],dtype=np.float32)

def preprocess(img):

    img=img.convert("RGB")
    img=img.resize((224,224))

    x=np.array(img).astype(np.float32)/255.0
    x=(x-MEAN)/STD
    x=np.transpose(x,(2,0,1))
    x=np.expand_dims(x,0)

    return x.astype(np.float32)

def predict(image):

    x=preprocess(image)

    logits=session.run(
        None,
        {input_name:x}
    )[0][0]

    logits-=logits.max()

    probs=np.exp(logits)
    probs/=probs.sum()

    idx=int(np.argmax(probs))

    disease=labels[str(idx)]

    confidence=float(probs[idx]*100)

    return image,f"{disease}\nConfidence: {confidence:.2f}%"

def create_demo():

    return gr.Interface(

        fn=predict,

        inputs=gr.Image(type="pil"),

        outputs=[
            gr.Image(),
            gr.Textbox(label="Prediction")
        ],

        title="Plant Disease Diagnosis",

        description="Plant Disease Classification using MobileNetV3-Large + ONNX Runtime"

    )
