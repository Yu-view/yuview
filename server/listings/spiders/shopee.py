from curses import meta
from urllib import response
import scrapy
import json
from scrapy.utils.response import open_in_browser
from listings.items import Listing
class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ['shopee.sg']
    custom_settings = {
        "ITEM_PIPELINES": {"listings.pipelines.ShopeePipeline": 300}
    }

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
            for i in range(0, listing['num_rating'], 6):
                url = f"https://shopee.sg/api/v2/item/get_ratings?filter=0&flag=1&itemid={listing['item_id']}&limit=6&offset={i}&shopid={listing['shop_id']}&type=0"
                yield scrapy.Request(url, callback=self.parse_review, meta=listing)
            
        
    def parse_review(self, response):
        listing = response.meta
        data = response.body.decode("utf-8")
        data = json.loads(data)
        ratings = data['data']['ratings'] 
        for rating in ratings:
            ret = {
                'model':  [i['model_name'] for i in rating['product_items']]
            }
            comment = rating['comment']
            if comment:
                ret["comment"] = comment
            listing['reviews'].append(ret)
        if listing['num_rating'] == len(listing['reviews']):
            return listing