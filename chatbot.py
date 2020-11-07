#import library
import datetime
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


            weatherCheck = "weather"
            newsCheck = "news"
            
            if(myText=="hello Jarvis"):
                playsound(".\good.mp3")
                end = False
                
            elif(myText=="play me xxx"):
                playsound(".\Meekz.mp3")
                end = False

            elif(myText=="what is the date"):
                playsound(".\date.mp3")
                end = False

            elif(weatherCheck in myText):
                webbrowser.open("https://www.google.com/search?q=weather")
                end = False
            elif(newsCheck in myText):
                webbrowser.open("https://www.google.com/search?q=news&sxsrf=ALeKk036rurS9ta79jzA6DCqMbECvw_fJw:1604718973065&source=lnms&tbm=nws&sa=X&ved=2ahUKEwi4_emCvO_sAhUColwKHf0oDSMQ_AUoAXoECA8QAw&biw=958&bih=919")
                end = False

            if(first=="open"):
                playsound(".\open.mp3")
                if(second=="Steam"):
                    os.startfile("G:\\Steam\\New folder\\steam.exe")
                if(second=="discord"):
                    os.startfile("C:\\Users\\Radius\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")
                if(second=="Spotify"):
                    os.startfile("C:\\Users\\Radius\\AppData\\Roaming\\Spotify\\Spotify.exe")
                if(second=="Minecraft"):
                    os.startfile("G:\\Minecraft\\MinecraftLauncher.exe")
                if(second=="paint"):
                    os.startfile("C:\\WINDOWS\\system32\\mspaint.exe")
                if(second=="audacity"):
                    os.startfile("C:\\Program Files (x86)\\Audacity\\audacity.exe")
                if(second=="CS"):
                    if(third=="GO"):
                        os.startfile("C:\\Users\\Radius\\Desktop\\Counter-Strike Global Offensive.url")
                elif(second=="YouTube"):
                    webbrowser.open("https://youtube.com")
                elif(second=="Gmail"):
                    webbrowser.open("https://gmail.com")
                elif(second=="Amazon"):
                    webbrowser.open("https://amazon.co.uk")
                elif(second=="Futurama"):
                    webbrowser.open("https://www.amazon.co.uk/gp/video/detail/0NYGDOILXA7CWK7FU7260JNXS4/ref=atv_sf_stream_prime_hd_ep?autoplay=1")
                elif(third=="Grand"):
                    webbrowser.open("https://www.amazon.co.uk/gp/video/detail/0G0VPA8QYRIR5GCAJNET1RCJGJ/ref=atv_sf_stream_prime_hd_ep?autoplay=1&t=0")
                elif(second=="Facebook"):
                    webbrowser.open("https://facebook.com")
                elif(second=="Twitter"):
                    webbrowser.open("https://twitter.com")
                elif(second=="my"):
                    if(third =="UWE"):
                        webbrowser.open("https://my.uwe.ac.uk")
                elif(second=="Outlook"):
                    webbrowser.open("https://outlook.com")
                    
                end = False
            elif(first=="search"):
                playsound(".\open.mp3")
                if(second=="Google"):
                    webbrowser.open("https://www.google.com/search?q=" + query)
                elif(second=="Bing"):
                    webbrowser.open("https://www.bing.com/search?q=" + query)
                elif(second=="YouTube"):
                    webbrowser.open("https://youtube.com/results?search_query=" + query)
                elif(second=="wiki"):
                    webbrowser.open("https://en.wikipedia.org/wiki/" + query)
                elif(second=="Wikipedia"):
                    webbrowser.open("https://en.wikipedia.org/wiki/" + query)
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
