import numpy as np
import sys
import cv2
# You should replace these 3 lines with the output in calibration step
DIM=(640, 480)
K=np.array([[395.2474957410931, 0.0, 313.5019461730335], [0.0, 527.3954916199217, 196.37742657771022], [0.0, 0.0, 1.0]])
D=np.array([[-0.03798599445910202], [0.020273631739096985], [-0.00890488243952009], [-0.03915599454217283]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)
