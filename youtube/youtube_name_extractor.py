import requests
from bs4 import BeautifulSoup
from sys import argv

if len(argv) == 2:
    url = argv[1]

def name_extractor():    
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')    
        name = soup.title.string       
        return name

    else:
        print("Error")
         
name = name_extractor()
print(name)