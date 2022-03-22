from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#do path to executable path in wedrive.chrome

def main():

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.amazon.com")

    f = open(".\page_source\chrome", "wb")
    f.write((driver.page_source).encode('ascii','ignore'))
    f.close()

    driver.quit()

if __name__ == "__main__":
    main()