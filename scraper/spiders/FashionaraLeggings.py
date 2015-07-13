from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class FashionaraLeggings(Spider):
    name = "fashionara_leggings"
    allowed_domains = ["fashionara.com"]
    start_urls = [
        "http://www.fashionara.com/ladies/leggings.html?_escaped_fragment_=dir%3Ddesc%26product%3DLEGGINGS%26sort%3Dnew_bestselling#!product=LEGGINGS"
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        n = 0
        m=[]
        elem = self.driver.find_element_by_tag_name("body")
        while 1==1:
            for i in range(1,10):
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            m.append(len(self.driver.page_source))
            if n!=0 and m[-1]==m[-2] and m.count(m[-1]) > 2:
                break
            n = n+1
        hxs = Selector(response)
        selen_html = self.driver.page_source
        hxs  = Selector(text=selen_html)
        sites = hxs.css('li.item')
        items = []
        self.driver.quit()
        for site in sites:
            item = DmozItem()
            item['desc'] = site.css('h2.product-name a::text').extract()
            item['brand'] = site.css('p.brand::text').extract()
            if not site.css('div.price-box span.special-price span.price::text').extract():
                item['price'] = site.css('div.price-box span.regular-price span.price::text').extract()
            else:
                item['price'] = site.css('div.price-box span.special-price span.price::text').extract()
            item['imglink'] = site.css('a.product-image').xpath('@data-image-src').extract()
            item['prodlink'] = site.css('h2.product-name a').xpath('@href').extract()
            items.append(item) 
        return items