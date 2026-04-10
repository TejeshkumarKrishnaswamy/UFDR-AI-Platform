from ultralytics import YOLO
import cv2

# load pretrained model
model = YOLO("yolov8n.pt")

def detect_objects(image_path):

    results = model(image_path)

    detected_objects = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            detected_objects.append(label)

    # save output image
    output_path = "detected_output.jpg"
    results[0].save(filename=output_path)

    return detected_objects, output_path
