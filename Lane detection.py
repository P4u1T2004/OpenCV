import cv2 as cv
import numpy as np
cap = cv.VideoCapture("/Users/paul/Downloads/Lanedetection.avi")
while True:
    ret,_frame=cap.read()
    if not ret:
        cap=cv.VideoCapture("/Users/paul/Downloads/Lanedetection.avi")
        continue
    frame= cv.GaussianBlur(_frame,(5,5),0)   #IMPLEMENT GAUSSIAN BLUR
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower=np.array([18,94,140])
    upper=np.array([18,255,255])

    mask=cv.inRange(hsv,lower,upper)
    edges=cv.Canny(mask,74,150)
    lines=cv.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
            cv.imshow("frame",frame)
            cv.imshow("edges",edges)
            key=cv.waitKey(25)
            if(key==27):
                break
