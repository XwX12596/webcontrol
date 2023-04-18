from lib.bottle import run, get, post, static_file, template
from picam import fetch
from motor import gs90_angle
import time

class picam_server():
    def __init__(self):
        gs90_angle(45)
        time.sleep(0.3)
        gs90_angle('stop')

    @get('/')
    def index():
        return template('index')

    @get('/<filename:re:.*\.jpg>')
    def get_image(filename):
        return static_file(filename, root='./image', mimetype='image/jpg')

    @post('/<name:re:cam-[^.]+>')
    def response(name):
        print(name)

    @post('/fetch')
    def picture():
        fetch()

    #@post('/warning')
    #def bell():
    #    warning()

    @post('/15')
    def moveCam():
        gs90_angle(15)
        time.sleep(0.3)
        gs90_angle('stop')
        time.sleep(0.3)
        fetch()

    @post('/30')        
    def moveCam():
        gs90_angle(30)
        time.sleep(0.3)
        gs90_angle('stop')
        time.sleep(0.3)
        fetch()
        
    @post('/45')
    def moveCam():
        gs90_angle(45)
        time.sleep(0.3)
        gs90_angle('stop')
        time.sleep(0.3)
        fetch()
    
    @post('/60')
    def moveCam():
        gs90_angle(60)
        time.sleep(0.3)
        gs90_angle('stop')
        time.sleep(0.3)
        fetch()
    
    
    @post('/75')
    def moveCam():
        gs90_angle(75)
        time.sleep(0.3)
        gs90_angle('stop')
        time.sleep(0.3)
        fetch()
    
    @post('/90')
    def moveCam():
        gs90_angle(90)
        time.sleep(0.3)
        gs90_angle('stop')
        time.sleep(0.3)
        fetch()


    def start(self):
        run(host='0.0.0.0', port=80)
if __name__ == '__main__':
    server = picam_server()
    server.start()
