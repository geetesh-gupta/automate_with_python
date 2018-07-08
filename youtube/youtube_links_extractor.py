import requests
from bs4 import BeautifulSoup
import re
from sys import argv
from html_extract import html_extract, urls_extract, video_urls_format_extract
from url_maker import url_maker
from utf_decoder import utf_decoder
from youtube_name_extractor import name_extractor

url = "https://www.youtube.com/watch?v=p6D8u6lEDjQ"
if len(argv) == 2:
    url = argv[1]
else:
    print("ERROR")

def youtube_links_extractor():
     
    #open with GET method
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:

        soup=BeautifulSoup(resp.text,'html.parser')    
        n = soup.find("div", {'id': 'player'})
        with open('extract.txt', 'w') as file:
            file.write(n.text)
        return n.text
    else:
        print("Error")
         

def url_quality_format_extractor(quality, format, video_urls_mp4, video_urls_webm):
    quality = quality + 'p'
    if format is 'mp4':
        list = video_urls_mp4
    else:
        list = video_urls_webm
    for url in list:
        if quality in url:
            return url




def download(url_final, name):
    print("Video is downloading")
    r = requests.get(url_final, allow_redirects=True)
    print("Video is downloaded")
    name = name +'.webm'
    open(name, 'wb').write(r.content)


html = youtube_links_extractor()
decoded_html = utf_decoder(html)
(list, search_number) = html_extract(decoded_html)
(video_urls, audio_urls) = urls_extract(list)
(video_urls_mp4, video_urls_webm) = video_urls_format_extract(video_urls, audio_urls)
url_pre_finale = url_quality_format_extractor('720','mp4', video_urls_mp4, video_urls_webm)
url_final = url_maker(url_pre_finale, search_number)
name = name_extractor(url)
download(url_final, name)

# Link doesn't work because of content protection by youtube. I think cpn value is required.
print(url_final)


