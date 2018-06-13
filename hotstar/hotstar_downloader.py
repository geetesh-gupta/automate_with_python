from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from multiprocessing import Process
from threading import Thread
CHROMEDRIVER_PATH = '/Users/gg/Documents/my_stuff/automate_with_python/going_headless/chromedriver'

def enable_download_in_headless_chrome(browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

options = Options()
options.set_headless(headless=True)
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=options
                         ) 
enable_download_in_headless_chrome(driver, "/Users/gg/Movies/hotstar/")

def loopA():
    for i in range(10,30):    
        url = "https://hsprepack.akamaized.net/videos/bharat/khamp/234/master_Layer8_000" + str(i) + ".ts"     
        driver.get(url)
def loopB():
    for i in range(10,30):    
        url = "https://hsprepack.akamaized.net/videos/bharat/khamp/234/master_Layer9_000" + str(i) + ".ts"     
        driver.get(url)


p1 = Thread(target = loopA)
p2 = Thread(target = loopB)

p1.run()
p2.run()

time.sleep(30)
driver.quit()