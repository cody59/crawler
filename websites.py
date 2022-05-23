import multiprocessing

import scrapy
from multiprocessing import Pool, cpu_count

def choose(driver, file):

    category = input("Enter product Category: ")
    keyword = input("Enter product: ")

    if category.lower() == "tech":

        urls = tech(driver, file, keyword)

        section = [urls[x:x + 4] for x in range(0, len(urls), 4)]
        print(len(section))
        print(section)

        procs = []

        for u in range(len(section)):

            p = multiprocessing.Process(scrape(driver, file, section[u]))
            p.start()
            procs.append(p)

        for proc in procs:

            proc.join()


        #p = multiprocessing.Process(scrape(driver, file, url[0]))
        #p2 = multiprocessing.Process(scrape(driver, file, url[1]))
        #p3 = multiprocessing.Process(scrape(driver, file, url[2]))
        #p4 = multiprocessing.Process(scrape(driver, file, url[3]))

        #p.start()
        #p2.start()
        #p3.start()
        #p4.start()

        #p.join()
        #p2.join()
        #p3.join()
        #p4.join()


def scrape(driver, file, urls):

    for i in range(len(urls)):
        # amazon
        driver.get(urls[i])
        file.write(driver.page_source.encode('ascii', 'ignore'))

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