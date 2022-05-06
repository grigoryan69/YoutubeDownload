import os
from youtuber import YouTube
import linker
from pathlib import Path
downloads_dir = str(os.path.join(Path.home(), "Downloads/Youtube Download"))

if __name__ == '__main__':
    linker.init('web')

    @linker.expose
    def recv_data(search):
        print(search)

        link = search

        yt = YouTube(link)
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length)
        # Getting the highest resolution possible
        ys = yt.streams.get_highest_resolution()

        # Starting download
        print("Downloading...")
        ys.download(downloads_dir)
        print("Download completed!")

    linker.start('index.html', size=(440, 300))
