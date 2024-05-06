# 1. Provide speech_to_text with a Polish conversation in mp3 format
# 2. Run translation to English on the text
# 3. Convert translated text to mp3 file
from speech_to_text import speech_to_text, language_code
from text_to_speech import text_to_speech
from translation import translate
import time
from google.cloud import speech
from play_audio import play_audio
from record_audio import record_audio


def main():
    # Your main code logic here
    while (1):
        recording();playing(); # at the same time


def recording():
    record_audio("Record")

def playing():
    lang_code = language_code("Record")
    text = speech_to_text("Record", lang_code.upper())
    text = translate(text, "PL")
    text_to_speech(text)
    play_audio("result")

if __name__ == "__main__":
    main(),
