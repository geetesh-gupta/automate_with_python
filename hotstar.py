from sys import argv
from bs4 import BeautifulSoup
import re
import requests
import webbrowser
def hotstar():
	url =""
	if len(argv) == 2:
		url = argv[1]
	else:
		print("Error")
	url = "http://www.hotstar.com/tv/kya-haal-mr-paanchal/15017/why-is-prarthana-happy/1000213879"
	url_start = url[:47]
	url_end = url[-11:len(url)]
	url = url_start + "_" + url_end
	

	# print(url_start, url_end)
	# print(url)	
	webbrowser.open(url)	


hotstar()