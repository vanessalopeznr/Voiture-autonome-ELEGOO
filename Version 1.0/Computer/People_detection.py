#yolo predict model=yolov8n.pt source='http://192.168.0.100:8000/stream.mjpg'

import cv2

from ultralytics import YOLO
import socket

def receive_command(command):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Raspberry Pi's IP address and the port for command communication
    server_address = ('192.168.0.100', 8001)

    # Connect to the server
    client_socket.connect(server_address)

    # Send the command to the Raspberry Pi
    client_socket.sendall(command.encode())

    # Close the socket
    client_socket.close()


# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video file
source = "http://192.168.0.100:8000/stream.mjpg"
#source = '0'

results = model.predict(source, stream=True, conf=0.5)  # generator of Results objects

for r in results:
    print('------------------------------------------------------')
    boxes = r.boxes  # Boxes object for bbox outputs
    image = r.plot()
    for box in boxes:
        pers = int(box.cls[0])
        if pers==0:
            # box.xyxy[0] Coordinates of bounding boxes in the form (x1, y1, x2, y2) where (x1, y1) is the top-left corner of the bounding box, and (x2, y2) denotes the bottom-right corner
            centerx=((box.xyxy[0][2]-box.xyxy[0][0])/2)+box.xyxy[0][0]
            centery=((box.xyxy[0][3]-box.xyxy[0][1])/2)+box.xyxy[0][1]
            cv2.circle(image, (int(centerx), int(centery)), 5, (0, 0, 255),-1)

            if centerx>380:
                command_width="right"

            elif centerx<260:
                command_width="left"
            
            else: 
                command_width='None'

            if centery>260:
                command_height="front"

            elif centery<220:
                command_height="back"
             
            else:
                command_height='None'

            receive_command(command_width + '/' + command_height)
            print(command_width,command_height)

    cv2.imshow("result", image)


