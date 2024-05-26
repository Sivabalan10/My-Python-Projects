import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Withdrawel

def withdrawel():
    speak("You   choose    cash    withdrawel")
    speak("Enter     your      amount")
    print("Enter Amount")
    amo1 = int(input(">>"))
    # formula

    print("""Do you need Receipt
           YES-->press - 1 
           NO -->press - 2 """)
    che1 = int(input(">>"))
    if che1 == 1:
        # Receipt formula
        print("")
    else:
        print("")

    speak("please    wait.....   your    transaction   is     being    processed")
    print("please wait your transaction is being processed...")

    # insufficient balance using comparing with main by if else statement.
    # receipt and successfully credited message.


withdrawel()


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# debit
def debit():
    speak("You           choose       debit")
    speak("Enter          the           amount")
    print("Enter amount")
    amo2 = int(input(">>"))

    # formula

    print("""Do you need Receipt
               YES-->press - 1 
               NO -->press - 2 """)
    che2 = int(input(">>"))
    if che2 == 1:
        # Receipt formula
        print("")
    else:
        print("")

    speak("successfully       money        added        in       your       account...")
    # formula to add money in main and return a receipt


debit()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


