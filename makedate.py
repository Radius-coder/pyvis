import datetime
import os
from gtts import gTTS
#get today's date
date = datetime.datetime.now()
x = date.strftime("%d"+" %B, %Y")
tts = gTTS(text=x, lang='en')
tts.save("date.mp3")
print("Audio loaded!")
