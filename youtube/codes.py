import requests
from bs4 import BeautifulSoup
import re
import webbrowser
from sys import argv

def youtube_links_extractor():
    url = "https://www.w3schools.com/tags/ref_urlencode.asp"
    #open with GET method
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:

        soup=BeautifulSoup(resp.text,'html.parser')    
        n = soup.find("table", {"class":"w3-table-all notranslate"})
        with open('extract.txt', 'w') as file:
            file.write(n.text)
        return(n.text)
    else:
        print("Error")
        

text =youtube_links_extractor()

dictt = {}
filename= 'extract.txt'
lines = []
with open(filename, 'r') as infile:    
    for line in infile:
        lines.append(line.rstrip("\n"))
    for i in range(0,475,5):          
        dictt[lines[i+2]] = lines[i]

print(dictt)