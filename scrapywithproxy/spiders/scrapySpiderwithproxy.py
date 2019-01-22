import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'craigs'
    allowed_domains = ['sfbay.craigslist.org']
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    rules =(

        Rule(LinkExtractor(allow=(), restrict_css='a.button.next'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        if '/' in response.url:
            yield scrapy.Request(url=response.url, dont_filter=True, callback=self.parse_item_in)

    def parse_item_in(self,response):
        print(response.url)
        print(response.headers)





