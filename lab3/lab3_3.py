import cv2
import numpy as np

img = cv2.imread('images/kokserek.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 6)

cv2.imshow('original', img)
cv2.imshow('treshold', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()