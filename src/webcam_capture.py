
import cv2

# Step 1: Open the laptop webcam using DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Step 2: Check whether the camera opened
if not cap.isOpened():
    print("Cannot access the camera!")

else:
    print("Camera started successfully!")

    frame_count = 0

    # Step 3: Continuously capture video frames
    while True:

        ret, frame = cap.read()

        # Step 4: Check whether frame was captured
        if not ret:
            print("Cannot receive frame!")
            break

        # Step 5: Display live webcam video
        cv2.imshow("Live Webcam", frame)

        # Step 6: Read keyboard input
        key = cv2.waitKey(1) & 0xFF

        # Debugging: Display the pressed key
        if key != 255:
            print("Key pressed:", key)

        # Step 7: Press S to save the frame
        if key == ord('s') or key == ord('S'):

            frame_count += 1

            filename = f"data/captured_frames/frame_{frame_count}.png"

            cv2.imwrite(filename, frame)

            print("Frame saved:", filename)

        # Step 8: Press Q to quit
        elif key == ord('q') or key == ord('Q'):
            print("Closing webcam...")
            break

# Step 9: Release camera
cap.release()

# Step 10: Close all OpenCV windows
cv2.destroyAllWindows()

print("Webcam closed successfully!")
