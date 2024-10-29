from ultralytics import YOLO

# Load the model and run inference on the webcam
YOLO('runs/pose/train/weights/best.pt').predict(source=0, show=True, save=True)