import sys
import numpy as np
import pyzed.sl as sl
import cv2
import sys
import json
from datetime import datetime

ct = 0
zed = sl.Camera()

init_params = sl.InitParameters()
init_params.sdk_verbose = True
init_params.camera_fps = 21
err = zed.open(init_params)
print("Opening zed camera was a", err)

runtime_parameters = sl.RuntimeParameters()
runtime_parameters.sensing_mode = sl.SENSING_MODE.STANDARD  # Use STANDARD sensing mode

video_name = 'zed5.svo'
params = sl.RecordingParameters(
    video_filename=video_name,
    compression_mode=sl.SVO_COMPRESSION_MODE.H265
)
err = zed.enable_recording(params)

# Here is the code to record with ZED
key = ' '
get_time = 0

while key != 113 :
    zed.grab()
    if(not get_time):
        now = datetime.now()
        ct = now.strftime("%m/%d/%Y, %H:%M:%S")
        json_data = {}
        json_data['start_time'] = ct
        json_string = json.dumps(json_data)
        with open('zed_time.json', 'w') as  outfile:
             outfile.write(json_string)
        get_time = 1
 #   if zed.grab() == sl.ERROR_CODE.SUCCESS :
        # Each new frame is added to the SVO file
   #     zed.record()

# Disable recording
zed.disable_recording()

zed.close()



