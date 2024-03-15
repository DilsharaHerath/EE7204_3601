# Herath HMKDB
# EG/2019/3601

# Importing libraries
import cv2
import numpy as np

# Loading the image
image1 = cv2.imread('./images/dog3.jpg')

# Getting the height and width of the original input image, rotating the image by 45-degree anticlockwise
height, width = image1.shape[0:2]
matrix =cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
translated = cv2.warpAffine(image1, matrix, (width, height))

# Displaying the rotated image
cv2.imshow('45 Degrees Anticlockwise Rotated Image', translated)

# Getting the height and width of the original input image, rotating the image by 90-degree anticlockwise
height, width = image1.shape[0:2]
matrix =cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
translated = cv2.warpAffine(image1, matrix, (width, height))

# Displaying the rotated image
cv2.imshow('90 Degrees Anticlockwise Rotated Image', translated)

# Getting the height and width of the original input image, rotating the image by 45-degree Clockwise
height, width = image1.shape[0:2]
matrix =cv2.getRotationMatrix2D((width/2, height/2), -45, 1)
translated = cv2.warpAffine(image1, matrix, (width, height))

# Displaying the rotated image
cv2.imshow('45 Degrees Clockwise Rotated Image', translated)

# Getting the height and width of the original input image, rotating the image by 90-degree Clockwise
height, width = image1.shape[0:2]
matrix =cv2.getRotationMatrix2D((width/2, height/2), -90, 1)
translated = cv2.warpAffine(image1, matrix, (width, height))

# Displaying the rotated image
cv2.imshow('90 Degrees Clockwise Rotated Image', translated)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()