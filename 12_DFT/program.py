import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

image_float = np.float32(image)
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted_dft = np.fft.fftshift(dft)
print("Original image shape:", image.shape)
print("DFT result shape:", dft.shape)
print("Shifted DFT result shape:", shifted_dft.shape)
magnitude = cv2.magnitude(shifted_dft[:, :, 0],
                          shifted_dft[:, :, 1])

magnitude = np.log(1 + magnitude)
magnitude = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)
cv2.imwrite("output.png", magnitude)

print("DFT result saved as output.png")