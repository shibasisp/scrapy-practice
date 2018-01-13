from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    name = 'sitemaps'
    sitemap_urls = ['https://www.flipkart.com/robots.txt']
    rules = [ 
      ("/sitemap*", "parse_sitemap_url"), 
   ]
    sitemap_rules = ['/q/','parse_q']
    def parse(self, response):
        pass

    def parse_sitemap_url(self, response):
        yield {
            'title': response.css("title ::text").extract_first(),
            'url': response.url
        }
    def parse_q(self, response):
        pass