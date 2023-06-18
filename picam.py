from picamera import PiCamera 
from time import sleep
import time
import numpy as np
import cv2
from requests import request as req

def GetFace(imname):
    image = cv2.imread(imname)
    while not isinstance(image, np.ndarray):
        time.sleep(0.5)
        image = cv2.imread(imname)
    face_cascade = cv2.CascadeClassifier('./lib/haarcascade_frontalface_alt.xml') #使用Haar分类器作简单人脸识别
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    result_name = './image/result.jpg' #发现有人脸就在本地保存图片, 同时返回1
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
    if GetFace(imname=pic_name) == 1: #检查人脸返回1, 则向微信小程序发送GET请求, 产生APP推送
        f = open("sendkey")
        sendkey = f.read()
        get_url = "https://sctapi.ftqq.com/" + sendkey + ".send?title=warning"
        req("GET", get_url)
