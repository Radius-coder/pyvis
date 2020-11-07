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

            #breaking up words for searches
            splitted = myText.split()
            first = splitted[0]
            if(len(splitted)==2):
                second =splitted[1]
                song = second
                query = second
            if(len(splitted)==3):
                second =splitted[1]
                third =splitted[2]
                song = second+"_"+third
                query = third
            if(len(splitted)==4):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                song = second+"_"+third+"_"+fourth
                query = third+" "+fourth
            if(len(splitted)==5):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                song = second+"_"+third+"_"+fourth+"_"+fifth
                query = third+" "+fourth+" "+fifth
            if(len(splitted)==6):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                sixth =splitted[5]
                song = second+"_"+third+"_"+fourth+"_"+fifth+"_"+sixth
                query = third+" "+fourth+" "+fifth+" "+sixth


            
            
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
                webbrowser.open("https://youtube.com/results?search_query=" + song)
                end = False
            elif(first=="search"):
                playsound(".\open.mp3")
                webbrowser.open("https://www.google.com/search?q=" + query)
                if(second=="Google"):
                    webbrowser.open("https://www.google.com/search?q=" + query)
                elif(second=="Bing"):
                    webbrowser.open("https://www.bing.com/search?q=" + query)
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
