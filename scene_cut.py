import os
import glob
from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg

target_folder = "/Users/suzanefernandes/Downloads/techjam/scraped_db"

video_path_pattern = os.path.join(target_folder, '*.mp4')  # Only .mp4 videos

for video_file in glob.glob(video_path_pattern):
    print(f"Processing {video_file}")

    # Scene detection
    scene_list = detect(video_file, AdaptiveDetector())

    if len(scene_list) < 2:
        print(f"Not enough scene cuts in {video_file}, skipping.")
        continue

    # Output clips directly to the scraped_db folder, with clear filenames
    # Use original filename as prefix
    file_base = os.path.splitext(os.path.basename(video_file))[0]
    split_video_ffmpeg(
        video_file,
        scene_list,
        output_dir=target_folder,
        output_file_template=f"{file_base}_clip_%03d.mp4"
    )

    # Delete the original long video after successful split
    os.remove(video_file)
    print(f"Deleted original video: {video_file}")

print("All videos processed.")
