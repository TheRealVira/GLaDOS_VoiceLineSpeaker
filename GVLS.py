from gtts import gTTS
import os
import random

lines = open('vl').read().splitlines()
myline =random.choice(lines)

tts = gTTS(text=myline, lang='en-uk')
tts.save("speech.mp3")

os.startfile("speech.mp3")