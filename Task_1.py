# Herath HMKDB
# EG/2019/3601

# Importing libraries 
import cv2
import numpy as np

# Loading the image
image1 = cv2.imread('./images/dog3.jpg',0)

# Prompting the user to enter the value for the power of the intensity level-k (2^k)
k = input('Enter the value for k: ')
k = int(k)
k = 8-k

# Calculating the intensity level and compression
intensity_level = 2 ** k

# Image compression
img1_reduced = np.uint8(np.floor(np.double(image1) / intensity_level))

# Normalizing the image
norm_image = cv2.normalize(img1_reduced, None, 0, 255, norm_type=cv2.NORM_MINMAX)

# Displaying the original and the compressed image
cv2.imshow('Original Image (Gray Scaled)', image1)
cv2.imshow('Compressed Image', norm_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
