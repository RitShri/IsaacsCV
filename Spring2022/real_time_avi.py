import cv2

cap = cv2.VideoCapture('fisheye_video.avi')
cap.set(cv2.CAP_PROP_FPS,21)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]
calc_timestamps = [0.0]

while(cap.isOpened()):
    frame_exists, curr_frame = cap.read()
    gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    keyCode = cv2.waitKey(21) & 0xFF
    # Stop the program on the ESC key or 'q'
    if keyCode == 27 or keyCode == ord('q'):
        break
print(timestamps)
cap.release()
