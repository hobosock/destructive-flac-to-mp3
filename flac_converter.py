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


folder = "/media/seth/3037-6134/Music/"
subfolders, files = run_fast_scandir(folder, [".flac"])
mp3_subfolders, mp3_files = run_fast_scandir(folder, ".mp3")

# make some reports to write to file
existed = ""
failed = ""
passed = ""

for i in files:
    # remove .flac from filename
    filename = i[0:-5] + ".mp3"
    print(filename)
    if os.path.isfile(filename):  # check if mp3 file already exists
        print(filename + " already exists, skipping...")
        existed = existed + "\n" + filename
    else:  # convert if not
        os.system("ffmpeg -i " + "\"" + i + "\"" +
                  " -ab 320k -map_metadata 0 -id3v2_version 3 " + "\"" + filename + "\"")
    # check if mp3 exists now (converted correctly), then delete .flac
        if os.path.exists(filename):
            os.remove(i)
            passed = passed + "\n" + filename
        else:
            failed = failed + "\n" + filename

# write reports to files
existed_id = open(folder + "existed.txt", "a")
existed_id.write(existed)
existed_id.close()
passed_id = open(folder + "passed.txt", "a")
passed_id.write(passed)
passed_id.close()
failed_id = open(folder + "failed.txt", "a")
failed_id.write(failed)
failed_id.close()
