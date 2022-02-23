#!/usr/bin/env python
import cv2
import numpy as np


#zedVideo = cv2.VideoCapture(1)
#fisheyeVideo = cv2.VideoCapture(2)
fisheyeVideo = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)
#fisheyeVideo = cv2.VideoCapture('v4l2src device=/dev/video0 ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)
#fisheyeVideo = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)
index = 0
print("Hi")
while(True):
	#retZ, frameZ = zedVideo.read()
	retF, frameF = fisheyeVideo.read()
	print(frameF)
	#cv2.imshow("zed", frameZ)
	cv2.imshow("fisheye", frameF)
	k = cv2.waitKey(1)
	if(k == 32):
		#cv2.imwrite("./zedImg/" + str(index), frameZ)
		cv2.imwrite("./fisheyeImg/" + str(index), frameF)
		index += 1
	elif(k == 27 or k == 133):
		break
cv2.destroyAllWindows()
#zedVideo.release()
fisheyeVideo.release()
