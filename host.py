from lib.bottle import run, route, post, static_file, template
from picam import fetch
from motor import gs90_angle
from bell import warning
import time
import threading
import sys

class picam_server():
    def __init__(self):
        gs90_angle(45)
        time.sleep(0.3)
        gs90_angle('stop')
        self.fetchTime = 10
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    @route('/')
    def index():
        response.status = 301
        response.set_header('Location', '/index.html')
        return
    
    @route('/index.html')
    def html_page():
        content = PAGE.encode('utf-8')
        response.status = 200
        response.set_header('Content-Type', 'text/html')
        response.set_header('Content-Length', len(content))
        return content

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
        while True:
            try:
                t2.join(0.1)
            except KeyboardInterrupt:
                print("end")
                sys.exit(0)
        
    def host(self):
        run(host='0.0.0.0', port=25565, reloader=True)
        
    def timer(self):
        while True:
            time.sleep(self.fetchTime)
            fetch()
            print("autoFetching")
        
if __name__ == '__main__':
    server = picam_server()
    server.start()
