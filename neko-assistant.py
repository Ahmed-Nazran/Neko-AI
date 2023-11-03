import importlib
import subprocess

required_modules = [
    "DateTime",
    "pywhatkit",
    "wikipedia",
    "pyjokes",
    "random",
    "webbrowser",
    "pyttsx3",
    "subprocess",
    "os",
    "playsound",
    "time",
    "googletrans",
    "smtplib",
    "pyautogui",
    "requests",
    "math",
    "socket",
    "cv2",
    "winsound",
    "sys",
    "pyaudio",
    "newsapi",
    "psutil",
    "string",
    "speech_recognition",
    "screen_brightness_control",
    "PyPDF2",
    "calendar"
]

def install_missing_modules(modules):
    for module in modules:
        try:
            importlib.import_module(module)
        except ImportError:
            print(f"{module} not found. Installing {module}...")
            subprocess.check_call(["pip", "install", module])

# Check and install missing modules
install_missing_modules(required_modules)


import datetime                         # pip install DateTime
import pywhatkit                        # pip install pywhatkit
import wikipedia                        # pip install wikipedia
import pyjokes                          # pip install pyjokes
import random                           # pip install random
import webbrowser                       # pip install webbrowser
import pyttsx3                          # pip install pyttsx3
import subprocess                       # pip install subprocess.run
import os                               # pip install os-sys
import playsound                        # pip install playsound
import time                             # pip install time
import googletrans                      # pip install googletrans
import smtplib                          # pip install secure-smtplib
import pyautogui                        # pip install PyAutoGUI
import requests                         # pip install requests
import math                             # pip install math
import socket                           # pip install sockets
import cv2                              # pip install opencv-python
import winsound                         # pip install wav-win-sound
import sys                              # pip install os-sys
import pyaudio                          # pip install PyAudio
from newsapi import NewsApiClient       # pip install news-api
import psutil                           # pip install opencv-python
import string                           # pip install strings
import speech_recognition as sr         # pip install SpeechRecognition
import screen_brightness_control as pct # pip install screen-brightness-control
import PyPDF2                           # pip install PyPDF2
import calendar                         # pip install calendra


print('\n                                    Welcome to Neko AI\n')


def say(text):

    neko = pyttsx3.init()
    voices = neko.getProperty('voices')

    neko.setProperty('voice', voices[2].id)
    neko.setProperty('volume',+150)
    neko.setProperty('rate', +150)
    
    neko.say(text)
    neko.runAndWait()


def take_command():

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("listening")
		r.pause_threshold = 2
		audio = r.listen(source, timeout=4, phrase_time_limit=7)

	try:
		print("recognizing..\n")
		command = r.recognize_google(audio, language='en-in')
		print(f"you said   {command}\n")

	except Exception as e:
		print(e)
		return "none"

	command = command.lower()
	return command


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print("Good Morning Sir !")
        say("Good Morning Sir !")
    elif hour>= 12 and hour<18:
        print("Good Afternoon Sir !") 
        say("Good Afternoon Sir !") 
    else:
        print("Good Evening Sir !")
        say("Good Evening Sir !")


def alarm():
    hn = datetime.datetime.now().hour
    mn = datetime.datetime.now().minute
    sn = datetime.datetime.now().second
    print(f'Current time is {hn}:{mn}:{sn}')
    hour = int(input('Set Alarm hour: '))
    min = int(input('Set Alarm minute: '))
    apm = str(input('Set am or pm: '))
    if apm.lower() == 'pm':
        hour = hour + 12
    while True:
        print(f'Waiting for {hour}:{min}...')
        time.sleep(5)
        if hour == datetime.datetime.now().hour and min == datetime.datetime.now().minute:
            say('Wake Up!')
            print(f'Its {hour}:{min}{apm}')
            os.startfile("D:\PRO NZ\PRO NZ\python\mega_pro\m_alarm.mp3") 
            print("sir please wake up")
            say("sir please wake up")
            stop = take_command()
            if 'stop' in stop:
                os.system("taskkill /im wmplayer.exe")#"%ProgramFiles%\Windows Media Player\wmplayer.exe" /prefetch:1          
                break
            else:
                print("Sir please wake up!\n")


