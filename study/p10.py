import time
import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

sensor = DHT.DHT11
pin=4
try:
  while(True):
    h,t=DHT.read_retry(sensor,pin)
    if(h is not None) and (t is not None):
      DI=(1.8*t)-(0.55*(1-(h/100))*(1.8*t-26))+32
      print(DI)
      if(DI<70):
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
      elif(DI<76):
        GPIO.output(16,GPIO.LOW)
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
      else:
        GPIO.output(16,GPIO.LOW)
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
    else:
      print("Read Error")
    time.sleep(1)
except KeyboardInterrupt:
  print("Terminated by Keyboard")
finally:
  print("end program")
  GPIO.cleanup()