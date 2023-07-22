# YT_Playlist_DL

## youtube-dlp is waiting on official an fix for major bug, bug was fixed on master branch
## I didn't want to download ffmpeg to convert

Steps:
- pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz 

- create a folder and copy its path

- replace all instances of "{YOUR_PATH}" (line 3,4, and 8) with copied path
  - repeat for "{YOUR PLAYLIST URL}" (line 8) with your YT platlist (make sure its not private)

- copy line 8 without the "#" at the beginning and run it in your CLI
- after completion, run the python code to convert all the .webm files to mp3