def trans():
    while True:
        print('---------Neko Language Translator-------\n') 
        text = input('Your text: ')
        trans  = input('Translate into: ')
        translator = googletrans.Translator()
        translated = translator.translate(text,dest=trans)
        print('Translated: ',translated.text)
        say(translated.text)
        break


def mail():
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("neko@gmail.com", "************")
        print('from: neko@gmail.com')
        rec = input('to: ')
        message = input('Your message: ')
        s.sendmail("neko@gmail.com", rec, message)
        print('Succesfully sended')
        say('succesfully sended')
    except:
        print('Sorry cannot send the mail :(')
        say('sorry i cannot send the mail')
        s.quit()


def whatsapp():
    try:
        wrec = input('Reciver Phone number: ')
        wmessage = input('Your message: ')
        wsendh = input('Set hour you want to send the message: ')
        wsendm = input('Set minute you want to send the message: ')
        pywhatkit.sendwhatmsg(wrec,wmessage,wsendh,wsendm)
        print('Succesfully Sended')
        say('succesfully sended')
    except:
        print('sorry i cannot send the message')
        say('sorry i cannot send the message')


def tic():
    player = 1
    Win = 1
    Draw = -1
    Running = 0
    Stop = 1
    Game = Running
    Mark = 'X'
    b = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    class color:
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YEL = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
    def Board():
        print(" {}| {} | {} ".format(b[1],b[2],b[3]))
        print("__|___|__")    
        print(" {}| {} | {} " .format(b[4],b[5],b[6]))
        print("__|___|__")    
        print(" {}| {} | {} ".format(b[7],b[8],b[9]))
        print("  |   |   ")
    def CheckPosition(x):
        if(b[x] == ' '):
            return True
        else:
            return False
    def CheckWin():
        global Game
        if(b[1] == b[2] and b[2] == b[3] and b[1] != ' '):
            Game = Win
        elif(b[4] == b[5] and b[5] == b[6] and b[4] != ' '):
            Game = Win
        elif(b[7] == b[8] and b[8] == b[9] and b[7] != ' '):
            Game = Win
        elif(b[1] == b[4] and b[4] == b[7] and b[1] != ' '):
            Game = Win
        elif(b[2] == b[5] and b[5] == b[8] and b[2] != ' '):
            Game = Win
        elif(b[3] == b[6] and b[6] == b[9] and b[3] != ' '):
            Game=Win
        elif(b[1] == b[5] and b[5] == b[9] and b[5] != ' '):
            Game = Win
        elif(b[3] == b[5] and b[5] == b[7] and b[5] != ' '):
            Game=Win
        elif(b[1]!=' ' and b[2]!=' ' and b[3]!=' ' and b[4]!=' ' and b[5]!=' ' and b[6]!=' ' and b[7]!=' ' and b[8]!=' ' and b[9]!=' '):    
            Game=Draw
        else:
            Game=Running
    print(color.BLUE +"Tic-Tac-Toe Game Created by Nazran"+ color.ENDC)
    print(color.CYAN+"Player 1 [X] --- Player 2 [O]\n"+color.ENDC)
    while(Game == Running):
        Board()
        if(player % 2 != 0):
            print(color.RED+"Player 1's chance")
            Mark = 'X'
            choice = int(input("Enter the position between [1-9] where you want to mark : "))

        else:
            print(color.GREEN+"Player 2's chance")
            Mark = 'O'
        choice = random.choice([1,2,3,4,5,6,7,8,9,0])
        if(CheckPosition(choice)):
            b[choice] = Mark
            player+=1
            CheckWin()
        else:
            choice = int(input("Please Enter the position between [1-9] where you want to mark : "))
    Board()
    if(Game==Draw):
        print(color.YEL+"Game Draw"+color.ENDC)
    elif(Game==Win):
        player-=1
        if(player%2!=0):
            print(color.YEL+"Player 1 Won"+color.ENDC)
        else:
            print(color.YEL+"Player 2 Won"+color.ENDC)


def takeScreenshot():
    time.sleep(2)
    SS = pyautogui.screenshot()
    ss_save = input('Enter image name: ')
    SS.save(ss_save+'.png')
    print(f'{ss_save}.png screenshot saved')
    say(f'{ss_save}.png screenshot saved')


