import socket
import cv2
import pickle
import struct
import os
from datetime import datetime

# Specify the folder where you want to save the frames
save_folder = "D:\Desktop\Frames"  # You can change this to any folder path you want to save the frames in

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Server IP and Port
server_ip = '127.0.0.1'
server_port = 5000

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of the address

try:
    # Bind to the server IP and port
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Listening on {server_ip}:{server_port}")
    
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    
    data = b""
    payload_size = struct.calcsize("L")  # Length of the size field
    
    frame_count = 0  # To track the number of frames saved

    while True:
        # Receive data until we have the entire frame
        while len(data) < payload_size:
            data += client_socket.recv(4096)

        # Get the frame size and unpack it
        packed_size = data[:payload_size]
        data = data[payload_size:]
        frame_size = struct.unpack("L", packed_size)[0]

        # Receive the frame data
        while len(data) < frame_size:
            data += client_socket.recv(4096)

        frame_data = data[:frame_size]
        data = data[frame_size:]

        # Unpickle the frame data
        frame = pickle.loads(frame_data)

        # Display the frame (optional)
        cv2.imshow("Received Video Stream", frame)

        # Save the frame to the specified folder
        frame_count += 1
        frame_filename = os.path.join(save_folder, f"frame_{frame_count:04d}.jpg")  # Save with a unique name
        cv2.imwrite(frame_filename, frame)  # Save the frame as an image

        print(f"Frame {frame_count} saved as {frame_filename}")

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Close the sockets when done
    client_socket.close()
    server_socket.close()
    cv2.destroyAllWindows()
