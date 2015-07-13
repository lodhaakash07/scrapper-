from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FashionaraHandbagsbigSpider(Spider):
    name = "big_fashionara_handbags"
    allowed_domains = ["fashionara.com"]
    start_urls = [
        l.strip() for l in open('urlfashionara_handbags.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        try:
            img = sel.css('a.elevatezoom-gallery').xpath('@data-zoom-image').extract()[0]
        except:
            img = sel.css('a.elevatezoom-gallery').xpath('@data-zoom-image').extract()
        items = []
        item = DmozItem()
        item['desc'] = 'None'
        item['imglink'] = img
        item['price'] = 'None'
        item['prodlink'] = response.url
        item['brand'] = 'None'
        items.append(item)
        return items
        
        