from django.http import StreamingHttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def payments(request):
    return render(request, 'payments.html')

def profile(request):
    return render(request, 'profile.html')

def camera(request):
    return render(request, 'camera.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_stream(request):
    from setup.project import camera
    return StreamingHttpResponse(gen(camera.VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')