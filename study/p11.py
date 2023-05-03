import time
import datetime
import Adafruit_DHT as DHT

sensor = DHT.DHT11
pin=4
try:
  while True:
    h,t=DHT.read_retry(sensor,pin)
    if(h is not None) and (t is not None):
      now = datetime.datetime.now()
      print(str(now)+" : Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t,h))
      f = open('th.txt','a')
      f.write(str(now)+" : Temperature = {0:0.1f}*C Humidity = {1:0.1f}%\r\n".format(t,h))
      f.close()
    time.sleep(1)
finally:
  pass