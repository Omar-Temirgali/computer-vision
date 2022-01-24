import cv2

img = cv2.imread('original3.jpg') 
img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
img_blur = cv2.GaussianBlur(img, (3, 3), 2.0)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

dst = cv2.Laplacian(img_gray, cv2.CV_16S, ksize=3)
abs_dst = cv2.convertScaleAbs(dst)

cv2.imshow('Laplacian', abs_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()