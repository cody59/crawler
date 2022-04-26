


#Tech
def amazon(driver, file, keyword):

    for page in range(1, 10): #in the future look for need help for amazon so you can stop at a specific page

        driver.get(f"https://www.amazon.com/s?k={keyword}&page={page}")
        file.write(driver.page_source.encode('ascii', 'ignore'))


def newegg(driver, file, keyword):

    for page in range(1, 10): #in the future look for need help for amazon so you can stop at a specific page

        driver.get(f"https://www.newegg.com/p/pl?d={keyword}&page={page}")
        file.write(driver.page_source.encode('ascii', 'ignore'))


def microcenter(driver, file, keyword):

    for page in range(1, 10): #in the future look for need help for amazon so you can stop at a specific page
        driver.get(f"https://www.microcenter.com/search/search_results.aspx?NTX=mode+MatchPartial&NTT={keyword}&NTK=all&page={page}")
        file.write(driver.page_source.encode('ascii', 'ignore'))


#homegoods

#automobiles

#kitchenware

#