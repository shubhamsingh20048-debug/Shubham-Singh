import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

intensity = np.argmax(histogram)

print("Intensity with highest frequency:", intensity)

plt.plot(histogram)
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.title("Image Histogram")
plt.savefig("output.png")
plt.close()

print("Histogram saved as output.png")

print("Histogram saved successfully as output.png")
