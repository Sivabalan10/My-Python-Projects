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


a = input("Enter a number1:")
b = input("Enter a number2:")
try:
    a = int(a)
    b = int(b)
    print(a+b)
except Exception:
    print("it is a string:")