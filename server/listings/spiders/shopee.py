from tokenize import String
import scrapy
from scrapy.loader import ItemLoader
from listings.items import Listing
from server.main import Item
class ShopeeSpider(scrapy.Spider):
    name = "shopee"

    def start_requests(self):
        url = f'https://shopee.sg/search?keyword={self.query}' 
        yield scrapy.Request(url=url, callback=self.parseListing)

    def parse(self, response):
        for listing in response.css('div.shopee-search-item-result__item::'):
            url = listing.css('a::attr(href)').get()
            url = listing.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parseListing)
    
    def parseListing(self, response):
        l = ItemLoader(item=Listing(), response=response)
        l.add_css('name', 'div.VCNVHn span::text')
        l.add_css('rating', 'div.pmmxKx::text')
        l.add_css('num_rating', 'div.MrYJVA::text')
        l.add_css('num_sold', 'div._45NQT5::text')
        #l.add_css('reviews', )
        return l.load_item()
