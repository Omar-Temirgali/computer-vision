import numpy as np
import cv2

img = cv2.imread('original3.jpg')
r_img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
img_gray = cv2.cvtColor(r_img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

kernelx = np.array([[1, 0], [0, -1]])
kernely = np.array([[0, 1], [-1, 0]])
img_robertx = cv2.filter2D(img_gray, -1, kernelx)
img_roberty = cv2.filter2D(img_gray, -1, kernely)
res = cv2.addWeighted(img_robertx, 0.5, img_roberty, 0.5, 0)

x = cv2.Sobel(img_gray, cv2.CV_16S, 1, 0, ksize=3, scale=1.0)
y = cv2.Sobel(img_gray, cv2.CV_16S, 0, 1, ksize=3, scale=1.0)
abs_x= cv2.convertScaleAbs(x)
abs_y = cv2.convertScaleAbs(y)
edge = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

cv2.imshow('grayscale', img_gray)
cv2.imshow('Roberts Edge Detection', res)
cv2.imshow('Sobel Edge Detection', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()