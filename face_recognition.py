import numpy as np
import cv2

def GetFace():
    image = cv2.imread('./image/mountains.png')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imwrite('result.jpg', image)
    if faces == []:
        print('t')
    else:
        print('fuck')

GetFace()