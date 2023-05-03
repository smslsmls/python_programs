import RPi.GPIO as g
import time
g.setwarnings(False)
g.setmode(g.BCM)
g.setup(12, g.OUT)
g.setup(16, g.IN)
g.setup(19, g.IN)
g.setup(20, g.IN)
g.setup(21, g.IN)
g.setup(26, g.IN)
p = g.PWM(12, 100)
Frq = [ 349, 392, 440, 493, 523 ]
speed = 0.5
p.start(10)  
try:
  while 1:
    if g.input(16):
      p.ChangeFrequency(Frq[0])
    elif g.input(19):
      p.ChangeFrequency(Frq[1])
    elif g.input(20):
      p.ChangeFrequency(Frq[2])
    elif g.input(21):
      p.ChangeFrequency(Frq[3])
    elif g.input(26):
      p.ChangeFrequency(Frq[4])
    else:
      p.ChangeFrequency(1)
    time.sleep(0.5)
finally:
  p.stop()
  g.cleanup()