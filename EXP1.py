import numpy as np
import cv2

t = cv2.imread("C:\\Users\\Lenovo\\Downloads\\01IP (3).jpeg", 0)

# Negative Image
cv2.imshow("Image", t)
neg_img = 255 - t
cv2.imshow("Negative Image", neg_img)
cv2.imwrite('pea.png', t)

# Gray Level Slicing
if t is None:
    print("Error: Image not found!")
else:
    min_val = 100
    max_val = 150

    sliced_img = np.zeros_like(t)
    sliced_img[(t >= min_val) & (t <= max_val)] = 255

    cv2.imshow('Gray Level Sliced Image', sliced_img)

# Log Transformation
if t is None:
    print("Error: Image not found!")
else:
    t_log = np.log1p(np.float32(t))
    t_log = np.uint8(255 * t_log / np.max(t_log))

    cv2.imshow('Logarithmic Transformed Image', t_log)

cv2.waitKey(0)
cv2.destroyAllWindows()
