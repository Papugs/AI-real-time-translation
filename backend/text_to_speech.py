from pathlib import Path
from openai import OpenAI
import openai

def text_to_speech(text, num):
    api_key = "API-KEY
    client = OpenAI(api_key=api_key)
    client.api_key = api_key
    speech_file_path = Path(__file__).parent / str("audioFiles/Result"+str(num)+".mp3")
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
    )

    response.stream_to_file(speech_file_path)