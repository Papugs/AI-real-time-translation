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
import threading

def main():
    # Your main code logic here
    #while (1):
    if True:
        thread1 = threading.Thread(target=recording, args=("Record1",))
        #thread2 = threading.Thread(target=recording, args=("Record2",))
        thread3 = threading.Thread(target=playing, args=("Record1",))
        #thread4 = threading.Thread(target=playing, args=("Record2",))
        
        thread1.start()
        #thread2.start()
        thread3.start()
        #thread4.start()
        
        thread1.join()
        #thread2.join()
        thread3.join()
        #thread4.join()



def recording(file_name):
    print(11)
    if (file_name == "Record2"):
        time.sleep(4)
    record_audio(file_name)

def playing(file_name):
    print(22)
    if (file_name == "Record1"):
        print("siema")
        time.sleep(5)
        res_num = 1
    if (file_name == "Record2"):
        time.sleep(9)
        res_num = 2
    lang_code = language_code(file_name)
    text = speech_to_text(file_name, lang_code.upper())
    if text:
        text = translate(text, "EN-GB")
        text_to_speech(text, res_num)
        play_audio("Result"+str(res_num))

if __name__ == "__main__":
    main(),
