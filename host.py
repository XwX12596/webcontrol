import io
import sys
import time
import logging
import picamera
import threading
from lib.bottle import run, get, post, response, template
from picam import fetch
from motor import gs90_angle
from bell import warning
from threading import Condition

@get('/')
def index():
    response.status = 301
    response.set_header('Location', '/index.html')
    return

@get('/index.html')
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

def timer(self):
    while True:
        time.sleep(self.fetchTime)
        fetch()
        print("autoFetching")
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

if __name__ == '__main__':
    start()
