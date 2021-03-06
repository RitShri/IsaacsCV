import numpy as np
import cv2
import sys

#svo_input_path = sys.argv[1]

cap = cv2.VideoCapture("fisheye_video.avi")
fps = video.get(cv2.CAP_PROP_FPS)
print(fps)
while(cap.isOpened()):
    ret, frame = cap.read()
 
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
 
    keyCode = cv2.waitKey(25) & 0xFF
    # Stop the program on the ESC key or 'q'
    if keyCode == 27 or keyCode == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
