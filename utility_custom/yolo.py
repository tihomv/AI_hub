import cv2
import argparse
from ultralytics import YOLO

model = YOLO("yolov8l.pt")
def detect(frame):
    result = model(frame, agnostic_nms=True)[0]
    res_plot = result[0].plot()
    return result,res_plot
