from scrapy.spiders import SitemapSpider

class SiteSpider(SitemapSpider):

    name = 'SiteSpider'

    sitemap_urls = ['https://www.gov.br/pt-br/sitemap.xml']
    sitemap_rules = [('noticias', 'parse_noticia')]

    def parse_noticia(self, response):
        print('parse_noticia url:', response.url)
        filename = response.url.split("/arquivos")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        yield {'url': response.url}

# --- salvar csv ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',

    # salva arquivo coo CSV, JSON ou XML
    'FEED_FORMAT': 'csv',     # csv, json, xml
    'FEED_URI': 'lista.csv', # 
})
c.crawl(SiteSpider)
c.start()