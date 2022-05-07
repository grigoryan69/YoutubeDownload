import os
import re
from youtuber import YouTube
from youtuber import Playlist
import linker
from pathlib import Path
downloads_dir = str(os.path.join(Path.home(), "Downloads/Youtube Download"))

if __name__ == '__main__':
    linker.init('web')
    
    @linker.expose
    def downloader(search):
        try:
            playlist = Playlist(search)
            print(f'Downloading playlist: {playlist.title}')
            for video in playlist.videos:
                start = video.streams.get_highest_resolution()
                start.download(f'{downloads_dir}/{playlist.title}')

            print("Download completed!")
        
        except:
            video = YouTube(search)
            print("Downloading Video:", video.title)
            # Getting the highest resolution possible
            start = video.streams.get_highest_resolution()
            start.download(downloads_dir)
            
            print("Download completed!")
            

    linker.start('index.html', size=(440, 300))
