import RPi.GPIO as GPIO
import pyttsx3
from subprocess import call
import sys

engine = pyttsx3.init()
voicerate = 170
engine.setProperty('rate', voicerate)
engine.setProperty('voice', 'english_rp+f4') 
channel_lst = [26, 22, 16, 6, 25]
GPIO.setmode(GPIO.BCM)

GPIO.setup(channel_lst, GPIO.IN, pull_up_down=GPIO.PUD_UP)

engine.say('Welcome to the Artificial Vision System For Blinds')
engine.say('Please Press 1 for Object detection')
engine.say('Press 2 for Currency recognition')
engine.say('Press 3 to convert text into speech')
engine.say('And Press 4 to turn off the system')
engine.runAndWait()

def object_detection(channel):
    engine.say('Starting the object recognition. Please Wait!')
    engine.runAndWait()
    call(['python3', '/home/pi/Desktop/Artificial_Vision_System_for_Blinds/object_recognition.py'])

def currency_recognition(channel):
    engine.say('Starting the currency recognition')
    engine.say('Please press 2 to capture the image')
    engine.runAndWait()
    call(['python3', '/home/pi/Desktop/Artificial_Vision_System_for_Blinds/currency_recogniton/currency_recognition.py'])
   
def text_to_speech(channel):
	engine.say('This utility will convert text into speech')
	engine.say('Please press C to exit the system')
	engine.runAndWait()
	call(['python3', '/home/pi/Desktop/text_to_speech/text_to_speech/extract_text.py'])
	 
def exit_system(channel):
    engine.say('Closing the program. Good bye!')
    engine.runAndWait()
    call('sudo shutdown', shell=True)


GPIO.add_event_detect(25, GPIO.RISING, callback=object_detection)
GPIO.add_event_detect(6, GPIO.RISING, callback=currency_recognition)
GPIO.add_event_detect(16, GPIO.RISING, callback=text_to_speech)
GPIO.add_event_detect(26, GPIO.RISING, callback=exit_system)

message = input("Press enter to quit\n\n")
GPIO.cleanup()

