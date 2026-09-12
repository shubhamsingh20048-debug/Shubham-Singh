import cv2

# Read color image
import os

image_path = os.path.join(os.path.dirname(__file__), "input.jpg")
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output.png", gray)

print("Original Image Shape:", image.shape)
print("Grayscale Image Shape:", gray.shape)
print("Height:", image.shape[0])
print("Width:", image.shape[1])