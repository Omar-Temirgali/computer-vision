from matplotlib import pyplot as plt
import imutils
import cv2

image = cv2.imread("images/3.jpg")
channels = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (channel, color) in zip(channels, colors):
	hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
	plt.plot(hist, color=color)
	plt.xlim([0, 256])

plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))
plt.show()



image1 = cv2.imread("images/4.jpg")
channels1 = cv2.split(image1)
colors1 = ("b", "g", "r")
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (channel, color) in zip(channels1, colors1):
	hist1 = cv2.calcHist([channel], [0], None, [256], [0, 256])
	plt.plot(hist1, color=color)
	plt.xlim([0, 256])

plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image1))
plt.show()
