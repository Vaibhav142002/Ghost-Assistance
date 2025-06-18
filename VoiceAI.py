import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime as dt
import wikipedia #pip install wikipedia
import webbrowser
import os
# import smtplib
import random as r2
import sys
import wolframalpha

from threading import *

from tkinter import *
from tkinter import filedialog

from newgui import new_GUI
from credits import open_win


print('Please help me to choose video folder.')
video_folder = filedialog.askdirectory()
print('Please help me to choose music folder.')
music_folder = filedialog.askdirectory()

global img

win=Tk()
win.title('GHOST')
win.geometry('630x700+450+30')
win.resizable(FALSE,FALSE)
win.config(background="black")
img = PhotoImage(file = "ic_n.png")
win.iconphoto(False,img)

usertext=StringVar()
comtext=StringVar()

compframe=LabelFrame(
    win,
    text="GHOST ",
    font=('despairs',13,'bold'),
    highlightthickness=2,
    bd=3)
compframe.pack(fill='both',expand='yes')

left2=Message(
    compframe,
    textvariable=comtext,
    bg='gray',
    fg='black',
    justify='left'
    )

left2.config(font=('jetbrains mono',11,''),aspect=300)
left2.pack(fill='both',expand='yes')

userframe=LabelFrame(
    win,
    text="USER ",
    font=('despairs',13,'bold'),
    bd=3,
    highlightthickness=2,)
    
userframe.pack(fill='both',expand='yes')

left1=Message(
    userframe,
    textvariable=usertext,
    bg='black',
    fg='white',
    justify='right'
    )
left1.config(font=('jetbrains mono',13,''),aspect=300)
left1.pack(fill='both',expand='yes')




engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('497K74-LQ93WJ8229')

voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
comtext.set("""Hello! 
I am your Personal Assistant GHOST 

Click on Start button to give your Commands"""
            )
usertext.set(' ')

def printo(shan):
    global comtext
    comtext.set(shan)
    
 
def speak(audio):
    
    printo(audio+"\n")
    engine.setProperty('rate', 180)
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! " +name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon! " +name)   

    else:
        speak("Good Evening! " +name)
        
    speak("""Hello {} 
How can I help you?""".format(name))
    #speak("Click start speaking button to give Commands")
    usertext.set('''  Click 'ORDER!' button to give Commands''')


