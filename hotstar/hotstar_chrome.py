import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from multiprocessing import Process
from threading import Thread
import subprocess

CHROMEDRIVER_PATH = '/Users/gg/Documents/my_stuff/automate_with_python/going_headless/chromedriver'


def enable_download_in_headless_chrome(browser, download_dir):
   #add missing support for chrome "send_command"  to selenium webdriver
   browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
   browser.execute("send_command", params)

options = Options()
options.set_headless(headless=True )
options.add_argument("--no-sandbox")
#options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=options
                         ) 
   
enable_download_in_headless_chrome(driver, "/Users/gg/Movies/hotstar/")

def loopA():
   for i in range(1,5):    
       url = "https://hsprepack.akamaized.net/videos/bharat/khamp/234/master_Layer8_00" + str(i).rjust(3, '0') + ".ts"
       driver.get(url)
loopA()
time.sleep(30)
driver.quit()

url = "https://hsprepack.akamaized.net/videos/bharat/khamp/234/master_Layer8_00" 
episode = url[46:51]
episode_code = url[52:55]
path = "/Users/gg/Movies/hotstar/" + episode+ episode_code +".ts"
with open (path, "wb") as outputf:
    for i in range(1,5,1):
        path = '/Users/gg/Movies/hotstar/master_Layer8_00' + str(i).rjust(3, '0') + ".ts"
        with open(path, "rb") as inputf:
            outputf.write(inputf.read())

for i in range(1, 5, 1):
	path = '/Users/gg/Movies/hotstar/master_Layer8_00' + str(i).rjust(3, '0') + ".ts"
	os.remove(path)

path = "/Users/gg/Movies/hotstar/" + episode+ episode_code +".ts"
infile = path
outfile = path[-len(path):-11] + infile[25:30] + "_" + infile[30:33]+ ".mkv"

subprocess.run(['ffmpeg', '-i', infile,  '-vcodec', 'copy', '-acodec', 'copy', '-f', 'matroska', outfile])