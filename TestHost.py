from lib.bottle import run, get, post, static_file, template
import time
import threading
from requests import request as req
import sys

class picam_server():
    def __init__(self):
        time.sleep(0.3)
        self.fetchTime = 10

    @get('/')
    def index():
        return template('index')

    @get('/<filename:re:.*\.jpg>')
    def get_image(filename):
        return static_file(filename, root='./image', mimetype='image/jpg')


    @post('/<angle:re:[0-9]+>')
    def moveCam(angle):
        print(angle)
        time.sleep(0.3)
    
    @post('/<time:re:updateWait[0-9]*>')
    def updateWait(time):
        print(time)
        self.fetchTime = time


    def Entry(self):
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
        run(host='0.0.0.0', port=80, reloader=True)
        
    def timer(self):
        while True:
            time.sleep(self.fetchTime)
            print("fetch")
        
if __name__ == '__main__':
    server = picam_server()
    server.Entry()
