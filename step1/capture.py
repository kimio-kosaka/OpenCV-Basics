#!/usr/bin/python

import cv2

#capture device 0:/dev/video0
cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()

    # resize 320,240
    frame = cv2.resize(frame,(320,240))

    # show
    cv2.imshow('frame',frame)

    # if keyin "ESC" then exit while loop
    k = cv2.waitKey(5) & 0x7F
    if k == 27:
        break

# close frame display window
cv2.destroyAllWindows()
