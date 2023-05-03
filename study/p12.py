import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup([16,20,21],GPIO.OUT)

bleSerial = serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1.0)
try:
  while True:
    if bleSerial.readable():
      cmd=bleSerial.readline().decode().strip()
      if(cmd==''):
        continue
      if(cmd[0]=='r'):
        pin=16
      if(cmd[0]=='b'):
        pin=20
      if(cmd[0]=='g'):
        pin=21
      if(cmd[1:]=='on'):
        GPIO.output(pin,GPIO.HIGH)
      if(cmd[1:]=='off'):
        GPIO.output(pin,GPIO.LOW)
finally:
  bleSerial.close()
  GPIO.cleanup()