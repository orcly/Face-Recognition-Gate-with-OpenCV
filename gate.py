
import cv2
import numpy as np

# Load recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Load labels
label_map = {}
with open("labels.txt", "r") as f:
    for line in f:
        label, name = line.strip().split(":")
        label_map[int(label)] = name

# Start webcam
cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.3, 5)

    message = "Not recognized"

    for (x, y, w, h) in faces:
        face_gray = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face_gray)

        if confidence < 70:
            name = label_map.get(label, "Unknown")
            message = f"Welcome, {name}"
        else:
            message = "Not recognized"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

    cv2.putText(frame, message, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Gate", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
