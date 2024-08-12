# pip install gtts
from gtts import gTTS
import os

mytext= "Hello Everyone, My name is Shreekant"
language= "en"
myobj= gTTS(text= mytext, lang= language, slow= False)
myobj.save("text_to_speech.mp3")
print("Audio playing...")
os.system("mpg321 text_to_speech.mp3")
print("......")
