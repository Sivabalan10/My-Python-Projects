import datetime
import pyttsx3
import wikipedia
import speech_recognition as sr
import bs4

# Audio function


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def welcome():
    hour = int(datetime.datetime.now().hour)
    print("📶")
    if hour >= 12 and hour <= 16:
        print("Good  afternoon  sir.. ")
        speak("Good  afternoon  sir.. ")
        speak("i  am   avis , i   am   here   to  help  u  madam,")
    elif hour > 0 and hour < 12:
        print("Good  morning  sir...")
        speak("Good  morning  sir...")
        speak("i  am   avis , i   am   here   to  help  u  madam,")
    elif hour > 16 and hour <= 20:
        print("Good evening sir...")
        speak("Good evening sir...")
        speak("i  am   avis , i   am   here   to  help  u  madam,")
    else:
        speak("Hi sir, please    do    your    work    quickly   and go to sleep  sir, ")
        print("Go to sleep sir...")


# offline input
def takecommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source, 30, 3)
            try:
                me = r.recognize_google(audio)
                print("You said {}".format(me))

            except:
                print("Can't reach you!")

            me = me.lower()
            if "tgfdrsd" in me:
                print("")

            elif "wikipedia" in me:
                try:
                    speak("please  Wait   sir . Searching  in  wikipedia.")
                    me = me.replace("wikipedia", "")
                    results = wikipedia.summary(me, sentences=2)
                    speak("In  wikipedia")
                    print(results)
                    speak(results)

                except Exception as e:
                    print("WARNING: You are not connected in internet.")
                    speak("sir,      I think    you  are  not   connected   in  internet")

            elif "google" in me:
                speak("Searching please wait sir,")

                me = me.replace("google", "")
                try:
                    from googlesearch import search

                    query = me

                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                    speak("These   are   the   website   i   found    in  google  sir,")

                except ImportError:
                    print("No module found")
                except Exception as e:
                    speak("Internet connection  failed sir.")
                    print("Network error!")


            elif "hi" in me:
                speak("Hi sir")
            elif "how are you" in me:
                speak("Fine    sir. thank  u  for   caring   me  sir.")
            elif "ok" in me:
                speak("Ok sir")
            elif "thank" in me:
                speak("No  mention  sir")

                # HEART

            elif "my music" in me:
                speak("Just enjoy the vibe and work sir,")
                import os

                os.startfile("D:\Private\Workoutmusic.mp3")
            elif "sad" in me:
                speak("""Sir       . i want  to tell you   one   thing.   If    you    want   to   be  in  history, then  walk  on  the  others  path
                               if  you  want  to  make  a  history,  walk  on  your  own  path.""")

                print("""
                               If you want to be in history,then walk on the others path
                               if you want to make a history,walk on your own path.
                                                                   ~Siva""")
            elif "stress" in me:
                speak("""Sir       . i want  to tell you   one   thing.   If    you    want   to   be  in  history, then  walk  on  the  others  path
                                               if  you  want  to  make  a  history,  walk  on  your  own  path.""")
                print("""
                                               If you want to be in history,then walk on the others path
                                               if you want to make a history,walk on your own path.
                                                                                   """)
            elif "mistake" in me:
                speak(
                    " Sir   i   hope   you   never   do   a   mistake,  but   if   you   make   a   mistake.just  learn  from  it and  don't  make  it  happen  again.")
                print("Never do a mistake again."
                      "  learn from that.~TONY STARK :)")
                speak("and  i  need to  tell  you one  thing. You are  great  sir.")

                # Shortcuts
            elif "movie" in me:
                speak("Opening    movies   sir...")
                import os

                os.startfile("D:\Movies")
            elif "movies" in me:
                speak("Opening    movies   sir...")
                import os

                os.startfile("D:\Movies")
            elif "private" in me:
                speak("Opening   sir..")
                import os

                os.startfile("D:\Private")
            elif "time" in me:
                time = datetime.datetime.now().strftime("%H:%M")
                speak("The time  is")
                speak(time)

            elif "google" in me:
                speak(
                    "sir,  don't use   chrome  sir. because it consumes lot of ram  in   your   pc.i   opening   you   a  microsoft edge.")
                import os

                os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            elif "youtube" in me:
                speak(
                    "sir,  don't use   chrome  sir. because it consumes lot of ram  in   your   pc.i   opening   you   a  microsoft edge.")
                import os

                os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            elif "chrome" in me:
                speak(
                    "sir,  don't use   chrome  sir. because it consumes lot of ram  in   your   pc.i   opening   you   a  microsoft edge.")
                import os

                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            elif "pycharm" in me:
                speak("Opening your  project   sir,")
                import os

                os.startfile("C:\Pycharm\PyCharm Community Edition 2022.1.3\\bin\pycharm64.exe")
            elif "project" in me:
                speak("Opening your  project   sir,")
                import os

                os.startfile("C:\Pycharm\PyCharm Community Edition 2022.1.3\\bin\pycharm64.exe")
            elif "you learn" in me:
                f = open("brain.txt")
                var = f.read()
                speak("I  have   learned   new    things    from    the    user, For   example ......")
                speak(var)
                speak(
                    "these     are    things   i  learned.  i   find   the   solution  for   this ,  as   soon   as  possible")
            elif "tired" in me:
                speak("Then go to   sleep   sir")
            elif "wrong" in me:
                speak("Sir    i   am  perfectly  alright.")
            elif "idiot" in me:
                speak("If    i    do   any mistake,  i'm  sorry   sir.")
            elif "angry" in me:
                speak("If    i    do   any mistake,  i'm  sorry   sir.")
            elif "sundaram" in me:
                speak(
                    "Sundaram    is   your   mother.  She    is   very    intelligent,  that's  all   i   know   about   your  mother")
                print("Sundaram is very intelligent  person.")
            elif "your god" in me:
                speak("My   god   is  siva    sir.  he   is   my   inspiration")
            elif "vidhya" in me:
                speak("vidhya   is   your   sister.  she  is  busy   at   work.  that's  what i know  about  vidhya.")
            elif "modif" in me:
                speak("You  cannot   do  that.  i   never   allow   you.")
            elif "version" in me:
                speak("i  am  avis,  version  0.1")
            elif "girlfriend" in me:
                speak("i   follow  my   goals,   not  girls.  don't  ask  me  again  that")
            elif "hold" in me:
                speak("i'm  wait  sir.")
                print("Holding...")

                # SHut  down
            elif "system of" in me:
                speak(" system      shutting     down")
                print("AVIS: SYSTEM TURNED OFF!......")
                exit()
            elif "shutdown" in me:
                speak(" system      shutting     down")
                print("AVIS: SYSTEM TURNED OFF!......")
                exit()

                # ELSE
            else:
                speak(
                    "i don't   know   what   to tell        but   i   am   try   to       find     the   solution  for  this")


    except Exception as e:
        speak("Internet connection failed..")
        exit()



if __name__ == '__main__':
    welcome()
    while True:
        takecommand()
