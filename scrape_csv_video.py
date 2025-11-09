import pandas as pd
import re
import os
from yt_dlp import YoutubeDL

csv_file = "FVC_dup.csv"  # or "FVC_dup.csv"
output_folder = "scraped_db_2"
os.makedirs(output_folder, exist_ok=True)

# Load CSV columns
df = pd.read_csv(csv_file)

def extract_url(markdown_text):
    # Regex to extract URL from markdown [text](url)
    match = re.search(r'\((https?://[^\)]+)\)', str(markdown_text))
    if match:
        return match.group(1)
    # Handle if plain URL in brackets
    match = re.search(r'\[(https?://[^\]]+)\]', str(markdown_text))
    if match:
        return match.group(1)
    # Fallback: just return as-is
    return markdown_text

df['video_url'] = df['video_url'].apply(extract_url)
print(df.head())
print("Total YouTube videos:", df['video_url'].str.contains('youtube.com').sum())

# Download as mp4
youtube_df = df[df['video_url'].str.contains('youtube.com')]

ydl_opts = {
    "format": "mp4",
    "outtmpl": os.path.join(output_folder, "%(id)s.%(ext)s"),
    "quiet": False,
}

with YoutubeDL(ydl_opts) as ydl:
    for idx, row in youtube_df.iterrows():
        try:
            print(f"Downloading: {row['video_url']}")
            ydl.download([row["video_url"]])
        except Exception as e:
            print(f"Failed to download {row['video_url']}: {e}")

print(f"Done. Check the '{output_folder}/' folder for downloaded MP4s.")
