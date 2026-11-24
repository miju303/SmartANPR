# SmartANPR – Vehicle Detection and Automatic Number Plate Recognition

**A Computer Vision Project for Vehicle Detection and Number Plate Recognition**

## 1. Project Overview

SmartANPR is a computer vision-based project focused on detecting vehicles and recognizing their registration numbers from traffic images and video footage.

The project aims to explore image processing, vehicle detection, object tracking and Optical Character Recognition (OCR) to support automated vehicle identification.

The initial development phase focuses on understanding image and video processing techniques using Python and OpenCV.

## 2. Project Objectives

- Process vehicle images and traffic video frames.
- Detect and identify vehicles in traffic scenes.
- Locate vehicles using bounding boxes.
- Extract vehicle registration numbers using OCR.
- Explore vehicle tracking across consecutive video frames.
- Develop a structured pipeline for automatic number plate recognition.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| OpenCV | Image and video processing |
| NumPy | Numerical and array operations |
| YOLO | Vehicle detection (planned) |
| DeepSORT | Object tracking (planned) |
| OCR | Number plate text recognition (planned) |

## 4. Project Structure

```text
SmartANPR/
│
├── data/
│   ├── webcam_practice/
│   ├── captured_frames/
│   ├── sample_images/
│   └── sample_videos/
│
├── src/
│   ├── image_processing.py
│   ├── webcam_capture.py
│   ├── bounding_box.py
│   └── video_frame_capture.py
│
├── venv/
│
├── requirements.txt
├── README.md
├── week1_learning_note.md
└── .gitignore
```

## 5. Week 1 – Implementation and Learning

The first development phase focused on Python setup, image processing and basic computer vision operations.

### Image Processing
- Loaded and displayed vehicle images using OpenCV.
- Examined image dimensions, resolution and colour channels.
- Implemented image resizing.
- Converted colour images into grayscale.
- Applied Gaussian blur to reduce image noise.
- Performed thresholding to generate binary images.

### Video Processing
- Accessed the laptop webcam using OpenCV.
- Captured and displayed live video frames.
- Saved individual webcam frames as image files.
- Loaded a traffic video and extracted individual frames.
- Collected 13 vehicle frames for further experimentation.

### Object Detection Fundamentals
- Studied the concept of object detection.
- Understood bounding box coordinates and dimensions.
- Implemented manual bounding box selection using OpenCV.
- Added labels to selected vehicles.

## 6. Getting Started

### Prerequisites

- Python 3
- Visual Studio Code (recommended)
- Webcam (for webcam capture practical)

### Installation

**Step 1: Clone the repository**

```bash
git clone <your-github-repository-url>
```

**Step 2: Navigate to the project directory**

```bash
cd SmartANPR
```

**Step 3: Create a virtual environment**

```bash
python -m venv venv
```

**Step 4: Activate the virtual environment**

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**Step 5: Install dependencies**

```bash
pip install -r requirements.txt
```

## 7. Running the Scripts

Run the image processing program:

```bash
python src/image_processing.py
```

Run the webcam capture program:

```bash
python src/webcam_capture.py
```

Run the bounding box demonstration:

```bash
python src/bounding_box.py
```

Extract frames from the traffic video:

```bash
python src/video_frame_capture.py
```

## 8. Current Development Status

| Module | Status |
|---|---|
| Python environment setup | Completed |
| Basic image processing | Completed |
| Webcam frame capture | Completed |
| Traffic video frame extraction | Completed |
| Manual bounding box demonstration | Completed |
| Automatic vehicle detection | Planned |
| Vehicle tracking | Planned |
| Number plate detection | Planned |
| OCR-based text recognition | Planned |

## 9. Future Scope

- Integrate a YOLO-based vehicle detection model.
- Implement vehicle tracking using DeepSORT.
- Detect and extract vehicle number plates.
- Integrate OCR for registration number recognition.
- Develop an end-to-end vehicle detection and recognition pipeline.

## 10. Author

**Miju Akshaya**

Computer Science and Engineering (Artificial Intelligence and Machine Learning)

**Project:** SmartANPR – Vehicle Detection and Automatic Number Plate Recognition