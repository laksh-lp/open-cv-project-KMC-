import numpy as np
import cv2
#import time
import datetime
x = datetime.datetime.now()
day=x.strftime("%d")
month=x.strftime("%b")
year=x.strftime("%Y")

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
#add time in video name to make it unique
out = cv2.VideoWriter(day+'-'+month+'-'+year+'.avi', fourcc, 20.0, (640, 480)) 
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret, frame = cap.read()
    skinLower=(0,29,109)
    skinUpper=(87,176,221)
    frame = cv2.GaussianBlur(frame, (5,5), 0)
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame, skinLower, skinUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('mask',mask)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        #rect = cv2.minAreaRect(c)
        #rect = rect[1][0]*rect[1][1]
        xx,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame,(xx,y),(xx+w,y+h),(0,255,0),3)
        #localtime = time.asctime( time.localtime(time.time()) )
        localtime = x.strftime("%c")
        cv2.putText(frame,'Time : ' + localtime, (10,30), font, 0.5, (0,0,0), 1, cv2.LINE_AA)
        out.write(frame)





    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
