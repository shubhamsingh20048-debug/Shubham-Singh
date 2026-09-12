import cv2
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

median_image = cv2.medianBlur(image, 5)
cv2.imwrite("output.png", median_image)

print("Median filtering completed.")
print("Output saved as output.png")