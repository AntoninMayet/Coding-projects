# https://www.youtube.com/watch?v=bgR3yESAEVE
import pytube
from pytube import *

video = input("Paste the link to the video you want to download :\n")

yt = pytube.YouTube(video)

print(yt.title)
