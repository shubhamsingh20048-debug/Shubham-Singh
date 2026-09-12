import cv2
import numpy as np
img = cv2.imread("input.jpg", 0)

dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

mask = np.zeros((rows, cols), np.uint8)
size = 30
mask[crow-size:crow+size, ccol-size:ccol+size] = 1
filtered_dft = dft_shift * mask
filtered_dft = np.fft.ifftshift(filtered_dft)
result = np.fft.ifft2(filtered_dft)
result = np.abs(result)
result = np.uint8(result)

cv2.imwrite("output.png", result)

print("Low-pass filtered image saved as output.png")