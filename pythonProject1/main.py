import os
import smtplib
#I will add Generative ai API to it soon.
#Also,will add exit function to it.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. How can I help you?")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
         #print(e)
         print("Say that again please...")
         return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example.gmail.com', '_YOUR_PASSWORD_')
    server.sendmail('example.gmail.com',to, content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        #logic for executing tasks based on tasks
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open github' in query:
            webbrowser.open('github.com')

        elif 'play music' in query:
            webbrowser.open('https://music.youtube.com/watch?v=hoNb6HuNmU0&list=LM')

        elif 'instagram' in query:
            webbrowser.open('instagram.com')

        elif 'linkedin' in query:
            webbrowser.open('www.linkedin.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\HP711\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say")
                content = takecommand()
                to = "example.gmail.com"
                sendEmail(to,content)
                speak("Email sent!")
            except Exception as e:
                print(e)
                speak("I am currently not able to send email")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
