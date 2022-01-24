import cv2

img = cv2.imread('original3.jpg') 
img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)
img_blur = cv2.GaussianBlur(img, (3, 3), 2.0)
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img_gray, 100, 200)
canny1 = cv2.Canny(img_gray, 7, 236)
canny2 = cv2.Canny(img_gray, 7, 100)
canny3 = cv2.Canny(img_gray, 1, 1)

cv2.imshow("Canny Edge Detection", canny)
cv2.imshow("Canny Edge Detection 1", canny1)
cv2.imshow("Canny Edge Detection 2", canny2)
cv2.imshow("Canny Edge Detection 3", canny3)
cv2.waitKey(0)
cv2.destroyAllWindows()