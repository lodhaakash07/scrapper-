from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class FlipkartDress(Spider):
    name = "flipkart_dress"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.flipkart.com/womens-clothing/dresses-skirts/dresses/pr?sid=2oq%2Cc1r%2Cxzt%2C3y0&ref=380418d5-4459-490a-9a15-dde3546a1c8e"
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
            try:        
                self.driver.find_element_by_css_selector('div.fk-content div#browse div.line div.browse-vd div.gu-flexi-grid-20-16 div.gd-row div#browse-results-area div.results div#show-more-results').click()
            except:
                elem.send_keys(Keys.PAGE_DOWN)
            m.append(len(self.driver.page_source))
            if n!=0 and m[-1]==m[-2] and m.count(m[-1]) > 2:
                break
            n = n+1
        hxs = Selector(response)
        selen_html = self.driver.page_source
        hxs  = Selector(text=selen_html)
        sites = hxs.css('div.product-unit')
        items = []
        self.driver.quit()
        for site in sites:
            item = DmozItem()
            item['desc'] = site.css('a.fk-display-block::text').extract()
            item['brand'] = "Flipkart"
            item['price'] = site.css('div.pu-price div.pu-final span.fk-font-12::text').extract()
            item['imglink'] = site.css('div.setImages div.cp-item').xpath('@product-image').extract()
            item['prodlink'] = site.css('a.fk-display-block').xpath('@href').extract()
            items.append(item)            
        return items