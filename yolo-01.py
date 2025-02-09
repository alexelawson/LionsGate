from roboflow import Roboflow

rf = Roboflow(api_key="PLACEHOLDER")
project = rf.workspace().project("lane-opening")
model = project.version("1").download("yolov8")
#yolo task=detect mode=train model=yolov8n.pt data=/Users/alexlawson/lane-opening--1/data.yaml epochs=50 imgsz=640
#yolo task=detect mode=predict model=/Users/alexlawson/runs/detect/train5/weights/best.pt source=/Users/alexlawson/Documents/GitHub/LionsGate/static/images/image_2025-02-06_11-53-40.jpg