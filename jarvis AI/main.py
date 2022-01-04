import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening")

    speak("I am jarvis sir . please tell me how may i help you ")

def takeCommand():
    #it takes microphone input from the user and return string output 
    r =  sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        print("Say that again Please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 40)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendemail('youremail@gmail.com, to , content')
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query =   takeCommand().lower()
        # Logic for executing based on query
        if'wikipedia' in query:
            speak('searching Wkipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new("youtube.com")

        elif 'open google' in query:
            webbrowser.open("goggle.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"chinmay ji , The time is {strTime}")


        


