import cv2

img = cv2.imread('images/labka.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval, otsu = cv2.threshold(gaus, 0, 255, cv2.THRESH_OTSU) 

cv2.imshow('original', img)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

