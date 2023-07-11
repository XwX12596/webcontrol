import sys
import time
import threading
from lib.bottle import run, get, post, response, template, static_file
from picam import fetch
from motor import sg90_angle
from bell import warning

fetchTime = 20


@get('/')
def index():  # 根路由重定向到主网页 index.html
    response.status = 301
    response.set_header('Location', '/index.html')
    return


@get('/index.html')  # index.html
def html_page():
    return template("index")


@post('/fetch')  # post 'fetch' 拍照函数
def picture():
    fetch()


@post('/warning')  # post warning 响铃函数
def bell():
    warning()


@post('/<angle:re:[0-9]+>')  # post angle+<数字>(0-180)
def moveCam(angle):
    sg90_angle(int(angle))
    time.sleep(0.3)
    sg90_angle('stop')


@get('/<pic:re:.*jpg>')
def picFile(pic):
    return static_file(pic, root='image/')


@post('/<time:re:updateWait[0-9]*>')  # post updateWait + <数字>
def updateWait(time):
    global fetchTime
    fetchTime = time


def timer():  # 计时器部分，每隔一段时间拍摄照片
    while True:
        time.sleep(fetchTime)
        fetch()
        print("autoFetching")


def host():
    run(host='0.0.0.0', port=8000)  # 服务器部分，在本地所有IP上打开服务器


def start():
    t1 = threading.Thread(target=host)  # 打开两个线程分别对应计时和服务器
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=timer)
    t2.daemon = True
    t2.start()
    while True:
        try:
            t2.join(0.1)  # 阻塞0.1s, 让代码可以响应Ctrl+C
        except KeyboardInterrupt:
            print("end")
            sys.exit(0)


if __name__ == '__main__':
    start()
