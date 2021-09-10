# Artificial Vision System For Blinds

__Note: This project is under-development. Further modifications will be added soon. If there are any issues, please feel free to raise them.__

__Note2: Run the `main.py` file only if you want to implement all three of the functionalities of this system. However, if you're looking for only an object detection system, or a Currency recognition system, open their respective folders - no need to run the `main.py` file in that case.__

# An Overview of the System:
Typical human beings are gifted by the nature with number of senses that make them able to develop a fine perception of the surrounding world. Unfortunately, a number of people for different reasons have lost or deprived their visual sense. In any country the number of visually impaired people and those with very low vision are significant. This is an important issue amongst social as well as scientific society to find an adequate solution for this problem. Among the handicapped people, those visually impaired ones are facing more difficulties than others in gathering information, for about 70% information got by human being is through sight.

This system is specifically developed keeping the visually impaired people in mind, and we strongly believe that the AVSB can offer people with disabilities the assistance and support they need to achieve a good quality of life and allow them to participate in the social and economic life. Assistive advanced technologies are powerful tools to increase independence and improve participation. Therefore, the purpose of this project is to analyze how people with visual impairments can interact with and benefit from these technologies.

# Features of AVSB
The clear path indication and environment recognition is the aim of this system. By using an intelligent device, visually impaired people can improve their travel speed and can reduce minor collisions as well as double the safety. 
* Visually disabled people can use the device for walking purpose as it provides such features with the help of raspberry pi and Picam which are used for object detection, 
* it captures the images of detected obstacle and provides the information with the help of speaker or headphone. 
* It also identifies the currency notes when the user places a paper currency in front of the mounted camera and will convert text to speech as well. 

This type of system is based on the real-time embedded system because it is modern technologies that depend upon the hardware, software and other parts.

__The features of AVSB include:__
1. Object Detection: For a detailed overview, click [here](https://github.com/Ali-Usama/Artificial_Vision_System_for_Blinds/tree/main/Object%20detection).
2. Currency Recognititon for Pakistani denominations: Click [here](https://github.com/Ali-Usama/Artificial_Vision_System_for_Blinds/tree/main/Currency%20Recognition) for further details.
3. Conversion of Text (from images) into speech: Click [here](https://github.com/Ali-Usama/Artificial_Vision_System_for_Blinds/tree/main/Text%20To%20Speech) for details.

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

# Directory Structure for your Raspberry pi:
```
|-- home
  |-- pi
    |-- Desktop
      |--Artificial_Vision_System_for_Blinds
        |-- currency_recogntion
          |-- files                   # contains training images for Pakistani denominations
          |-- currecny_recognition.py     # code to run for detecting the value of different denominations
          |-- ReadDMe.md
        |
        |-- object_detection
          |-- coco_ssd_mobilenet_v1_1.0_quant_2018_06_29    # contains pre-trained ssd mobilenet v1 model
            |-- detect.tfllite
            |-- labelmap.txt
          |-- object_recogniton.py       # code to run for detecting objects in fron of the user
          |-- ReadMe.md
        |
        |-- text_to_speech
          |-- extract_text.py
          |-- ReadMe.md
        |
        |-- main.py   # main file, containing paths to all other .py files, that can be run individually, by their assigned push buttons.
        |-- README.md
```
# Run AVSB without a GUI:
The sole purpose of creating the `main.py` file was to enable the raspberry pi to run all of the programs without a Graphical User Interface. In other words, we wanted to develop a portable system, that can be powered by a power bank and the user can take it anywhere they want. 

For this purpose, the following steps can be followed to run the `main.py` script at the startup, which would call the object detection, or currency recogniton, or text-to-speech systems, with the help of push buttons: 
1. Enable Console AutoLogin
```
$ sudo raspi-config
Choose: Boot Options
Choose: Desktop/CLI
Choose: Console Autologin
Select Finish, but don't reboot yet
```
2. Put the path of `main.py` in /etc/profile
```
$ sudo nano /etc/profile
```
Don't change anything else in that file, scroll to the bottom and add the follwing line at the end:
```
sudo python3 /home/pi/Desktop/Artificial_Vision_System_for_Blinds/main.py
```
Type `Ctrl+S` to save the changes, and then `Ctrl+X` to exit.

3. Now, reboot and check if this has worked:
```
$ sudo reboot
```

# Push Buttons Arrangement:

|  Button Name   | GPIO Pin Number   | Function |
|	:-----------: | :----------------:  |  :------------ |
|Button 1 | Pin # 25 | Starts object detection |
|Button 2 | Pin # 6 | Detects a currency denomination after capturing an image |
|Button 3 | Pin # 16 | Converts text into speech after capturing an image |
|Button C | Pin # 22 | Captures images for Currency recogntion and text to speech, and quits object detection
|Button 4	| Pin # 26 | Shut down the system |
