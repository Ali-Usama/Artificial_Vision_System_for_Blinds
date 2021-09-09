import cv2, pytesseract
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

webcam = cv2.VideoCapture(0)
while True:
	try:
		check, frame = webcam.read()
		print(check)  # prints true as long as the webcam is running
		# print(frame)  # prints matrix values of each framecd
		cv2.imshow("Capturing", frame)
		key = cv2.waitKey(1)
		if not GPIO.input(pin):
			cv2.imwrite(filename='text_img.jpg', img=frame)
			webcam.release()
			# img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
			# img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(1650)
			cv2.destroyAllWindows()
			break
		elif key == ord('q'):
			print("Turning off camera.")
			webcam.release()
			print("Camera off.")
			print("Program ended.")
			cv2.destroyAllWindows()
			break

	except(KeyboardInterrupt):
		print("Turning off camera.")
		webcam.release()
		print("Camera off.")
		print("Program ended.")
		cv2.destroyAllWindows()
		break


image = cv2.imread('/home/pi/Desktop/Artificial_Vision_System_for_Blinds/text_to_speech/text_img.jpg')

# Converting image into a gray-scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Converting it to binary image by thresholding
threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


# configuring parameters for tesseract:
custom_config = r'--oem 3 --psm 6'

# feeding image to tesseract
details = pytesseract.image_to_data(threshold_img, output_type=pytesseract.Output.DICT, config=custom_config, lang='eng')

# print(details.keys())

# Drawing bounding boxes on the original image:
total_boxes = len(details['text'])

for sequence_number in range(total_boxes):
	if int(details['conf'][sequence_number]) > 30:
		(x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number], details['height'][sequence_number])

		threshold_img = cv2.rectangle(threshold_img, (x, y), (x+w, y+h), (0, 255, 0), 2)


# arranging the current text into a file:

parse_text = []
word_list = []
last_word = ''

for word in details['text']:
	if word != '':
		word_list.append(word)
		last_word = word
	if (last_word != '' and word == '') or (word == details['text'][-1]):
		parse_text.append(word_list)
		word_list = []

print(parse_text)
import csv
with open('result_text.txt', 'w', newline="") as file:
	csv.writer(file, delimiter= " ").writerows(parse_text)

file = open('result_text.txt', 'r')
text = file.read()


engine.say(text)
engine.runAndWait()
