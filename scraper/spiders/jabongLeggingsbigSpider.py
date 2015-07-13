from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class jabongLeggingsbigSpider(Spider):
    name = "big_jabong_leggings"
    allowed_domains = ["jabong.com"]
    start_urls = [
        l.strip() for l in open('urljabong_leggings.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        img = sel.css('div#prdthumb div.thumb-view div.thumb-slider span').xpath('@data-image-big')
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
            
        