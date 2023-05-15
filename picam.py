from picamera import PiCamera 
from time import sleep
import time
import numpy as np
import cv2

def GetFace(imname):
    image = cv2.imread(imname)
    while not isinstance(image, np.ndarray):
        time.sleep(0.5)
        image = cv2.imread(imname)
    face_cascade = cv2.CascadeClassifier('./lib/haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    result_name = './image/result.jpg'
    cv2.imwrite(result_name, image)
    if len(faces) != 0:
        return 1
    else:
        return 0

def fetch():
    camera = PiCamera()
    camera.resolution = (640, 360)
    pic_name = './image/original.jpg'
    camera.capture(pic_name)
    camera.close()
    if GetFace(imname=pic_name) == 1:
        warning()
        f = open("sendkey")
        sendkey = f.read()
        get_url = "https://sctapi.ftqq.com/" + sendkey + ".send?title=warning"
        req("GET", get_url)

if __name__=='__main__':
    fetch()
