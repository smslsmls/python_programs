import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

l=0

press=0

try:
    while 1:
        if GPIO.input(12)==1:
            press=1
            if l==0:
                GPIO.output(20,1)
                GPIO.output(21,0)
                l=1
            else:
                GPIO.output(20,0)
                GPIO.output(21,1)
                l=0
            time.sleep(0.1)
        if GPIO.input(12)==0 and press==1:
            press=0
            GPIO.output(20,0)
            GPIO.output(21,0)

finally:
    GPIO.cleanup()