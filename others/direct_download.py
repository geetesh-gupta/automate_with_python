import requests
from sys import argv

def download(url):
	print("Video is downloading")
	r = requests.get(url, allow_redirects=True)
	print("Video is downloaded")
	open("face.mp4", 'wb').write(r.content)

def main():    	
	if len(argv) == 2:
        url = argv[1]
	else:
	    print("Usage: python3 direct_download.py url")
	download(url)

if __name__ == "__main__":
	main()