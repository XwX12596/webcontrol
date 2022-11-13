import RPi.GPIO as GPIO
import time

def warning():
    fm = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(fm, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.output(fm, GPIO.LOW)
    time.sleep(1)
    GPIO.output(fm, GPIO.HIGH)
    GPIO.cleanup()
    print('Warning!!')

