import html
from bs4 import BeautifulSoup
import requests
# import re
# import webbrowser
# from sys import argv
# from w3lib.html import replace_entities
# import unicode
# import HTMLParser
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

        soup = BeautifulSoup(resp.content.decode('utf-8', 'ignore'))
        soup = soup.decode('utf-8', 'ignore')
        # soup=BeautifulSoup(resp.content,'html.parser')        
        # soup = soup.decode('utf-8', 'ignore')
        # n = soup.find("div", {'id': 'player'})
        # with open('extract.txt', 'w') as file:
        #     file.write(n.text)
        # print(soup)
        # print("\n\n\n")
        # print(n)
        return soup
    else:
        print("Error")
         
text = youtube_links_extractor()
print(text)
# a = text.read().decode('utf-8', 'ignore')
# print(a)
# b = text.encode('utf-8')
# print(b)
# # h = HTMLParser.HTMLParser()
# # # soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)

# # text = html.encode('utf-8')
# # # text = b('\' {tet})
# # text1 =h.unescape(text)
# d = b.decode('utf-8', 'ignore')
# # print(html.decode("utf-8", "ignore"))

# print(d)
# # print(BeautifulSoup("<p>&pound;682m</p>", "lxml"))
# # soup = BeautifulSoup(html, 'lxml')
# # print(soup)

# # print(replace_entities(html))

# # text1 = unicode(text)
# # text2 = html.unescape(text1)
# # print(text[:20], text1[:20], text2[:20])