from matplotlib import pyplot as plt
import numpy as np
import cv2

# Read the image in grayscale
img = cv2.imread("/home/computer/Downloads/images.jpeg", 0)
cv2.imshow('input image', img)

# Original histogram and CDF
hist, bins = np.histogram(img.flatten(), 256, [0, 255])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 255], color='r')
plt.xlim([0, 255])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

# Histogram Equalization
equ = cv2.equalizeHist(img)

# Equalized histogram and CDF
hist, bins = np.histogram(equ.flatten(), 256, [0, 255])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(equ.flatten(), 256, [0, 255], color='r')
plt.xlim([0, 255])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

# Show equalized image
cv2.imshow('equalized Image.png', equ)
cv2.waitKey(0)
cv2.destroyAllWindows()