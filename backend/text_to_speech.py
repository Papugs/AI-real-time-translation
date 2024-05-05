from pathlib import Path
from openai import OpenAI
import openai

def text_to_speech(text):
    api_key = "sk-proj-GXn89aJrbsBYXtLdydcsT3BlbkFJPdo1D76HpFf2kuU611XO"
    client = OpenAI(api_key=api_key)
    client.api_key = api_key
    speech_file_path = Path(__file__).parent / "audioFiles/result.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
    )

    response.stream_to_file(speech_file_path)