import cv2
import numpy
from matplotlib import pyplot as plt
import imutils
import os

img1 = cv2.imread('images/3.jpg')
img2 = cv2.imread('images/5.jpg')
colors = ("b", "g", "r")

hist1 = cv2.calcHist([img1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist1 = cv2.normalize(hist1, hist1).flatten()
channels1 = cv2.split(img1)
plt.figure()
plt.title('img1')
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (channel, color) in zip(channels1, colors):
	hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(img1))

hist2 = cv2.calcHist([img2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist2 = cv2.normalize(hist2, hist2).flatten()
channels2 = cv2.split(img2)
plt.figure()
plt.title('img2')
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (channel, color) in zip(channels2, colors):
	hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(img2))

print(cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL))
plt.show()


