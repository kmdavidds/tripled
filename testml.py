from ultralytics import YOLO
import cv2
import math
from fast_plate_ocr import ONNXPlateRecognizer
# from util import read_license_plate 


# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/bestv1.pt")
# m = ONNXPlateRecognizer('argentinian-plates-cnn-model')

# object classes
classNames = ["License_Plate"]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->", confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            # OCR ???

            license_plate_crop = img[int(y1):int(y2), int(x1): int(x2), :]

            # process license plate
            license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
            # _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

            # text = m.run(license_plate_crop_gray)

            cv2.imshow('Crop', license_plate_crop_gray)
            # cv2.imshow('Crop2', license_plate_crop_thresh)

            # for tex in text:
            #     print("Text --->", tex)

            # read license plate number
            # license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

            cv2.putText(img, str(confidence), org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()