import tkinter as tk
from tkinter import messagebox
import time
import webbrowser as wb
import wikipedia
import speech_recognition as sr
import datetime
import pyttsx3
from unittest import result
import smtplib
from multiprocessing.connection import Listener
from logging.config import listen
import os
import pyaudio
import subprocess
import pyjokes
from time import sleep
import requests
import json
import shutil
import wolframalpha as Zatch
client = Zatch.Client('GAX2RG-J766E3V962')
api_key1 = "f5605ed338c34456a6691f7778adc42b"
news_url = f"https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key1}"

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
api_key = "AIzaSyBmE1sYrfW_fxEPLMHbJfjl8BH56DBkliw"
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
voicespeed = 180
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("A very Good morning Kori")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Kori")
    elif hour >= 18 and hour < 19:
        speak("A very good evening Kori")
    else:
        speak("A very good night Kori ")

    speak(" I am zatch . Please tell me how may i help you ")



def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
    # set the energy threshold to a higher value
        r.energy_threshold = 500
        r.pause_threshold
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Pardon me , Say that again please...")
        speak("Pardon me ,Say that again please...")
        return None  # None string will be returned
    return query

def get_news():
    try:
        news_response = requests.get(news_url)
        news_json = json.loads(news_response.text)
        articles = news_json["articles"]
        main_news = None
        other_news = []
        for article in articles:
            if "source" in article and "country" in article["source"] and article["source"]["country"] == "us":
                main_news = article["title"]
                break
        for article in articles:
            if "source" in article and "country" in article["source"] and article["source"]["country"] != "us" and len(other_news) < 2:
                other_news.append(article["title"])
        return main_news, other_news
    except Exception as e:
        print("Error fetching news")
        print(e)
        return None




def show_news():
    news = get_news()
    if news:
        main_news, other_news = news
        root = tk.Tk()
        root.title("News Headlines")
        root.geometry("500x150")
        if main_news is None:
            main_news = "No news from US today"
        else:
            main_news = f"India: {main_news}"
        main_news_label = tk.Label(root, text=main_news, font=("Arial", 14), wraplength=450, justify="center")
        main_news_label.pack(pady=10)
        other_news_label = tk.Label(root, text="\n".join(other_news), font=("Arial", 12), wraplength=450, justify="left")
        other_news_label.pack(pady=10)
        root.mainloop()
    else:
        messagebox.showerror("Error", "Failed to fetch news")

def news_feature():
    root = tk.Tk()
    root.geometry("300x100")
    root.title("News Headlines")

    news_button = tk.Button(root, text="Show News", command=show_news)
    news_button.pack(pady=20)

    root.mainloop()
    



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("mummykori@gmail.com", "uormouiijwrnapez")
    server.sendmail("mummykori@gmail.com", to, content)
    server.close
# open chrome


def open_chrome():
    url = "https://www.google.com/"
    wb.get(chrome_path).open(url)


def assist():

    user_query = input('Enter your query: ')

    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    # soup = BeautifulSoup4(page.content, 'html.parser')
    result = soup.find(class_='uyUSCd').get_text()
    print(result)


if __name__ == "__main__":

    wishme()
    while True:

        query = takeCommand().lower()
        # logic for executing tasks based on query

        if "wikipedia" in query:
            speak('Searching in Wikipedia....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'open chrome' in query:
            open_chrome()

        elif 'news' in query:
            news_feature()

        if 'search' in query:
            speak("What should i search your grace")
            search = takeCommand().lower()
            wb.get(chrome_path).open_new_tab(search + '.com ')
        elif 'go for' in query:
            query = query.replace("go for", "")
            wb.open_new_tab(query)
            sleep(5)
        elif 'open gmail' in query:
            wb.open_new_tab("gmail.com")
            speak("Google Mail open now")
            sleep(5)
        elif 'play music' in query:
            music_dir = 'E:\Kori Aryan\VidMate\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Sir your code application is opened for you")

        elif "email to me" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "koriaryan@gmail.com"
                sendEmail(to, content)
                print("Sir your mail has been sent!!")
                speak("Sir your mail has been sent!!")
            except Exception as e:
                print(e)
                print(f"sorry sir, i couldn't able to send your email")
                speak(f"sorry sir, i couldn't able to send your email")

        elif "email to my brother" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "koriarsh@gmail.com"
                sendEmail(to, content)
                print("Sir your mail has been sent!!")
                speak("Sir your mail has been sent!!")
            except Exception as e:
                print(e)
                print(f"sorry sir, i couldn't able to send your email")
                speak(f"sorry sir, i couldn't able to send your email")

        elif "send an email to a person " in query:
            try:
                speak("what should i say ")
                content = takeCommand()
                speak("whom to should i send this mail")
                to = takeCommand(' ' + '@gmail.com')
                sendEmail(to, content)
            except Exception as e:
                print(e)
                print(f"sorry sir, i couldn't able to send your email")
                speak(f"sorry sir, i couldn't able to send your email")

        elif 'open vlc' in query:
            speak('Opening vlc my lord')
            location = '"C:/Program Files/VideoLAN/VLC/vlc.exe"'
            vlc = subprocess.Popen(location)

        elif 'close vlc' in query:
            speak('closing vlc your grace')
            vlc.terminate()
# jokes
        elif 'jokes' in query:
            speak(pyjokes.get_jokes())

        elif 'am i living' in query:
            voicespeed = 140
            engine.setProperty('rate', voicespeed)
            speak('Your Grace you live in my heart for eternity  i am just joking Sorry actually you live in nayagoan , chandigarh ')

        elif "you darling" in query:
            speak("i love you more Raksh Baby")

        elif "you honey" in query:
            speak("I love you more my Siyah baby ")

        elif "you baby" in query:
            speak('i love you more Aryan babe')


# logout,shutdown,restart
        elif 'logout' in query:
            speak("logging out in 5 seconds your grace ")
            sleep(5)
            os.system("shutdown -l")
        elif 'shutdown' in query:
            speak(" Shutting down in 5 seconds  your grace ")
            sleep(5)
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            speak("am Restarting your grace in 5 seconds  ")
            sleep(5)
            os.system("shutdown /r /t 1")
        elif 'full name' in query:
            speak(' Your Grace my full  name Zatch bell ')
        elif "do for me" in query:
            speak(" i am An AI , I was designed to assist you  with a variety of tasks,including answering questions and providing information on a wide range of topics.Is there anything in particular you would like to know or discuss from me ?")

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Zatch version  1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        elif "who made you" in query or "who created you" in query or "who discovered you" in query or 'who invented you' in query:
            speak("I was built by My lord Kori Aryan")
            print("I was built by My lord Kori Aryan")

        elif 'knowledge' in query:
            speak('Knowledge Mode Onn')

        # elif ' zatch ' or 'computer ' in query:
        #     res = client.query(query)
        #     output = next(res.results).text
        #     print(output)
        #     speak(output)

        elif 'news' in query:
         speak('Getting the latest news, please wait')
        news = get_news()
        if news is not None:
            print(news)
            speak(news)
        else:
         speak('Sorry, I could not fetch the news at the moment. Please try again later.')
