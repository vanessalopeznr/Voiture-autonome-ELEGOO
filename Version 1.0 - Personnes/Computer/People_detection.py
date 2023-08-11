#yolo predict model=yolov8n.pt source='http://192.168.0.100:8000/stream.mjpg'

import cv2

from ultralytics import YOLO
import socket

address="192.168.0.100"

def send_command(command):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Raspberry Pi's IP address and the port for command communication
    server_address = (address, 8001)

    # Connect to the server
    client_socket.connect(server_address)

    # Send the command to the Raspberry Pi
    client_socket.sendall(command.encode())

    # Close the socket
    client_socket.close()


# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video file
source = "http://" + address + ":8000/stream.mjpg"
#source = '0' #For the camera

results = model.predict(source, stream=True, classes=0, max_det=1, conf=0.5)  # generator of Results objects

for r in results:
    print('------------------------------------------------------')
    boxes = r.boxes  # Boxes object for bbox outputs
    image = r.plot()
    for box in boxes:
        pers = int(box.cls[0])
        if pers==0:
            # box.xyxy[0] Coordinates of bounding boxes in the form (x1, y1, x2, y2) where (x1, y1) is the top-left corner of the bounding box, and (x2, y2) denotes the bottom-right corner
            width=box.xyxy[0][2]-box.xyxy[0][0]
            height=box.xyxy[0][3]-box.xyxy[0][1]
            area=width*height

            centerx=(width/2)+box.xyxy[0][0]
            centery=(height/2)+box.xyxy[0][1]
            cv2.circle(image, (int(centerx), int(centery)), 5, (0, 0, 255),-1)

            if area < 30000:
                command_height="fast"

            elif 30000 < area < 90000:
                command_height="normal"

            else:
                command_height="slow"
            

            if centerx>380:
                command_width="right"

            elif centerx<260:
                command_width="left"
            
            else: 
                command_width='None'

            send_command(command_width + '/' + command_height)
            print(command_width,command_height)

    cv2.imshow("result", image)


