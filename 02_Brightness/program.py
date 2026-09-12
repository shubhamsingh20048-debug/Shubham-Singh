import cv2
image = cv2.imread("input.jpg")

brightness = 180
bright_image = cv2.add(image, brightness)
cv2.imwrite("output.png", bright_image)

print("Pixel before:", image[100, 100])
print("Pixel after:", bright_image[100, 100])