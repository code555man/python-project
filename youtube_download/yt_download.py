from pytube import YouTube

url = "https://www.youtube.com/watch?v=PMYcQSMXzKw&list=RDPMYcQSMXzKw&start_radio=1"
video = YouTube(url)

stream = video.streams.get_highest_resolution()
stream.download()