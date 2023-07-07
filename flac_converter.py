import os


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
mp3_subfolders, mp3_files = run_fast_scandir(folder, ".mp3")

for i in files:
    # remove .flac from filename
    filename = i[0:-5] + ".mp3"
    print(filename)
    if os.path.isfile(filename):  # check if mp3 file already exists
        print(filename + " already exists, skipping...")
    else:  # convert if not
        os.system("ffmpeg -i " + "\"" + i + "\"" + " -ab 320k -map_metadata 0 -id3v2_version 3 " + "\"" + filename + "\"")
    # check if mp3 exists now (converted correctly), then delete .flac
    if os.path.exists(filename):
        os.remove(i)