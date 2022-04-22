import initialize
initialize.check()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
import urllib, requests, json


def main():
    start = True

    while start == True:

        user = input("Enter a command:")

        if user.lower() == "upgrade".lower():
            initialize.upgrade()

        elif user.lower() == "chrome".lower():

            getHtmlChrome()

        elif user.lower() == "firefox".lower():

            getHtmlFirefox()

        elif user.lower() == "chromium".lower():

            getHtmlChromium()

        elif user.lower() == "edge".lower():

            getHtmlEdge()

        elif user.lower() == "ie".lower():

            getHtmlIe()

        elif user.lower() == "brave".lower():

            getHtmlBrave()

        elif user.lower() == "opera".lower():

            getHtmlOpera()

        elif user == "exit":

            start = False

        else:
            print("\ninvalid command\n")
            print("COMMANDS:\n\tchrome\n\tfirefox\n\tchromium\n\tedge\n\tie (internet explorer)\n\tbrave\n\topera\n\texit\n ")


def getHtmlChrome():

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    driver.get("view-source:https://www.amazon.com")

    f = open(".\page_source\\chrome", "wb")
    f.write((driver.page_source).encode('ascii', 'ignore'))
    f.close()

    driver.quit()

def getHtmlChromium():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

def getHtmlEdge():

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

def getHtmlBrave():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

def getHtmlFirefox():

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    # put execution path into parenthesis to make code easily distributable

    driver.get("view-source:https://www.amazon.com")

    f = open(".\page_source\\firefox", "wb")
    f.write((driver.page_source).encode('ascii', 'ignore'))
    f.close()

    driver.quit()

def getHtmlIe():

    driver = webdriver.Ie(service=Service(IEDriverManager().install()))

def getHtmlOpera():
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())

if __name__ == "__main__":

    main()