def generate_random_password():
    abcd = list(string.ascii_letters)
    nums = list(string.digits)
    special_chars = list("!@#$%^&*()")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    try:
        length = int(input("Enter password length: "))
        abcd_count = int(input("Enter alphabets count in password: "))
        nums_count = int(input("Enter digits count in password: "))
        special_chars_count = int(input("Enter special characters count in password: "))
        characters_count = abcd_count + nums_count + special_chars_count
        if characters_count > length:
            print("Characters total count is greater than the password length")
            say("Characters total count is greater than the password length")
            return
        password = []
        for i in range(abcd_count):
            password.append(random.choice(abcd))
        for i in range(nums_count):
            password.append(random.choice(nums))
        for i in range(special_chars_count):
            password.append(random.choice(special_chars))
        if characters_count < length:
            random.shuffle(characters)
            for i in range(length - characters_count):
                password.append(random.choice(characters))
        random.shuffle(password)
        print("".join(password))
        say("password created please cheak the password")
    except:
        print("something went wrong :( please try again!")
        say("something went wrong :( please try again!")


def routine2():
    datetimenow = datetime.datetime.now()
    timex = int(datetimenow.strftime("%H"))
    timeY = datetime.datetime.now().strftime('%I:%M %p')
    print(f"Current time is {timeY}")
    
    if timex >= 4 and timex <= 5:
        print("Fojor er Namaj")
        #say("sir you should go for Fojor er Namaj")
    elif timex >= 13 and timex <= 15:
        print("Johor er Namaj")
        #say("sir you should go for Johor er Namaj")
    elif timex >= 16 and timex <= 17:
        print("Asore er Namaj")
        #say("sir you should go for Asor er Namaj")
    elif timex >= 18 and timex <= 19:
        print("Magrib er Namaj")
        #say("sir you should go for Magrib er Namaj")
    elif timex >= 21 and timex <= 24:
        print("Esher Namaj")
        #say("sir you should go for Eshar Namaj")
    elif timex >= 1 and timex <= 3 or timex >= 6 and timex <= 8:
        print("Go to sleep")
        say("sir you should go to sleep")

    else:
        print("")


def routine1():
    datetimenow = datetime.datetime.now()
    


def bd():
    x = datetime.datetime.now()



def calcu():
    print(""" 
press -  
+ - Addition(x, y) 
- - subtraction(x,y) 
* -multiplication(x,y) 
/ - division(x, y) 
** - exponent(x, y) 
tan - tan(x, y) 
sin - sin(x) 
cos - cos(x) 
! - factorial(x) 
log - log(x) 
x - exit
""") 
    while True:
        try:
            o = input(">>>") 
            if o == "+": 
                x = int(input("1st number: ")) 
                y = int(input("2nd number: "))
                print(x + y)
                say(x+y)
            elif o == "-": 
                x = int(input('1st number: ')) 
                y = int(input('2nd number: ')) 
                print(x-y) 
                say(x-y)
            elif o == "*": 
                x = int(input('1st number: ')) 
                y = int(input('2nd number: ')) 
                print(x*y)
                say(x*y) 
            elif o == "/": 
                x = int(input('1st number: ')) 
                y = int(input('2nd number: ')) 
                print(x/y)
                say(x/y) 
            elif o == "**": 
                x = int(input('1st number: ')) 
                y = int(input('2nd number: ')) 
                print(x**y)
                say(x**y) 
            elif o == "tan": 
                x = int(input('1st number: ')) 
                y = int(input('2nd number: ')) 
                z = math.tan(x)
                print(z)
                say(z)
            elif o == "sin": 
                x = int(input('>>')) 
                z = math.sin(x)
                print(z)
                say(z)
            elif o == "cos": 
                x = int(input('>>')) 
                z = math.cos(x)
                print(z)
                say(z)
            elif o == "!": 
                x = int(input('>>')) 
                z = math.factorial(x)
                print(z)
                say(z)
            elif o == "log": 
                x = int(input('>>'))
                z = math.log(x)
                print(z)
                say(z)
            elif o == "x":
                break
            else:
                print("Math_Error")
                say("Math_Error")
        except:
            print("Math_Error")
            say("Math_Error")


