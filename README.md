# PyEncoder
Basic video encoder that leverages FFMPEG to encode the supplied video file. 

## Usage
Work in progress...

### Environment Variables
| Name | Required | Description | Default | 
| ----------- | ----------- | ----------- | ----------- |
| CODEC | No | The name of the [video codec] you want to utilize | libx264 | 
| VIDEO_TO_ENCODE | Yes | The relative path to the video you want to encode | n/a | 
| FILE_SUFFIX | No | The suffix you want to apply to your output video file.  | codec name | 
| QUALITY | No | Adjusts output video quality.  Either MAX, LOW, or left out to use default. | Default | 

[video codec]: https://ffmpeg.org/ffmpeg-codecs.html