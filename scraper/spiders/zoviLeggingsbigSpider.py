from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class zoviLeggingsbigSpider(Spider):
    name = "big_zovi_leggings"
    allowed_domains = ["zovi.com"]
    start_urls = [
        l.strip() for l in open('urlzovi_leggings.json').readlines()
    ]
    def parse(self, response):
        time.sleep(1)
        sel = Selector(response)
        s = response.url
        pos = s.find("--");
        sub_str = s[pos+2:] 
        # img = sel.xpath('//div[@id="breadcrumbs"]/div/section/img/@src')
        # img = sel.xpath('//*[@id="detail-image"]/img/@src')
        img = sel.css('section#detail-image img')
        items = []
        item = DmozItem()
        # item['imglink'] = img.extract()
        item['imglink'] = "http://c3.zovi.com/bd1/g/p/"+sub_str+"/1_d.jpg"
        item['desc'] = 'None'
        item['price'] = 'None'
        item['prodlink'] = response.url
        item['brand'] = 'None'
        items.append(item)
        return items
        