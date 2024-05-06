import pyaudio
import wave

def record_audio(filename, record_seconds=5):
  """Records audio from microphone and saves as 16-bit PCM WAV.

  Args:
      filename: Name of the output WAV file.
      record_seconds: Duration of recording in seconds (default 5).
  """

  FORMAT = pyaudio.paInt16  # 16-bit linear PCM
  CHANNELS = 1  # Mono
  RATE = 16000  # Sample rate in Hz
  CHUNK = 1024  # Buffer size in bytes

  audio = pyaudio.PyAudio()

  # Start recording stream
  stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
  frames = []

  print("Recording...")

  for i in range(0, int(RATE / CHUNK * record_seconds)):
    data = stream.read(CHUNK)
    frames.append(data)

  # Stop recording
  stream.stop_stream()
  stream.close()
  audio.terminate()

  print("Finished recording.")

  # Convert recorded data to integers (assuming signed short)
  audio_data = []
  for frame in frames:
    for i in range(0, len(frame), 2):
      # Assuming little-endian byte order
      audio_data.append(frame[i:i+2])

  # Write data to WAV file
  with wave.open('backend/audioFiles/'+filename+'.wav', 'wb') as wav_file:
    wav_file.setnchannels(CHANNELS)
    wav_file.setsampwidth(2)  # 2 bytes per sample (16-bit)
    wav_file.setframerate(RATE)
    wav_file.writeframes(b''.join(audio_data))