# Herath HMKDB
# EG/2019/3601

# Importing libraries
import cv2
import numpy as np

# Loading the image
image1 = cv2.imread('./images/dog3.jpg')

# Defining 3x3 averaging kernels
kernel_3 = np.ones((3,3), dtype=np.float32) / 9
kernel_10 = np.ones((10,10), dtype=np.float32) / 100
kernel_20 = np.ones((20,20), dtype=np.float32) / 400

# Applying the defined kernels to the image
out_3 = cv2.filter2D(image1, -1, kernel_3)
out_10 = cv2.filter2D(image1, -1, kernel_10)
out_20 = cv2.filter2D(image1, -1, kernel_20)

# Displaying the original and the filter applied images
cv2.imshow('Original Image', image1)
cv2.imshow('Spatial filter: 3x3 Image', out_3)
cv2.imshow('Spatial filter: 10x10 Image', out_10)
cv2.imshow('Spatial filter: 20x20 Image', out_20)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()