import os

# ffmpeg -i "01 Once More, Jubilations Shall Ring Through The Halls Of Durin's Folk.flac" -ab 320k -map_metadata 0 -id3v2_version 3 output.mp3


def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)

    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files


folder = "/home/seth/Music/Gimli- Son of Glóin (copy 1)/"
subfolders, files = run_fast_scandir(folder, [".flac"])

for i in files:
    os.system("ffmpeg -i " + "\"" + i + "\"" + " -ab 320k -map_metadata 0 -id3v2_version 3 " + "\"" + i + "\"" + ".mp3")