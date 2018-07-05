import requests
from bs4 import BeautifulSoup
import re
import webbrowser
from sys import argv

def youtube_links_extractor():
    url = "https://www.youtube.com/watch?v=p6D8u6lEDjQ"
    if len(argv) == 2:
        url = argv[1]
    else:
        print("ERROR")
     
    #open with GET method
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:

        soup=BeautifulSoup(resp.text,'html.parser')    
        n = soup.find("div", {'id': 'player'})
        with open('extract.txt', 'w') as file:
            file.write(n.text)
        print(n)

    else:
        print("Error")
         
youtube_links_extractor()