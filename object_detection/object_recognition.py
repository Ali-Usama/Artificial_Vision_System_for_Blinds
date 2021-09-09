import os
import argparse
import cv2
import numpy as np
import sys
import time
from threading import Thread
import importlib.util
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Set the pin#25 for closig the program.
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
import pyttsx3
engine = pyttsx3.init()
voiceRate = 170
engine.setProperty('rate', voiceRate)
engine.setProperty('voice', 'english_rp+f4')

# Source - Adrian Rosebrock, PyImageSearch: https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/
class VideoStream:
    """Camera object that controls video streaming from the Picamera"""
    def __init__(self,resolution=(1024,768),framerate=30):
        # Initialize the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(0)
        ret = self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        ret = self.stream.set(3,resolution[0])
        ret = self.stream.set(4,resolution[1])
            
        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()

    # Variable to control when the camera is stopped
        self.stopped = False

    def start(self):
    # Start the thread that reads frames from the video stream
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
    # Return the most recent frame
        return self.frame

    def stop(self):
    # Indicate that the camera and thread should be stopped
        self.stopped = True

# Define and parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite',
                    default='detect.tflite')
parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt',
                    default='labelmap.txt')
parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
                    default=0.5)
parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.',
                    default='1024x768')
parser.add_argument('--edgetpu', help='Use Coral Edge TPU Accelerator to speed up detection',
                    action='store_true')

args = parser.parse_args()

MODEL_NAME = 'coco_ssd_mobilenet_v1'
GRAPH_NAME = args.graph
LABELMAP_NAME = args.labels
min_conf_threshold = float(args.threshold)
resW, resH = args.resolution.split('x')
imW, imH = int(resW), int(resH)


categories = [{'id': 1, 'name': 'person'}, {'id': 2, 'name': 'bicycle'}, {'id': 3, 'name': 'car'}, 
              {'id': 4, 'name': 'motorcycle'}, {'id': 5, 'name': 'airplane'}, {'id': 6, 'name': 'bus'},
              {'id': 7, 'name': 'train'}, {'id': 8, 'name': 'truck'}, {'id': 9, 'name': 'boat'}, 
              {'id': 10, 'name': 'traffic light'}, {'id': 11, 'name': 'fire hydrant'}, {'id': 13, 'name': 'stop sign'}, 
              {'id': 14, 'name': 'parking meter'}, {'id': 15, 'name': 'bench'}, {'id': 16, 'name': 'bird'}, 
              {'id': 17, 'name': 'cat'}, {'id': 18, 'name': 'dog'}, {'id': 19, 'name': 'horse'}, {'id': 20, 'name': 'sheep'}, 
              {'id': 21, 'name': 'cow'}, {'id': 22, 'name': 'elephant'}, {'id': 23, 'name': 'bear'},
              {'id': 24, 'name': 'zebra'}, {'id': 25, 'name': 'giraffe'}, {'id': 27, 'name': 'backpack'}, 
              {'id': 28, 'name': 'umbrella'}, {'id': 31, 'name': 'handbag'}, {'id': 32, 'name': 'tie'}, 
              {'id': 33, 'name': 'suitcase'}, {'id': 34, 'name': 'frisbee'}, {'id': 35, 'name': 'skis'}, 
              {'id': 36, 'name': 'snowboard'}, {'id': 37, 'name': 'sports ball'}, 
              {'id': 38, 'name': 'kite'}, {'id': 39, 'name': 'baseball bat'}, 
             {'id': 40, 'name': 'baseball glove'}, {'id': 41, 'name': 'skateboard'}, 
            {'id': 42, 'name': 'surfboard'}, {'id': 43, 'name': 'tennis racket'}, 
             {'id': 44, 'name': 'bottle'}, {'id': 46, 'name': 'wine glass'}, {'id': 47, 'name': 'cup'}, 
            {'id': 48, 'name': 'fork'}, {'id': 49, 'name': 'knife'}, {'id': 50, 'name': 'spoon'}, 
             {'id': 51, 'name': 'bowl'}, {'id': 52, 'name': 'banana'}, {'id': 53, 'name': 'apple'}, 
                {'id': 54, 'name': 'sandwich'}, {'id': 55, 'name': 'orange'}, {'id': 56, 'name': 'broccoli'}, 
                {'id': 57, 'name': 'carrot'}, {'id': 58, 'name': 'hot dog'}, {'id': 59, 'name': 'pizza'}, 
                {'id': 60, 'name': 'donut'}, {'id': 61, 'name': 'cake'}, {'id': 62, 'name': 'chair'}, 
                {'id': 63, 'name': 'couch'}, {'id': 64, 'name': 'potted plant'}, {'id': 65, 'name': 'bed'}, 
                {'id': 67, 'name': 'dining table'}, {'id': 70, 'name': 'toilet'}, {'id': 72, 'name': 'tv'}, 
                {'id': 73, 'name': 'laptop'}, {'id': 74, 'name': 'mouse'}, {'id': 75, 'name': 'remote'}, 
                {'id': 76, 'name': 'keyboard'}, {'id': 77, 'name': 'cell phone'}, {'id': 78, 'name': 'microwave'}, 
                {'id': 79, 'name': 'oven'}, {'id': 80, 'name': 'toaster'}, {'id': 81, 'name': 'sink'}, 
                {'id': 82, 'name': 'refrigerator'}, {'id': 84, 'name': 'book'}, {'id': 85, 'name': 'clock'}, 
                {'id': 86, 'name': 'vase'}, {'id': 87, 'name': 'scissors'}, {'id': 88, 'name': 'teddy bear'}, 
                {'id': 89, 'name': 'hair drier'}, {'id': 90, 'name': 'toothbrush'}]

