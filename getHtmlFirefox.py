from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def main():

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    # put execution path into parenthesis to make code easily distributable
    driver.get("https://www.newegg.com/p/pl?d=gpu")
    #gpus = driver.find_element(by=By.XPATH, value='')

    source = open(r"source.txt", "wb")
    source.write((driver.page_source).encode('ascii', 'ignore'))
    source.close()

    print(driver.page_source)
    driver.quit()

if __name__ == "__main__":
    main()
