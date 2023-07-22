import os

path = r"{YOUR PATH}"

for song in os.listdir(path):
    song = f"{path}\{song}"
    os.rename(song,song[:-4]+"mp3")
    

<<<<<<< HEAD
#yt-dlp -x --audio-format mp3 -o "{YOUR PATH}\%(playlist_index)s - %(title)s.%(ext)s" "{YOUR PLAYLIST URL}}"
=======
#yt-dlp -x --audio-format mp3 -o "{YOUR PATH}\%(playlist_index)s - %(title)s.%(ext)s" "{YOUR PLAYLIST URL}"
>>>>>>> 413bae8da2588eee1cd7f7a61d7e78a0e5630b6f
