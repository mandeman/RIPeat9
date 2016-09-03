from moviepy.editor import *
import os

#Created these black clips with moviepy
#movieblack is a black video of duration 0.03 seconds
#moviebig is a black video of duration 0.15 seconds
#Used for delays
black_clip = VideoFileClip(r"movieblack.mp4")
black_clip_big = VideoFileClip(r"moviebig.mp4")

#Hold moviepy objects to be passed for concatenation
vid_arr = []

n = input("Number of iterations after original clip : ")

#----------------------------------------------------------------------------------------------------------------------
#CREATE GRIDS TO BE CONCATENATED LATER
#----------------------------------------------------------------------------------------------------------------------
for i in range(0, n):
    if i is 0:
        clip = VideoFileClip(r"movie.mp4")
    else:
        clip = VideoFileClip(r"movie" +str(i)+ ".mp4")

    newclip = clips_array(
        [[clip, concatenate_videoclips([black_clip, clip]), concatenate_videoclips([black_clip, black_clip, clip])],
         [concatenate_videoclips([black_clip, black_clip, black_clip, clip]),
          concatenate_videoclips([black_clip, black_clip, black_clip, black_clip, clip]),
          concatenate_videoclips([black_clip, black_clip, black_clip, black_clip, black_clip, clip])],
         [concatenate_videoclips([black_clip_big, clip]), concatenate_videoclips([black_clip, black_clip_big, clip]),
          concatenate_videoclips([black_clip, black_clip, black_clip_big, clip])]])

    newclip = newclip.resize(height = 720)

    newclip.write_videofile(r"movie" + str(i+1)+ ".mp4")
#----------------------------------------------------------------------------------------------------------------------
#END OF GRIDMAKING
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
#CONCATENATE THE GRIDS IN ONE VIDEO
#----------------------------------------------------------------------------------------------------------------------
for i in range(0, n+1):
    name = "movie" + str(i) + ".mp4"
    if i is 0:
        vid_arr.append(VideoFileClip(r"movie.mp4"))
    vid_arr.append(VideoFileClip(r"movie" +str(i)+ ".mp4"))

newclip = concatenate_videoclips(vid_arr)
newclip.write_videofile(r"movie.mp4")
#----------------------------------------------------------------------------------------------------------------------
#END OF CONCATENATION
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
#DELETE TEMPORARY FILES
#----------------------------------------------------------------------------------------------------------------------
for i in range(1, n+1):
    if os.path.exists(r"movie" +str(i)+ ".mp4"):
        os.remove(r"movie" +str(i)+ ".mp4")