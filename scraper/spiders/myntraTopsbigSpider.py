from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class myntraTopsbigSpider(Spider):
    name = "big_myntra_tops"
    allowed_domains = ["myntra.com"]
    start_urls = [
        l.strip() for l in open('urlmyntra_tops.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        img = sel.css('div.thumbs img').xpath('@data-zoom')
        items = []
        item = DmozItem()
        item['imglink'] = img.extract()
        try:
            item['imglink'] = item['imglink'][0]
        except:
            item['imglink'] = item['imglink']
        item['desc'] = 'None'
        item['price'] = 'None'
        item['prodlink'] = response.url
        item['brand'] = 'None'
        items.append(item)
        return items       
        