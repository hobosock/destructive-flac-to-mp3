import os

# ffmpeg -i "01 Once More, Jubilations Shall Ring Through The Halls Of Durin's Folk.flac" -ab 320k -map_metadata 0 -id3v2_version 3 output.mp3

folder = "/home/seth/Music/Gimli- Son of Glóin (copy 1)/"
dir_list = os.listdir(folder)

for i in dir_list:
    if os.path.isdir(folder + i):
        print(i)
