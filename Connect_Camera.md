# Connect camera in system

```py
#!/usr/bin/python3
import cv2

#starting camera
cap=cv2.VideoCapture(0)
                    #first camera

#to check camera is started or not
if cap.isOpened() :
    print("Camera is ready to click pictures")
else :
    print("Check your webcam")

# now we can read input from camera
status,img=cap.read()   # it will take current picture or first picture
status1,img1=cap.read()     # it will take next picture

# now showing 
cv2.imshow('liveimage',img)
cv2.imshow('liveimage1',img1)
cv2.waitKey(0)

```

```py
#!/usr/bin/python3

import cv2

# staring camera
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()

    # coverting image frame into grayscale
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # draw a line
    cv2.line(frame,(0,0),(255,400),(0,255,0),3)

    # draw a rectangle
    cv2.rectangle(frame,(50,50),(150,200),(255,0,0),2)

    # draw a circle
    cv2.circle(frame,(120,200),100,(0,0,255),2)

    cv2.imshow('live',frame)
    cv2.imshow('livegray',grayimg)
    #cv2.waitKey(0)
    if cv2.waitKey(10)     &   0xff == ord('q') :
        break               # 0xff used take ascii input , ord('q') is used to bind 'q' , ord takes ascii value of argument.

# cv2.destroyWindow('live')
cv2.destroyAllWindows()     # this will destroy all windows

# to close camera
cap.release()

```
# To save a Video
    * A plugin is required
```py
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
    cv2.imshow('live',frame)
    output.write(frame)     # sending data to VideoWriter
     
    if cv2.waitKey(10)     &   0xff == ord('q') :
        break         


cv2.destroyAllWindows()

# to close camera
cap.release()


```