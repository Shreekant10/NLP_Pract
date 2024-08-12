# pip install SpeechRecognition
# pip install pydub

import speech_recognition as sr
from pydub import AudioSegment
from os import path
import subprocess

recognizer= sr.Recognizer()
audio_src= "C:\\Users\\Shreekant Kadam\\Desktop\\NLP Practs\\text_to_speech.mp3"
audio= AudioSegment.from_mp3(audio_src)
audio_file_wav= "C:\\Users\\Shreekant Kadam\\Desktop\\NLP Practs\\text_to_speech.mp3"
audio.export(audio_file_wav, format= "wav")
with sr.AudioFile(audio_file_wav)as source:
    audio_data= recognizer.record(source)
   
try:
    text= recognizer.recognize_google_cloud(audio_data)
    print('Recognized Speech:', text)
except sr.UnknownValueError:
    print('Speech recognition could not uderstand the audio')
except sr.RequestError as e:
    print("Could not request results from Googlr Speech Recognition service; {0}".format(e))