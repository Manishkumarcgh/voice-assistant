import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am spandy man. please tell me how may I help you")
    
def takecommand():
    #It takes microphone input from the user return string output
    
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recogning...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "none"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        
        #lodic for exexuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strtime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        