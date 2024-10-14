from ffmpeg import FFmpeg, Progress
from os import getenv
from pathlib import Path

# Grab the path to the video we want to encode from environment.
path_from_env = getenv('VIDEO_TO_ENCODE')

# Ensure the VIDEO_TO_ENCODE environment variable exists, if not, exit and log. 
if path_from_env:
    input_video_path = Path(path_from_env)
else: 
    print("VIDEO_TO_ENCODE environment variable not set,  exiting.")
    exit()

# Reuse the input vidoes path and append with x264 to show it's the encoded file along
# with the appropriate extension.
output_video_path =  input_video_path.parent / (input_video_path.stem + "_x264.mp4")

# Quality can be set if desired, else we default to 18 which is
# a good balance of quality and filesize. 
quality = getenv('QUALITY')
if quality == "LOW":
    crf_value = 38
elif quality == "MAX":
    crf_value = 0
else: 
    crf_value = 18

def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(input_video_path)
        .output(
            output_video_path,
            {"codec:v": "libx264"},
            crf={crf_value},
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    @ffmpeg.on("completed")
    def on_completed():
        print(f"completed encoding file {output_video_path}")

    ffmpeg.execute()


if __name__ == "__main__":
    main()