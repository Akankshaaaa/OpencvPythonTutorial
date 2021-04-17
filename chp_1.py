import cv2

print("Package imported ")

"""
# read and display image
img = cv2.imread("Resources/baby_dory.jpeg")
cv2.imshow("Output",img)
cv2.waitKey(0)      # adds delay, 0 means infinite delay
"""

"""
# import and display video
cap = cv2.VideoCapture("Resources/sample.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):       # add delay and quit on q key press
        break
"""

# capture webcam
cap = cv2.VideoCapture(0)  # default webcam
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # add delay and quit on q key press
        break
