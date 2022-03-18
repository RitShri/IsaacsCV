import sys
import numpy as np
import pyzed.sl as sl
import cv2
import sys
import json
from datetime import datetime
from multiprocessing import Process
from subprocess import Popen
import time

if __name__ == "__main__":
    processes = [Popen(['python3 zed_recording.py'], shell=True), 
		 Popen(['python record_fisheye_video.py'], shell=True)]
    
    time.sleep(60)
    for p in processes:
        p.terminate()
    # does not kill the process properly

