import scrapy

def choose(driver, file):

    category = input("Enter product Category: ")
    keyword = input("Enter product: ")

    if category.lower() == "tech":

        tech(driver, file, keyword)





def tech(driver, file, keyword):

    page = 1

    #amazon
    while page != 11: #in the future look for need help for amazon so you can stop at a specific page

        #amazon
        driver.get(f"https://www.amazon.com/s?k={keyword}&page={page}")
        file.write(driver.page_source.encode('ascii', 'ignore'))

        #newegg
        driver.get(f"https://www.newegg.com/p/pl?d={keyword}&page={page}")
        file.write(driver.page_source.encode('ascii', 'ignore'))

        #microcenter
        driver.get(f"https://www.microcenter.com/search/search_results.aspx?NTX=mode+MatchPartial&NTT={keyword}&NTK=all&page={page}")
        file.write(driver.page_source.encode('ascii', 'ignore'))

        page += 1


#homegoods

#automobiles

#kitchenware

#clothing