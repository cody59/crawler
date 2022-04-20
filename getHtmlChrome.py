import urllib, requests, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    driver.get("view-source:https://www.amazon.com")

    #test
    #pre = driver.page_source
    #pre = driver.find_elements(by=By.TAG_NAME, value="pre").text
    #data = json.loads(pre)
    #print(data)

    f = open(".\page_source\\chrome", "wb")
    f.write((driver.page_source).encode('ascii', 'ignore'))
    f.close()

    driver.quit()

if __name__ == "__main__":
    main()