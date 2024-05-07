import whisper
import os
import argparse
from google.cloud import speech

client = speech.SpeechClient.from_service_account_file("backend/key.json")

def speech_to_text(file_name, lang_code):
    """Transcribe the given audio file."""

    with open('backend/audioFiles/'+file_name+'.wav', "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        language_code=str(lang_code),
    )
    response = client.recognize(config=config, audio=audio)
    if response.results:
        if response.results[0]:
            if response.results[0].alternatives:
                if response.results[0].alternatives[0]:
                    return response.results[0].alternatives[0].transcript


def language_code(file_name):

    model = whisper.load_model("base")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio('backend/audioFiles/'+file_name+'.wav')
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    return max(probs, key=probs.get)