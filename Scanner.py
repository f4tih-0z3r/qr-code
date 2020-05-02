import cv2
import pyzbar.pyzbar as pyzbar

cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame=cap.read()

    d=pyzbar.decode(frame)
    for obj in d:
        print(d[0].data.decode("ascii"))
        cv2.putText(frame, str(d[0].data.decode("ascii")), (50, 50), font, 3, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)

    key=cv2.waitKey(1)
    if key==0:
       break