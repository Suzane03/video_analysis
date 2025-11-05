import os
from yt_dlp import YoutubeDL

# Set the target folder where you want to store the downloaded Shorts
target_folder = "/Users/suzanefernandes/Downloads/techjam/scraped_db"  # Replace with your path

# Make sure the folder exists
os.makedirs(target_folder, exist_ok=True)

channel_shorts_url = "https://www.youtube.com/@CuteBabyCats267/shorts"

ydl_opts = {
    'outtmpl': os.path.join(target_folder, '%(title)s.%(ext)s'),  # save each video as Title.ext
    'yes_playlist': True,   # download all shorts in the playlist
    'format': 'best',       # get best quality available
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([channel_shorts_url])
