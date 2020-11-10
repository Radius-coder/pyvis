#import library
import datetime
import os
from playsound import playsound
import requests
from bs4 import BeautifulSoup 
import speech_recognition as sr 
import webbrowser
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 168)

'''voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
# Use british female voice 
engine.setProperty('voice', voice_id)'''
engine.say("Welcome back Sir")
engine.runAndWait()
print("Say open 'website or application', search 'website and query', weather, news,\ndate, calculate 'sum', play song 'name' play video 'name'") 

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
end = False



#calculator funciton
def calc(a,op,b):
    if op=="+":
        answer = a+b
        return answer
    elif op=="-":
        answer = a-b
        return answer
    elif op=="x":
        answer = a*b
        return answer
    elif op=="/":
        if a == 0 | b == 0:
            print("cannot divide by 0")
        else:
            answer = a/b
            return answer
    else:
        print("Please calculate a valid sum")

        
# Reading Microphone as source
# listening the speech and store in audio_text variable
while end == False:
    #get today's date
    date = datetime.datetime.now()
    x = date.strftime("%d"+" %B, %Y")
    with sr.Microphone() as source:
        print("Yes Sir?")
        audio_text = r.listen(source)
        print("One second...")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

        try:
            myText =r.recognize_google(audio_text)
            myText = myText.lower()
            print(myText)
            
            #breaking up words for searches
            splitted = myText.split()
            first = splitted[0]
            if(len(splitted)==2):
                second =splitted[1]
                query = second
            if(len(splitted)==3):
                second =splitted[1]
                third =splitted[2]
                query = third
            if(len(splitted)==4):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                query = third+" "+fourth
            if(len(splitted)==5):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                query = third+" "+fourth+" "+fifth
            if(len(splitted)==6):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                sixth =splitted[5]
                query = third+" "+fourth+" "+fifth+" "+sixth
            if(len(splitted)==6):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                sixth =splitted[5]
                query = third+" "+fourth+" "+fifth+" "+sixth
            if(len(splitted)==6):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                sixth =splitted[5]
                query = third+" "+fourth+" "+fifth+" "+sixth
            if(len(splitted)==6):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                sixth =splitted[5]
                query = third+" "+fourth+" "+fifth+" "+sixth
            if(len(splitted)==6):
                second =splitted[1]
                third =splitted[2]
                fourth =splitted[3]
                fifth =splitted[4]
                sixth =splitted[5]
                query = third+" "+fourth+" "+fifth+" "+sixth

            #general shortcuts and sentence activation
            dateCheck = "the date"
            weatherCheck = "weather"
            newsCheck = "news"
            wellBeing = "how are you"
            wellBeingGood = ["happy", "great", "good", "amazing"]
            wellBeingSad = ["sad", "unhappy", "upset", "not", "unwell"]
            
            if("hello" in myText):
                if(wellBeing in myText):
                    engine.say("Good day Sir, I am well Sir, how are you today?")
                    engine.runAndWait()
                    audio_text = r.listen(source)
                    myText =r.recognize_google(audio_text)
                    for i in wellBeingSad:
                        if(i in myText):
                            engine.say("Maybe this will make you smile")
                            engine.runAndWait()
                            webbrowser.open("https://youtu.be/SB-qEYVdvXA")
                            end = False
                    for j in wellBeingGood:
                        if(j in myText):
                            engine.say("Good to hear Sir, how may I assist?")
                            engine.runAndWait()
                            end = False
                elif(dateCheck in myText):
                    engine.say("Good day Sir,Todays date is" +x)
                else:
                    engine.say("Good day Sir")
                engine.runAndWait()
                end = False

            if("hi" in myText):
                if(wellBeing in myText):
                    engine.say("Good day Sir, I am well Sir, how are you today?")
                    engine.runAndWait()
                    audio_text = r.listen(source)
                    myText =r.recognize_google(audio_text)
                    for i in wellBeingSad:
                        if(i in myText):
                            engine.say("Maybe this will make you smile")
                            engine.runAndWait()
                            webbrowser.open("https://youtu.be/SB-qEYVdvXA")
                            end = False
                    for j in wellBeingGood:
                        if(j in myText):
                            engine.say("Good to hear Sir, how may I assist?")
                            engine.runAndWait()
                            end = False
                elif(dateCheck in myText):
                    engine.say("Good day Sir,Todays date is" +x)
                else:
                    engine.say("Good day Sir")
                engine.runAndWait()
                end = False

            if("hey" in myText):
                if(wellBeing in myText):
                    engine.say("Good day Sir, I am well Sir, how are you today?")
                    engine.runAndWait()
                    audio_text = r.listen(source)
                    myText =r.recognize_google(audio_text)
                    for i in wellBeingSad:
                        if(i in myText):
                            engine.say("Maybe this will make you smile")
                            engine.runAndWait()
                            webbrowser.open("https://youtu.be/SB-qEYVdvXA")
                            end = False
                    for j in wellBeingGood:
                        if(j in myText):
                            engine.say("Good to hear Sir, how may I assist?")
                            engine.runAndWait()
                            end = False
                elif(dateCheck in myText):
                    engine.say("Good day Sir,Todays date is" +x)
                else:
                    engine.say("Good day Sir")
                engine.runAndWait()
                end = False
            elif(wellBeing in myText):
                engine.say("I am well sir, how are you today?")
                engine.runAndWait()
                audio_text = r.listen(source)
                myText =r.recognize_google(audio_text)
                for i in wellBeingSad:
                    if(i in myText):
                        engine.say("Maybe this will make you smile")
                        engine.runAndWait()
                        webbrowser.open("https://youtu.be/SB-qEYVdvXA")
                        end = False
                for j in wellBeingGood:
                    if(j in myText):
                        engine.say("Good to hear Sir, how may I assist?")
                        engine.runAndWait()
                        end = False
                end = False

            
            elif("thank you" in myText):
                engine.say("My pleasure Sir")
                engine.runAndWait()
                end = False
                

            elif(dateCheck in myText):
                engine.say(x)
                engine.runAndWait()
                end = False

            elif(weatherCheck in myText):
                engine.say("Just a moment Sir")
                engine.runAndWait()
                webbrowser.open("https://www.google.com/search?q=weather")
                end = False
                
            elif(newsCheck in myText):
                engine.say("Just a moment Sir")
                engine.runAndWait()
                webbrowser.open("https://www.google.com/search?q=news&sxsrf=ALeKk036rurS9ta79jzA6DCqMbECvw_fJw:1604718973065&source=lnms&tbm=nws&sa=X&ved=2ahUKEwi4_emCvO_sAhUColwKHf0oDSMQ_AUoAXoECA8QAw&biw=958&bih=919")
                end = False
            

            if(first=="open"):
                engine.say("One moment Sir")
                engine.runAndWait()
                if(second=="google"):
                    webbrowser.open("https://www.google.com")
                if(second=="steam"):
                    os.startfile("G:\\Steam\\New folder\\steam.exe")
                if(second=="discord"):
                    os.startfile("C:\\Users\\Radius\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")
                if(second=="spotify"):
                    os.startfile("C:\\Users\\Radius\\AppData\\Roaming\\Spotify\\Spotify.exe")
                    os.system("open /Applications/Spotify.app")
                if(second=="minecraft"):
                    os.startfile("G:\\Minecraft\\MinecraftLauncher.exe")
                if(second=="paint"):
                    os.startfile("C:\\WINDOWS\\system32\\mspaint.exe")
                if(second=="audacity"):
                    os.startfile("C:\\Program Files (x86)\\Audacity\\audacity.exe")
                if(second=="visual"):
                    if(third=="code"):
                        os.startfile("C:\\Users\\Radius\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    elif(third=="studio"):
                        os.startfile("D:\\vs\\Common7\\IDE\\devenv.exe")
                if(second=="cs"):
                    if(third=="go"):
                        os.startfile("C:\\Users\\Radius\\Desktop\\Counter-Strike Global Offensive.url")
                if(second=="new"):
                    if(third=="tab"):
                        webbrowser.open("https://google.com")
                elif(second=="youtube"):
                    webbrowser.open("https://youtube.com")
                elif(second=="google"):
                    if(third=="keep"):
                        res = "https://keep.google.com"
                    elif(third=="mail"):
                        res="https://gmail.com"
                    webbrowser.open(res)
                elif(second=="gmail"):
                    webbrowser.open("https://gmail.com")
                elif(second=="amazon"):
                    webbrowser.open("https://amazon.co.uk")
                elif(second=="futurama"):
                    webbrowser.open("https://www.amazon.co.uk/gp/video/detail/0NYGDOILXA7CWK7FU7260JNXS4/ref=atv_sf_stream_prime_hd_ep?autoplay=1")
                elif("grand tour" in myText):
                    webbrowser.open("https://www.amazon.co.uk/gp/video/detail/0G0VPA8QYRIR5GCAJNET1RCJGJ/ref=atv_sf_stream_prime_hd_ep?autoplay=1&t=0")
                elif(second=="facebook"):
                    webbrowser.open("https://facebook.com")
                elif(second=="twitter"):
                    webbrowser.open("https://twitter.com")
                elif(second=="my"):
                    if(third =="uwe"):
                        webbrowser.open("https://my.uwe.ac.uk")
                elif(second=="outlook"):
                    webbrowser.open("https://outlook.com")
                elif(second=="github"):
                    webbrowser.open("https://github.com/Radius-coder/pyvis") 
                end = False

            elif(first=="logout"):
                engine.say("Are you sure you want to do this Sir")
                engine.runAndWait()
                print("Say yes or no")
                audio_text = r.listen(source)
                myText =r.recognize_google(audio_text)
                if("no" in myText):
                    end = False
                elif("yes" in myText):
                    os.system("shutdown -l")
                else:
                    end = False
                
                
            elif(first=="search"):
                engine.say("One moment Sir")
                engine.runAndWait()
                if(second=="google"):
                    webbrowser.open("https://www.google.com/search?q=" + query)
                elif(second=="bing"):
                    webbrowser.open("https://www.bing.com/search?q=" + query)
                elif(second=="youtube"):
                    webbrowser.open("https://youtube.com/results?search_query=" + query)
                elif(second=="wiki"):
                    webbrowser.open("https://en.wikipedia.org/wiki/" + query)
                    url =("https://en.wikipedia.org/wiki/" + query)
                elif(second=="wikipedia"):
                    webbrowser.open("https://en.wikipedia.org/wiki/" + query)
                    url =("https://en.wikipedia.org/wiki/" + query)
                elif(second=="amazon"):
                    webbrowser.open("https://www.amazon.co.uk/s?k=" + query)

                end = False
                
            #reading wiki pages    
            elif(first=="reed"):
                #open with GET method 
                resp=requests.get(url) 
                              
                 #http_respone 200 means OK status 
                if resp.status_code==200:
                    print("Successfully opened the web page")                               
                    # parser 
                    soup=BeautifulSoup(resp.text,'html.parser') 
                    # l is the div which contains all the text   
                    l=soup.find("div",{"class":"mw-parser-output"})        
                    #now we want only the text part. 
                    #find all the elements of p  
                    for i in l.findAll("p"):
                        engine.say(i.text)
                        engine.runAndWait()
                        end = False
                else:
                    engine.say("I could not read this page, sorry Sir")
                    engine.runAndWait()
                    print("Error")
                    end = False
                        
            elif(first=="calculate"):
                engine.say("The answer is ")
                engine.runAndWait()
                finsum = calc(int(second), third, int(fourth))
                engine.say(finsum)                
                engine.runAndWait()
                end = False
            elif(second=="calculate"):
                engine.say("The answer is ")
                engine.runAndWait()
                finsum = calc(int(third), fourth, int(fifth))
                engine.say(finsum)                
                engine.runAndWait()
                end = False

            
            elif(first == "play"):
                if(second=="song"):                  
                    os.startfile(query+".mp3")
                if(second=="music"):                  
                    os.startfile(query+".mp3")
                elif(second=="video"):
                    os.startfile(query+".mp4")
                end = False
                
            if("bye" in myText):
                 engine.say("Pleasure Sir")
                 engine.runAndWait()
                 end = True
            if("sia" in myText):
                 engine.say("See you later Sir")
                 engine.runAndWait()
                 end = True

                
        except:
             print("Sorry, I did not get that, try again")
             end = False
             
#pip install SpeechRecognition
#pip install PyAudio
#pip install playsound
#pip install requests
#pip install BeautifulSoup 
#pip install pyttsx3
"""
could use a file which contains user personalised charateristics to use in conversation and could setup new one if user doesnt have one
eventually get it to open any application, search the web, turn off computer or restart or log off,
after that could get the user to have more control and so can close applications, maybe close the open tab within a browser
and one day it will 
"""
