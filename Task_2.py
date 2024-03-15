import cv2
import numpy as np

# Load the image
image1 = cv2.imread('./images/lena.png')

kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])
kernel_3 = np.ones((3,3), dtype=np.float32) / 9
kernel_10 = np.ones((10,10), dtype=np.float32) / 100
kernel_20 = np.ones((20,20), dtype=np.float32) / 400

out1 = cv2.filter2D(image1, -1, kernel_identity)
out_3 = cv2.filter2D(image1, -1, kernel_3)
out_10 = cv2.filter2D(image1, -1, kernel_10)
out_20 = cv2.filter2D(image1, -1, kernel_20)



# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()