# destructive-flac-to-mp3
replaces any .flac file found in a directory with an .mp3 file (with preserved meta data) and deletes the original

I put this together because I filled up my phone's SD card with .flac files.  I needed to convert them to mp3 to save space, and going through all the sub directories manually would have been a terrible experience.

FFMPEG does all the heavy lifting here, I just put together a bit of Python to find all the files that needed to be converted.  Meta data is preserved, and files are converted to 320 kbps MP3s.
