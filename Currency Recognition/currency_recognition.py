import os
import cv2
from utils import *
import subprocess
import numpy as np
import glob
import time
import RPi.GPIO as GPIO

pin = 22
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
start = time.time()

import pyttsx3
engine = pyttsx3.init()
voiceRate = 170
engine.setProperty('rate', voiceRate)
engine.setProperty('voice', 'english_rp+f4')

#key = cv2.waitKey(1)

    
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        print(check)  # prints true as long as the webcam is running
        # print(frame)   prints matrix values of each framecd
        cv2.imshow("Capturing", frame)
        
        # Press the assigned push button to capture the image
        if not GPIO.input(pin):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            
            engine.say('Image Captured Successfully!')
            engine.runAndWait()
            break     

    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

max_val = 8
max_pt = -1
max_kp = 0
orb = cv2.ORB_create()

#Importing the captured image into this program:
test_img = cv2.imread('saved_img.jpg')

(kp1, des1) = orb.detectAndCompute(test_img, None)

# Declaring Training set:
training_set=[]
ext = ['jpg', 'jpeg']
for e in ext:
    for files in glob.glob('/home/pi/Desktop/FYP/files/' + '*' + e):
        training_set.append(files)
        
engine.say('Processing Image. Please Wait!')
engine.runAndWait()

for i in range(0, len(training_set)):

    train_img = cv2.imread(training_set[i])
    
    (kp2, des2) = orb.detectAndCompute(train_img, None)

    bf = cv2.BFMatcher(normType=cv2.NORM_HAMMING, crossCheck=False)
    all_matches = bf.knnMatch(des1,des2,k=2)
    good = []
    
    # if good then append to list of good matches
    for (m, n) in all_matches:
        if m.distance< 0.80 * n.distance:
            good.append([m])
    if len(good) >max_val:
        max_val = len(good)
        max_pt = i
        max_kp = kp2
        print(i, ' ', training_set[i], ' ', len(good))
if max_val != 8:
    print(training_set[max_pt])
    print('good matches ', max_val)
    
note = str(training_set[max_pt])[27:-6][6:]

print('\nDetected denomination: Rs. ', note)


end_time = time.time() - start
print(f'Total time taken by the program: {end_time}')

engine.say(f'This is {note} rupees note')
engine.runAndWait()

