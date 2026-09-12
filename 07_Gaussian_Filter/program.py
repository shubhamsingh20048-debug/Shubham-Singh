import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imwrite("output.png", gaussian_image)

print("Gaussian smoothing completed.")
print("Output saved as output.png")