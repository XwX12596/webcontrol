import io
import sys
import logging
import picamera
import time
import threading
from lib.bottle import run, route, post, response, template
from picam import fetch
from motor import gs90_angle
from bell import warning
from threading import Condition
from stream import mjpg_stream

class picam_server():
    def __init__(self):
        gs90_angle(45)
        time.sleep(0.3)
        gs90_angle('stop')
        self.fetchTime = 10

    @route('/')
    def index():
        response.status = 301
        response.set_header('Location', '/index.html')
        return

    @route('/index.html')
    def html_page():
        return template("index")

    @post('/fetch')
    def picture():
        fetch()

    @post('/warning')
    def bell():
        warning()

    @post('/<angle:re:[0-9]+>')
    def moveCam(angle):
        print(angle)
        gs90_angle(int(angle))
        time.sleep(0.3)
        gs90_angle('stop')
        gs90_pwm.stop()
    
    @post('/<time:re:updateWait[0-9]*>')
    def updateWait(time):
        print(time)
        self.fetchTime = time
    
    @route('/stream.mjpg')
    def stream():
        def generate():
            while True:
                with output.condition:
                    output.condition.wait()
                    frame = output.frame
                    print(type(frame))
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


    def start(self):
        t1 = threading.Thread(target=self.host)
        t1.daemon = True
        t1.start()
        t2 = threading.Thread(target=self.timer)
        t2.daemon = True
        t2.start()
        t3 = threading.Thread(target=self.streamStart)
        t3.daemon = True
        t3.start()
        while True:
            try:
                t2.join(0.1)
            except KeyboardInterrupt:
                self.mjpg.stop()
                print("end")
                sys.exit(0)
    def streamStart(self):
        self.mjpg = mjpg_stream()
        self.mjpg.run()
        print("mjpg_stream running")

    def host(self):
        run(host='0.0.0.0', port=8000)
        
    def timer(self):
        while True:
            time.sleep(self.fetchTime)
            fetch()
            print("autoFetching")
        
if __name__ == '__main__':
    server = picam_server()
    server.host()
