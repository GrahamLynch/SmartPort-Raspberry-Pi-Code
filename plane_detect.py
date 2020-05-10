import cv2
import numpy as np
import json
import io
import re
import imutils 
from firebase import firebase
from matplotlib import pyplot as plt

userId = "sVoQ9YpOJXZaumzuDpfuztuZTGp2"

firebase = firebase.FirebaseApplication('https://smartport-68b3c.firebaseio.com/',None)

cap = cv2.VideoCapture(0)


cv2.namedWindow("Frame")
points = []
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ## define colour detection
    # Define upper and lower green ranges
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])

    # Define upper and lower blue ranges
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])


    bluemask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    bluebit = cv2.bitwise_and(frame, frame, mask=bluemask)
    blue = cv2.cvtColor(bluebit, cv2.COLOR_HSV2BGR)
    blue = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    bluecount = cv2.countNonZero(bluemask)

    greenmask = cv2.inRange(hsv_frame, lower_green, upper_green)
    greenbit = cv2.bitwise_and(frame, frame, mask=greenmask)
    green = cv2.cvtColor(greenbit, cv2.COLOR_HSV2BGR)
    green = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
    greencount = cv2.countNonZero(greenmask)

	
    plane_cascade = cv2.CascadeClassifier('planecascade.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
   
    #print result
    planes = plane_cascade.detectMultiScale(gray, 1.1, 25)
	
    for (x,y,w,h) in planes:
	if (bluecount > greencount) and planes.all():
		print "Ryanair"
		firebase.put(userId,'airline','Ryanair')
		firebase.put(userId,'flightStatus','Landed')
	else:
			pass
	if (greencount > bluecount) and planes.all():
		print "Aer Lingus"
		firebase.put(userId,'airline','Aer Lingus')
		firebase.put(userId,'flightStatus','Landed')
    cv2.imshow("frame", frame)



    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("d"):
        circles = []
cap.release()
cv2.destroyAllWindows()
