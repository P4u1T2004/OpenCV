import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
 _, frame = cap.read()
 hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 lower_blue = np.array([80, 50, 50])
 upper_blue = np.array([130, 255, 255])
 lower_red = np.array([160,80,20])
 upper_red = np.array([179, 255, 255])

 mask1 = cv.inRange(hsv, lower_blue, upper_blue)
 mask2 = cv.inRange(hsv, lower_red,upper_red)
 mask = cv.bitwise_or(mask1,mask2)
 res = cv.bitwise_and(frame,frame, mask= mask)
 cv.imshow('frame',frame)
 cv.imshow('mask',mask)
 cv.imshow('res',res)
 k = cv.waitKey(1) & 0xFF
 if k == 27:
    break
cv.destroyAllWindows()
