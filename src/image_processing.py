
import cv2

# Step 1: Load the image
image = cv2.imread("data/sample_images/car.jpg")

if image is None:
    print("Image not found!")

else:
    print("Image loaded successfully!")

    # Step 2: Resize the image
    resized = cv2.resize(image, (500, 500))

    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 4: Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 5: Apply thresholding
    ret, threshold = cv2.threshold(
        blurred, 127, 255, cv2.THRESH_BINARY
    )

    # Display all processed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Blurred Image", blurred)
    cv2.imshow("Threshold Image", threshold)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
