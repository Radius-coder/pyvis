#import library
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
playsound(".\good.mp3")
# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
end = False

    
# Reading Microphone as source
# listening the speech and store in audio_text variable
while end == False:
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            myText =r.recognize_google(audio_text)
            if(myText=="hello"):
                print("goodbyE")
                
            # using google speech recognition
            print("Text: "+myText)
            end = False
        except:
             print("Sorry, I did not get that, try again")
             stop = input();
             if stop == 'y':
                 end = True
             else:
                 end = False
             
#pip install SpeechRecognition
#pip install PyAudio