def Name():
    #It takes microphone input from the user and returns string output
    global r,source,audio,query,name
    name=" "
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is your name")
        printo("Please tell me Your name\n")
        printo("Listening...\n")
        #r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")    
        name = r.recognize_google(audio, language='en-in') #language = english india
        #print(f"User said: {name}\n") 
        

    except Exception as e:
        printo(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Name() 
        return None
    return name
    wishMe()

def Commands():
    global r,source,audio,query,usertext
    r = sr.Recognizer()
    r.energy_threshold=2500
    with sr.Microphone() as source:
        printo("Listening...\n")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        usertext.set("User said:"+query+"\n")

    except Exception as e:
        # print(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Commands() 
        return query
    return query

def Comands():
    global r,source,audio,query,usertext
    r = sr.Recognizer()
    r.energy_threshold=2500
    with sr.Microphone() as source:
        printo("Listening...\n")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")
        query = r.recognize_google(audio, language='mr-in')
        usertext.set("User said:"+query+"\n")

    except Exception as e:
        # print(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Commands() 
        return query
    return query

def srch_google():
    #speak("Seaching on Google.....\n")
    #printo("Seaching on Google.....\n")
    #audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        keywords=(text.split(" "))
        printo(keywords)
        del keywords[0]
        del keywords[0]
        printo(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        printo("You said : {}\n".format(keyword))
        url='https://www.google.co.in/search?q='
        search_url=f'https://www.google.co.in/search?q='+keyword
        speak('searching on google' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")

def srch_google_map():
    #speak(" Searching on Google Map.....")
    #printo("Searching on Google Map.....\n")
    #audio=r.listen(source)
    try:
        text2=r.recognize_google(audio)
        #text="google map Taj mahal"
        keywords=(text2.split(" "))
        print(keywords)
        del keywords[0]
        del keywords[0]
        #del keywords[0]
        print(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        print("You said : {}\n".format(keyword))
        #url='https://www.google.com/maps/place/?'
        search_url=f'http://maps.google.com/?q='+keyword
        speak('searching on google map' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")


def search_yt():
    #speak("searching on youtube.....\n")
    #printo("searching on youtube.....\n")
    try:
        text=r.recognize_google(audio)
        key=(text.split(" "))
        #print(keywords)
        del key[0]
        del key[0]
        #print(keywords)
        
        def lis(s):
            str1=" "
            new=str1.join(s)
            return new
    
        key=lis(key)

        print("You said : {}".format(key))
        url='http://www.youtube.com/results?search_query='
        search_url=f'http://www.youtube.com/results?search_query='+key
        speak('searching on youtube ' +" "+ key)
        webbrowser.open(search_url)
    except:
        print("Can't recognize")

def mainfn():
    global query
    if __name__ == "__main__":
        Name()
        wishMe()
    # while True: #while use kiya taki vo jabtak command nahi samjhe tabtak bar bar chale say that again vala
    # if 1:
    
def reco():   
    query = Commands().lower()
    # query = 'pubg'
    print(query)
    # Logic for executing tasks based on query
    
    if 'search google' in query or "search on google"  in query:
        srch_google()

    elif 'search youtube' in query:
            search_yt()

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        printo(results+"\n")
        speak(results)

    elif 'open youtube' in query:
        speak("opening youtube ")
        url='http://www.youtube.com/results?search_query='
        webbrowser.open(url)

    elif 'open calculator' in query or 'calculate' in query:
        speak('Opening calculator')
        os.system("calc")

    # elif 'open calendar' in query:
    #     speak('Opening Calendar')
    #     os.system("cali")

    elif 'news' in query or 'live news' in query:
        speak('Showing news')
        webbrowser.open("https://www.google.com/search?q=live+news+marathi&rlz=1C1FHFK_enIN1029IN1029&sxsrf=APwXEdfPMGCzLNibB_UhuKPehNfcC1QohA%3A1682143174801&ei=xndDZJq2MOnXseMP5paHgAI&oq=live+news+marat&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgsIABCABBCxAxCDATIKCAAQgAQQAhDLATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEMsBOgoIABBHENYEELADOg0IABCKBRCxAxCDARBDOggIABCABBCxA0oECEEYAFDvB1jUZmDscWgFcAF4AIABlQGIAYgGkgEDMC42mAEAoAEByAEIwAEB&sclient=gws-wiz-serp")

    elif 'google map' in query:
        srch_google_map()

    elif 'open google' in query:
        speak('opening google')
        webbrowser.open("google.com")

    elif 'go offline' in query:
        speak('ok '+name)
        quit()
        win.destroy()

    elif 'shutdown' in query:
        #self.compText.set('okay')
        speak('okay')
        os.system('shutdown -s')


    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(r2.choice(stMsgs))
        
    elif 'play music' in query:
        print(music_folder)
        os.chdir(music_folder)
        music = os.listdir()
        # print(music)
        random_music = r2.choice(music)
        print(random_music)
        os.startfile(random_music)
        speak('Okay, here is your music! Enjoy!')

    elif 'play video' in query:
            os.chdir(video_folder)
            video = os.listdir()
            random_video = r2.choice(video)
            os.startfile(random_video)
            speak('Okay, here is your video! Enjoy!')

    elif 'your name' in query:
        stMsgs = ['My name is GHOST', 'I am GHOST!', 'GHOST is here!', 'You can call me GHOST']
        speak(r2.choice(stMsgs))

    elif 'open file' in query or "open app" in query:
        speak('please locate your file')
        codePath = filedialog.askopenfilename()
        speak("Opening your ")
        os.startfile(codePath)
            
    elif 'open code' in query:
        speak("Locating your VS Code...")
        speak("Opening VS Code")
        os.system("Code")

    elif 'open notepad' in query:
        speak("Locating your Notepad...")
        speak("Opening Notepad")
        os.system("notepad")

    elif 'open word' in query or 'microsoft word' in query:
        speak("Locating your Word...")
        speak("Opening Microsoft Word")
        webbrowser.open('winword')

    elif 'weather' in query:
         webbrowser.open('https://www.google.com/search?q=weather&rlz=1C1FHFK_enIN1029IN1029&oq=weather&aqs=chrome..69i57j46i67i131i433i650j0i131i433i512j0i512j0i131i433i457i512j0i402i650l2j0i67i131i433i650j46i199i465i512j0i131i433i512.2392j1j4&sourceid=chrome&ie=UTF-8')
         speak('Displaying weather!')

    elif 'open files' in query:
        speak("Locating your This PC...")
        speak("Opening This PC")
        os.system("explorer")

    elif 'open c drive' in query:
        cdrive = "C:"
        speak("openning C Drive....")
        os.startfile(cdrive)

    elif 'open d drive' in query:
        ddrive = "D:"
        speak("openning C Drive....")
        os.startfile(ddrive)

    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak('okay')
        speak('Bye'+name+', have a good day.')
        win.destroy()
        quit()
          
    elif 'hello' in query:
        speak('Hello '+name)

    elif 'bye' in query:
        speak('Bye'+name+', have a good day.')
        win.destroy()
        quit()
        
        #elif 'calculate' or 'solve' or 'what' in query:

    elif 'type' in query or 'speech to text' in query or 'write' in query or "note" in query:
              speak('what should i write')
              printo('What should I write?')
              vb = Comands().lower()
              datas = str(vb)
            #   fl = open("demo.txt","w+")
              with open('demo.txt', 'w', encoding='utf-8') as f:
                f.write(datas)
                f.close
              speak('sir command executed.')
              os.startfile("demo.txt")
              
    
    # elif 'open this pc' in query:
    #     os.startfile(fileexplorer)

    elif 'college website' in query:
              speak('Showing colleges in kolhapur')
              webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=colleges+in+kolhapur')

    elif 'our college' in query or 'vvit website' in query:
              speak('Opening VVIT website')
              webbrowser.open('https://vvitpal.in/')

    elif 'download games' in query:
              speak("Opening games website")
              webbrowser.open('https://thepcgames.net/')

    elif 'download movies' in query:
              speak("Opening Movies website")
              webbrowser.open('https://moviesmod.net.in/')

    else:
        query = query
        try:
            speak('Searching in API...')
            res = client.query(query)
            results = next(res.results).text
            speak('API says - ')
            speak('please wait.')
            speak(results)
                
        except Exception as e:
                #print(e)
            speak("sorry sir. i can't recognize your command maybe google can handle this should i open google for you?")
            ans=Commands()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                webbrowser.open('www.google.com')
            elif 'no' in str(ans) or 'nah' in str(ans):
                speak("ok disconnecting")
                sys.exit()
            else:
                speak("No respnse I am disconnecting...")
                sys.exit()

def exit():
    win.destroy()
    sys.exit()
    #pass

def start():
    Thread(target=mainfn).start()

def speakingbtn():
    Thread(target=reco).start()

# def stopp():
#     a = input("Enter...")

btn = Button(
    win, 
    text='START!', 
    font=('Dispence', 12, ''), 
    bg='black', 
    fg='white',
    borderwidth=5,
    command=start).pack(fill='x', expand='no')

btn1 = Button(
    win, 
    text='order!', 
    font=('Dispence', 12, ''), 
    bg='black', fg='white',
    borderwidth=5,
    command=speakingbtn).pack(fill='x', expand='no')

# btn5 = Button(
#     win, 
#     text='stop?', 
#     font=('Dispence', 12, ''), 
#     bg='black', 

#     fg='red',
#     borderwidth=5,
#     command=stopp
#     ).pack(fill='x', expand='no')


btn2 = Button(
    win, text='Need Help?', 
    font=('Dispence', 12, ''), 
    bg='black', fg='white',
    borderwidth=5,
    command=new_GUI).pack(fill='x', expand='no')

btn4 = Button(
    win, 
    text='CREDITS!', 
    font=('Dispence', 12, ''), 
    bg='black', 
    fg='white',
    borderwidth=5,
    command=open_win).pack(fill='x', expand='no')

btn3 = Button(
    win, 
    text='EXIT?', 
    font=('Dispence', 13, ''), 
    bg='black', 
    fg='red',
    borderwidth=5,
    command=win.destroy
    ).pack(fill='x', expand='no')


win.mainloop()
