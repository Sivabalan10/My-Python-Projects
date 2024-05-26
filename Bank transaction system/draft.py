import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def create():
    speak(
        "If            you           want           to            create            a            new            account            plz   fill the  details....")
    print("Enter name")
    name = input(">>")
    while True:
        print("Enter 4-Digit pin")
        pin = int(input(">>"))
        a = str(pin)
        l = len(a)
        int(l)
        if l == 4:
            print("Successfully created")
            break
        else:
            print("Incorrect !")
            speak("Incorrect     pin")
            continue

    f = open("pin.txt","a")
    f.write(name)
    f.write("\n")
    f.write(a)
    f.close()




create()
