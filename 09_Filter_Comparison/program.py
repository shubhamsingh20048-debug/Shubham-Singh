import cv2
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

mean_image = cv2.blur(image, (5, 5))

gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)

median_image = cv2.medianBlur(image, 5)
cv2.imwrite("output_mean.png", mean_image)
cv2.imwrite("output_gaussian.png", gaussian_image)
cv2.imwrite("output_median.png", median_image)

print("Mean filter result saved as output_mean.png")
print("Gaussian filter result saved as output_gaussian.png")
print("Median filter result saved as output_median.png")