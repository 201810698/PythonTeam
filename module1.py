import cv2
from ultralytics import YOLO

# 향후 여러 개의 CCTV 주소 확장 가능
URLS = {
    "경복궁": "https://topiscctv1.eseoul.go.kr/sd2/ch21.stream/chunklist_w1765911301.m3u8",
}

# func1. CCTV에서 프레임 1장 받아오기 및 화면에 표시
def func1(url):
    cap = cv2.VideoCapture(url)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("프레임 수신 실패")
        return None

    return frame

# func2. 차량 수 인식 (차량 관련 객체만 필터링)
def func2(frame, model=None):

    if model is None:
        model = YOLO("yolov8m.pt")

    results = model.predict(frame, conf=0.15, verbose=False) # 신뢰도 하향
    vehicle_labels = ['car', 'bus', 'truck', 'motorbike']
    count = 0

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        if label in vehicle_labels:
            count += 1

    print(f"탐지된 차량 수: {count}")


    return count
