from cgitb import text
from http import server
from math import remainder
from click import command
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import os
import random
import smtplib

# install  every single moudle in hear 
# remember to also  install pyaoudio if it don't work download from unofficial pip bainary

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# this speak funtion is for taking the text and make it into vocal 

def speak(text):
    engine.say(text)
    engine.runAndWait()

# wish me function  will wish the user 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Riya Sir. how may I help you")  
# this function useed for taking the commend fron the source via mic and retun the commend 

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en-in')
            print(f"User said: {command}")
            command = command.lower()
            if 'riya' in command:
                command = command.replace('riya', '')
    except:
        pass
    return command
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password') #the less secure app enable funtion not working with gmail so you can just enable 2 setp varifecation and go to app password to genaret a passwerd
    server.sendmail('youremail.com',to,content)

if __name__ == "__main__":
    wishMe()
    while True:
# logic
        command = take_command()
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current time is ' + time)
        elif'music' in command:
            music_dir = 'D:\\Artcell\\Aniket Prantor' #{you need to replelace this path to work .replece with your feavorite songs folder local link}
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)])) 
        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'tell me about' in command:
            look_for = command.replace('tell me about', '')
            info = wikipedia.summary(look_for,2)
            print(info)
            speak("According to wikipedia")
            speak(info)
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif 'date' in command:
            speak('Yes sure,You are an amezing person i hope our date will be grate')
        elif "open youtube" in command:
            speak("opening youtube")
            webbrowser.open('youtube.com')
        elif "open facebook" in command:
            webbrowser.open('facebook.com')
            speak("opening facebook")
        elif "open google" in command:
            webbrowser.open('google.com')
            speak("opening google")

        elif "open stackoverflow" in command:
            webbrowser.open('stackoverflow.com')
            speak("opening google")
        elif 'open code' in command:
            speak("opening vs code")
            codepath = "C:\\Users\\sheik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #use your app location
            os.startfile(codepath)
        elif 'open figma' in command:
            speak("opening figma")
            codepath = 'C:\\Users\\sheik\\AppData\\Local\\Figma\\Figma.exe'#use your app location
            os.startfile(codepath)
        elif "email to crush" in command:
            try:
                speak("what should i say")
                content = take_command()
                to = 'yourcrush@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir I'm not able to send this email")
        else:
            speak('I did not get it but I am going to search it for you')
            pywhatkit.search(command)