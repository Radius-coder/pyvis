#import library
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr 
import webbrowser


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
end = False

#load audio files
print("Loading audio...")
tts = gTTS(text='Good day Sir. How may I assist you today?', lang='en')
tts.save("good.mp3")
print("Audio loaded!")

# Reading Microphone as source
# listening the speech and store in audio_text variable
while end == False:
    
    with sr.Microphone() as source:
        print("Yes Sir?")
        audio_text = r.listen(source)
        print("One second...")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            myText =r.recognize_google(audio_text)
            print(myText)
            
            if(myText=="good morning"):
                playsound(".\good.mp3")
                end = False
                
            elif(myText=="play me xxx"):
                playsound(".\Meekz.mp3")
                end = False
                
            elif(myText=="open Steam"):
                playsound(".\open.mp3")
                os.startfile("G:\\Steam\\New folder\\steam.exe")
                end = False

            elif(myText=="open YouTube"):
                webbrowser.open("https://youtube.com")
                end = False
                
            if(myText=="goodbye"):
                 end = True
                
        except:
             print("Sorry, I did not get that, try again")
             end = False
             
#pip install SpeechRecognition
#pip install PyAudio
"""
could use a file which contains user personalised charateristics to use in conversation and could setup new one if user doesnt have one
eventually get it to open any application, search the web, turn off computer or restart or log off,
after that could get the user to have more control and so can close applications, maybe close the open tab within a browser
and one day it will 
"""
