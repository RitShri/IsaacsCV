import sys
import numpy as np
import pyzed.sl as sl
import cv2
import sys

zed = sl.Camera()

init_params = sl.InitParameters()
init_params.sdk_verbose = True

err = zed.open(init_params)
print("Opening zed camera was a", err)

runtime_parameters = sl.RuntimeParameters()
runtime_parameters.sensing_mode = sl.SENSING_MODE.STANDARD  # Use STANDARD sensing mode

video_name = 'test.svo'
params = sl.RecordingParameters(
    video_filename=video_name,
    compression_mode=sl.SVO_COMPRESSION_MODE.H264
)
err = zed.enable_recording(params)

# Here is the code to record with ZED
key = ' '
while key != 113 :
    zed.grab()
 #   if zed.grab() == sl.ERROR_CODE.SUCCESS :
        # Each new frame is added to the SVO file
   #     zed.record()

# Disable recording
zed.disable_recording()

zed.close()
