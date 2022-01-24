import cv2
import numpy as np

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):
    ret, frame = vid.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, threshed = cv2.threshold(grayFrame, 100, 150, cv2.THRESH_BINARY)
    newFrame = np.array(threshed)
    cv2.imshow('frame', newFrame)
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

vid.release()
cv2.destroyAllWindows()