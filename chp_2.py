import cv2
import numpy as np

img = cv2.imread("Resources/baby_dory.jpeg")

kernel = np.ones((5, 5), np.uint8)  # 5x5 matrix of ones
# grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # ksize has to have odd number

# Canny image detection
imgCanny = cv2.Canny(img, 150, 200)

# image Dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# image Erosion
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Erosion Image", imgEroded)


cv2.waitKey(0)
