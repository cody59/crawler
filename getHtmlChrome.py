from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#do path to executable path in wedrive.chrome

def main():

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.google.com/")

    driver.quit()

if __name__ == "__main__":
    main()