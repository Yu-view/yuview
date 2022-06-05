from curses import meta
from urllib import response
import scrapy
import json
from scrapy.utils.response import open_in_browser
from listings.items import Listing
class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ['shopee.sg']

    def start_requests(self):
        start_url = f'https://shopee.sg/search?keyword={self.query}' 
        yield scrapy.Request(url=start_url, callback=self.parse_listings)

    def parse_listings(self, response):
        headers = {
        'User-Agent': 'Chrome',
        'Referer': response.url
        }
        url = f"https://shopee.sg/api/v4/search/search_items?by=relevancy&keyword={self.query}&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"

        yield scrapy.Request(url, callback=self.parse_listing, headers=headers)
    
    def parse_listing(self, response):
        data = response.body.decode("utf-8")
        data = json.loads(data)
        items = data['items']
        for item in items:
            listing = Listing()
            details = item['item_basic']
            listing['name'] = details['name']
            listing['rating']= details['item_rating']['rating_star']
            listing['price'] = details['price']/100000
            listing['num_rating'] = details['item_rating']["rating_count"][0]
            listing['num_sold'] = details['historical_sold']
            listing['item_id'] = details['itemid']
            listing['shop_id'] = details['shopid']
            listing['reviews'] = []
            i = 0
            url = "https://shopee.sg/api/v2/item/get_ratings?filter=0&flag=1&itemid={0}&limit=6&offset={1}&shopid={2}&type=0"
            yield scrapy.Request(url.format(listing['item_id'], i,listing['shop_id']), meta=listing, callback=self.parse_review, cb_kwargs={'main_url': url, 'i': i})
            
        
    def parse_review(self, response, main_url, i): 
        listing = response.meta
        data = response.body.decode("utf-8")
        data = json.loads(data)
        ratings = data['data']['ratings'] 
        for rating in ratings:
            ret = {
                "rating": rating['rating_star']
            }
            comment = rating['comment']
            if comment:
                ret["comment"] = comment
            listing['reviews'].append(ret)
        if i < listing['num_rating']:
            i += 6
            yield scrapy.Request(main_url.format(listing['item_id'], i, listing['shop_id']), meta=listing, callback=self.parse_review, cb_kwargs={'main_url': main_url, 'i': i})
        else:
            return listing