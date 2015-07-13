from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class MyntraLeggings(Spider):
    name = "myntra_leggings"
    allowed_domains = ["myntra.com"]
    page_no = 2
    start_urls = [
        "http://www.myntra.com/women-leggings-capris?src=tn&nav_id=49&f=categories%3ALeggings"
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        x = 0
        n = 0
        m=[]
        elem = self.driver.find_element_by_tag_name("body")
        while 1==1:
            try:
                self.driver.find_element_by_css_selector('.content .results-cnt .show-more').click()
            except:
                elem.send_keys(Keys.PAGE_DOWN)
            for i in range(1,7):
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            m.append(len(self.driver.page_source))
            if n!=0 and m[-1]==m[-2] and m.count(m[-1]) > 2:
                break
            n = n+1
        hxs = Selector(response)
        selen_html = self.driver.page_source
        hxs  = Selector(text=selen_html)
        sites = hxs.css('ul.results li')
        items = []
        self.driver.quit()
        for site in sites:
            item = DmozItem()
            item['desc'] = site.css('a div.product::text').extract()
            item['brand'] = site.css('a div.brand::text').extract()
            item['price'] = site.css('a div.price::text').extract()
            item['imglink'] = site.css('a img.thumb').xpath('@_src').extract()
            item['prodlink'] = site.css('a').xpath('@href').extract()
            items.append(item)            
        return items