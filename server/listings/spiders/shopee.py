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
            details = item['item_basic']
            name = details['name']
            item_id = details['itemid']
            shop_id = details['shopid']
            price = details['price']/100000
            rating = details['item_rating']["rating_star"]
            yield {
                'Name': name,
                'Price': price,
                'Rating': rating
            }
            n_ratings = details['item_rating']["rating_count"][0]
            for i in range(0, n_ratings, 6):
                url = f"https://shopee.sg/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=6&offset={i}&shopid={shop_id}&type=0"
                yield scrapy.Request(url, callback=self.parse_review)

            
        
    def parse_review(self, response):
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
            return ret
