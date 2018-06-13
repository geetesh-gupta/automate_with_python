import subprocess

infile = '/Users/gg/Movies/infile.ts'
outfile = '/Users/gg/Movies/hotstar/outfile.mkv'

subprocess.run(['ffmpeg', '-i', infile,  '-vcodec', 'copy', '-acodec', 'copy', '-f', 'matroska', outfile])