import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # use 3 channel to add color
# print(img)

# color a part of the image blue
# img[200:300, 300:400] = 255, 0, 0

# line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# circle
cv2.circle(img, (400, 200), 30, (255, 255, 0), 4)

# put text on image
cv2.putText(img, "OpenCV", (300, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 150, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
