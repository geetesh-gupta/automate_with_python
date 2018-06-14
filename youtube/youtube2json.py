import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = '/Users/gg/Documents/my_stuff/automate_with_python/going_headless/chromedriver'


def enable_download_in_headless_chrome(browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

options = Options()
options.set_headless(headless=False)
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=options
                         ) 
enable_download_in_headless_chrome(driver, "/Users/gg/Movies/hotstar/")

# driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get('https://www.youtube.com/watch?v=l_MyUGq7pg')
time.sleep(5)
timings = driver.execute_script("return window.performance.getEntries();")
timee = timings
with open('youtube.json', 'w') as json_file:
    json.dump(timee, json_file, indent=4)

