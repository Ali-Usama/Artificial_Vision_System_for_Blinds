# Currency Recognition System for Pakistani Denominations
As we know that the Identification of various denominations of currency is not an easy task for visually impaired people. In Pakistan, though, there are special symbols embossed on different denominations, still the task is tedious for blind people. Also, the sizes of the Pakistan currency notes have changed drastically, over the past few years. For example, the new Rs.100 and Rs.50 notes have almost similar physical dimensions. Though the color of such notes is very contrasting, this difference is beneficial only to those blessed with eyesight. The blind people have a hard time identifying these currency notes (even the Braille and small dots on these notes seem to fade away with the prolonged usage).

The lack of identification devices motivated the need of a handheld device for the segregation of different denominations .In this project, Features of the images are compared with all the reference images of the currency, if the difference is less than the threshold then the numeric part of the currency is extracted and compared; if it matches, then the matched currency denomination is recognized. Pakistan currency denomination like 10, 20, 50, 100, 500, 1000, 5000 currency notes are recognized.

# Algorithm used for Feature Extraction
The SIFT and SURF key point detector and descriptor, although comparatively old, have proven remarkably successful in a number of applications using visual features, including object recognition, image stitching, visual mapping, etc. However, it imposes a large computational burden, especially for real-time systems. A computationally efficient replacement to SIFT and SURF that has similar matching performance, less affected by image noise and capable of being used for real-time performance is called ORB (Oriented FAST and Rotated BRIEF). 

ORB is a good alternative to SIFT and SURF in computation cost and matching performance. ORB is basically a fusion of FAST key point detector and BRIEF descriptor with many modifications to enhance the performance. First it uses FAST to find key points then apples Harris corner measure to find top N points among them. It also uses pyramids to produce multi-scale-features.

# Algorithm used for Image Classification
Brute Force Matcher is used for image classification. It takes the descriptor of one feature in first set and is matched with all other features in second set using a distance calculation and the closest one is returned as the most matched one. For any two images it calculates the hamming distance using the descriptors and returns the point with minimum hamming distance.

# Dataset Description:
A small dataset is used for this system, that comprises of different images for all of the Pakistani currency notes. A detailed description of the dataset is shown below:

| Currency Note  | No. of images |
|  :-----------: |  :-------------: |
| 10 rupees  |  4  |
| 20 rupees  |  4  |
| 50 rupees  |  4  |
| 100 rupees |  7  |
| 500 rupees |  4  |
| 1000 rupees | 4  |
| 5000 rupees | 4  |

# Methodology:
The system is divided into two parts. The first part is to identify the currency denomination through Feature Extraction and images classification. The second part is the oral output to notify the visually impaired person about the denomination of the note that they are currently having. 

The development of this device is based on a Picam integrated with Raspberry Pi, and a set of earphones for sound output. The real time images of Pakistani currency notes are captured and processed through different image processing techniques like edge detection, segmentation, and feature extraction and classification.

Here Raspberry Pi is used as a processor which processes the image of the currency note captured by the picam. The controlling code for picam is written and stored in Raspberrypi. Captured image is stored in memory. And Raspberry Pi will process the image to identify the denomination of the currency.

# Install the necessary libraries:
This system requires the installation of following modules:
* Open-CV
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
* `utils` that includes various utilities for working with images:
```
$ python3 -m pip install utils
```
*  Install RPi GPIO in order to perform function with the help of push buttons:
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
