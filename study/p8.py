# 필요한 라이브러리를 불러옵니다.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#센서에 연결한 Trig와 Echo 핀의 번호 설정
TRIG = 16
ECHO = 20
print("Distance measurement in progress")
#Trig와 Echo 핀의 출력/입력 설정
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(12,GPIO.OUT)
#Trig핀의 신호를 0으로 출력
GPIO.output(TRIG, False)
p = GPIO.PWM(12, 100)
Frq = [ 262, 294, 330, 349, 392, 440, 493, 523 ]
print("Waiting for sensor to settle")
time.sleep(2)
p.start(10)  

try:
  while True:
    # Triger 핀에 펄스신호를 만들기 위해 1 출력
    GPIO.output(TRIG, True)
    time.sleep(0.00001) # 10μs 딜레이
    GPIO.output(TRIG, False)
    # start time
    while GPIO.input(ECHO)==0:
      start = time.time()
    while GPIO.input(ECHO)==1:
      stop = time.time()
    check_time = stop - start
    distance = check_time * 34300 / 2
    print("Distance : %.1f cm" % distance)
    if distance<10:
      p.ChangeFrequency(Frq[0])
    elif distance<20:
      p.ChangeFrequency(Frq[1])
    elif distance<30:
      p.ChangeFrequency(Frq[2])
    elif distance<40:
      p.ChangeFrequency(Frq[3])
    elif distance<50:
      p.ChangeFrequency(Frq[4])
    elif distance<60:
      p.ChangeFrequency(Frq[5])
    elif distance<70:
      p.ChangeFrequency(Frq[6])
    elif distance<80:
      p.ChangeFrequency(Frq[7])
    else:
      p.ChangeFrequency(1)
    time.sleep(0.1)
finally:
  print("Measurement stopped by User")
  GPIO.cleanup()