import requests
from datetime import datetime
from pytube import YouTube

now = datetime.now()

try:
    response = requests.get("https://dodam.b1nd.com/api/wakeup-song/allowed?"+now.strftime('year=%Y&month=%m&day=%d')).json()
except:
    try:
        requests.get("https://dodam.b1nd.com")
        GPIO.output(15,GPIO.HIGH)
    except:
        GPIO.output(14,GPIO.HIGH)
    finally:
        exit()
        

if response['status']!=200:
    GPIO.output(15,GPIO.HIGH)
    exit()

for idx, val in enumerate(response['data']):
    yt = YouTube(val['videoUrl'])
    yt.streams.filter(only_audio=True).first().download(filename=str(idx+1)+'.mp4')