from moviepy.editor import VideoFileClip

video = VideoFileClip("video.mp4")
video.write_gif("export.gif")

