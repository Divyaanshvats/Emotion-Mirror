# Emotion-Mirror

Emotion Mirror is a real-time emotion recognition application built using Python, OpenCV, and DeepFace. The application captures live webcam footage, detects faces in real time, and predicts emotions such as happy, sad, angry, fear, surprise, and neutral.

The project focuses on delivering stable real-time emotion recognition through asynchronous processing, prediction smoothing, confidence visualization, and independent multi-face emotion tracking.

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
* Simultaneous multi-face emotion recognition
* Independent emotion history and smoothing for each detected face
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
2. Detect one or more faces using OpenCV's Haar Cascade classifier.
3. Extract each detected face region.
4. Perform emotion analysis using DeepFace.
5. Maintain independent emotion buffers for each detected face.
6. Smooth predictions across multiple frames to reduce fluctuations.
7. Apply custom post-processing logic to improve emotion sensitivity.
8. Display the dominant emotion, confidence score, and emotion distribution in real time.

## Key Enhancements

### Real-Time Emotion Smoothing

Emotion predictions can fluctuate significantly between consecutive frames. A rolling buffer is used to average recent predictions, resulting in smoother and more reliable emotion recognition.

### Asynchronous Processing

DeepFace inference is executed in a separate thread, preventing the webcam feed from freezing while emotion analysis is performed.

### Independent Multi-Face Tracking

Each detected face maintains its own emotion history, confidence tracking, and smoothing buffer. This prevents predictions from one person affecting another person's emotion analysis.

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

## Challenges Encountered

* Managing fluctuating emotion predictions across frames
* Maintaining smooth real-time performance during inference
* Handling the dominance of neutral predictions in pre-trained models
* Supporting multiple faces without mixing prediction histories
* Improving responsiveness without blocking the webcam feed

These challenges were addressed through emotion smoothing, threaded inference, and independent per-face emotion tracking.

**##What I Learned and Found Challenging**

1. Creating the application itself was not an issue, but making changes to improve the detection of specific emotions was challenging.

2. One of the main challenges was changing the sensitivity of the model to make it more accustomed to my facial expressions. Handling multiple faces simultaneously was also challenging, as each face needed to       maintain its own emotion history and prediction state.

3. I also observed that DeepFace has a bias toward predicting neutral emotions. To address this, I modified the code so that it could better recognize other emotions instead of defaulting to neutral too often.

4. Another challenge was tuning the constraints and parameters. I had to adjust them multiple times before reaching a configuration that produced satisfactory results.

5. Overall, it was an interesting learning experience. It helped me understand emotion recognition in practice and gave me a better understanding of face and object detection concepts.

## License

This project is released for educational and demonstration purposes as part of the Bipolar Factory Emotion Mirror assignment.

Copyright (c) 2026 Divyaansh Vats

Permission is granted to use, modify, and distribute this project with appropriate attribution.
