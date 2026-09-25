from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
from dotenv import load_dotenv
from pypdf import PdfReader
import sys

load_dotenv()

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} <file.pdf>")

path = sys.argv[1]

reader = PdfReader(path)
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

if not text.strip():
    sys.exit(f"No extractable text in {path} (scanned image?)")

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = client.text_to_speech.convert(
    text=text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)
