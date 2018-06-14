import subprocess

if len(argv) == 3:
	audio_name = argv[1]
	video_name = argv[2]
else:
	print(Usage: python3 av_merger audio_path video_path)

output_name = video_name + ".mkv"
def merge():
	print("Audio and Video are Merging")
	subprocess.run(['ffmpeg', '-i', video_name, '-i', audio_name, '-c:v', 'copy', '-c:a', 'copy', output_name])
	print("Voila! Audio and Video are merged.")
merge()