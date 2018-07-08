from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browsermobproxy import Server
import requests
import time
# server = Server("/Users/gg/Documents/my_stuff/automate_with_python/going_headless/browsermob-proxy-2.1.4/bin/browsermob-proxy")
# server.start()
# proxy = server.create_proxy({'captureHeaders': True, 'captureContent': True, 'captureBinaryContent': True})
# service_args = ["--proxy-server=%s" % proxy.proxy]

# CHROMEDRIVER_PATH = '/Users/gg/Documents/my_stuff/automate_with_python/going_headless/chromedriver'
# options = Options()
# options.set_headless(headless=False)
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_argument("'--proxy-server={host}:{port}'.format(host='localhost', port=proxy.port)")

# driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH, options=options)
# proxy.enableHarCaptureTypes(CaptureType.REQUEST_CONTENT, CaptureType.RESPONSE_CONTENT);

# https://www.youtube.com/watch?v=p6D8u6lEDjQ
# url = "https://www.youtube.com/watch?v=p6D8u6lEDjQ"
# proxy.new_har()
# driver.get(url)
# print (proxy.har)  # this is the archive
# # for example:
# all_requests = [entry['request']['url'] for entry in proxy.har['log']['entries']]




# Configure proxy server and return server object
def configure_proxy_server():
    server = Server("/Users/gg/Documents/my_stuff/automate_with_python/going_headless/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    return server

# Configure proxy using the server object and return proxy object
def configure_proxy(server):
    server.start()
    # server.enableHarCaptureTypes(CaptureType.REQUEST_CONTENT, CaptureType.RESPONSE_CONTENT);
    proxy = server.create_proxy()    
    
    return proxy

# Configure selenium driver and return driver object
def configure_driver(proxy_data):
    try:
        co = webdriver.ChromeOptions()
        co.set_headless(headless=True)
        co.add_argument("--no-sandbox")
        co.add_argument("start-maximized")
        co.add_argument("disable-infobars")
        co.add_argument("--disable-extensions")
        co.add_argument("--allow-insecure-localhost")
        co.add_argument('--proxy-server={host}:{port}'.format(host='localhost', 
                                                                port=proxy_data.port))
        driver = webdriver.Chrome(executable_path = "/Users/gg/Documents/my_stuff/automate_with_python/going_headless/chromedriver", 
                                                                chrome_options=co)                                                                       
        return driver
    except WebDriverException as e:
        print(">>>WebDriver exception: {}".format(e))


# Track network traffic
def get_networkTraffic(server, proxy_data, driver):
    try:
        # input_url = input(">>>Enter the url to be checked for network traffic: ")
        request = requests.get("https://www.youtube.com/watch?v=p6D8u6lEDjQ")
        response_code = request.status_code
        # Store the http requests as har object
        if response_code == 200:
            proxy_data.new_har(options={'captureHeaders':True, 'captureContent': True})
            # proxy_data.new_har("google")
            # with open("youtube.har", "wb" ) as file:
            #     file.write(proxy_data.new_har("youtube"))
            
            driver.get("https://www.youtube.com/watch?v=p6D8u6lEDjQ")
            # time.sleep(1)
            # driver.execute_script('document.cookie="VISITOR_INFO1_LIVE=oKckVSqvaGw; path=/; domain=.youtube.com";window.location.reload();')
            # source = driver.get_pagesource()
            # print(source)
            # time.sleep(2)
            video = driver.find_element_by_id("player")
            video.click()
            time.sleep(5)            
            proxy_data.har
            # time.sleep(10)
            # print(google)
            for ent in proxy_data.har['log']['entries']:
                with open("youtube.har", "a" ) as file:
                    file.write(ent['request']['url'])
                print(ent['request']['url'])
        else:
            print(">>>Status code: "+str(response_code))
        driver.quit()
        server.stop()
    except requests.exceptions.RequestException as e:
        print(">>>Request Exception: {}".format(e))


server = configure_proxy_server()
proxy_data = configure_proxy(server)
driver = configure_driver(proxy_data)
get_networkTraffic(server, proxy_data, driver)