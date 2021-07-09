from time import sleep
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


speak("Hello ,I am ROSA...Welcome to our Project.Now you can start talking")



def listen():
    recog = Recognizer()
    mic = Microphone()

    with mic:
        recog.adjust_for_ambient_noise(mic, duration=2)

        print("START TALKING")
        #sleep(2)
        audio = recog.record(mic, 3)

    try:
        recognized = recog.recognize_google(audio)
        print("YOU SAID: ", recognized)
        sleep(5)

    except RequestError as exc:
        print(exc)

    except UnknownValueError:
        print("UNABLE TO RECOGNIZE !!!")
        sleep(5)

def foo():
    while True:
        print('ARE YOU TALKING ?')
        sleep(5)
        print('YOU SAID: No')
        sleep(2)
        print('Okay,thank you!')
        sleep(100)

listen()
foo()


