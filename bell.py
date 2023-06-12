import RPi.GPIO as GPIO
import time

def warning():
    for i in range(3):
        fm = 2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(fm, GPIO.OUT, initial=GPIO.HIGH)
    
        GPIO.output(fm, GPIO.LOW)
        time.sleep(1)
        GPIO.output(fm, GPIO.HIGH)
        GPIO.cleanup()
        time.sleep(0.5)

if __name__=="__main__":
    warning()
