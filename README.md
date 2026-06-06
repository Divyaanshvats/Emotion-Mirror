# Emotion-Mirror
Emotion Mirror is a real-time emotion recognition application that uses OpenCV and DeepFace to detect faces from a webcam feed and predict emotions such as happy, sad, angry, fear, surprise, and neutral. It features confidence scores, emotion smoothing, multi-face support, and live visualization.

# Emotion Mirror

Emotion Mirror is a real-time facial emotion recognition application built using Python, OpenCV, and DeepFace. The application captures live webcam footage, detects faces in real time, and predicts the dominant emotion for each detected face.

The project focuses on delivering a smooth and user-friendly experience while handling practical challenges such as fluctuating predictions, multiple faces in a frame, and neutral emotion dominance.

## Features

* Real-time webcam-based emotion detection
* Face detection using OpenCV Haar Cascade Classifier
* Emotion recognition using DeepFace pre-trained models
* Support for multiple faces in a single frame
* Emotion confidence score visualization
* Emotion probability bars for improved interpretability
* Real-time emotion smoothing to reduce prediction flickering
* Asynchronous emotion analysis using threading for better performance
* No-face detection handling
* Lightweight and easy to run locally

## Technologies Used

* Python
* OpenCV
* DeepFace
* TensorFlow
* Threading
* Collections (Deque)

## System Workflow

1. Capture live video frames from the webcam.
2. Detect faces using OpenCV's Haar Cascade classifier.
3. Crop detected face regions.
4. Perform emotion analysis using DeepFace.
5. Apply smoothing across recent predictions to improve stability.
6. Use custom post-processing logic to improve sensitivity toward subtle emotions.
7. Display the dominant emotion, confidence score, and emotion distribution in real time.

## Key Improvements Implemented

### Emotion Smoothing

Raw emotion predictions often fluctuate between consecutive frames. A rolling buffer is used to average predictions across multiple frames, resulting in more stable and consistent outputs.

### Asynchronous Inference

Emotion analysis runs in a background thread, allowing the webcam feed to remain responsive while DeepFace performs inference.

### Enhanced Emotion Sensitivity

Additional post-processing logic was introduced to:

* Reduce the dominance of neutral predictions
* Improve detection sensitivity for subtle emotions
* Stabilize emotion transitions using configurable thresholds

### Visualization Enhancements

The application displays:

* Bounding boxes around detected faces
* Dominant emotion labels
* Confidence scores
* Top emotion probability bars

These additions improve transparency and make model predictions easier to interpret.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Emotion-Mirror
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## Challenges Encountered

* Managing fluctuating emotion predictions across frames
* Maintaining real-time performance during inference
* Handling neutral emotion bias in pre-trained emotion models
* Improving responsiveness without blocking the webcam feed

These challenges were addressed through smoothing, threading, and custom post-processing techniques.

## Future Improvements

* Replace Haar Cascade with MediaPipe face detection
* Face tracking for improved multi-person support
* Web-based deployment
* Integration of more advanced emotion recognition models
* Historical emotion analytics and session summaries

## License

This project is licensed under the MIT License.

Copyright (c) 2026 Divyaansh Vats

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
