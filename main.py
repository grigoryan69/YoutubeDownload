import sys
from pytube import YouTube
import eel
from pathlib import Path

eel.init('web')


@eel.expose
def recv_data(search):
    print(search)
    downloads_path = str(Path.home() / "Downloads")

    link = search

    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)
    # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    # Starting download
    print("Downloading...")
    ys.download(downloads_path)
    print("Download completed!")


eel.start('main.html', size=(440, 300))
