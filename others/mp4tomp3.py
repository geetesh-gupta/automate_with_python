import os
os.system(("ffmpeg -i facebook.mp4 -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 audio.mp3")