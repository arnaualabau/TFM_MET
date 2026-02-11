# --------------------------------------
#  Vision Sensor - YOLO Object Detection
#
# Author : Arnau Alabau Serra
# Date   : 11/02/2026
# --------------------------------------

import cv2
from ultralytics import YOLO


class VisionSensor:
    def __init__(self, camera_index=0, model_name="yolov8n.pt"):
        """
        camera_index: usually 0 for USB camera
        model_name: YOLO model (yolov8n.pt recommended for Raspberry Pi)
        """
        self.camera_index = camera_index
        self.model = YOLO(model_name)
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera.")

    def capture_and_detect(self, confidence_threshold=0.5):
        """
        Captures a frame and runs object detection.
        Returns structured detection results.
        """
        ret, frame = self.cap.read()

        if not ret:
            return None

        results = self.model(frame)[0]

        detections = []

        for box in results.boxes:
            conf = float(box.conf[0])
            if conf >= confidence_threshold:
                class_id = int(box.cls[0])
                class_name = self.model.names[class_id]

                detections.append({
                    "class": class_name,
                    "confidence": round(conf, 2)
                })

        return detections

    def release(self):
        """Release camera resource"""
        self.cap.release()
