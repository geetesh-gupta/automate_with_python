
import one_in_another
print('World')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import os
import os.path
# import youtube_download_2

CHROMEDRIVER_PATH = '/Users/gg/Documents/my_stuff/automate_with_python/going_headless/chromedriver'


def enable_download_in_headless_chrome(browser, download_dir):
   #add missing support for chrome "send_command"  to selenium webdriver
   browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
   browser.execute("send_command", params)

options = Options()
options.set_headless(headless=False )
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)  
enable_download_in_headless_chrome(driver, "/Users/gg/Movies/hotstar/")


# audio_name = name + "_audio.webm"
# video_name = name + "_video.webm"
# path_a = "/usr/local/bin/python3 /Users/gg/Documents/my_stuff/automate_with_python/youtube/"+ audio_name
# path_v = "/usr/local/bin/python3 /Users/gg/Documents/my_stuff/automate_with_python/youtube/"+ video_name

# if os.path.exists(path_a):
# 	os.remove(path_a)
# if os.path.exists(path_v):
# 	os.remove(path_v)