import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(320,240))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of target color in HSV
    lower_color = np.array([0,150,150])
    upper_color = np.array([25,255,255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Take the moments to get the centroid
    moments = cv2.moments(mask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)

    # Assume no centroid
    ctr = (-1,-1)

    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
        # Put disk in at centroid in image
        cv2.circle(frame, ctr, 4, (255,255,255),-1)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0x7F
    if k == 27:
        break

cv2.destroyAllWindows()
