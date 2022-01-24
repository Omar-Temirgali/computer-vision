import os
import cv2
from random import seed
from random import random

seed(1)
images = {}
# image_original = cv2.imread('original.jpg')
# hist_original = cv2.calcHist([image_original], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
# print(len(os.listdir('images/')))

for image_path in os.listdir('images/'):
    images[image_path] = random()

print(images)
all_values = images.values()
print(max(all_values))
print(max(images, key=images.get))

