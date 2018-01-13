from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    name = 'sitemaps'
    sitemap_urls = ['http://www.flipkart.com/sitemap_o_index.xml',
                    'http://www.flipkart.com/sitemap_q_index.xml',
                    'http://www.flipkart.com/sitemap_d_index.xml']
    # sitemap_rules = ['/q/','parse_sitemap_url']
    def parse(self, response):
        yield {
            'title': response.css("title ::text").extract_first(),
            'url': response.url
        }

    def parse_sitemap_url(self, response):
        yield {
            'title': response.css("title ::text").extract_first(),
            'url': response.url
        }