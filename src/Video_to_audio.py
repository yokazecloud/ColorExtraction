from moviepy.editor import VideoFileClip, AudioFileClip

def convert(
    *,
    input: str
) -> None:
    OUTPUT: str = f"{input}_audio.mp3"
    video: VideoFileClip = VideoFileClip(input)
    audio: AudioFileClip = video.audio
    audio.write_audiofile(OUTPUT)