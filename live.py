#!/usr/bin/python3
import cv2

# staring camera
cap=cv2.VideoCapture(0)

# adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# saving video
output=cv2.VideoWriter('class.mkv',plugin,20,(640,480))     # (480,680) are dimension of camera, 20 is frame size

while cap.isOpened():
    status,frame=cap.read()
    print(frame.shape)
    cv2.imshow('live',frame)
    output.write(frame)     # sending data to VideoWriter
     
    if cv2.waitKey(10)     &   0xff == ord('q') :
        break         


cv2.destroyAllWindows()

# to close camera
cap.release()
