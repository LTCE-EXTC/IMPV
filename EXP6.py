import numpy as np
import cv2

# Read image in grayscale
img = cv2.imread('/home/computer/Desktop/rose.jpeg', 0)
cv2.imshow('ip', img)

# Get image dimensions
m, n = img.shape

# Crop a portion of the image [Rows: 10 to 250, Columns: 50 to 390]
cropped_image = img[10:250, 50:390]
cv2.imshow('cropped', cropped_image)

# Resize to smaller dimensions (downscale)
down_width = 100
down_height = 100
down_points = (down_width, down_height)
resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)

# Resize to larger dimensions (upscale)
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(img, up_points, interpolation=cv2.INTER_LINEAR)

# Show results
cv2.imshow('resize down', resized_down)
cv2.imshow('resize up', resized_up)

cv2.waitKey(0)
cv2.destroyAllWindows()