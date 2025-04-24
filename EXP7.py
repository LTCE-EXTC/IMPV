import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('/home/computer/Downloads/img7.jpeg', 0)

# Create a kernel (7x7 matrix of ones)
kernel = np.ones((7, 7), np.uint8)

# Apply erosion
img_erosion = cv2.erode(img, kernel, iterations=1)

# Apply dilation
img_dilation = cv2.dilate(img, kernel, iterations=1)

# Apply opening (erosion followed by dilation)
img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Apply closing (dilation followed by erosion)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Show the results
cv2.imshow('original images', img)
cv2.imshow('erosion', img_erosion)
cv2.imshow('dilation', img_dilation)
cv2.imshow('opening', img_opening)
cv2.imshow('closing', img_closing)

cv2.waitKey(0)
cv2.destroyAllWindows()