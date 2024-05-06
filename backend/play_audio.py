from pydub import AudioSegment
from pydub.playback import play


def play_audio(file_name):
    audio = AudioSegment.from_file('backend/audioFiles/'+file_name+'.mp3', format="mp3")
    play(audio)