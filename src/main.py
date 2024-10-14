from ffmpeg import FFmpeg, FFmpegError, FFmpegUnsupportedCodec, Progress
from os import getenv
from pathlib import Path

# Grab the path to the video we want to encode.
input_video_path = Path(getenv('VIDEO_TO_ENCODE'))

if not input_video_path:
    print("VIDEO_TO_ENCODE environment variable not set, exiting.")
    exit()

# Provide a codec, otherwise default to libx264.
codec = getenv('CODEC') or "libx264"

# Provide a file suffix, otherwise default to the codec name.
filename_suffix = getenv('FILE_SUFFIX') or codec

# Reuse the input vidoes path and append with the codec name to show it's the encoded file along
# with the appropriate extension.

# TODO custom output path
output_video_path =  input_video_path.parent / (input_video_path.stem + "_" + filename_suffix + ".mp4")

# Quality can be set if desired, else we default to 18 which is
# a good balance of quality and filesize. 
quality = getenv('QUALITY')
crf_value = {
    "LOW": 38,
    "MAX": 0
}.get(quality, 18)

def main():
    try:
        ffmpeg = (
            FFmpeg()
            .option("y")
            .input(input_video_path)
            .output(
                output_video_path,
                {"codec:v": {codec}},
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

    except FFmpegUnsupportedCodec as exception:
        print(
            "Unsupported codec provided, please use a valid codec or remove codec flag to default to x264."
        )

    except FFmpegError as exception:
        print("Error running ffmpeg")
        print("Exception:", exception.message)
        print("Arguments used to execute ffmpeg:", exception.arguments)

if __name__ == "__main__":
    main()