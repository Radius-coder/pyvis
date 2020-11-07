#import library
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr 
import webbrowser


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
end = False

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
            splitted = myText.split()
            first = splitted[0]
            second = splitted[1]
            third = splitted[2]
            
            
            if(myText=="good morning"):
                playsound(".\good.mp3")
                end = False
                
            elif(myText=="play me xxx"):
                playsound(".\Meekz.mp3")
                end = False

            if(first=="open"):
                playsound(".\open.mp3")
                if(second=="Steam"):
                    os.startfile("G:\\Steam\\New folder\\steam.exe")
                    end = False
                elif(second=="YouTube"):
                    webbrowser.open("https://youtube.com")
                    end = False
            elif(first=="play"):
                playsound(".\open.mp3")
                song = (second+"_"+third)
                webbrowser.open("https://youtube.com/results?search_query=" + song)
                end = False
            elif(first=="search"):
                playsound(".\open.mp3")
                if(second=="Google"):
                    webbrowser.open("https://www.google.com/search?q=" + third)
                elif(second=="Bing"):
                    webbrowser.open("https://www.bing.com/search?q=" + third)
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
