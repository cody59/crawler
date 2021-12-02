from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://google.com")
driver.page_source
