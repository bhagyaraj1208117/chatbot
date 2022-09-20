import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

print("hi")
engine =pyttsx3.init("sapi5")
voices =engine.getProperty("voices")
print(voices[2].id)
engine.setProperty("voice",voices[2].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    date=datetime.datetime.now()
    hour=date.hour 
    if hour <= 12:
        speak("Good Morning. Robin")
    elif hour<16:
        speak("Good Afternoon. Robin")    
    elif hour<20:
        speak("Good Afternoon Robin")    
    else:
        speak("Good Night Robin")    
       
def takeCommand():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("listening....")   
        speak("I am sara. How can I help You")
        r.pause_threshold =1
        audio=r.listen(source)
    try:
        print("Recognizing")  
        query=r.recognize_google(audio,language="en-in") 
        print("User said:{} ".format(query))
    except Exception as e:
        print(e)    
        speak("Sorry I didn't get that. Can you repeat?")
        return "None" 
    return query       
if __name__ == "__main__":
    
   wishMe()
   is_true=True
   while is_true:
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("searching for wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open insta" in query:
            webbrowser.open("instagram.com")
        elif "open cricbuzz" in query:
            webbrowser.open("cricbuzz.com")    
             
        elif "time now" in query:
            st=datetime.datetime.now().strftime("%H:%M")
            speak(st)
        elif "joke" in query:
            speak("Two men are hiking through the woods when one of them cries out, “Snake! Run!” His companion laughs at him. “Oh, relax. It’s only a baby,” he says. “Don’t you hear the rattle?” —Steve Smith")  
        elif "exit" in query:
            print("exit")
            break
