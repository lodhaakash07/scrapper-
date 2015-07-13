from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class JabongTops(Spider):
    name = "jabong_tops"
    allowed_domains = ["jabong.com"]
    start_urls = [
        "http://www.jabong.com/women/clothing/tops-tees-shirts/tops/"
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        n = 0
        m=[]
        elem = self.driver.find_element_by_tag_name("body")
        elem.send_keys(Keys.PAGE_DOWN)
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
        sites = hxs.css('ul#productsCatalog li')
        items = []
        self.driver.quit()
        for site in sites:
            item = DmozItem()
            item['desc'] = site.css('a span.qa-brandTitle::text').extract()
            item['brand'] = site.css('a span.qa-brandName::text').extract()
            item['price'] = site.css('a span.price strong.qa-price::text').extract()
            item['imglink'] = site.css("a span.cat-prd-img span").xpath('@id').extract()
            item['prodlink'] = site.css('a').xpath('@href').extract()
            items.append(item)            
        return items