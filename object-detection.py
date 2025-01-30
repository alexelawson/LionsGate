from ultralytics import YOLO

# Load a pretrained YOLOv11 model
model = YOLO('yolov11n.pt')

# Perform object detection on an image
results = model('/Users/alexlawson/Documents/GitHub/LionsGate/static/images/latest.jpg')

# Display the results
results.show()