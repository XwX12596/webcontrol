import RPi.GPIO as gpio
import time
import sys

gpio_pin = 4  
gpio.setmode(gpio.BCM)  
gpio.setup(gpio_pin, gpio.OUT)  
gs90_pwm = gpio.PWM(gpio_pin, 50)  
gs90_pwm.start(0)  
gpio.setwarnings(False)

def gs90_angle(angle):
    '''angle 输入0-180度 如果输入 'stop' 则停止'''
    if isinstance(angle, str):  
            gs90_pwm.ChangeDutyCycle(0)  
    elif isinstance(angle, int) or isinstance(angle, float):  
        gs90_pwm.ChangeDutyCycle(2.5 + angle * 10 / 180)  


if __name__ == '__main__':

    anger = sys.argv[1]
    print(anger)

    gs90_angle(int(anger))
    time.sleep(0.3)
    gs90_angle('stop')

    gs90_pwm.stop()  
    gpio.cleanup()  
