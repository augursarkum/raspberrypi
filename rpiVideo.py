from picamera2 import Picamera2

camera = Picamera2()
camera.start_recording('video.mp4')
camera.wait_recording(10)  # Record for 10 seconds
camera.stop_recording()