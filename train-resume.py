from ultralytics import YOLO

# Load the partially trained model
model = YOLO("runs/pose/train/weights/last.pt")

# Resume training
results = model.train(resume=True)