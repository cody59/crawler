from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import sys

options = Options()
options.add_argument("-profile")
options.add_argument("/home/blue/.mozilla/firefox/pee7qm22.default")
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_options=options)
print(sys.path)
os.system("echo hi")
driver = webdriver.Firefox()
driver.get("https://google.com")
driver.page_source