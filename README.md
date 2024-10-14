# PyEncoder
Basic video encoder that leverages FFMPEG to encode the supplied video file. 

## Usage
- Check out repo locally.
- Run setup.sh to put down i/o directories `./setup.sh`
- Add video files you wish to encode to the `videos/to_be_processed` directory.
- Add a [.env] file if you wish to modify an of the available environment variables from default (see below).
- Run `docker compose up --build`.
- Docker should exit with code 0 and your files should be available in `videos/processed`.

### Environment Variables
| Name | Description | Default | 
| ----------- | ----------- | ----------- |
| CODEC | The name of the [video codec] you want to utilize | libx264 | 
| FILE_SUFFIX | The suffix you want to apply to your output video file.  | codec name | 
| QUALITY | Adjusts output video quality.  Either MAX, LOW, or left out to use default. | Default | 

[video codec]: https://ffmpeg.org/ffmpeg-codecs.html
[.env]: https://dotenvx.com/docs/env-file