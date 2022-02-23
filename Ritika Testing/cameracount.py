import cv2 

def camera_count():
	'''Returns the number of avalible camera devices connected to the host device'''
	camera = 0 
	while camera <3:
		try:
			if (cv2.VideoCapture(camera).grab()) is True:
				print("Camera found")
				cv2.destroyAllWindows()
		except:
			break
		camera +=1
	return camera
				

print(camera_count())
