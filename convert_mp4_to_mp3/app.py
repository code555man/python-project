# pip install moviepy

from moviepy.editor import *

mp4_file = "path"
mp3_output_file = "path"

video = VideoFileClip(mp4_file)

audio = video.audio
audio.write_audiofile(mp3_output_file)

audio.close()
video.close()

