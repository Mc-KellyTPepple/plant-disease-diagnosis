import asyncio
import tempfile
import edge_tts

VOICE = "en-US-AriaNeural"


async def speak_async(text):

    outfile = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    ).name

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save(outfile)

    return outfile


def speak(text):

    return asyncio.run(
        speak_async(text)
    )
