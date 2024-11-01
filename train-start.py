from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n-pose.pt") # load a pretrained model

# Train hand model from hand-keypoints dataset
results = model.train(data="data.yaml", epochs=100, imgsz=640)