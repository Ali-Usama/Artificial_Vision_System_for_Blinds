# Conversion of Text into Speech on Raspberry Pi
Optical character recognition (OCR) systems provide persons who are blind or visually impaired with the capacity to scan printed text and then have it spoken in synthetic speech or saved to a computer file. There are three essential elements to OCR technology—scanning, recognition, and reading text.

Initially, a printed document is scanned by a camera. OCR software then converts the images into recognized characters and words and creates temporary files containing the text’s characters and page layout. In some OCRs these temporary files can be converted into formats retrievable by commonly used computer software such as word processors, spreadsheets, and databases. A person who is blind or visually impaired can access the scanned text by using adaptive technology devices that magnify the computer screen or provide speech or braille output.

# TESSERACT OCR
Tesseract is an open-source text recognition engine, and its development has been sponsored by Google since 2006. In the year 2006, Tesseract was considered as one of the most accurate open- source OCR engines. We can use it directly or use the API to extract the printed text from images. The best part is that it supports an extensive variety of languages. It is through wrappers that Tesseract can be made compatible with different programming languages and frameworks.

For our project, we made use of the Python wrapper named `pytesseract`. It is used to recognize text from a large document, or it can also be used to recognize text from an image of a single text line.

By default, Tesseract considers the input image as a page of text in segments. We can configure the Tesseract’s different segmentations if we are interested in capturing a small region of text from the image. We can dot it bay assigning `–psm` mode to it. Tesseract fully automates the page segmentation but it does not perform orientation and script detection. The different configuration parameters for Tesseract are:
* `Page segmentation mode (--psm):` By configuring this, we can assist Tesseract in how it should split an image in the form of texts.
```
Here is the complete list of supported arguments by –psm: 
| Argument | Description |
| :------: | :--------  |
|  0 |  Orientation and script detection (OSD) only. |
|  1  |  Automatic page segmentation with OSD. |
|  2  |  Automatic page segmentation, but no OSD, or OCR. |
|  3  |  Fully automatic page segmentation, but no OSD. (Default) |
|  4  |  Assume a single column of text of variable sizes. |
|  5  |  Assume a single uniform block of vertically aligned text. |
|  6  |  Assume a single uniform block of text. |
|  7  |  Treat the image as a single text line. |
|  8  |  Treat the image as a single word. |
|  9  |  Treat the image as a single word in a circle. |
| 10 |   Treat the image as a single character. |
| 11 |   Sparse text. Find as much text as possible in no particular order. |
| 12 |   Sparse text with OSD. |
| 13 |  Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific. |
```
* `Engine mode (--oem):` Tesseract has several engine modes with different performance and speed, it includes:
```
| Argument | Description |
| :------:  | :---------  |
| 0 | Legacy engine only |
| 1 | Neural net LSTM only |
| 2 | Legacy + LSTM mode only |
| 3 | By defualt, based on what is currently available|
```
We have used `--oem 3 --psm 6` in our system.

# Install required Libraries:
For this project, you'd need the following modules on your Raspberry Pi:
* pytesseract
First, install the Tesseract library
```
$ sudo apt install tesseract-ocr
```
Next, install the command line Tesseract tool:
```
$ sudo apt install libtesseract-div
```
Finally, install the Python wrapper for Tesseract, named `pytesseract`:
```
pip3 install pytesseract
```
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
pip3 install opencv-contrib-python
```
* Install RPi GPIO in order to perform function with the help of push buttons:
```
pip3 install RPi.GPIO
```
OR, you can also install it directly from the Raspbian repository:
```
$ sudo apt install rpi.gpio
```
*  Install pyttsx3 for voice outputs (you'd also need `espeak`):
```
pip3 install pyttsx3
$ sudo apt install espeak
```

