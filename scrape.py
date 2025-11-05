import os
from yt_dlp import YoutubeDL

target_folder = "/Users/suzanefernandes/Downloads/techjam/scraped_db"
os.makedirs(target_folder, exist_ok=True)

channel_url = "https://www.youtube.com/@cadanimals"  # The channel's main URL

ydl_opts = {
    'outtmpl': os.path.join(target_folder, '%(title)s.%(ext)s'),
    'yes_playlist': True,   # download all videos in the channel's playlist
    'format': 'best',
    'ignoreerrors': True,   # skip videos with errors
    # You can add 'download_archive': 'downloaded.txt' to skip previously downloaded
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([f"{channel_url}/videos"])
