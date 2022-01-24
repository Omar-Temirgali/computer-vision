import cv2 as cv
import numpy as np

img = cv.imread('LicensePlate.jpg')
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv.getRotationMatrix2D((cX, cY), -15, 1.0)
rotated = cv.warpAffine(img, M, (w, h))

input_pts = np.float32([[31, 36], [10, 106], [271, 39], [250, 103]])
output_pts = np.float32([[41, 36], [40, 106], [246, 36], [246, 106]])
M = cv.getPerspectiveTransform(input_pts, output_pts)
skewed = cv.warpPerspective(rotated, M, (w, h))

input_pts = np.float32([[41, 36], [39, 106], [247, 37]])
output_pts = np.float32([[5, 36], [5, 106], [278, 37]])
M = cv.getAffineTransform(input_pts, output_pts)
panoramic_dist = cv.warpAffine(skewed, M, (w, h))
cv.imshow("License Plate", panoramic_dist)

input_pts = np.float32([[26, 67], [22, 138], [257, 6]])
output_pts = np.float32([[14, 67], [14, 138], [268, 67]])
affine_matrix = cv.getAffineTransform(input_pts, output_pts)
affine_trans = cv.warpAffine(img, affine_matrix, (w, h))
cv.imshow('Affine Transformation', affine_trans)

input_pts = np.float32([[26, 67], [22, 138], [257, 6], [254, 74]])
output_pts = np.float32([[15, 67], [15, 138], [268, 67], [268, 138]])
perspective_matrix = cv.getPerspectiveTransform(input_pts, output_pts)
perspective_trans = cv.warpPerspective(img, perspective_matrix, (w, h))
cv.imshow('Perspective Transformation', perspective_trans)

cv.waitKey(0)
cv.destroyAllWindows()

