import moviepy.editor
#tkinter helps in accessing the mp4 file or location
from tkinter.filedialog import *
#through tkinter vid variable will search the file by opening the folder
vid=askopenfilename()
video=moviepy.editor.VideoFileClip(vid)
#video variable moviepy.editor class is called and function VideoFileClip through which the video path is given
#instead of vid variable you can also give the video location double quotes
aud=video.audio
aud.write_audiofile("audio.mp3")

print("done")
#run this file in command prompt