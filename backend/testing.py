# 1. Provide speech_to_text with a Polish conversation in mp3 format
# 2. Run translation to English on the text
# 3. Convert translated text to mp3 file
from speech_to_text import speech_to_text, speech_to_text_dg
from text_to_speech import text_to_speech
from translation import translate
import time

def main():
    # Your main code logic here
    print(1)
    start_time = time.time()
    text = speech_to_text_dg("/Users/norbertpapuga/Desktop/Computer Science/PROJECTS/Real-Time-Translator/AI-real-time-translation/backend/audioFiles/example2.mp3")
    elapsed_time = (time.time() - start_time) % 60
    print(elapsed_time)
    print(2)
    text = translate(text, "EN-GB")
    print(3)
    text_to_speech(text)
    print(4)


if __name__ == "__main__":
    main()
