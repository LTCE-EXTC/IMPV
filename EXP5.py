import numpy as np
import cv2

# Read image in grayscale
img1 = cv2.imread('/home/computer/Desktop/images.png', 0)

# Get the number of rows and columns
m, n = img1.shape

# Sobel mask for horizontal edge detection
mask = np.array([[-1, -2, -1],
                 [ 0,  0,  0],
                 [ 1,  2,  1]])

# Create an output image
img_new = np.zeros((m, n))

# Convolve with Sobel horizontal mask
for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = (img1[i-1, j-1]*mask[0,0] + img1[i-1, j]*mask[0,1] + img1[i-1, j+1]*mask[0,2] +
                img1[i,   j-1]*mask[1,0] + img1[i,   j]*mask[1,1] + img1[i,   j+1]*mask[1,2] +
                img1[i+1, j-1]*mask[2,0] + img1[i+1, j]*mask[2,1] + img1[i+1, j+1]*mask[2,2])
        img_new[i, j] = temp

img_new1 = np.clip(img_new, 0, 255).astype(np.uint8)

# Display horizontal edges
cv2.imshow('INPUT IMAGE', img1)
cv2.imshow('Horizontal Edges', img_new1)

# Sobel mask for vertical edge detection
mask = np.array([[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]])

# Reset output image
img_new = np.zeros((m, n))

# Convolve with Sobel vertical mask
for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = (img1[i-1, j-1]*mask[0,0] + img1[i-1, j]*mask[0,1] + img1[i-1, j+1]*mask[0,2] +
                img1[i,   j-1]*mask[1,0] + img1[i,   j]*mask[1,1] + img1[i,   j+1]*mask[1,2] +
                img1[i+1, j-1]*mask[2,0] + img1[i+1, j]*mask[2,1] + img1[i+1, j+1]*mask[2,2])
        img_new[i, j] = temp

img_new2 = np.clip(img_new, 0, 255).astype(np.uint8)

# Display vertical edges
cv2.imshow('Vertical Edges', img_new2)

cv2.waitKey(0)
cv2.destroyAllWindows()