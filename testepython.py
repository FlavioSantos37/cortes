from moviepy.editor import VideoFileClip

video = VideoFileClip("D:\SALVOS\video.mp4")
print(f"Duração do vídeo: {video.duration} segundos")
video.close()
