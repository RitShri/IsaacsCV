import numpy as np
import cv2
 
<<<<<<< Updated upstream
 
=======
>>>>>>> Stashed changes
cap = cv2.VideoCapture('fisheye_video.avi')
 
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
