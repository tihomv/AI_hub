import cv2
import numpy as np
import copy
from utility_custom.yolo import detect


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # image_ = copy.deepcopy(image)
        result,annoted_frame = detect(image)
        # print(result)
        # frame_flip = cv2.flip(annoted_frame, 1)

        ret, jpeg = cv2.imencode('.jpg', annoted_frame)
        return jpeg.tobytes()


class IPWebCam(object):
    def __init__(self):
        video_path = r"C:\Users\Mohit\PycharmProjects\AI_hub\Static_demo\demo_video.mp4"
        self.video_ = cv2.VideoCapture(video_path)

    def __del__(self):
        self.video_.release()

    def get_frame(self):
        success, image = self.video_.read()
        frame_flip = cv2.flip(image, 1)
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
