from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class YepmeDress(Spider):
    name = "yepme_leggings"
    allowed_domains = ["yepme.com"]
    page_no = 2
    start_urls = [
        "http://www.yepme.com/products.aspx?sCatId=2&pCatId=927&CID=162&pCatName=Leggings&pSubName=Pants"
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
        sites = hxs.css('a.position')
        items = []
        self.driver.quit()
        for site in sites:
            item = DmozItem()
            item['desc'] = site.css('img.prod_Itm_img').xpath('@title').extract()
            item['brand'] = "Yepme"
            item['price'] = site.xpath('span/span[3]/div/div/span[2]/text()').extract()
            if not item['price']:
            	item['price'] = site.xpath('span/span[3]/div/div/span[1]/text()').extract()
            item['imglink'] = site.css("img.prod_Itm_img").xpath('@src').extract()
            item['prodlink'] = site.css('a.position').xpath('@href').extract()
            items.append(item)            
        return items