import io
import sys
import time
import logging
import picamera
import threading
from lib.bottle import run, route, post, response, template
from threading import Condition

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

@route('/')
def index():
    response.status = 301
    response.set_header('Location', '/stream.html')
    return

@route('/stream.html')
def html_page():
    return template("stream")

@route('/stream.mjpg')
def startStream(): #向用户不断发送.mjpg图像，形成图片流，做到实时监控
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


if __name__ == '__main__':
    print("start")
    camera = picamera.PiCamera(resolution='640x480', framerate=24)
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')
    run(host='0.0.0.0', port=8000)
    camera.stop_recording()

