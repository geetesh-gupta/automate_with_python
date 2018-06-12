import requests
from bs4 import BeautifulSoup
import re
import webbrowser
from selenium import webdriver
from sys import argv
from openload import OpenLoad
def openload():
    # the target we want to open    
    url = "https://www.google.com"
    if len(argv) == 2:
        url = argv[1]
    else:
       print("ERROR")
#    url='https://www.hindilinks4u.to/2018/06/jurassic-world-fallen-kingdom-2018-in-hindi.html'
     
    #open with GET method
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')    
        n = soup.text.find("openload.co/f/") -8
        url = soup.text[n:n+34]
        webbrowser.open(url, new=0, autoraise=True)
 
    else:
        print("Error")
         
openload()