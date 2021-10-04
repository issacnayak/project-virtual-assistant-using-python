import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')#is used to take voices
voices = engine.getProperty('voices')
#print(voices)
#print(voices[0].id)# to check the voice type i.e male voic or female voice
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("i am issac's assistant.please tell me sir how i may help you")
def takeCommand():
    #it takes input from user and give string output
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing......")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("say again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia please...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open geeksforgeeks' in query:
            speak("best tutorial for learning and practicing coding")
            webbrowser.open("geeks for geeks.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'hackerrank' in query:
            webbrowser.open("hackerrank.com")
        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'hackerearth' in query:
            webbrowser.open("hackerearth.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'who is our class teacher' in query:
            speak("mr.Bhabani sankar panda")
        elif 'introduce' in query:
            speak("good morning everyone,i have been created by group 11 for fourth semester project")
        elif 'thank you' in query:
            speak("you are welcome sir.")    
        elif 'stop' in query:
            speak("have a good day.")
            exit()
        elif 'weather' in query:
            webbrowser.open("weather.com")
        elif 'time'in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")
        elif 'open code' in query:
            codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
        elif 'news' in query:
            webbrowser.open("worldometers.info")
        

         