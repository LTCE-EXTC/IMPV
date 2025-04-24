import numpy as np
import cv2

img1 = cv2.imread('/home/computer/Desktop/image.jpeg', 0)

# Get the dimensions of the image
m, n = img1.shape

# High-pass filter (HPF) mask
mask = np.ones((3, 3))
mask[1, 1] = -8

# Initialize a new image with zeros
img_new = np.zeros((m, n))

# Apply convolution with the HPF mask
for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = (
            img1[i - 1, j - 1] * mask[0, 0] +
            img1[i - 1, j] * mask[0, 1] +
            img1[i - 1, j + 1] * mask[0, 2] +
            img1[i, j - 1] * mask[1, 0] +
            img1[i, j] * mask[1, 1] +
            img1[i, j + 1] * mask[1, 2] +
            img1[i + 1, j - 1] * mask[2, 0] +
            img1[i + 1, j] * mask[2, 1] +
            img1[i + 1, j + 1] * mask[2, 2]
        )
        img_new[i, j] = temp

# Convert the result to unsigned 8-bit integer
img_new = img_new.astype(np.uint8)

# Show images
cv2.imshow('Input Image', img1)
cv2.imshow('HPF Image', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()