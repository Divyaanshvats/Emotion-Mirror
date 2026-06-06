import cv2
from deepface import DeepFace
import threading
import collections

# The next lines handles Emoji
EMOJI_MAP={
    "happy": ":D",
    "sad": ":(",
    "angry": ">:(",
    "fear": "D:",
    "surprise": ":O",
    "neutral": ":|",
    "disgust": ":S"
}

# The following code will be for FACE DETECTION
face_detector=cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#WEBCAM
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to access webcam")
    exit()

# Smoothing buffer: stores last N emotion score dicts per face slot
SMOOTH_FRAMES = 8
emotion_buffer = collections.deque(maxlen=SMOOTH_FRAMES)
locked_emotion = "neutral"
locked_confidence = 0
SWITCH_THRESHOLD = 8  # new emotion must lead by this % to take over

# Shared state for threaded DeepFace analysis
latest_emotion_result = None
analysis_lock = threading.Lock()
is_analyzing = False

def analyze_face_async(face_crop):
    """Run DeepFace in background thread and store result"""
    global latest_emotion_result, is_analyzing
    try:
        result = DeepFace.analyze(
            face_crop,
            actions=["emotion"],
            enforce_detection=False,
            detector_backend="opencv"
        )
        if isinstance(result, list):
            result = result[0]
        with analysis_lock:
            latest_emotion_result = result["emotion"]
    except Exception:
        pass
    finally:
        is_analyzing = False

def get_smoothed_emotions():
    """Average emotion scores across buffer for stable readings"""
    if not emotion_buffer:
        return None
    all_emotions = list(emotion_buffer)
    averaged = {}
    for emotion in all_emotions[0]:
        averaged[emotion] = sum(d[emotion] for d in all_emotions) / len(all_emotions)
    return averaged

def get_sensitive_dominant(emotion_scores):
    """
    Boost non-neutral emotions so subtle expressions are caught.
    Neutral wins only if it leads by a large margin.
    """
    global locked_emotion, locked_confidence

    boosted = emotion_scores.copy()

    # Heavy boost for hard-to-detect emotions
    boosted["fear"]     *= 2.5
    boosted["surprise"] *= 2.5

    # Normal boost for others (except neutral)
    boosted["happy"]    *= 1.2
    boosted["sad"]      *= 1.5
    boosted["angry"]    *= 1.3

    # Suppress neutral so it doesn't dominate
    boosted["neutral"]  *= 0.6
    boosted["disgust"]  *= 0.0  # Remove disgust completely

    top = max(boosted, key=boosted.get)

    # Only switch if new emotion beats current by SWITCH_THRESHOLD
    if top != locked_emotion:
        if boosted[top] - boosted.get(locked_emotion, 0) >= SWITCH_THRESHOLD:
            locked_emotion = top

    locked_confidence = emotion_scores[locked_emotion]
    return locked_emotion
def draw_emotion_bars(frame, emotion_scores, x, y, w):
    """Draw top 3 emotion bars below the face box for better sensitivity display"""
    sorted_emotions = sorted(emotion_scores.items(), key=lambda e: e[1], reverse=True)[:3]
    bar_x = x
    bar_y = y + 10
    for emotion, score in sorted_emotions:
        bar_width = int((w) * score / 100)
        # Background bar
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + w, bar_y + 14), (50, 50, 50), -1)
        # Filled bar
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + 14), (0, 200, 100), -1)
        # Label
        cv2.putText(
            frame,
            f"{emotion}: {score:.1f}%",
            (bar_x + 3, bar_y + 11),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.38,
            (255, 255, 255),
            1
        )
        bar_y += 18

#Variables
frame_count=0
while True:
    success, frame=cap.read()
    if not success:
        print("Failed to capture frame")
        break
    frame_count+=1
    
    #We then convert to grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Then we detect faces — lowered minNeighbors for higher sensitivity
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(50, 50)
    )
    # If no face detected
    if len(faces) == 0:
        cv2.putText(
            frame,
            "NO FACE DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )
        
    #Process each face
    for (x, y, w, h) in faces:

        # Draw bounding box
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Ignore very small faces
        if w < 50 or h < 50:
            continue

        # Crop face
        face = frame[y:y + h, x:x + w]

        # Kick off background analysis every frame if not already running
        if not is_analyzing:
            is_analyzing = True
            t = threading.Thread(target=analyze_face_async, args=(face.copy(),), daemon=True)
            t.start()

        # Pull latest result into smoothing buffer
        with analysis_lock:
            if latest_emotion_result is not None:
                emotion_buffer.append(latest_emotion_result)
                latest_emotion_result = None

        # Get smoothed scores
        smoothed = get_smoothed_emotions()

        if smoothed:
            dominant_emotion = get_sensitive_dominant(smoothed)
            confidence = smoothed[dominant_emotion]
            emoji = EMOJI_MAP.get(dominant_emotion, "")

            label = (
                f"{emoji} "
                f"{dominant_emotion.upper()} "
                f"{confidence:.1f}%"
            )

            # Display emotion label
            cv2.putText(
                frame,
                label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            # Draw top 3 emotion bars for sensitivity visibility
            draw_emotion_bars(frame, smoothed, x, y + h, w)

        else:
            cv2.putText(
                frame,
                "Analyzing...",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 0),
                2
            )
    
    #Face Count
    cv2.putText(
        frame,
        f"Faces Detected: {len(faces)}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )
    
    #Show Window
    cv2.imshow(
        "Emotion Mirror",
        frame
    )
    
    #Exit Key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()