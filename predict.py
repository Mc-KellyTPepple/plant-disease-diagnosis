from classifier import assess, probabilities, supported_plants
from disease_info import DISEASE_INFO

PHOTO_TIPS = (
    "• One leaf, filling most of the frame\n"
    "• Natural daylight, no flash, no heavy shadows\n"
    "• Plain background, in focus\n"
    "• Choose a leaf that shows the problem clearly (not the whole plant)"
)


def _info(label):
    return DISEASE_INFO.get(label, {
        "name": label, "cause": "Unknown", "description": "Information unavailable.",
        "symptoms": [], "treatment": [], "prevention": [],
    })


def _bullets(items):
    return "\n".join(f"• {i}" for i in items)


def _top_text(top):
    return "\n".join(f"• {_info(lab)['name']} ({p * 100:.1f}%)" for _, lab, p in top)


def build_report(probs):
    """Return (report_text, speech_text) for a probability vector."""
    a = assess(probs)
    top = a["top"]
    _, label, p1 = top[0]
    info = _info(label)
    plant_line = f"Looks like a {a['plant'].replace('_', ' ').replace(',', '')} leaf.\n\n" if a["plant"] else ""

    if a["level"] == "high":
        text = "\n".join([
            "🌿 Diagnosis", info["name"], "",
            "🎯 Confidence", f"{p1 * 100:.1f}%", "",
            "🏆 Top 3 Predictions", _top_text(top), "",
            "🦠 Cause", info["cause"], "",
            "📝 Description", info["description"], "",
            "⚠ Symptoms", _bullets(info["symptoms"]), "",
            "💊 Recommended Treatment", _bullets(info["treatment"]), "",
            "🛡 Prevention", _bullets(info["prevention"]),
        ])
        speech = (
            f"The predicted disease is {info['name']}. The confidence is {p1 * 100:.0f} percent. "
            f"{info['description']} Recommended treatment. {' '.join(info['treatment'])} "
            f"Prevention tips. {' '.join(info['prevention'])}"
        )
        return text, speech

    if a["level"] == "medium":
        second = _info(top[1][1])
        text = "\n".join([
            "🤔 Possible diagnosis, NOT certain", "",
            f"{plant_line}Most likely: {info['name']} ({p1 * 100:.1f}%)",
            "", "🏆 Candidates", _top_text(top), "",
            f"⚠ Check the leaf against these symptoms",
            f"{info['name']}:", _bullets(info["symptoms"]), "",
            f"{second['name']}:", _bullets(second["symptoms"]), "",
            "💊 Only if the symptoms above match your plant",
            _bullets(info["treatment"]), "",
            "📷 For a firmer answer, retake the photo:", PHOTO_TIPS, "",
            "If it keeps coming out unclear, ask a local agricultural extension officer.",
        ])
        speech = (
            f"I am not certain. The most likely problem is {info['name']}, at {p1 * 100:.0f} percent, "
            f"but it could also be {second['name']}. Please compare the listed symptoms with your leaf, "
            f"or retake the photo in good light."
        )
        return text, speech

    text = "\n".join([
        "❓ I can't tell from this photo", "",
        f"{plant_line}The model could not match this leaf to a known condition with enough "
        f"confidence (best guess only {p1 * 100:.1f}%). No treatment is suggested, because acting "
        f"on a wrong diagnosis can waste money or harm the crop.", "",
        "Weak hints only:", _top_text(top), "",
        "📷 Try again:", PHOTO_TIPS, "",
        "This model only knows: " + ", ".join(supported_plants()) + ".",
        "Other crops, non-leaf images, and pest or nutrient problems it wasn't trained on "
        "can't be diagnosed reliably.",
    ])
    speech = (
        "I could not identify this leaf with enough confidence. "
        "Please retake the photo with one leaf in natural light on a plain background."
    )
    return text, speech


def predict(image):
    if image is None:
        return None, "Please upload a leaf photo.", None
    report, speech = build_report(probabilities(image))
    try:
        from speech import speak
        audio = speak(speech)
    except Exception:
        audio = None
    return image, report, audio


def create_demo():
    import gradio as gr

    return gr.Interface(
        fn=predict,
        inputs=gr.Image(type="pil", label="Upload a Plant Leaf"),
        outputs=[
            gr.Image(label="Uploaded Image"),
            gr.Textbox(label="Diagnosis", lines=28),
            gr.Audio(label="Voice Explanation", autoplay=True),
        ],
        title="🌿 AI Plant Disease Diagnosis System",
        description=(
            "Upload a clear image of a single plant leaf. The app reports a diagnosis only when "
            "the model is confident; otherwise it shows possibilities or asks for a better photo."
        ),
        allow_flagging="never",
    )


if __name__ == "__main__":
    create_demo().launch(server_name="0.0.0.0", server_port=7860)
