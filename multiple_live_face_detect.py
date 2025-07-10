import cv2 as cv
from deepface import DeepFace
import numpy as np

# Load Haar cascade for face detection
face_cascade = cv.CascadeClassifier('haar_face.xml')

# Start webcam
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Error: Cannot access webcam.")
    exit()

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if faces are detected
    if len(faces) == 0:
        print("No faces detected.")

    for (x, y, w, h) in faces:
        roi_color = frame[y:y + h, x:x + w]

        # Resize and convert to RGB for better accuracy in DeepFace
        try:
            face_img = cv.resize(roi_color, (324, 324))
            face_rgb = cv.cvtColor(face_img, cv.COLOR_BGR2RGB)

            # Analyze emotion
            analysis = DeepFace.analyze(face_rgb, actions=['emotion'], enforce_detection=False)
            dominant_emotion = analysis[0]['dominant_emotion']
            emotions = analysis[0]['emotion']

            # Draw face rectangle and emotion
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, f'Emotion: {dominant_emotion}', (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

            # Show emotion probabilities (optional bar chart for emotions)
            bar_x, bar_y = x, y + h + 20
            for emotion, score in emotions.items():
                bar_length = int(score * 3)  # Scale the bar length for better visualization
                cv.rectangle(frame, (bar_x, bar_y), (bar_x + bar_length, bar_y + 20), (255, 0, 0), -1)
                cv.putText(frame, f'{emotion} {int(score)}%', (bar_x + 5, bar_y + 15),
                           cv.FONT_HERSHEY_PLAIN, 0.8, (255, 255, 255), 1)
                bar_y += 25  # Stack bars vertically

        except Exception as e:
            cv.putText(frame, "Emotion: Unknown", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            print("Error:", e)

    cv.imshow('Enhanced Emotion Detection', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