# Import TensorFlow libraries
# If tflite_runtime is installed, import interpreter from tflite_runtime, else import from regular tensorflow

pkg = importlib.util.find_spec('tflite_runtime')
if pkg:
    from tflite_runtime.interpreter import Interpreter

else:
    from tensorflow.lite.python.interpreter import Interpreter


PATH_TO_CKPT = '/home/pi/Desktop/FYP/coco_ssd_mobilenet_v1/detect.tflite'
PATH_TO_LABELS = '/home/pi/Desktop/FYP/coco_ssd_mobilenet_v1/labelmap.txt'

# Load the label map
with open(PATH_TO_LABELS, 'r') as f:
    labels = [line.strip() for line in f.readlines()]


# First label is '???', which has to be removed.
if labels[0] == '???':
    del(labels[0])

# Load the Tensorflow Lite model.
# If using Edge TPU, use special load_delegate argument

interpreter = Interpreter(model_path=PATH_TO_CKPT)

interpreter.allocate_tensors()

# Get model details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

floating_model = (input_details[0]['dtype'] == np.float32)


# Initialize frame rate calculation
frame_rate_calc = 1
freq = cv2.getTickFrequency()

# Initialize video stream
videostream = VideoStream(resolution=(imW,imH),framerate=30).start()
time.sleep(1)

# Create window
cv2.namedWindow('Object detector', cv2.WINDOW_NORMAL)

