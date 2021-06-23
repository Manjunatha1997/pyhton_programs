import cv2
import json
import numpy as np


with open('config.json') as f:
	data = json.load(f)


indexes = data.items()
x = (list(indexes))



video0 = cv2.VideoCapture(x[0][1])
video1 = cv2.VideoCapture(x[1][1])
video2 = cv2.VideoCapture(x[2][1])
video3 = cv2.VideoCapture(x[3][1])
video4 = cv2.VideoCapture(x[4][1])
video5 = cv2.VideoCapture(x[5][1])
video6 = cv2.VideoCapture(x[6][1])
video7 = cv2.VideoCapture(x[7][1])


while True:
	ret0, frame0 = video0.read()
	ret1, frame1 = video0.read()
	ret2, frame2 = video0.read()
	ret3, frame3 = video0.read()
	ret4, frame4 = video0.read()
	ret5, frame5 = video0.read()
	ret6, frame6 = video0.read()
	ret7, frame7 = video0.read()

	if ret0:
		cv2.imshow('frame0',frame0)

	if ret1:
		cv2.imshow('frame1',frame1)

	if ret2:
		cv2.imshow('frame2',frame2)

	if ret3:
		cv2.imshow('frame3',frame3)

	if ret4:
		cv2.imshow('frame4',frame4)

	if ret5:
		cv2.imshow('frame5',frame5)

	if ret6:
		cv2.imshow('frame6',frame6)

	if ret7:
		cv2.imshow('frame7',frame7)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



video0.release()
video1.release()
video2.release()
video3.release()
video4.release()
video5.release()
video6.release()
video7.release()

cv2.destroyAllWindows()








