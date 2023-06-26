import RPi.GPIO as gpio
import time
import sys

gpio.setwarnings(False)
gpio_pin = 4  
gpio.setmode(gpio.BCM)  
gpio.setup(gpio_pin, gpio.OUT)  
sg90_pwm = gpio.PWM(gpio_pin, 50)  
sg90_pwm.start(0)  

def sg90_angle(angle):
    '''angle 输入0-180度 如果输入 'stop' 则停止'''
    if isinstance(angle, str):  
            sg90_pwm.ChangeDutyCycle(0) #占空比设置为0 
    elif isinstance(angle, int) or isinstance(angle, float):  
        if (angle >= 0 and angle <= 180): 
            #角度设置在0~180度之间
            sg90_pwm.ChangeDutyCycle(2.5 + angle * 10 / 180) 
            #占空比在2.5%到12.5%之间变化，对应脉冲长度为0.5ms到2.5ms之间
