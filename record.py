import cv2
import sys

# Function to parse command line arguments
def parse_args():
    if len(sys.argv) != 2:
        print("Usage: python script.py <IP_address>")
        sys.exit(1)
    return sys.argv[1]

# Base URL of the stream (prefix)
base_url = "http://{}:8080/?action=stream"

# Get IP address from command line argument
ip_address = parse_args()

# Construct the full URL
url = base_url.format(ip_address)

# OpenCV VideoCapture object
cap = cv2.VideoCapture(url)

# Check if the capture is open
if not cap.isOpened():
    print("[!] Error: Unable to open video capture")
    exit()

# Initialize variables to store frames
frames = []

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        print("[*] Frame captured successfully")
        frames.append(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("[!] Error capturing frame")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Check if any frames were captured
if not frames:
    print("[!] Error: No frames captured")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can try 'avc1' for better compatibility
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frames[0].shape[1], frames[0].shape[0]))

# Check if the VideoWriter is initialized
if not out.isOpened():
    print("[!] Error: Unable to initialize VideoWriter")
    exit()

# Write frames to video file
for frame in frames:
    out.write(frame)

# Release VideoWriter
out.release()

print("[✓] Video file 'output.mp4' created successfully")
