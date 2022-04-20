from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def main():

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    # put execution path into parenthesis to make code easily distributable
    driver.get("https://www.newegg.com/p/pl?d=gpu")
    #gpus = driver.find_element(by=By.XPATH, value='')

    f = open(".\page_source\\firefox", "wb")
    f.write((driver.page_source).encode('ascii','ignore'))
    f.close()

    driver.quit()



if __name__ == "__main__":
    main()
