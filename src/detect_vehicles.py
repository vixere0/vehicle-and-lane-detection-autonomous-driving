import os
import cv2
import time
from ultralytics import YOLO

# Proje ana klasörü
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

video_path = os.path.join(
    BASE_DIR,
    "data",
    "sample_videos",
    "highway.mp4"
)

# Model
model = YOLO("yolov8n.pt")

# Video aç
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Video açılamadı")
    exit()

prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ZAMAN BAŞI
    start_time = time.time()

    # YOLO inference
    results = model(frame, conf=0.75, iou=0.5)

    annotated = frame.copy()
    car_count = 0

    for box, conf, cls in zip(
        results[0].boxes.xyxy,
        results[0].boxes.conf,
        results[0].boxes.cls
    ):
        x1, y1, x2, y2 = map(int, box)
        area = (x2 - x1) * (y2 - y1)

        if conf > 0.75 and area > 2500:
            car_count += 1
            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0,255,0), 2)

    # FPS HESABI
    end_time = time.time()
    fps = 1 / (end_time - start_time)

    cv2.putText(
        annotated,
        f"Cars: {car_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        annotated,
        f"FPS: {fps:.2f}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )
    frame = cv2.resize(frame, (640, 360))


    cv2.imshow("YOLO Vehicle Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
