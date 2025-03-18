import pyttsx3
import pyautogui as pg

## set up in startup folder to automate the task to run py every time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
print("AUTO REFRESHING")
speak("AUTO REFRESHING IN  PROCESS....")


pg.hotkey('win','d')

for n in range(4):
    pg.click(x=950,y=500,button="right")
    pg.click( x=975 , y=560)


speak("AUTO  REFRESHING  COMPLETED  ")

exit()


