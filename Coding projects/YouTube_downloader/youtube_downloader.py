import pytube
from pytube import YouTube

video = input("Paste the link to the video you want to download :\n")

yt = pytube.YouTube(video)

print(yt.title)
