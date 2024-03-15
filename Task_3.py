import cv2
import numpy as np

# Load the image
image1 = cv2.imread('./images/nature.jpg')

height, width = image1.shape[0:2]
matrix =cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
translated = cv2.warpAffine(image1, matrix, (width, height))

cv2.imshow('45 Degrees Rotated Image', translated)

height, width = image1.shape[0:2]
matrix =cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
translated = cv2.warpAffine(image1, matrix, (width, height))

cv2.imshow('90 Degrees Rotated Image', translated)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()