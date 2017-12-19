#encoding : utf-8
import scrapy
import re
from scrapy.selector import Selector
from BBCNews.items import BbcnewsItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule

class NewsSpider(CrawlSpider):
    name = "bbc"
    allowed_domains = ['www.bbc.com']
    start_urls = ['http://www.bbc.com/']

    rules = (
        Rule(
            LinkExtractor(allow=r"/news/42*"),
            callback = 'parse_news',
            follow = True
        ),
    )

    def parse_news(self,response):
        item = BbcnewsItem()
        item['news_thread'] = response.url.strip().split('/')[-1]
        self.get_title(response,item)
        self.get_body(response,item)
        return item

    def get_title(self,response,item):
        title = response.xpath("/html/head/title/text()").extract()
        if title:
            item['news_title'] = title

    def get_body(self,response,item):
        body = response.xpath('//div[@class="story-body"]/p/text()').extract()
        if body:
            item['news_body'] = body