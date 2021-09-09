# Object Recognition System using Raspberry pi 4
As we know that, The blind people suffer regular and constant challenges in Navigation especially when they are on their own.They are mostly dependent on someone for even accessing their basic day-to-day needs. So, it’s a quite challenging task and the technological solution for them is of utmost importance and much needed. We came up with an Integrated Machine Learning System which allows the Blind Victims to identify and classify  RealTime Based Common day-to-day Objects and generate voice feed-backs and calculates distance which produces warnings whether he/she is very close or far away from the object. 

                          
__A detailed overview of the system:__
1. The system is set up in such a way that a Pi-Cam will capture the real-time frames and will send it to a pre-trained SSD detection model trained on COCO Datasets. It will then test the output class and will get detected with an accuracy metrics.						
2. After testing with the help of voice modules the class of the object will be converted into a default voice notes which will then be sent to the blind victims for their assistance.
3. Along with the object detection , we have used an alert system where approximate distance will get calculated. If the Blind Person is very close to the frame or is far away at a safer place , it will generate voice-based outputs along with distance units.	

# Hardware Modules Used in the System:
```
1. Raspberry pi 4 Model B (4GB)
2. PiCam v2 8MP
3. PowerBank 10kmAh (5V/3A output)
4. Push Buttons
5. BreadBoard
6. Jumper wires
7. Earphones
```

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
* install following openCV dependencies:
```
$ sudo apt install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
$ sudo apt install libavodec-dev libavformat-dev libswscale-dev lib41-dev
$ sudo apt install libxvidcore-dev libx264-dev
$ sudo apt install libatlas-base-dev gfortran
$ sudo apt install libhdf5-dev libhdf5-serial-dev libhdf5-103
$ sudo apt install libqtgui4 libqtwebkit4 libtqt4-test python3-pyqt5
$ sudo apt install python3-dev
```
* Now, install openCV
```
pip3 install opencv-contrib-python
```
* Install RPi GPIO in order to perform function with the help of push buttons:
```
pip3 install RPi.GPIO
```
OR, you can also install it directly from the Raspbian repository:
```
sudo apt install rpi.gpio
```
*  Install pyttsx3 for voice outputs:
```
pip3 install pyttsx3
```
* And, lastly, install numpy:
```
pip3 install numpy
```

