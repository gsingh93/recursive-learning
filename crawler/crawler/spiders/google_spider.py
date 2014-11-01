from scrapy.spider import Spider
from scrapy.selector import Selector

from crawler.items import GoogleItem

class GoogleSpider(Spider):
   name = "google"
   allowed_domains = ["google.com"]
   start_urls = [
       "https://www.google.com/?#q=computer+science"
   ]

   def parse(self, response):
       sel = Selector(response)
       sites = sel.xpath('//ul/li')
       items = []
       for site in sites:
           item = GoogleItem()
           item['title'] = site.xpath('a/text()').extract()
           item['link'] = site.xpath('a/@href').extract()
           item['desc'] = site.xpath('text()').extract()
           items.append(item)
       return items
