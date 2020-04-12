import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from pynput.keyboard import Key, Controller
keyboard_press=Controller()
lst_what_doing=['I am trying to go on moon, but someone has stolen the conductor of my spaceship.','I am waiting for your next question.','I was sleeping, but now I am ready to help you.']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
lst1=[]
lst2=[]
lst3=[]
city=""

global file_con_name
global text_to_write
global text_to_write2
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello! Good Morning...")

    elif hour>=12 and hour<13:
        speak("Hello! Good noon...")   

    elif hour>=13 and hour<19:
        speak("Hello! Good Afternoon...")
    else:
        speak("Hello! Good Evening...")

    speak("How may I assist you ?")
   

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.non_speaking_duration = 1
      
        audio = r.listen(source,timeout=None, phrase_time_limit=None)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(query)
    except Exception:
        #print(e)  
        speak("I'm unable to understand, Please say that again.")
        start_ass()
        return str(0)
        
    return query
your_password=mails.pass_code['pass_s']
your_email=mails.your_mail['e_mail']

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(your_email,your_password)
    server.sendmail(your_password, to, content)
    server.close()

def hotword():
    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.non_speaking_duration = 1
            audio = r.listen(source,timeout=None,phrase_time_limit=None)
            if audio:
                query2 = r.recognize_google(audio,language='en-IN')
                if query2:
                    print(query2)
                else:
                    return str(0)
            else:
                start_ass()
        return query2
    except Exception as e:
        print(e)
        hotword().lower()
def start_ass(z=0):
   
    k=z
    try:
        query2=hotword().lower()
    except Exception as e:
        query2=hotword().lower()
    if "lucy" in query2 or "hey lucy" in query2:
        
        if(k==0):
            wishMe()
            z=5
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            start_ass()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"The time is {strTime}")
            start_ass()
        
        elif 'created you' in query or 'made you' in query:
            speak("I am created by group of people, who studies in Lovely Professional University.")
            start_ass()

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            start_ass()

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
            start_ass()
            

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            start_ass()

        elif 'video song on youtube' in query or 'video on youtube' in query:
            speak("opening youtube on Microsoft edge browser.")
            speak("Getting the latest video song...")
            speak("Here I have got a latest video on youtube...")
            webbrowser.open("youtu.be/PV4LMYstfnI")
            start_ass()
            
        elif 'music' in query:
            ran=random.randint(0,100)
            music_dir2 = r'E:\music'
            songs = os.listdir(music_dir2)
            speak("Playing music on Groove...")
            os.startfile(os.path.join(music_dir2, songs[ran]))
            start_ass()
            

        elif 'video' in query or 'a video' in query or 'a video from my device' in query:
            ran2=random.randint(0,26)
            music_dir=r"C:\\Users\\RESTART\\Videos"
            songs = os.listdir(music_dir)
            speak("Opening video...")
            os.startfile(os.path.join(music_dir, songs[ran2]))
            start_ass()


        

        elif 'gaana' in query or 'on gaana' in query or 'song on gaana' in query:
            if 'song' in query or 'the' in query:
                query=query.replace("the ","")
                query=query.replace("song ","")
            lst1=query[5:-9]
            lst1=lst1.replace(" ","-")
            speak("Here I have got different "+query[5:-9]+" song. Please select the song of your choice from the browser.")
            web_add="https://gaana.com/search/"+lst1
            webbrowser.open(web_add)
            start_ass()


        elif 'shutdown' in query:
            speak("Are you sure you want to shutdown your PC.")
            query2=takeCommand().lower()
            if 'yes' in query2:
                speak("Shutting down your PC.")
                os.system("shutdown /s /t 1")
            else:
                speak("Ok, PC will remain Open.")
                start_ass()

        elif 'restart' in query:
            speak("Are you sure you want to restart your PC.")
            query2=takeCommand().lower()
            if 'yes' in query2:
                speak("Restarting your PC...")
                os.system("shutdown /r /t 1")
            else:
                speak("Ok, PC will remain Open.")
                start_ass()

        elif 'news' in query:
            speak("Here are some category.")
            speak("Business")
            print("1. Business")
            speak("Entertainment")
            print("2. Entertainment")
            speak("Health")
            print("3. Health")
            speak("Science")
            print("4. Science")
            speak("Sports")
            print("5. Sports")
            speak("Technology")
            print("6. Technology")
            get_cat=takeCommand().lower()
            if 'business' in get_cat:
                catg="business"
            elif 'entertainment' in get_cat:
                catg="entertainment"
            elif 'health' in get_cat:
                catg="health"
            elif 'science' in get_cat:
                catg="science"
            elif 'sports' in get_cat:
                catg="sports"
            elif 'technology' in get_cat:
                catg="technology"
            else:
                catg=""
            if catg=="":
                url="https://newsapi.org/v2/top-headlines?country=in&apiKey=4b7f6f7d4b0d492e9bbb9bb107708a65"
            else:
                url="https://newsapi.org/v2/top-headlines?country=in&category="+catg+"&apiKey=4b7f6f7d4b0d492e9bbb9bb107708a65"
            news_str=requests.get(url).text
            news_dict=json.loads(news_str)
            content=news_dict['articles']
            speak("Here is latest news heading...")
            for at in content:
                print(at['title'].replace("-","from"))
                speak(at['title'].replace("-","from"))
                print(at['description'])
                speak(at['description'])
                break
            start_ass()
        
        

            
           
        
        
        elif 'email' in query or 'mail' in query:
            try:
                speak("Please say the name to whome you want to send the mail.")
                mail_name=takeCommand().lower()
                speak("What should I say?")
                content = takeCommand()
                to = mails.mail[mail_name]    
                sendEmail(to, content)
                speak("Email has been sent!")
                start_ass()
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
                start_ass()

        elif 'stop' in query or 'close' in query or 'cancel' in query:
            speak("GoodBye ! See you later.")
        

        else:
            if "0" not in query:
                speak("Searching on google...")
                #query = query.replace(query, "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
                    query=""
                    start_ass()
                except Exception as e:
                    start_ass()


    
    elif "lucy" not in query2:
        start_ass()
    else:
        if "0" in query2:
            start_ass()



if __name__ == "__main__": 
    start_ass()
    
        
