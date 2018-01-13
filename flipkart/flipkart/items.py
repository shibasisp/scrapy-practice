# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_category = scrapy.Field()
    product_link = scrapy.Field()
    product_name = scrapy.Field()
    product_image = scrapy.Field()
    product_selling_price = scrapy.Field()
    product_MRP = scrapy.Field()
    product_discount = scrapy.Field()
    product_rating = scrapy.Field()
    product_warranty = scrapy.Field()
    product_features = scrapy.Field()
