import spidev
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

delay=0.01
ldr_channel = 0
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=100000
f=0

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r=spi.xfer2([6+((adcnum&0x4)>>2),(adcnum&0x3)<<6,0])
    data = ((r[1]&15)<<8)+r[2]
    return data

try:
    while True:
        ldr_value = readadc(ldr_channel)
        if ldr_value<3000 and f==0:
            GPIO.output(21,GPIO.HIGH)
            f=1
        elif ldr_value>3000 and f==1:
            GPIO.output(21,GPIO.LOW)
            f=0
        print(ldr_value)
        time.sleep(delay)
finally:
    GPIO.cleanup()