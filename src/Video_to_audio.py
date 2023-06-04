from moviepy.editor import VideoFileClip, AudioFileClip

def convert(
    *,
    input: str, 
    output: str
) -> None:
    video: VideoFileClip = VideoFileClip(input)
    audio: AudioFileClip = video.audio
    audio.write_audiofile(output)