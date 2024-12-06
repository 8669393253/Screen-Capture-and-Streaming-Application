import pyautogui
import socket
import pickle
import struct
import cv2
import numpy as np

# Server IP and port
server_ip = '127.0.0.1'  # Localhost (same machine)
server_port = 5000  # Use the same port as the server

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Set screen size for capturing (avoid zooming effect)
screen_width, screen_height = pyautogui.size()  # Get the screen size

while True:
    # Capture the full screen
    screen = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))  # Capture the screen with its native size
    frame = np.array(screen)  # Convert the screenshot to a NumPy array
    
    # Convert RGB (PIL format) to BGR (OpenCV format)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Serialize the frame
    data = pickle.dumps(frame)

    # Send the size of the frame first
    frame_size = struct.pack("L", len(data))
    client_socket.sendall(frame_size)  # Send the size of the frame
    client_socket.sendall(data)  # Send the frame data

    print("Frame sent to server...")

    # Optionally, you can add a small delay to avoid high CPU usage
    cv2.waitKey(1)  # Prevent high CPU usage by adding a small delay

client_socket.close()  # Close the client socket when done
