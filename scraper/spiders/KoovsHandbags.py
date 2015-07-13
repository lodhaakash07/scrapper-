from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scraper.items import DmozItem
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class KoovsHandbags(Spider):
    name = "koovs_handbags"
    allowed_domains = ["koovs.com"]
    start_urls = [
        "http://www.koovs.com/women/bags_purses-652/style-handbags"
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        n = 0
        m=[]
        elem = self.driver.find_element_by_tag_name("body")
        while 1==1:
            for i in range(1,5):
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            try:
                self.driver.find_element_by_css_selector('div#bodyContent div#searchResults table tbody tr td.productResults div#pageResults div.itemLisitng div#show_more_product_div.showMoreBar').click()
            except:
                elem.send_keys(Keys.PAGE_DOWN)
            m.append(len(self.driver.page_source))
            if n!=0 and m[-1]==m[-2] and m.count(m[-1]) > 2:
                break
            n = n+1
        hxs = Selector(response)
        selen_html = self.driver.page_source
        hxs  = Selector(text=selen_html)
        sites = hxs.css('div.prodBox')
        items = []
        self.driver.quit()
        for site in sites:
            item = DmozItem()
            item['desc'] = site.css('div.prodDescp a.product_url::text').extract()
            item['brand'] = "koovs"
            item['price'] = site.css('span.prodPrice::text').extract()
            item['imglink'] = site.css('a.product_url img.productImage').xpath('@src').extract()
            item['prodlink'] = site.css('a.product_url').xpath('@href').extract()
            items.append(item)            
        return items