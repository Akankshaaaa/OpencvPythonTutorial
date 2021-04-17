import cv2
import numpy as np

img = cv2.imread("Resources/baby_dory.jpeg")
# check dimensions of an image
print(img.shape)  # outputs (328, 309, 3)

# resize image
imgResize = cv2.resize(img, (500, 450))

# crop image
imgCropped = img[0:250, 170:300]  # here height comes first then width

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
