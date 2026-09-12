import cv2
import os

image_path = os.path.join(os.path.dirname(__file__), "input.jpg")

img = cv2.imread(image_path, 0)

min_val = img.min()
max_val = img.max()

print("Minimum intensity:", min_val)
print("Maximum intensity:", max_val)

stretched = ((img - min_val) * 255 / (max_val - min_val)).astype("uint8")

cv2.imwrite("output.png", stretched)

print("Contrast stretching completed.")