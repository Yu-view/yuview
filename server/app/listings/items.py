# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class Listing(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    num_rating = scrapy.Field()
    num_sold = scrapy.Field()
    shop_id = scrapy.Field()
    item_id = scrapy.Field()
    reviews = scrapy.Field()
