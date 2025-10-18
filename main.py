import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('Video Preview', frame)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break