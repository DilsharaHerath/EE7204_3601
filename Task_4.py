import cv2
import numpy as np

# Load the image
image1 = cv2.imread('./images/nature.jpg', 0)

image_array = np.array(image1)
image_array.shape

# Iterate over the image array in steps of 3 to get each 3x3 matrix
for i in range(0, image_array.shape[0], 3):
    for j in range(0, image_array.shape[1], 3):
        # Extract the 3x3 matrix
        current_matrix = image_array[i:i+3, j:j+3]
        # Calculate the average of the elements in the matrix
        avg = np.sum(current_matrix) / 9
        # Replace all elements in the matrix with the calculated average
        current_matrix[:] = avg

cv2.imshow('3x3 Block', image_array)

# Iterate over the image array in steps of 3 to get each 3x3 matrix
for i in range(0, image_array.shape[0], 5):
    for j in range(0, image_array.shape[1], 5):
        # Extract the 3x3 matrix
        current_matrix = image_array[i:i+5, j:j+5]
        # Calculate the average of the elements in the matrix
        avg = np.sum(current_matrix) / 25
        # Replace all elements in the matrix with the calculated average
        current_matrix[:] = avg

# Print the modified image array
cv2.imshow('5x5 Block', image_array)

# Iterate over the image array in steps of 3 to get each 3x3 matrix
for i in range(0, image_array.shape[0], 7):
    for j in range(0, image_array.shape[1], 7):
        # Extract the 3x3 matrix
        current_matrix = image_array[i:i+7, j:j+7]
        # Calculate the average of the elements in the matrix
        avg = np.sum(current_matrix) / 49
        # Replace all elements in the matrix with the calculated average
        current_matrix[:] = avg

# Print the modified image array
cv2.imshow('7x7 Block', image_array)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()