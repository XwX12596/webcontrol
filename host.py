from lib.bottle import run, get, post, static_file, template
from picam import fetch
from motor import gs90_angle
from bell import warning
import time
import threading
from requests import request as req
import sys

class picam_server():
    def __init__(self):
        gs90_angle(45)
        time.sleep(0.3)
        gs90_angle('stop')
        self.fetchTime = 1

    @get('/')
    def index():
        return template('index')

    @get('/<filename:re:.*\.jpg>')
    def get_image(filename):
        return static_file(filename, root='./image', mimetype='image/jpg')

    @post('/fetch')
    def picture():
        fetch()

    @post('/warning')
    def bell():
        warning()

    @post('/<angle:re:[0-9]+>')
    def moveCam(angle):
        print(angle)
        gs90_angle(angle)
        time.sleep(0.3)
        gs90_angle('stop')
        time.sleep(0.3)
        fetch()
    
    @post('/<time:re:updateWait[0-9]*>')
    def updateWait(time):
        print(time)


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
        run(host='0.0.0.0', port=80, reloader=True)
        
    def timer(self):
        while True:
            time.sleep(self.fetchTime)
            if fetch() == 1:
                warning()
                f = open("sendkey")
                sendkey = f.read()
                get_url = "https://sctapi.ftqq.com/" + sendkey + ".send?title=warning"
                req("GET", get_url)
        
if __name__ == '__main__':
    server = picam_server()
    server.start()
