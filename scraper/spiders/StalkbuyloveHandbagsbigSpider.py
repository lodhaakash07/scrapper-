from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class StalkbuyloveHandbagsbigSpider(Spider):
    name = "big_stalkbuylove_handbags"
    allowed_domains = ["stalkbuylove.com"]
    start_urls = [
        l.strip() for l in open('urlstalkbuylove_handbags.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        img = sel.css('div.list p.cloud-zoom-gallery').xpath('@href')
        items = []
        item = DmozItem()
        try:
            item['imglink'] = img.extract()[0]
        except:
            item['imglink'] = img.extract()
        item['desc'] = 'None'
        item['price'] = 'None'
        item['prodlink'] = response.url
        item['brand'] = 'None'
        items.append(item)
        return items
        