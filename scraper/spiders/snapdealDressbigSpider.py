from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class snapdealDressbigSpider(Spider):
    name = "big_snapdeal_dress"
    allowed_domains = ["fashionara.com"]
    start_urls = [
        l.strip() for l in open('urlsnapdeal_dress.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        items = []
        item = DmozItem()
        try:
            item['imglink'] = sel.css('li img.jqzoom').xpath('@src').extract()[0]
        except:
            item['imglink'] = sel.css('li img.jqzoom').xpath('@src').extract()
        item['desc'] = 'None'
        item['price'] = 'None'
        item['prodlink'] = response.url
        item['brand'] = 'None'
        items.append(item)
        return items
        