from picamera import PiCamera 
from face_recognition import GetFace as face
camera = PiCamera()
camera.resolution = (1280, 720)
camera.capture('original.jpg')
face(imname='original.jpg')
