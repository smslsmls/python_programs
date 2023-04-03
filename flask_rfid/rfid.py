import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def read():
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()
    return id, text


def write(text):
    try:
        reader.write(text)
        print("written")
    finally:
        GPIO.cleanup()