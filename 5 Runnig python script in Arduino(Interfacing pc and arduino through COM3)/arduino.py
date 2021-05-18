import time

try:
    from pyfirmata import Arduino, util
    print("got it")
except:
    import pip
    pip.main(['install', 'pyfirmata'])
    from pyfirmata import Arduino, util
    print("installed it")

arduino = Arduino('COM3')
it = util.Iterator(arduino)

import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
talk = pyttsx3.init()
voices = talk.getProperty('voices')
talk.setProperty('voice', voices[1].id)

def talk_now(text):
    talk.say(text)
    talk.runAndWait()

def MyCommand():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            time.sleep(2)
            talk_now("I am waiting for your Command")
            listener.adjust_for_ambient_noise(source, duration= 1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        talk_now("I can not understand your command")
    print(command)
    return command


while True:
    what = MyCommand()
    if 'on' in what:
        arduino.digital[13].write(1)
        time.sleep(0.1)
        talk_now("ok, Light turned on")
    elif 'of' in what:
        arduino.digital[13].write(0)
        time.sleep(0.1)
        talk_now("ok, Light turned off")



