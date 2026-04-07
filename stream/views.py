

# Create your views here.
import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render

# OpenCV Video Capture
class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)  # 0 for default webcam

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if success:
            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        return None

# Generator function to stream frames
def generate_frames(camera):
    while True:
        frame = camera.get_frame()
        if frame:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Django View for video stream
def video_feed(request):
    return StreamingHttpResponse(generate_frames(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

# Home Page
def home(request):
    return render(request, "index.html")
