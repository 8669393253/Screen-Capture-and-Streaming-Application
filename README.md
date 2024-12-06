# **Screen Capture and Streaming Application**

This project allows you to capture the screen of your machine, send the captured frames over a network, and then receive, display, and save these frames on a server. The system works with two Python scripts: one for the **client** that captures the screen and sends the frames, and another for the **server** that receives the frames, displays them, and saves them locally.

## **Project Structure**

├── client.py               # Client-side script to capture and send frames
├── server.py               # Server-side script to receive and save frames
├── README.md               # Project documentation


## **Prerequisites**
Before you run the client and server scripts, make sure you have the following Python libraries installed:

- **pyautogui**: For screen capture
- **cv2 (OpenCV)**: For displaying and saving images
- **pickle**: For serializing and deserializing the image frames
- **struct**: For packing and unpacking the frame size
- **numpy**: For converting images into NumPy arrays

### Installation
You can install the required libraries using pip:

pip install pyautogui opencv-python numpy

## **Client-Side (Screen Capture and Sender)**

The client script captures the screen in real-time, serializes each frame, and sends it over a TCP socket to the server. It continuously captures frames and sends them as long as the server is available.

### **Client Code (client.py)**

#### **How it works:**
1. **Capture Screen**: The client uses `pyautogui.screenshot()` to capture the screen.
2. **Serialization**: The captured frame is serialized using `pickle` into a byte stream.
3. **Data Sending**: The size of the frame is sent first, followed by the serialized frame data.
4. **Continuous Loop**: This loop continues sending frames to the server indefinitely until the program is terminated by pressing 'q'.

#### **Running the Client:**
1. Ensure the server is running (as described below).
2. Run the client script:

   python client.py


3. The client will automatically start capturing and sending the screen data to the server.

#### **Important Notes for Client-Side:**
- The client script captures the **entire screen**; you can modify the region if you want to capture only part of the screen.
- The client and server must be on the same network or the same machine (`localhost`), as the client connects to the server on `127.0.0.1` (localhost).
- The default port for communication is `5000`. Make sure the port is open and not used by other applications.


## **Server-Side (Receiver and Saver)**

The server listens on a specific port for incoming connections from the client. Once a connection is established, it receives the frame data, deserializes it, displays it in a window, and saves the frame as a `.jpg` image.

### **Server Code (server.py)**

#### **How it works:**
1. **Wait for Client**: The server listens for incoming connections on `127.0.0.1:5000` (localhost and port 5000).
2. **Receive Data**: Once a connection is established, the server reads the frame size and the frame data sent by the client.
3. **Deserialization**: The frame is deserialized using `pickle` to restore it as an image.
4. **Display and Save**: The server displays the frame in a window and saves it locally in the `D:\Desktop\Frames` directory (can be modified in the code).

#### **Running the Server:**
1. Ensure the client is ready to send data.
2. Run the server script:

   python server.py

3. The server will start and listen for connections from the client. Once connected, it will start displaying the frames and saving them in the specified folder.

#### **Important Notes for Server-Side:**
- By default, the frames are saved to the `D:\Desktop\Frames` directory. You can change this path in the script to any folder where you want to save the frames.
- The frames are saved with filenames like `frame_0001.jpg`, `frame_0002.jpg`, etc. If you want to modify the naming pattern, adjust the `frame_filename` code.
- The server will continuously display and save frames until the 'q' key is pressed.


## **How to Use the System**

1. **Set up the server**:
   - Open a terminal and run the server script (`server.py`).
   - The server will start listening on `127.0.0.1:5000`.

2. **Run the client**:
   - Once the server is running, open another terminal and run the client script (`client.py`).
   - The client will start capturing the screen and sending frames to the server.
   
3. **View the frames**:
   - The server will display the received frames in a window with the title "Received Video Stream".
   - Each frame will also be saved as a `.jpg` file in the specified folder (by default `D:\Desktop\Frames`).

4. **Stop the program**:
   - Press `q` while the server's window is focused to stop receiving frames and close the server.


## **Troubleshooting**

- **Client Cannot Connect to Server**:
  - Ensure the server is running and listening on the correct IP and port (`127.0.0.1:5000`).
  - Check that no firewall or security software is blocking the connection on the specified port.
  
- **Frames Not Displaying/Receiving**:
  - Make sure both scripts are running on the same machine or network.
  - Verify that the screen capture resolution on the client matches the screen's actual resolution.

- **Frames Not Saving**:
  - Check that the specified folder exists, or modify the path in the `server.py` script to a valid folder on your system.
  - Ensure you have write permissions to the folder where frames are being saved.


## **Security Considerations**

- **Data Integrity**: The client and server communicate over plain TCP sockets with no encryption. If you're using this system in a production environment or over an insecure network, consider encrypting the communication using libraries like `ssl` or `cryptography`.
  
- **Pickle Security**: The `pickle` module is used to serialize and deserialize data, which can be unsafe if you're handling untrusted data. In this case, since both the client and server are trusted, it is acceptable, but for production use, it's advised to use a safer serialization method.


## **License**

This project is open-source and licensed under the MIT License. Feel free to modify and use it as needed.


## **Conclusion**

This system provides a simple way to stream and save screen captures using Python. It can be extended to support features like streaming multiple screens, adding a frame rate control, or encrypting the data for secure communication.
