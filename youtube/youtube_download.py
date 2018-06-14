import pychrome
import requests
from bs4 import BeautifulSoup
from sys import argv
import subprocess

url = "https://www.youtube.com/watch?v=l_MyUGq7pgs"

if len(argv) == 2:
    url = argv[1]

def list_fetcher():
	# def pychrome():
	# create a browser instance
	listt = []
	browser = pychrome.Browser(url="http://127.0.0.1:9222")

	# create a tab
	tab = browser.new_tab()

	# register callback if you want
	def request_will_be_sent(**kwargs):
	    # print("loading: %s" % kwargs.get('request').get('url'))
	    listt.append(kwargs.get('request').get('url'))

	tab.Network.requestWillBeSent = request_will_be_sent

	# start the tab 
	tab.start()
	# call method
	tab.Network.enable()
	# call method with timeout
	tab.Page.navigate(url=url)
	# wait for loading
	tab.wait(5)

	browser.close_tab(tab)

	return listt

def list_av_generate():
	search_query = "https://r1---sn-cnoa-w5pe.googlevideo.com/videoplayback?"
	list_av = []
	count = 0
	for s in listt:	
		if search_query in s: 
			count += 1
			list_av.append(s)
			if count == 2:
				return list_av
					
def name_extractor():
    #open with GET method
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')    
        name = soup.title.string
        return name
    else:
        print("Error")

def download():

	a = list_av[1].find('&cver')
	v = list_av[0].find('&cver')	

	audio  = list_av[1][:a]
	video  = list_av[0][:v]

	audio_name = name + "_audio.webm"
	video_name = name + "_video.webm"
	
	print("Audio is downloading")
	r = requests.get(audio, allow_redirects=True)
	print("Audio is downloaded")
	open(audio_name, 'wb').write(r.content)

	print("Video is downloading")
	r = requests.get(video, allow_redirects=True)
	print("Video is downloaded")
	open(video_name, 'wb').write(r.content)

def merge():

	audio_name = name + "_audio.webm"
	video_name = name + "_video.webm"
	output_name = name + ".mkv"
	print("Audio and Video are Merging")
	subprocess.run(['ffmpeg', '-i', video_name, '-i', audio_name, '-c:v', 'copy', '-c:a', 'copy', output_name])
	print("Voila! Audio and Video are merged.")


listt = list_fetcher()
list_av = list_av_generate()
name = name_extractor()
download()
merge()
