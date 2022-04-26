from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.ie.options import Options as ieOptions
from selenium.webdriver.opera.options import Options as operaOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
import search
import json
import scrapy
from websites import choose


def getHtmlChrome():

    options = chromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    f = open(".\page_source\\chrome", "ab")

    choose(driver, f)

    f.close()

    driver.quit()


def getHtmlChromium():

    options = chromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    f = open(".\page_source\\chromium", "ab")

    choose(driver, f)

    f.close()

    driver.quit()


def getHtmlEdge():

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))


def getHtmlBrave():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))


def getHtmlFirefox():

    options = firefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    # put execution path into parenthesis to make code easily distributable

    f = open(".\page_source\\firefox", "ab")

    choose(driver, f)

    f.close()

    driver.quit()


def getHtmlIe():

    driver = webdriver.Ie(service=Service(IEDriverManager().install()))


def getHtmlOpera():
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())

