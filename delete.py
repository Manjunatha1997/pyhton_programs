

# importing libraries
import cv2
import numpy as np

# reading the image data from desired directory
img = cv2.imread("dent_2a_22_1.jpg")
# cv2.imshow('Image',img)

# counting the number of pixels
total_pixels = np.sum(img)
print(total_pixels)





