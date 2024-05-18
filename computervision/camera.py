import cv2
import numpy as np
from django.conf import settings


class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

class IPWebCam(object):
	def __init__(self):
		video_path = r"C:\Users\Mohit\PycharmProjects\AI_hub\Static_demo\demo_video.mp4"
		self.video_ = cv2.VideoCapture(video_path)

	def __del__(self):
		self.video_.release()

	def get_frame(self):
		success, image = self.video_.read()
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

# class Videoplayback(object):
# 	def __init__(self):
# 		self.video = cv2.VideoCapture(0)
#
# 	def __del__(self):
# 		self.video.release()
#
# 	def get_frame(self):
# 		success, image = self.video.read()
# 		frame_flip = cv2.flip(image,1)
# 		ret, jpeg = cv2.imencode('.jpg', frame_flip)
# 		return jpeg.tobytes()
