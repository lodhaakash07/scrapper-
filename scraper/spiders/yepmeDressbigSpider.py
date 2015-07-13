from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class yepmeDressbigSpider(Spider):
    name = "big_yepme_dress"
    allowed_domains = ["yepme.com"]
    start_urls = [
        l.strip() for l in open('urlyepme_dress.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        items = []
        item = DmozItem()
        sel = Selector(response)
        img = sel.css('img#img2').xpath('@src').extract()       
        item['desc'] = 'None'
        item['imglink'] = img
        if not item['imglink']:
             item['imglink'] = sel.css('img#img1').xpath('@src').extract()  
        item['price'] = 'None'
        item['prodlink'] = response.url
        item['brand'] = 'None'
        items.append(item)
        return items
        