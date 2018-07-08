import pychrome
import requests
from bs4 import BeautifulSoup
from sys import argv
import subprocess
from tqdm import tqdm
import math
import os
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def url():
	url = "https://www.youtube.com/watch?v=p6D8u6lEDjQ"

	if len(argv) == 2:
	    url = argv[1]

	print("Fetching: " + url)
	return url



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
	
	search_query = "---sn-cnoa-w5pe.googlevideo.com/videoplayback?"
	count = 0
	while True:
	 	if len(listt) > 100:
	 		return listt


def list_av_generate():
	search_query = "---sn-cnoa-w5pe.googlevideo.com/videoplayback?"
	search_v = "aitags"
	list_av = []
	list_a = []
	list_v = []
	for s in listt:	
		if search_query in s:
			with open("list.txt", "a") as file: 
				file.write(s)
				file.write("\n\n")
				list_av.append(s)
	for v in list_av:
		if search_v in v:
			with open("list_v.txt", "a") as file:
				file.write(v)
				file.write("\n\n")
				list_v.append(v)
		else:
			with open("list_a.txt", "a") as file:
				file.write(v)
				file.write("\n\n")
				list_a.append(v)
					
	return list_av		

url = url()
listt = list_fetcher()
print(listt)
list_av = list_av_generate()
print(list_av)