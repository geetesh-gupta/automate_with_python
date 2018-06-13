import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from multiprocessing import Process
from threading import Thread
import subprocess
import os.path
from sys import argv

if len(argv) == 2:
	episode_no = argv[1]
else:
	print("Usage: python3 hotstar_chrome.py episode_no")

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

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options) 
   
enable_download_in_headless_chrome(driver, "/Users/gg/Movies/hotstar/")

def loopA():
   	for i in range(1,302):    
   		path = '/Users/gg/Movies/hotstar/master_Layer9_00' + str(i).rjust(3, '0') + ".ts"
   		if not (os.path.exists(path)):
   			url = "https://hsprepack.akamaized.net/videos/bharat/khamp/"+episode_no+"/master_Layer9_00" + str(i).rjust(3, '0')+".ts"
   			driver.get(url)
loopA()
time.sleep(30)
driver.quit()

url = "https://hsprepack.akamaized.net/videos/bharat/khamp/235/master_Layer9_00"
episode = url[46:51]

path = "/Users/gg/Movies/hotstar/" + episode+ episode_no +".ts"
with open (path, "wb") as outputf:
    for i in range(1,302,1):
        path = '/Users/gg/Movies/hotstar/master_Layer9_00' + str(i).rjust(3, '0') + ".ts"
        if os.path.exists(path):
            with open(path, 'rb') as inputf:
                outputf.write(inputf.read())

for i in range(1, 302, 1):
    path = '/Users/gg/Movies/hotstar/master_Layer9_00' + str(i).rjust(3, '0') + ".ts"
    if os.path.exists(path):
        os.remove(path)

path = "/Users/gg/Movies/hotstar/" + episode+ episode_no +".ts"
infile = path
outfile = path[-len(path):-11] + infile[25:30] + "_" + infile[30:33]+ ".mkv"

subprocess.run(['ffmpeg', '-i', infile,  '-vcodec', 'copy', '-acodec', 'copy', '-f', 'matroska', outfile])
os.remove(infile)