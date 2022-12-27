import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(1)

while True:
	success, img = cap.read()
	imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results = hands.process(imgRGB)
	print(results.multi_hand_landmarks)

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
		mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)   //draw the hand and the connections
