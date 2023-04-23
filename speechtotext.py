from google.cloud import speech
import os
import io

def speech_to_text():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'google_speeech_to_text.json'
    client = speech.SpeechClient()
    file_name = "Test Audio.wav"

    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        audio_channel_count=1,
        language_code="en-US",
    )

    response = client.recognize(request={"config": config, "audio": audio})

    for result in response.results:
        with open("output.txt", "w")as f:

            print("Transcript: {}".format(result.alternatives[0].transcript), file = f)

if __name__== "__main__":
    speech_to_text()