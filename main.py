"""
Project by Clinton Anani
This project demonstrates how
to draw shapes on images

github: yendiDev
email: kceequan01@gmail.com
"""

import cv2

# read in image
img = cv2.imread('lena.jpg', 0)

# draw line on same image
img = cv2.line(img, (0, 0), (255, 255), (255, 23, 9), 23)

# draw arrowed line
img = cv2.arrowedLine(img, (120, 300), (300, 300), (0, 255, 0), 10)

# draw rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5)

# draw circle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# write text on image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 100), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

# display image
cv2.imshow('image', img)

cv2.waitKey(0)