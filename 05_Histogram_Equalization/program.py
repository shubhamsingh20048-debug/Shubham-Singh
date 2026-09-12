import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

equalized_image = cv2.equalizeHist(image)
cv2.imwrite("output.png", equalized_image)

hist_before = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_after = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

plt.plot(hist_before, label="Before Equalization")
plt.plot(hist_after, label="After Equalization")

plt.title("Histogram Before and After Equalization")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("histogram_comparison.png")
plt.close()

print("Histogram equalization completed.")
print("Equalized image saved as output.png")
print("Comparison histogram saved as histogram_comparison.png")