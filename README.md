# Plant Disease Diagnosis

Deep Learning Plant Disease Classification

## Model

LeafScan ConvNeXt-T (int8 ONNX), field-calibrated

## Inference

ONNX Runtime

## Deployment

Render

## Run

pip install -r requirements.txt

python app.py

## Model credits

LeafScan ConvNeXt-T by Marconcini, https://huggingface.co/Marconcini/leafscan-convnext-tiny (CC BY-SA 4.0).
Trained on PlantVillage (CC BY-SA 3.0) and PlantDoc (CC BY 4.0).
Download `model_int8.onnx` from that page into `model/`.
