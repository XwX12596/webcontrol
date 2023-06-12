import io
import logging
import picamera
import time
import threading
from bottle import run, route, post, response, template
from picam import fetch
from motor import gs90_angle
from bell import warning
from threading import Condition
import sys

PAGE = """\
<html>
<head>
<title>picamera MJPEG streaming demo</title>
</head>
<body>
<h1>PiCamera MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

@route('/')
def index():
    response.status = 301
    response.set_header('Location', '/index.html')
    return

# @route('/index.html')
# def html_page():
#     content = PAGE.encode('utf-8')
#     response.status = 200
#     response.set_header('Content-Type', 'text/html')
#     response.set_header('Content-Length', len(content))
#     return content

@route('/index.html')
    def html_page():
        return template("index")

@route('/stream.mjpg')
def stream():
    def generate():
        while True:
            with output.condition:
                output.condition.wait()
                frame = output.frame
            yield b'--FRAME\r\n'
            yield b'Content-Type: image/jpeg\r\n'
            yield b'Content-Length: ' + str(len(frame)).encode() + b'\r\n\r\n'
            yield frame
            yield b'\r\n'

    response.status = 200
    response.set_header('Age', '0')
    response.set_header('Cache-Control', 'no-cache, private')
    response.set_header('Pragma', 'no-cache')
    response.set_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
    return generate()

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')

    # 运行Bottle服务器
    run(host='0.0.0.0', port=8000)

    camera.stop_recording()
