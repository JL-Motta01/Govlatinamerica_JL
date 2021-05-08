from scrapy.spiders import CrawlSpider
from scrapy import Request
from urllib.parse import urljoin

class MySpider(CrawlSpider):
    name = 'myspider'
    start_urls = ['https://www.gov.br']

    def parse(self, response):
        # This method is called for every successfully crawled page

        # get all pagination links using xpath
        for link in response.xpath('.//a/@href').getall():
            # build the absolute url 
            url = urljoin('https://www.gov.br', link)
            print(url)
            yield Request(url=url, callback=self.parse)  # <-- This makes your spider recursiv crawl subsequent pagespip