
import cv2

# Step 1: Load the vehicle image
image = cv2.imread("data/sample_images/car.jpg")

if image is None:
    print("Image not found!")

else:
    print("Vehicle image loaded successfully!")

    # Step 2: Select the vehicle using your mouse
    print("Draw a rectangle around the vehicle.")
    print("Press ENTER or SPACE after selecting.")

    x, y, w, h = cv2.selectROI("Select Vehicle", image)

    # Step 3: Draw the bounding box
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

    # Step 4: Add a label
    cv2.putText(
        image,
        "Vehicle",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Step 5: Display the result
    cv2.imshow("Vehicle Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
