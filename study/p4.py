import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
soft_pwm = GPIO.PWM(20, 50)

press=0

toggle=0

duty=20

soft_pwm.start(0)

try:
    while 1:
        if GPIO.input(12)==1 and press==0:
            press=1
            soft_pwm.ChangeDutyCycle(duty)
            duty+=20
            if(duty>100):
                duty=0
        if GPIO.input(12)==0 and press==1:
            press=0
finally:
    soft_pwm.stop()
    GPIO.cleanup()