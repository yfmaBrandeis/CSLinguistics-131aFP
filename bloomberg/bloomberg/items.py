# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BloomItem(scrapy.Item):
    # define the fields for your item here like:
    news_thread = scrapy.Field()
    news_title = scrapy.Field()
    news_body = scrapy.Field()
