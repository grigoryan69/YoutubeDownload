from youtuber import YouTube

while True:
    link = input('search: ')

    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)
    # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    # Starting download
    print("Downloading...")
    ys.download('YoutubeDownload')
    print("Download completed!")
