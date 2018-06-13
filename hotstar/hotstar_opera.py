#


from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
import time
from multiprocessing import Process
from threading import Thread
CHROMEDRIVER_PATH = '/Users/gg/Documents/my_stuff/automate_with_python/going_headless/operadriver'
#
def enable_download_in_headless_chrome(browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

webdriver_service = service.Service('/Users/gg/Documents/my_stuff/automate_with_python/going_headless/operadriver')
webdriver_service.start()

options = Options()
options.set_headless(headless=True )
options.add_argument("--no-sandbox")
#options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Opera(executable_path=CHROMEDRIVER_PATH,
                          options=options
                         ) 

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)



#driver.get('https://www.google.com/')
enable_download_in_headless_chrome(driver, "/Users/gg/Movies/hotstar/")

def loopA():
    for i in range(1,302):    
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
    for i in range(1,302,1):
        path = '/Users/gg/Movies/hotstar/master_Layer8_00' + str(i).rjust(3, '0') + ".ts"
        with open(path, "rb") as inputf:
            outputf.write(inputf.read())



for i in range(1, 302, 1):
    path = '/Users/gg/Movies/hotstar/master_Layer8_00' + str(i).rjust(3, '0') + ".ts"
    os.remove(path)
