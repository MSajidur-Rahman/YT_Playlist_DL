import os

path = r"{YOUR PATH}"
url = r"{YOUR PLAYLIST URL}"

for song in os.listdir(path):
    song = f"{path}\{song}"
    os.rename(song,song[:-4]+"mp3")
    

#yt-dlp -x --audio-format mp3 -o "{path}\%(playlist_index)s - %(title)s.%(ext)s" "{url}"
