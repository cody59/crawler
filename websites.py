import scrapy
from multiprocessing import Pool, cpu_count

def choose(driver, file):

    category = input("Enter product Category: ")
    keyword = input("Enter product: ")

    if category.lower() == "tech":

        urls = tech(driver, file, keyword)

        #p = Pool(cpu_count()-1)
        #p.map(scrape, urls)
        #p.terminate()
        #p.join()

def scrape(urls):
    print("C:\\Users\\blue\\.wdm\\drivers\\geckodriver\\win64\\v0.31.0")

    print(urls)

def tech(driver, file, keyword):

    page = 1
    urls = list()

    while page != 11:

        #amazon
        #driver.get(f"https://www.amazon.com/s?k={keyword}&page={page}")
        #file.write(driver.page_source.encode('ascii', 'ignore'))

        urls.append(f"https://www.amazon.com/s?k={keyword}&page={page}")

        #newegg
        #driver.get(f"https://www.newegg.com/p/pl?d={keyword}&page={page}")
        #file.write(driver.page_source.encode('ascii', 'ignore'))

        urls.append(f"https://www.newegg.com/p/pl?d={keyword}&page={page}")

        #microcenter
        #driver.get(f"https://www.microcenter.com/search/search_results.aspx?NTX=mode+MatchPartial&NTT={keyword}&NTK=all&page={page}")
        #file.write(driver.page_source.encode('ascii', 'ignore'))

        urls.append(f"https://www.microcenter.com/search/search_results.aspx?NTX=mode+MatchPartial&NTT={keyword}&NTK=all&page={page}")

        page += 1

    return urls



#homegoods

#automobiles

#kitchenware

#clothing