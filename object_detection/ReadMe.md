# Object Recognition System using Raspberry pi 4
As we know that, The blind people suffer regular and constant challenges in Navigation especially when they are on their own.They are mostly dependent on someone for even accessing their basic day-to-day needs. So, it’s a quite challenging task and the technological solution for them is of utmost importance and much needed. We came up with an Integrated Machine Learning System which allows the Blind Victims to identify and classify  RealTime Based Common day-to-day Objects and generate voice feed-backs and calculates distance which produces warnings whether he/she is very close or far away from the object. 

                          
__A detailed overview of the system:__
1. The system is set up in such a way that a Pi-Cam will capture the real-time frames and will send it to a pre-trained SSD detection model trained on COCO Datasets. It will then test the output class and will get detected with an accuracy metrics.						
2. After testing with the help of voice modules the class of the object will be converted into a default voice notes which will then be sent to the blind victims for their assistance.
3. Along with the object detection , we have used an alert system where approximate distance will get calculated. If the Blind Person is very close to the frame or is far away at a safer place , it will generate voice-based outputs along with distance units.	


# Set up and Run Tensorflow Lite Object Detection model on Raspberry Pi:
It's much easier to set up the TensorFlow lite on raspberyy pi, as compared to setting up the Tensorflow on a PC/laptop. The following steps should be followed for the setup of this system:

1. For installing the raspbian OS, follow [this](https://www.raspberrypi.org/documentation/computers/getting-started.html#installing-the-operating-system) guide 
2. Update the raspberry pi
```
sudo apt update && sudo apt upgrade -y
```
3. Download this repository and create a virtual environment
```
git clone https://github.com/Ali-Usama/Artificial_Vision_System_for_Blinds/object_detection.git 
cd object_detection
sudo pip3 install virtualenv
python3 -m venv avsb_od
source avsb_od/bin/activate
```
4. Install the required libraries:

* use [this](https://www.tensorflow.org/lite/guide/python) guide to install tensorflow lite
* install OpenCV:
First, install some dependencies:
```
$ sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev
$ sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
$ sudo apt install libatlas-base-dev liblapacke-dev gfortran
$ sudo apt install libhdf5-dev libhdf5-103
```
Now, go ahead and install OpenCV:
```
$ python3 -m pip install opencv-python
```
* Install RPi GPIO in order to perform function with the help of push buttons:
```
pip3 install RPi.GPIO
```
OR, you can also install it directly from the Raspbian repository:
```
sudo apt install rpi.gpio
```
*  Install pyttsx3 for voice outputs (you'd also need `espeak`):
```
pip3 install pyttsx3
$ sudo apt install espeak
```
* And, lastly, install numpy:
```
pip3 install numpy
```

