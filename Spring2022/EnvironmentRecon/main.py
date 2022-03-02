import cv2
import threading
import numpy as np

from CSI_Camera import CSI_Camera

# TODO: may want to move this to the CSI camera module
def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=1920,
    display_height=1080,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d ! "
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

DIM=(640, 480)
K=np.array([[395.2474957410931, 0.0, 313.5019461730335], [0.0, 527.3954916199217, 196.37742657771022], [0.0, 0.0, 1.0]])
D=np.array([[-0.03798599445910202], [0.020273631739096985], [-0.00890488243952009], [-0.03915599454217283]])

def undistort(frame):
    img = frame
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted_img

def run_cameras():
    window_title = "Dual CSI Cameras"
    left_camera = CSI_Camera()
    left_camera.open(
        gstreamer_pipeline(
            sensor_id=0,
            capture_width=1280,
            capture_height=720,
            flip_method=0,
            display_width=960,
            display_height=540,
        )
    )
    left_camera.start()
    print(left_camera)

    #right_camera = cv2.VideoCapture(1)

    if left_camera.video_capture.isOpened():

        cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)

        try:
            while True:
                _, left_image = left_camera.read()
                #_, right_image = right_camera.read()
                #left_image = undistort(left_image)
                print(left_image.shape)
                # Use numpy to place images next to each other
                #camera_images = np.hstack((left_image, right_image)) 
                # Check to see if the user closed the window
                # Under GTK+ (Jetson Default), WND_PROP_VISIBLE does not work correctly. Under Qt it does
                # GTK - Substitute WND_PROP_AUTOSIZE to detect if window has been closed by user
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    cv2.imshow("fisheye", left_image)
		    #cv2.imshow(window_title,cv2.resize(right_image,(600,720)))
		    #print("Hi")
                else:
                    break

                # This also acts as
                keyCode = cv2.waitKey(30) & 0xFF
                # Stop the program on the ESC key or q
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:

            left_camera.stop()
            left_camera.release()
	    #_camera.release()
        cv2.destroyAllWindows()
    else:
        print(cv2.getBuildInformation()) 
        print("Error: Unable to open both cameras")
        left_camera.stop()
        left_camera.release()
        #right_camera.release()
        #dright_camera.release()



if __name__ == "__main__":
    run_cameras()
