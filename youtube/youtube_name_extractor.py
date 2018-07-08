import requests
from bs4 import BeautifulSoup
from sys import argv

def name_extractor(url):  
    
    if len(argv) == 2:
        url = argv[1]  
    
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')    
        name = soup.title.string       
        return name

    else:
        print("Error")
         