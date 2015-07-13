from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LimeroadDress(Spider):
    name = "limeroad_dress"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.limeroad.com/clothing/bottom-wear/jeans-jeggings"
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        n = 0
        m=[]
        elem = self.driver.find_element_by_tag_name("body")
        while 1==1:
            # try:
            #     self.driver.find_element_by_css_selector('div#loadmore span.span12').click()
            # except:
            #     elem.send_keys(Keys.PAGE_DOWN)
            
            for i in range(1,10):
                print 'ho'
                elem.send_keys(Keys.PAGE_DOWN)
            m.append(len(self.driver.page_source))
            if n!=0 and m[-1]==m[-2] and m.count(m[-1]) > 2:
                break
            n = n+1
        hxs = Selector(response)
        selen_html = self.driver.page_source
        hxs  = Selector(text=selen_html)
        sites = hxs.css('div.item-container-cell div.pos-rel')
        items = []
        self.driver.quit()
        for site in sites:
            item = DmozItem()
            item['desc'] = site.css('div.prd-name span::text').extract()
            item['brand'] = site.css('div.brand-name a span::text').extract()
            item['price'] = site.css('span.selling_price::text').extract()
            item['imglink'] = site.css('img.img-t').xpath('@src').extract()
            item['prodlink'] = site.css('a.feed-prod').xpath('@href').extract()
            if not item['desc'] or not item['brand'] or not item['price'] or not item['imglink'] or not item['prodlink']:
                continue
            items.append(item)   
        return items
        