from pytube import YouTube
import glob
import os

url = "https://www.youtube.com/watch?v=YnSW8ian29w"

dir=os.path.split(os.path.abspath(__file__))[0]

yt = YouTube(url)

print(yt.streams)

yt.streams.filter(only_audio=True).first().download(dir)

files = glob.glob(dir+r'\*.mp4')
for x in files:
	if not os.path.isdir(x):
		filename = os.path.split(x)
		try:
			os.rename(x,filename[0] +r'\1.mp3')
		except:
			pass

# files = glob.glob(dir+r'\*.mp3')
# print(files)
# for file in files:
# 	if not os.path.isdir(x):
# 		filename = os.path.splitext(x)
# 		playsound(file)