def onlinedownload():
    url = input('URL: ')
    save_file_name=input('File Name: ')
    ls=input('If Large file type(b) if small type(s): ')
    if ls=='b':
        r = requests.get(url, stream = True)
    if ls== 's':
        r = requests.get(url, allow_redirects=True)
    open(save_file_name, 'wb').write(r.content)
    print(f'{save_file_name}_Download_Complete!')
    say(f'{save_file_name} Download Complete!')


def pdf_reader():
    try:
        book=open()
        pdf_r=PyPDF2.PdfFileReader(book)
        ps=pdf_r.numPages
        print(ps)
        p=int(input())
        pa=pdf_r.getPage(p)
        text=pa.extractText()
        say(text)
    except:
        print('pdf_not_found')


def host():
    s=socket.socket()
    host=socket.gethostname()
    print("Server will start on host:",host)
    say("server will start on host ", host)
    port=1234
    s.bind((host,port))
    print("Server is bound successfully")
    say("server is bound succesfully")
    s.listen(1)
    conn,addr=s.accept()
    print(addr,"has connected")
    say(addr," has connected")
    while 1:
        message=input(str("You: "))
        message=message.encode()
        conn.send(message)
        incoming_message=conn.recv(1024)
        incoming_message=incoming_message.decode()
        print("Client: ",incoming_message)


def server():
    s=socket.socket()
    say("please enter host name")
    host=input(str("Please enter host name:"))
    port=1234
    try:
        s.connect((host,port))
        print("connected to server")
        say("connected to server")
    except:
        print("connection to server is failed : (")
        say("connection failed")
    while 1:
        incoming_message=s.recv(1024)
        incoming_message=incoming_message.decode()
        print("Server: ",incoming_message)
        message=input(str("You: "))
        message=message.encode()
        s.send(message)


def camera():
    try:
        camw = input("font camera or back camera: ")
        if camw == "back":
            video = cv2.VideoCapture(0)
            while True:
                isTrue,frame = video.read()
                cv2.imshow("Neko Camera",frame)
                key = cv2.waitKey(10)
                if key == ord('q'):
                    cv2.imwrite(f'{datetime.datetime.now()}.jpg',frame)
                    break
            video.release()
        elif camw == "font":
            cam = cv2.VideoCapture(1)
            while cam.isOpened():
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                for c in contours:
                    if cv2.contourArea(c) < 5000:
                        continue
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                if cv2.waitKey(10) == ord('q'):
                    cv2.imwrite('Z.jpg',frame1)
                    break
                cv2.imshow('Neko Cam', frame1)
        else:
            print('Please set camera')
    except:
        print('Unknown error occured')

   
