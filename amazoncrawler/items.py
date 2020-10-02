# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazoncrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    stars = scrapy.Field()
    reviews_count = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
