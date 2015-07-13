from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class koovsHandbagsbigSpider(Spider):
    name = "big_koovs_handbags"
    allowed_domains = ["koovs.com"]
    start_urls = [
        l.strip() for l in open('urlkoovs_handbags.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        img = sel.xpath('//div[@id="mainProductImage"]/img/@src')
        items = []
        item = DmozItem()
        item['imglink'] = img.extract()
        item['desc'] = 'None'
        item['price'] = 'None'
        item['prodlink'] = response.url
        item['brand'] = 'None'
        items.append(item)
        return items
        