import requests
from datetime import datetime
from pytube import YouTube

now = datetime.now()

response = requests.get("https://dodam.b1nd.com/api/wakeup-song/default").json()

if response['status']!=200:
    print('error code : '+response['status'])
    exit()

for i, v in enumerate(range(4)):
    yt = YouTube(response['data'][i]['videoUrl'])
    yt.streams.filter(only_audio=True).first().download(filename=str(v+1)+'.mp4')