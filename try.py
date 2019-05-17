import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    skinLower=(0,29,109)
    skinUpper=(87,176,221)
    frame = imutils.resize(frame, width=600)
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame, skinLower, skinUpper)
    #mask = cv2.erode(mask, None, iterations=3)
    #mask = cv2.dilate(mask, None, iterations=1)
    cv2.imshow('mask',mask)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        #rect = cv2.minAreaRect(c)
        #rect = rect[1][0]*rect[1][1]
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)






    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()