def weather():
    city = "dhaka"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    print(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
    say(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")


def news():
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    topic = input("What topic you need the news about: ")
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        print(y["description"])
        bgnews = y["description"]
        trans = 'bn'
        translatorr = googletrans.Translator()
        translatedd = translatorr.translate(bgnews,dest=trans)
        print(translatedd.text)
        say(y["description"])


def remember():
    data = input(">> ")
    print("You Said me to remember  " + data)
    say("You Said me to remember  " + data)
    with open("data.txt", "a", encoding="utf-8") as r:
        print(data, file=r)


def rps():
    while True:
        p1 = str(input("Enter a choise- rock, paper, scissors:- "))
        p3 = ['rock', 'paper', 'scissors']
        p2 = random.choice(p3)
        print(f'neko: {p2}')
        if p1 == "rock" and p2  == "paper":
            print("oh I won...!")
        elif p1 == "rock" and p2 == "scissors":
            print('congrats you won!')
        if p1 == "paper" and p2  == "scissors":
            print("oh I won...")
        elif p1 == "paper" and p2 == "rock":
            print('congrats you won!')
        if p1 == "scissors" and p2  == "rock":
            print("oh I won")
        elif p1 == "scissors" and p2 == "paper":
            print('congrats you won!')
        elif p1 == "rock"and p2 == "rock":
            print("Tie!")
        elif p1 == "paper"and p2 == "paper":
            print("Tie!")
        elif p1 == "scissors"and p2 == "scissors":
            print("Tie!")
        else:
            print("-")
        play_again = input("Play again?\n")
        if play_again.lower() != "yes":
                break


def run_neko():

    command = take_command()
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('current time is '+ time)
        say('Current time is ' + time)

    elif 'date' in command:
        date = datetime.datetime.now()
        dateno = date.strftime("%x")
        print(f'Today is {dateno}')
        say(f'Today is {dateno}')

    elif 'browse' in command:
        brow_for = command.replace('browse','')
        webbrowser.open(brow_for)

    elif 'battery left' in command or 'battery we have' in command:
        battery = psutil.sensors_battery()
        percent = battery.percent
        mileft = int(battery.secsleft / 3600)
        minleft = int(battery.secsleft / 60 )
        hleft = int(minleft / 60)
        print(f"our system heve {percent}% battery")
        print(f"left {hleft} hours and {mileft} minutes")
        say(f"our system heve {percent}% battery")
        if percent >= 70:
            print("we have enough power")   
            say("we have enough power")   
        elif percent >= 30 and percent <=55:
            print("we should connect our system to charging point to charge our battery")
            say("we should connect our system to charging point to charge our battery")
        elif percent >=15 and percent <=30:
            print("we don't have enough power, please connect to charging")
            say("we don't have enough power, please connect to charging")
        elif percent <=15:
            print("The battery is very low, please connect to charging the system will shutdown soon!")
            say("The battery is very low, please connect to charging the system will shutdown soon!")
        else:
            print("")
    
    elif 'password' in command:
        generate_random_password()

    elif 'volume up' in command:
        pyautogui.press("volumeup")

    elif 'volume down' in command:
        pyautogui.press("volumedown")
        
    elif 'mute' in command:
        pyautogui.press("volumemute")

    elif 'call' in command:
        print("Sorry something went wrong can't call :(")
        say('sorry something went wrong cannot call')

    elif 'read' in command and 'pdf' in command:
        pdf_reader()

    elif 'search' in command:
        search_for = command.replace('search','')
        pywhatkit.search(search_for)
        print(f"Searching {search_for}")
        say(f"Searching {search_for}")

    elif 'what do you think about me' in command:
        iam = ['so good', 'so cute', 'not bad at all', 'so cool']
        am_i = random.choice(iam)
        print(f'You are {am_i}')
        say(f'You are {am_i}')

    elif 'what is' in command or 'who is' in command:
        pywhatkit.search(command)

    elif 'hi' in command or 'hello' in command:
        print('Hello sir! How can I help you?')
        say('Hello sir! How can I help you?')

    elif 'how are you' in command:
        feel = ['fine','great','good']
        feelr = random.choice(feel)
        print(f'I am {feelr}')
        say(f'I am {feelr}')

    elif 'good job' in command:
        print('Thanks! ^-^')
        say('Thanks!')

    elif 'thank' in command:
        print('my pleasure sir ^-^')
        say('my pleasure sir')

    elif 'play' in command:
        song = command.replace('play', '')
        say('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        say(info)

    elif 'join' and 'zoom' in command:
        if 'mamun sir' in command or 'english' in command:
            webbrowser.open("https://us02web.zoom.us/j/8768919309?pwd=ZFVreFZocm9vWVhCZmoxekJOSGh5QT09&fbclid=IwAR3eA_PBgw-apTKMZ1ABH03EKDYVzKiaOrWtXaCLp0ZDK2MwpeokS7XXVAI#success")
            print("Joining Mamun Sir's personal meeting room...")
            say("Joining english sir's personal meeting room")
        elif 'joshim sir' in command or 'math' in command:
            webbrowser.open('https://us04web.zoom.us/j/3702552016?pwd=Rm5Ic1lvd21ENVY3TW55N2pJM2tnZz09')
            print("Joining Joshim Uddin's personal meeting room...")
            say("Joining math sir's personal meeting room")
        elif 'isc' in command:
            webbrowser.open('https://zoom.us/j/94012944505?pwd=OHRPNkNia0ZBT2hKS2JWR3NHSHd1Zz09')
            print("Joining ISC zoom meeting room...")
            say("Joining isc zoom meeting room")
        else:
            print('zoom meeting not found')
            say('zoom meeting not found')

    elif 'more about weather' in command:
        webbrowser.open('https://weather.com/weather/today/')

    elif 'weather' in command:
        weather()

    elif 'code' in command:
        os.startfile('C:\\Users\Achin\AppData\Local\Programs\Microsoft VS Code\Code.exe')

    elif 'where is' in command:
        loc = command.replace('where is','')
        webbrowser.open(f'https://www.google.com/maps/place/{loc}/')

    elif 'my location' in command:
        webbrowser.open('https://www.ipaddress.my/')

    elif 'open' in command:
        if 'download' in command:
            os.startfile('C:\\download')
        elif 'messenger' in command:
            webbrowser.open('https://www.facebook.com/messages/')
        elif 'facebook' in command:
            webbrowser.open('https://www.facebook.com/')
        elif 'discord' in command:
            webbrowser.open('https://discord.com/')
        elif 'youtube' in command:
            webbrowser.open('https://www.youtube.com/')
        elif 'mail' in command:
            webbrowser.open('https://www.google.com/gmail/')
        elif 'git' in command:
            webbrowser.open('https://www.github.com')
        elif 'whatsapp' in command:
            webbrowser.open('https://www.whatsapp.com/')
        else:
            print('file not found!')
            say('file not found')

    elif 'close' in command and 'apps' in command:
        os.system("taskkill /f /im notepad.exe")
        os.system("taskkill /f /im winword.exe")
        os.system("taskkill /f /im excel.exe")
        os.system("taskkill /f /im powerpnt.exe")
        #os.system("taskkill /f /im msedge.exe.")
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im calc.exe")
        os.system("taskkill /f /im iexplore.exe")
        #os.system("taskkill /f /im powershell.exe")
        os.system("taskkill /f /im wordpad.exe")
        print("notepad,excel,powerpoint,chrome,calculator,internet explore,wordpad,word  closed")
#        say("notepad,excel,powerpoint,chrome,calculator,internet explore,wordpad,word  closed")

    elif 'set alarm' in command:
        alarm()

    elif 'remember' in command:
        remember()

    elif 'chat' in command:
        cask = input('Host or server: ')
        if cask =='Host':
            host()
        elif cask =='server':
            server()
        else:
            print('sorry_server_problem')
            say('sorry_server_problem')

    elif 'translate' in command:
        trans()

    elif 'send mail' in command:
        mail()

    elif 'calculat' in command:
        calcu()

    elif 'calendar' in command:
        x = datetime.datetime.now()
        m = int(x.strftime("%m"))
        y = int(x.strftime("%Y"))
        cal = calendar.month(y,m)
        print(cal)\

    elif 'send message' in command:
        print('The message will be send with WhatsApp')
        say('The message will be send with WhatsApp')
        whatsapp()

    elif "covid" in command:
        r = requests.get(
            'https://coronavirus-19-api.herokuapp.com/all').json()
        print(f'Confirmed Cases: {r["cases"]} \nDeaths: {r["deaths"]} \nRecovered {r["recovered"]}')
        say(f'Confirmed Cases: {r["cases"]} \nDeaths: {r["deaths"]} \nRecovered {r["recovered"]}')

    elif 'take screenshot' in command or 'take ss' in command:
        takeScreenshot()

    elif 'download' in command:
        onlinedownload()

    elif 'camera' in command or 'take photo' in command:
        camera()

    elif 'news' in command:
        news()

    elif 'shutdown system' in command:
        print("Shut down...")
        say("Shut down...")
        subprocess.call('shutdown / p /f')

    elif "happy birthday" in command:
        x = datetime.datetime.now()
        ddd = x.strftime("%d")
        mon = x.strftime("%m")
        if ddd == "17" and mon == "9":
            print("Oh! Thank you sir!! You remember that")
        elif "happy birthday" in command and ddd != "17" and mon != "9":
            print("ummm... Sorry, Today is not my Birth Day")
                 
    elif 'create' in command:
        if 'text file' in command:
            tfc_n = input('enter file name: ')
            with open(f'{tfc_n}.txt', 'w') as f:
                f.write(input('Enter Your Text: '))
            print(f'{tfc_n}.txt file created')
            say(f'{tfc_n}.txt file created')
        elif 'python file' in command:
            pfc_n = input('enter file name: ')
            with open(f'{pfc_n}.py', 'w') as f:
                f.write(input('Enter Your Text: '))
            print(f'{pfc_n}.py file created')
            say(f'{pfc_n}.py file created')
        elif 'html file' in command:
            hfc_n = input('enter file name: ')
            with open(f'{hfc_n}.html', 'w') as f:
                f.write(input('Enter Your Text: '))
            print(f'{hfc_n}.html file created')
            say(f'{hfc_n}.html file created')
        elif 'css file' in command:
            cfc_n = input('enter file name: ')
            with open(f'{cfc_n}.css', 'w') as f:
                f.write(input('Enter Your Text: '))
            print(f'{cfc_n}.css file created')
            say(f'{cfc_n}.css file created')
        elif 'js file' in command or 'javascript file' in command or 'java script file' in command:
            jfc_n = input('enter file name: ')
            with open(f'{jfc_n}.js', 'w') as f:
                f.write(input('Enter Your Text: '))
            print(f'{jfc_n}.js file created')
            say(f'{jfc_n}.js file created')
        elif 'batch file' in command:
            bfc_n = input('enter file name: ')
            with open(f'{bfc_n}.bat', 'w') as f:
                f.write(input('Enter Your Text: '))
            print(f'{bfc_n}.bat file created')
            say(f'{bfc_n}.bat file created')
        elif 'file' in command:
            f_n = input('enter file name with type: ')
            with open(f'{f_n}', 'w') as f:
                f.write(input('Enter Your Text: '))
            print(f'{f_n} file created')
            say(f'{f_n} file created')
        else:
            print("Sorry! I can't Create this file :(")
            say("sorry! I can't create this file")

    elif 'run' in command:
        if 'calculator' in command:
            subprocess.call('calc.exe')
            say("opening calculator app")
        elif 'cmd' in command:
            subprocess.call('cmd.exe')
            say("opening command promport")
        elif 'notepad' in command:
            subprocess.call('notepad.exe')
            say("opening notepad app")
        elif 'chrome' in command:
            os.startfile("C:\\Program Files\Google\Chrome\Application\chrome.exe")
            say("opening chrome app")
        elif 'microsoft edge' in command:
            os.startfile("C:\\Program Files\Microsoft\Edge\Application\msedge.exe") 
            say("opening microsoft edge app")       
        else:
            print('sorry I cannot open this app :(')
            say('sorry I cannot open this app')

    elif 'bored' in command or 'so boring' in command:
        print("um lets play a game!")
        say("um lets play a game!")
        want = input("want to play?\n")
        if want == 'yes' or want == 'ok':
            a = input("ok do you like to play rock, paper, scissors?\n")
            if a == 'yes' or a == 'ok':
                print("than lets play!")
                rps()                
            elif a == 'no':
                ask = input("umm.. want to play tic tac toe?\n")
                if ask == 'yes' or ask == 'ok':
                    tic()
        elif want == 'no':
            askk = input("umm.. want to here a song?\n")
            if askk == 'yes' or askk == 'ok':
                song = []
                print("playing song...")
            elif askk == 'no':
                print("")
        print("ummm.. you should go some where out!")

    elif 'what' in command and 'do' in command:
        routine1()
        routine2()

    elif 'brightness' in command:
        bri = pct.get_brightness()
        print(f"current brightness is {bri}")
        say(f"current brightness is {bri}")
        try:
            lvl = input("Enter brightness level: ")
            pct.set_brightness(lvl)
            say(f"brightness set to {lvl}")
        except:
            pass

    elif 'games' in command:
        if 'poki' in command:
            webbrowser.open('https://poki.com/en/g/we-become-what-we-behold')
        elif 'google' in command:
            webbrowser.open('https://www.google.com/search?q=google+doodle&oq=google+do&aqs=chrome.2.69i57j0i433i512l2j46i433i512j0i512j0i433i512j69i60l2.6514j1j7&sourceid=chrome&ie=UTF-8')
        else:
            print('game not found')
            say('game not found')

    elif 'joke' in command:
        print(pyjokes.get_joke())
        say(pyjokes.get_joke())

    elif 'who are you' in command or 'what are you' in command or 'who created you' in command:
        print('''
I am Neko your Personal Voice Assistant.
Creator Name: Ahmed Nazran
Created date: 17/9/2021 4:00pm''')
        say('I am neko your personal Desktop Assistant. Ahmed Nazran created me in 17 9 2021. ')

    elif 'exit' in command:
        print("Thanks for giving me your time")
        say("Thanks for giving me your time")
        exit()

    else:
        print('Sorry! I did not get it')
        say('sorry i did not get it')


while True:
    wishMe()
    routine2()
    break

while True:
    run_neko()
