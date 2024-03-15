import cv2
import numpy as np

# Load the image
image1 = cv2.imread('./images/dog.jpg',0)

# Ask the user to enter the value for k
# k = input('Enter the value for k: ')
# k = int(k)
# k = 8-k

k=12
k=8-k

# Calculate intensity level and compression
intensity_level = 2 ** k
current_compression = 255 / intensity_level

# Perform image compression
img1_reduced = np.uint8(np.floor(np.double(image1) / intensity_level))

# Normalize the image
norm_image = cv2.normalize(img1_reduced, None, 0, 255, norm_type=cv2.NORM_MINMAX)

# Display the compressed image
cv2.imshow('Compressed Image', norm_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
