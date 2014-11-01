import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from crawler.items import GenericItem

class GenericSpider(CrawlSpider):
   name = "generic"
   #allowed_domains = [""] # Use this to filter domains
   start_urls = [
       "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
       "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
   ]
   rules = (
      Rule(LinkExtractor(allow=('.*', )), callback='parse_item'),
   )

   def parse_item(self, response):
      item = GenericItem()
      item['url'] = response.url
      item['title'] = response.xpath('/html/head/title/text()').extract()
      item['h'] = response.xpath('//h1/text()').extract()
      item['h'].extend(response.xpath('//h2/text()').extract())
      item['h'].extend(response.xpath('//h3/text()').extract())
      item['p'] = response.xpath('//p/text()').extract()
      return item
