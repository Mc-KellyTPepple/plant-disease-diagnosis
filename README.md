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

## Confidence cutoff

The "confident" cutoff is 0.7477, fitted by the model's author. I checked it on the PlantDoc test photos with a split-sample test: fit the cutoff on a random half, score the other half, repeat 500 times. Re-fitting gave no reliable gain over the author's value (about 65% answered and 85% right on the held-out half either way), so it stays. A stricter cutoff is a trade, not a fix: 0.85 gives about 91% right but answers only about 55% of photos. Set `LEAFSCAN_THRESHOLD=0.85` if you prefer fewer, safer answers.

What each answer type is worth on the 236 test photos:

| The app says | Photos | Top choice right | True disease among the 3 candidates shown |
|---|---|---|---|
| Diagnosis (confident) | 154 | 85.1% | 98.7% |
| Possible diagnosis, not certain | 68 | 48.5% | 91.2% |
| Can't tell | 14 | 28.6% | 78.6% |

So a "possible" answer is a shortlist, not a verdict: the right disease was on it 9 times in 10, though first place was right only about half the time. The "can't tell" cutoff (0.40) is a safe, untuned choice. Only 14 photos fall below it, too few to tune.

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
