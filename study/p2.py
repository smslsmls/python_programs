import RPi.GPIO as GPIO
import time

pins=[13,19,26,20,21]
outputs=[[0,0,1,1,0],[0,1,0,0,0],[1,0,0,0,1]]

GPIO.setmode(GPIO.BCM)
for i in pins:
    GPIO.setup(i,GPIO.OUT)

try:
    while 1:
        for output in outputs:
            for i, p in enumerate(pins):
                GPIO.output(p,output[i])
            time.sleep(3)
        
finally:
    GPIO.cleanup()