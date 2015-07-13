from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FlipkartTopsbigSpider(Spider):
    name = "big_flipkart_tops"
    allowed_domains = ["fashionara.com"]
    start_urls = [
        l.strip() for l in open('urlflipkart_tops.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        items = []
        item = DmozItem()
        if not sel.css('div.mainImage div.imgWrapper img.productImage').xpath('@data-zoomimage').extract():
            item['imglink'] = sel.css('div.mainImage div.imgWrapper img.productImage').xpath('@src').extract()
        else:
            item['imglink'] = sel.css('div.mainImage div.imgWrapper img.productImage').xpath('@data-zoomimage').extract() 
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
        