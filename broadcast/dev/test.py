import os 
import pytube # pip install pytube 
from pytube.cli import on_progress 

url = "https://www.youtube.com/watch?v=YnSW8ian29w"

yt = pytube.YouTube(url, on_progress_callback=on_progress) 
print(yt.streams) 

dir=os.path.split(os.path.abspath(__file__))[0]

yt.streams.filter(progressive=True, file_extension="mp4")\
    .order_by("resolution")\
    .desc()\
    .first()\
    .download(dir)