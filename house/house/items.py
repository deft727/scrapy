# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    space = scrapy.Field()
    image = scrapy.Field()
    seller = scrapy.Field()

    # door = scrapy.Field()
    # park = scrapy.Field()
    # new_price = scrapy.Field()
    # old_price = scrapy.Field()
    # discount = scrapy.Field()
    # price_per_meter = scrapy.Field()
    #
    # pass
