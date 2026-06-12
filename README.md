# Hand Gesture Controlled Image Viewer

## Overview
Hand Gesture Controlled Image Viewer is a computer vision project that enables users to manipulate images on a laptop screen using hand gestures. The system uses a webcam and real-time hand tracking to detect finger movements and convert them into image control actions such as rotation and zooming.
This project demonstrates the application of Computer Vision, Human-Computer Interaction (HCI), and Gesture Recognition using Python, OpenCV, and MediaPipe.

## Features
* Real-time hand tracking
* Image rotation using hand movement
* Zoom In and Zoom Out using finger gestures
* Touch-free image manipulation
* Webcam-based interaction
* User-friendly interface

## Technologies Used
* Python 3
* OpenCV
* MediaPipe
* NumPy

## Project Structure
GestureImageControl/
│
├── main.py
├── hand_tracker.py
├── image_controller.py
├── image.jpg
├── requirements.txt
└── README.md

## Installation

1. Clone the repository:
git clone https://github.com/your-username/GestureImageControl.git
cd GestureImageControl

2. Install dependencies:
pip install -r requirements.txt

Or install manually:
pip install opencv-python mediapipe numpy


## Usage
1. Place the image you want to control inside the project folder and name it `image.jpg`.

2. Run the application: python main.py

3. Use your hand gestures in front of the webcam:
* Move thumb and index finger apart → Zoom In
* Move thumb and index finger closer → Zoom Out
* Rotate hand → Rotate image

4. Press `ESC` to exit.

## How It Works

The system uses MediaPipe Hands to detect 21 hand landmarks in real time.

### Zoom Control
The distance between:
* Thumb Tip & Index Finger Tip is used to determine zoom level.


## Rotation Control
The orientation of the hand is calculated using:

* Wrist & Middle Finger Tip mapped to image rotation.


## Applications
* Touchless User Interfaces
* Smart Classrooms
* Interactive Presentations
* Medical Image Viewing
* Virtual Reality Systems
* Human-Computer Interaction Research



## Future Enhancements
* Image translation (move image on screen)
* Multi-hand gesture support
* 3D object manipulation
* PDF and document control
* PowerPoint presentation control
* AI-based custom gesture recognition
* Voice command integration

## Results
The project successfully tracks hand movements and performs real-time image rotation and zooming without requiring any physical contact with the computer.


This project is open-source and available under the MIT License.
