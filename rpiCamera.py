#pip install picamera2
from picamera2 import Picamera2, Preview
import time

camera = Picamera2()
camera.start_preview()
time.sleep(2)  # Wait for the camera to initialize
camera.capture('photo.jpg')
camera.stop_preview()