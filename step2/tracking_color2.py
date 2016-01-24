import cv2
import numpy as np

font = font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()
#    frame = cv2.resize(frame,(320,240))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of target color in HSV
    lower_color = np.array([0,150,150])
    upper_color = np.array([25,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Take the moments to get the centroid
    moments = cv2.moments(mask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)

    cv2.circle(frame, (320,240), 10, (255,255,255),2)
    cv2.line(frame,(320,0),(320,480),(0,0,255),1)
    cv2.line(frame,(0,240),(640,240),(0,0,255),1)

    # Assume no centroid
    ctr = (-1,-1)

    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:

        ctr = (centroid_x, centroid_y)
        # Put disk in at centroid in image
        cv2.circle(frame, ctr, 4, (255,255,255),-1)
        cv2.line(frame,(centroid_x,0),(centroid_x,480),(255,255,255),1)
        cv2.line(frame,(0,centroid_y),(648,centroid_y),(255,255,255),1)
	#disp marker position 
        text = str(centroid_x)+","+str(centroid_y)
        cv2.putText(frame,text,(centroid_x+10,centroid_y-3),font, 1,(255,255,255))

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
#    cv2.imshow('mask',mask)
#    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0x7F
    if k == 27:
        break

cv2.destroyAllWindows()