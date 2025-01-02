import cv2  # For video capture and QR code detection
import time  # For handling timing and intervals
from sense_hat import SenseHat
import threading  # For running tasks in parallel
import os  # For file handling
import pygame  # For playing audio files
from gtts import gTTS  # For converting text to speech

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Initialize camera for capturing video frames and QR code scanner for detection
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

# Timing variables for controlling detection frequency
last_detect_time = time.time()
interval = 0.005  # Time interval between consecutive detections
loop_counter = 0  # Counter to manage QR code processing

# Initialize Sense HAT for displaying messages
sense = SenseHat()

# Lock to ensure thread-safe access to message display functionality
is_showing_message = False  
message_lock = threading.Lock()

# Function to display a message on the Sense HAT and play its audio
def show_message_thread(text):
    global is_showing_message

    with message_lock:  
        if is_showing_message:  # Avoid overlapping message processing
            return  
        is_showing_message = True  

    # Convert text to speech using Google TTS and save it as an MP3 file
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)

    # Play the audio message using pygame
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    # Scroll the message on the Sense HAT's LED matrix
    sense.show_message(text, scroll_speed=0.03, text_colour=[255, 255, 255])

    # Reset the lock state after completing the task
    with message_lock:
        is_showing_message = False  

# Main loop for capturing video and detecting QR codes
while True:
    _, img = cap.read()  # Capture a frame from the camera
    
    # Check if sufficient time has elapsed for QR code detection
    if time.time() - last_detect_time >= interval:
        text, bbox, _ = detector.detectAndDecode(img)  # Detect QR code and decode its content
        
        if bbox is not None:  # If a QR code is detected
            # Draw bounding box around the detected QR code
            for i in range(len(bbox)):
                pt1 = tuple(map(int, bbox[i][0]))
                pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))
                cv2.line(img, pt1, pt2, color=(255, 0, 255), thickness=2)
            
            if text:  # If QR code contains text
                # Overlay the detected text on the video frame
                cv2.putText(img, text, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                loop_counter += 1
                if loop_counter >= 2:  # Process the message only after a set number of detections
                    print("Data found: ", text)
                    
                    # Handle the detected text in a separate thread
                    threading.Thread(target=show_message_thread, args=(text,)).start()

                    loop_counter = 0  # Reset the counter
        
        # Update the last detection timestamp
        last_detect_time = time.time()
    
    # Display the processed video frame
    cv2.imshow("QR Code Detector", img)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release camera resources and close OpenCV windows
cap.release()
cv2.destroyAllWindows()