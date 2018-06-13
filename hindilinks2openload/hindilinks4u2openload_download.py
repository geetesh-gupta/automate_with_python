import requests
from bs4 import BeautifulSoup
import re
import webbrowser
from sys import argv
from openload import OpenLoad
def hindilink4u_to_openload():
    url = ""
    if len(argv) == 2:
        url = argv[1]
    else:
        print("ERROR")
     
    #open with GET method
    resp=requests.get(url)
     
    #http_respone 200 means OK status
    if resp.status_code==200:

        soup=BeautifulSoup(resp.text,'html.parser')    
        n = soup.text.find("openload.co/f/") + 14
        
        file_id = soup.text[n:n+11]
        username = '832f1bf304225c91'
        key = '_fi7pPg3'
        
        ol = OpenLoad(username, key)
        
        # Get a download ticket and captcha url.
        preparation_resp = ol.prepare_download(file_id)
        ticket = preparation_resp.get('ticket')
#        print(ticket)
        # Sometimes no captcha is sent in openload.co API response.
        captcha_url = preparation_resp.get('captcha_url')
#        print(captcha_url)
        if captcha_url:
            # Solve captcha.
            captcha_response = solve_captcha(captcha_url)
        else:
            captcha_response = ''

        download_resp = ol.get_download_link(file_id, ticket, captcha_response)
#        print(download_resp.get('url'))
#        try:
        direct_download_url = download_resp.get('url')
#            
#        except PermissionDeniedException:
#            print("Error")
        webbrowser.open(direct_download_url, new=0, autoraise=True)
        

    else:
        print("Error")
         
hindilink4u_to_openload()