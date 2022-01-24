import os
import cv2
import imutils
from matplotlib import pyplot as plt

images = {}
image_original = cv2.imread('original3.jpg')
hist_original = cv2.calcHist([image_original], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
hist_original = cv2.normalize(hist_original, hist_original).flatten()

for image in os.listdir('images/'):
    img = cv2.imread('images/' + image)
    hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    images[image] = cv2.compareHist(hist_original, hist, cv2.HISTCMP_CORREL)

def get_max_key(val):
    for key, value in images.items():
        if val == value:
            return key

    return "key doesn't exist"

def histAndImage(image, image_name):
    colors = ("b", "g", "r")
    channels = cv2.split(image)
    plt.figure()
    plt.title(image_name)
    plt.xlabel("Bins")
    plt.ylabel("Num of Pixels")

    for (channel, color) in zip(channels, colors):
	    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
	    plt.plot(hist, color=color)
	    plt.xlim([0, 256])

    plt.figure()
    plt.axis("off")
    plt.title(image_name)
    plt.imshow(imutils.opencv2matplotlib(image))

values = images.values()
max = max(values)
image_name = get_max_key(max)

print(max)
histAndImage(image_original, 'original')
histAndImage(cv2.imread('images/' + image_name), 'similar')
plt.show()