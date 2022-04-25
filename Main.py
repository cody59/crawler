import initialize
initialize.check()
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
from bs4 import BeautifulSoup
import search
import json

def main():

    start = True

    while start == True:

        user = input("Enter a command:")

        if user.lower() == "upgrade":
            initialize.upgrade()

        elif user.lower() == "chrome":

            getHtmlChrome()

        elif user.lower() == "firefox":

            getHtmlFirefox()

        elif user.lower() == "chromium":

            getHtmlChromium()

        elif user.lower() == "edge":

            getHtmlEdge()

        elif user.lower() == "ie":

            getHtmlIe()

        elif user.lower() == "brave":

            getHtmlBrave()

        elif user.lower() == "opera":

            getHtmlOpera()

        elif user.lower() == "update":

            initialize.upgrade()

        elif user == "exit":

            start = False

        else:
            print("\ninvalid command\n")
            print("COMMANDS:\n\tchrome\n\tfirefox\n\tchromium\n\tedge\n\tie (internet explorer)\n\tbrave\n\topera\n\tupdate\n\texit\n ")


def getHtmlChrome():

    options = chromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    keyword = input("Enter product: ")
    f = open(".\page_source\\chrome", "ab")

    for page in range(1, 31): #in the future look for need help for amazon so you can stop at a specific page

        driver.get(f"https://www.amazon.com/s?k={keyword}&page={page}")
        f.write(driver.page_source.encode('ascii', 'ignore'))

    f.close()

    driver.quit()


def getHtmlChromium():

    options = chromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    driver.get("view-source:https://www.amazon.com")

    f = open(".\page_source\\chromium", "wb")
    f.write((driver.page_source).encode('ascii', 'ignore'))
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