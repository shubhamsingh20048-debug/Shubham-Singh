import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

small_kernel = cv2.blur(image, (3, 3))
cv2.imwrite("output_3x3.png", small_kernel)

large_kernel = cv2.blur(image, (5, 5))

cv2.imwrite("output.png", large_kernel)

print("3x3 mean filter applied and saved as output_3x3.png")
print("5x5 mean filter applied and saved as output.png")