import urllib, requests, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

def main():

    print("hi")

def getHtmlChrome(url):

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    driver.get("view-source:https://www.amazon.com")

    f = open(".\page_source\\chrome", "wb")
    f.write((driver.page_source).encode('ascii', 'ignore'))
    f.close()

    driver.quit()

def getHtmlChromium(url):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

def getHtmlEdge(url):

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

def getHtmlBrave(url):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

def getHtmlFirefox(url):

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    # put execution path into parenthesis to make code easily distributable

    driver.get(url)

    f = open(".\page_source\\firefox", "wb")
    f.write((driver.page_source).encode('ascii','ignore'))
    f.close()

    driver.quit()

def getHtmlIe(url):

    driver = webdriver.Ie(service=Service(IEDriverManager().install()))

def getHtmlOpera(url):
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
