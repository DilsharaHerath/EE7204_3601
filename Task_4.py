# Herath HMKDB
# EG/2019/3601

# Importing libraries
import cv2
import numpy as np

# Loading the image
image1 = cv2.imread('./images/dog3.jpg', 0)

# Converting the original input image to a NumPy array
image_array = np.array(image1)
# image_array.shape

# Displaying the original (gray scaled) image
cv2.imshow('Original Image (Gray Scaled)', image1)

# Iterating over the image array in steps of 3 to get each 3x3 matrix
for i in range(0, image_array.shape[0], 3):
    for j in range(0, image_array.shape[1], 3):
        # Extracting the 3x3 matrix
        current_matrix = image_array[i:i+3, j:j+3]
        # Calculating the average of the elements in the matrix
        avg = np.sum(current_matrix) / 9
        # Replacing all elements in the matrix with the calculated average
        current_matrix[:] = avg

# Displaying the modified image
cv2.imshow('3x3 Block', image_array)

# Iterating over the image array to get each 5x5 matrix
for i in range(0, image_array.shape[0], 5):
    for j in range(0, image_array.shape[1], 5):
        # Extracting the 3x3 matrix
        current_matrix = image_array[i:i+5, j:j+5]
        # Calculating the average of the elements in the matrix
        avg = np.sum(current_matrix) / 25
        # Replacing all elements in the matrix with the calculated average
        current_matrix[:] = avg

# Displaying the modified image
cv2.imshow('5x5 Block', image_array)

# Iterating over the image array to get each 7x7 matrix
for i in range(0, image_array.shape[0], 7):
    for j in range(0, image_array.shape[1], 7):
        # Extracting the 3x3 matrix
        current_matrix = image_array[i:i+7, j:j+7]
        # Calculating the average of the elements in the matrix
        avg = np.sum(current_matrix) / 49
        # Replacing all elements in the matrix with the calculated average
        current_matrix[:] = avg

# Displaying the modified image
cv2.imshow('7x7 Block', image_array)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()