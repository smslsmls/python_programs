import requests
from datetime import datetime
from pytube import YouTube

dir='~'

now = datetime.now()

response = requests.get("https://dodam.b1nd.com/api/wakeup-song/allowed?"+now.strftime('year=%Y&month=%m&day=%d')).json()

if response['status']!=200:
    print('error code : '+response['status'])
    exit()

for idx, val in enumerate(response['data']):
    yt = YouTube(val['videoUrl'])
    yt.streams.filter(only_audio=True).first().download(output_path=dir,filename=str(idx+1)+'.mp4')