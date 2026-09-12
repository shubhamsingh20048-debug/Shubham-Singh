import cv2
import numpy as np
import os

folder = os.path.dirname(os.path.abspath(__file__))

img = cv2.imread(os.path.join(folder, "input.jpg"), 0)

if img is None:
    print("Error: input.jpg not found!")
    exit()

dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
magnitude = np.abs(dft_shift)
magnitude = 20 * np.log(magnitude + 1)
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
magnitude = np.uint8(magnitude)

cv2.imwrite(os.path.join(folder, "output.png"), magnitude)

print("Magnitude Spectrum saved successfully!")