#!/usr/bin/python3

# Mostly copied from https://picamera.readthedocs.io/en/release-1.13/recipes2.html
# Run this script, then point a web browser at http:<this-ip-address>:8000
# Note: needs simplejpeg to be installed (pip3 install simplejpeg).

import io
import logging
import socketserver
import socket
import serial
import time
from http import server
from threading import Condition, Thread

from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

PAGE = """\
<html>
<head>
<title>picamera2 MJPEG streaming demo</title>
</head>
<body>
<h1>Picamera2 MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""


class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True
  
#Camera
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
output = StreamingOutput()
picam2.start_recording(JpegEncoder(), FileOutput(output))

try:
    
    server_thread = Thread(target=StreamingServer(('', 8000), StreamingHandler).serve_forever)
    server_thread.daemon=True
    server_thread.start()
    '''
    address = ('', 8000)
    server = StreamingServer(address, StreamingHandler)
    server.serve_forever()
    '''
    #Create a socket objet
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to a specific address and port
    server_address=('',8001) #Different port than the streaming
    server_socket.bind(server_address)
    
    #Listen for incoming connections
    server_socket.listen(5)
    
    #Serial Communication Arduino
    ser=serial.Serial('/dev/ttyACM0',115200, timeout=1.0)
    time.sleep(3)
    ser.reset_input_buffer() #If arduino send data, the buffer is where all the data arrive, reset
    print("Serial OK")
        
    while True:
        print('Waiting for command...')
        client_socket, client_address = server_socket.accept()
        
        #Receive the command from the client
        command = client_socket.recv(1024).decode()
        
        client_socket.close()

        #Send the command to Arduino
        ser.write((str(command)+"_").encode('utf-8'))
        ser.reset_input_buffer() #If arduino send data, the buffer is where all the data arrive, reset


except KeyboardInterrupt:
    ser.close()
    pass
    
finally:
    ser.close()
    picam2.stop_recording()
