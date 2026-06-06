# Emotion-Mirror
Emotion Mirror is a real-time emotion recognition application that uses OpenCV and DeepFace to detect faces from a webcam feed and predict emotions such as happy, sad, angry, fear, surprise, and neutral. It features confidence scores, emotion smoothing, multi-face support, and live visualization.

The project emphasizes real-time performance, prediction stability, and user experience through emotion smoothing, asynchronous processing, and confidence visualization.

## Features

* Real-time webcam-based emotion detection
* Face detection using OpenCV Haar Cascade Classifier
* Emotion recognition using DeepFace pre-trained models
* Detection of six primary emotions:

  * Happy
  * Sad
  * Angry
  * Fear
  * Surprise
  * Neutral
* Multiple face support
* Confidence score visualization
* Emotion probability bars
* Emotion smoothing for stable predictions
* Background threaded inference for improved responsiveness
* No-face detection handling

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
3. Extract the detected face region.
4. Perform emotion analysis using DeepFace.
5. Smooth predictions across multiple frames to reduce fluctuations.
6. Apply custom post-processing logic to improve emotion sensitivity.
7. Display the dominant emotion, confidence score, and emotion distribution in real time.

## Key Enhancements

### Real-Time Emotion Smoothing

Emotion predictions can fluctuate significantly between consecutive frames. A rolling buffer is used to average recent predictions, resulting in smoother and more reliable emotion recognition.

### Asynchronous Processing

DeepFace inference is executed in a separate thread, preventing the webcam feed from freezing while emotion analysis is performed.

### Improved Emotion Sensitivity

Custom post-processing logic was implemented to:

* Reduce excessive neutral predictions
* Improve sensitivity to subtle emotional expressions
* Stabilize emotion transitions using threshold-based switching

### Enhanced Visualization

The application provides:

* Face bounding boxes
* Dominant emotion labels
* Confidence percentages
* Top emotion probability bars

These additions improve interpretability and make predictions easier to understand.

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
* Maintaining smooth real-time performance during inference
* Handling the dominance of neutral predictions in pre-trained models
* Improving responsiveness without blocking the webcam feed

These challenges were addressed through emotion smoothing, threaded inference, and custom post-processing techniques.

## Future Improvements

* Replace Haar Cascade with MediaPipe face detection
* Add face tracking for improved multi-person support
* Deploy as a web application
* Integrate more advanced emotion recognition models
* Add historical emotion analytics and session summaries

## License

This project is licensed under the MIT License. See the LICENSE file for details.
son obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
