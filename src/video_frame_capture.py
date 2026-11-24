
import cv2
import os

# Open the traffic video
video_path = "data/sample_videos/traffic.mp4"
cap = cv2.VideoCapture(video_path)

# Create output folder
output_folder = "data/captured_frames"
os.makedirs(output_folder, exist_ok=True)

if not cap.isOpened():
    print("Cannot open traffic video!")

else:
    print("Traffic video opened successfully!")

    frame_count = len([
    name for name in os.listdir(output_folder)
    if name.startswith("vehicle_") and name.endswith(".png")
])

    while True:
        # Read each video frame
        ret, frame = cap.read()

        if not ret:
            print("Video ended!")
            break

        # Display traffic video
        cv2.imshow("Traffic Video", frame)

        # Read keyboard input
        key = cv2.waitKey(25) & 0xFF

        # Press S to save a frame
        if key == ord('s') or key == ord('S'):
            frame_count += 1

            filename = os.path.join(
                output_folder,
                f"vehicle_{frame_count}.png"
            )

            cv2.imwrite(filename, frame)
            print("Saved:", filename)

        # Press Q to stop
        elif key == ord('q') or key == ord('Q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Total frames saved:", frame_count)
