from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox()
driver.get("https://google.com")
driver.page_source
