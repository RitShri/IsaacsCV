import numpy as np
import cv2
import matplotlib.pyplot as plt

# read video
cap = cv2.VideoCapture('/home/isaacs/IsaacsCV/Spring2022/output.avi')

ret, frame = cap.read()    
plt.figure()
plt.imshow(frame)
