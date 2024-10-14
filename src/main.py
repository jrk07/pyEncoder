from ffmpeg import FFmpeg, FFmpegError, FFmpegUnsupportedCodec, Progress
from logging import info, error
from os import getenv
from pathlib import Path

# Provide a codec, otherwise default to libx264.
codec = getenv('CODEC') or "libx264"

# Provide a file suffix, otherwise default to the codec name.
filename_suffix = getenv('FILE_SUFFIX') or codec

# Quality can be set if desired, else we default to 18 which is
# a good balance of quality and filesize. 
quality = getenv('QUALITY')
crf_value = {
    "LOW": 38,
    "MAX": 0
}.get(quality, 18)

def main():
    video_files = files_from_dir("videos/to_be_processed/")
    for video_file in video_files:
        original_file_path = Path(video_file)
        output_video_path =  "videos/processed/" + original_file_path.stem + "_" + filename_suffix + ".mp4"
        try:
            info(f"encode {video_file} start")
            ffmpeg = (
                FFmpeg()
                .option("y")
                .input(video_file)
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
                info(f"completed encoding file {video_file}")

            ffmpeg.execute()

        except FFmpegUnsupportedCodec as exception:
            error(
                "Unsupported codec provided, please use a valid codec or remove codec flag to default to x264."
            )

        except FFmpegError as exception:
            error("Error running ffmpeg")
            error("Exception:", exception.message)
            error("Arguments used to execute ffmpeg:", exception.arguments)

def files_from_dir(directory):
    files = []
    path = Path(directory)
    for file in path.rglob("*"):
        if file.is_file():
            files.append(file)
    return files

if __name__ == "__main__":
    main()