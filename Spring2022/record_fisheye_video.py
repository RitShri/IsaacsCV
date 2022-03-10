import cv2
import numpy as np
from datetime import datetime
import json
""" 
gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
Flip the image by setting the flip_method (most common values: 0 and 2)
display_width and display_height determine the size of each camera pane in the window on the screen
Default 1920x1080 displayd in a 1/4 size window
"""

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=3264,
    capture_height=2464,
    display_width=960,
    display_height=540,
    framerate=21,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
    
    #return "nvarguscamerasrc ! nvvidconv ! xvimagesink"
ct = 0
DIM=(640, 480)
K=np.array([[395.2474957410931, 0.0, 313.5019461730335], [0.0, 527.3954916199217, 196.37742657771022], [0.0, 0.0, 1.0]])
D=np.array([[-0.03798599445910202], [0.020273631739096985], [-0.00890488243952009], [-0.03915599454217283]])

#takes in image
def undistort(frame):
    img = frame
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted_img


def show_save_camera():
    window_title = "Fisheye Camera"

    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    print(gstreamer_pipeline(flip_method=0))
    video_capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print(fps)
    if video_capture.isOpened():
        ret_val, frame_fish = video_capture.read()
	s1 = frame_fish.shape[:2][0]
	s2 = frame_fish.shape[:2][1]
        result = cv2.VideoWriter('fisheye_video.avi', 
                             cv2.VideoWriter_fourcc(*'MJPG'),
                             1000, (s2,s1))
	
    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
	    get_time = 0
            while True:
                if(not get_time):
                    now = datetime.now()
		    ct = now.strftime("%m/%d/%Y, %H:%M:%S")
		    json_data = {}
                    json_data['start_time'] = ct
                    json_string = json.dumps(json_data)
                    with open('fish_time.json', 'w') as  outfile:
	                outfile.write(json_string)
                    get_time = 1
                ret_val, frame_fish = video_capture.read()
                result.write(frame_fish)
                
                keyCode = cv2.waitKey(1) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:
            video_capture.release()
            result.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    show_save_camera()
