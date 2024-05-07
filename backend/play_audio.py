from pydub import AudioSegment
from pydub.playback import play
import pygame
import simpleaudio as sa
import time

#def play_audio(file_name):
 #   audio = AudioSegment.from_mp3('backend/audioFiles/'+file_name+'.mp3')
  #  play(audio)
    

def play_audio(file_name):
    convert_mp3_to_wav(file_name, file_name)
    try:
        wave_obj = sa.WaveObject.from_wave_file('backend/audioFiles/'+file_name+'.wav')
        wave_obj.play()
        time.sleep(5)
        print(123)
        #play_obj.wait_done()
    except Exception as e:
        print(f"Error playing WAV file: {e}")


from pydub import AudioSegment
import simpleaudio as sa
"""
def play_audio(file_name):
    # Load the audio file
    audio = AudioSegment.from_mp3('backend/audioFiles/'+file_name+'.wav')
    
    # Convert to raw audio data
    raw_audio_data = audio.raw_data
    
    # Play the audio
    play_obj = sa.play_buffer(raw_audio_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
    
    # Wait for playback to finish
    play_obj.wait_done()"""

def convert_mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3('backend/audioFiles/'+mp3_file+'.mp3')
    
    # Export the audio to WAV format
    audio.export('backend/audioFiles/'+wav_file+'.wav', format="wav")