#for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
while True:

    # Start timer (for calculating frame rate)
    t1 = cv2.getTickCount()

    # Grab frame from video stream
    frame1 = videostream.read()

    # Acquire frame and resize to expected shape [1xHxWx3]
    frame = frame1.copy()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (width, height))
    input_data = np.expand_dims(frame_resized, axis=0)


    # Perform the actual detection by running the model with the image as input
    interpreter.set_tensor(input_details[0]['index'],input_data)
    interpreter.invoke()

    # Retrieve detection results
    boxes = interpreter.get_tensor(output_details[0]['index'])[0] # Bounding box coordinates of detected objects
    classes = interpreter.get_tensor(output_details[1]['index'])[0] # Class index of detected objects
    scores = interpreter.get_tensor(output_details[2]['index'])[0] # Confidence of detected objects
    #num = interpreter.get_tensor(output_details[3]['index'])[0]  # Total number of detected objects (inaccurate and not needed)
    
    for i in range(len(scores)):
        if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):

            # Get bounding box coordinates and draw box
            # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
            ymin = int(max(1,(boxes[i][0] * imH)))
            xmin = int(max(1,(boxes[i][1] * imW)))
            ymax = int(min(imH,(boxes[i][2] * imH)))
            xmax = int(min(imW,(boxes[i][3] * imW)))
            
           # cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)
            
            # Draw label
            object_name = labels[int(classes[i])] # Look up object name from "labels" array using class index
            label = '%s: %d%%' % (object_name, int(scores[i]*100)) # Example: 'person: 72%'
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
            label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
            # cv2.rectangle(frame, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
            # cv2.putText(frame, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text
            
            
            #                 car                    bus                  truck
            if object_name=='car' or object_name=='bus' or object_name=='truck':
                mid_x = (boxes[i][1]+boxes[i][3])/2
                mid_y = (boxes[i][0]+boxes[i][2])/2
                apx_distance = round(((1 - (boxes[i][3] - boxes[i][1]))**4),1)
                #cv2.putText(image_np, '{}'.format(apx_distance), (int(mid_x*800),int(mid_y*450)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
                
                if apx_distance <=0.3:
                    if mid_x > 0.3 and mid_x < 0.7:
                        #cv2.putText(image_np, 'WARNING!!!', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 3)
                        print("Warning -Vehicles Approaching")
                        engine.say("Warning -Vehicles Approaching")
                        engine.runAndWait()
                        #sleep(2.0)
                   
            if object_name=='bottle':
                mid_x = (boxes[i][1]+boxes[i][3])/2
                mid_y = (boxes[i][0]+boxes[i][2])/2
                apx_distance = round(((1 - (boxes[i][3] - boxes[i][1]))**4),1)
                #cv2.putText(image_np, '{}'.format(apx_distance), (int(mid_x*800),int(mid_y*450)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
                print(apx_distance)
                
                        
                if apx_distance > 0.2:
                    engine.say(f'{apx_distance} units')
                    engine.say("BOTTLE IS AT A SAFER DISTANCE")
                    engine.runAndWait()
                        
                elif apx_distance <=0.5:
                    if mid_x > 0.3 and mid_x < 0.7:
                        #cv2.putText(image_np, 'WARNING!!!', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 3)
                        #print("Warning -BOTTLE very close to the frame")
                        engine.say(f'{apx_distance} units')
                        engine.say("Warning -BOTTLE very close to the frame")
                        engine.runAndWait()
                            
            if object_name=='person':
                mid_x = (boxes[i][1]+boxes[i][3])/2
                mid_y = (boxes[i][0]+boxes[i][2])/2
                apx_distance = round(((1 - (boxes[i][3] - boxes[i][1]))**4),1)
                #cv2.putText(image_np, '{}'.format(apx_distance), (int(mid_x*800),int(mid_y*450)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
                print(apx_distance)
                
                        
                if apx_distance > 0.5:
                    engine.say(f'{apx_distance} units')
                    engine.say("Person is AT A SAFER DISTANCE")
                    engine.runAndWait()
                        
                elif apx_distance <=0.5:
                    if mid_x > 0.3 and mid_x < 0.7:
                        #cv2.putText(image_np, 'WARNING!!!', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 3)
                        #print("Warning -Person very close to the frame")
                        engine.say(f'{apx_distance} units')
                        engine.say("Warning -Person very close to the frame")
                        engine.runAndWait()
                         
            if object_name!='person' and object_name!='bottle' and object_name!='car' and object_name!='bus' and object_name!='truck':
                for item in categories:
                    if object_name == item['name']:
                        if scores[i] >= 0.6:
                            #print({item['name']})
                            engine.say(item['name'])
                            engine.say('is in front of you.')
                            engine.runAndWait()
                         
    # Draw framerate in corner of frame
    cv2.putText(frame,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)

    # All the results have been drawn on the frame, so it's time to display it.
    cv2.imshow('Object detector', frame)

    # Calculate framerate
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc= 1/time1

    # Press the assigned push button to quit
    
    if not GPIO.input(22):
        break

# Clean up
cv2.destroyAllWindows()
videostream.stop()
