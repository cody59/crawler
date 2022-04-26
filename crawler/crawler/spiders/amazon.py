# Import library
import scrapy
# Create Spider class
class booksToScrape(scrapy.Spider):
    # Name of spider
    name = 'books'
    # Website you want to scrape
    start_urls = [
        'http://books.toscrape.com'
    ]
    # Parses the website
    def parse(self, response):
        # Book Information cell
        for i in response.css('.product_pod'):
            # Attributes
            title = i.css('a[title]::text').getall()
            price = i.css('.price_color::text').getall()
            # Output
            yield {
                'Title': title,
                'Price': price
            }