# Plant Disease Diagnosis

Upload a photo of one leaf. The app names the crop and disease only when the model is confident, shows possible candidates when it is not, and says it can't tell when it has no good answer.

## Model

LeafScan ConvNeXt-T (int8 ONNX, 38 crop and disease classes, 14 crops) by Marconcini, fine-tuned on PlantVillage and then PlantDoc field photos. Confidence is calibrated with the model's own temperature (0.8376), and "confident" means a calibrated probability of at least 0.7477, a threshold the author fitted on held-out field photos.

## Measured accuracy on real field photos

Measured by `evaluate_plantdoc.py` on the 236 photos of the PlantDoc test split, which the model never saw in training:

| Measure | Result (95% interval) |
|---|---|
| Right disease and crop, all photos | 71.2% (65.1–76.6) |
| Right crop | 87.3% (82.4–90.9) |
| Healthy versus diseased | 95.3% (91.8–97.4) |
| Photos the app answers confidently | 65.3% (59.0–71.0) |
| Right when it answers confidently | 85.1% (78.6–89.8) |

The author reports 71.9%, 66% answered and 84.7% right on 228 photos (a few duplicates removed), so the numbers agree. Differences below about 6 points are within noise on a test set this small. Lab-photo accuracy is much higher and says little about photos taken in a field: the author's PlantVillage-only model scores 99.7% on lab photos and 31% on field photos.

Preprocessing is not stated on the model card. This app resizes the shorter side to 256 and centre-crops 224, the backbone's default, which matched the published numbers better than squashing the photo to 224x224 (69.5% accuracy, 70.3% answered, 86.7% right). `LEAFSCAN_PREPROCESS=squash` switches it.

## What it can't do

It knows only the 38 PlantVillage classes. Other crops, pests and nutrient problems get forced into one of them or answered "can't tell". Photos that are not leaves can still get a diagnosis. It is a decision aid, not a substitute for an agronomist.

## Run

    pip install -r requirements.txt
    python app.py

Settings: `LEAFSCAN_THRESHOLD` (confident cutoff) and `LEAFSCAN_LOW` (below this, "can't tell", default 0.40, untuned).

Reproduce the measurement:

    git clone --depth 1 --filter=blob:none --sparse https://github.com/pratikkayal/PlantDoc-Dataset plantdoc
    git -C plantdoc sparse-checkout set test
    python evaluate_plantdoc.py plantdoc/test

## Deployment

Render.

## Model credits

LeafScan ConvNeXt-T by Marconcini, https://huggingface.co/Marconcini/leafscan-convnext-tiny (CC BY-SA 4.0). Trained on PlantVillage (CC BY-SA 3.0) and PlantDoc (CC BY 4.0).
