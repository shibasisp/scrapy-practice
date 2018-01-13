import scrapy
from urllib.parse import urljoin

class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        'https://www.phidgets.com/?tier=1&catid=64&pcid=57',
    ]

    def parse(self, response):
        products = response.xpath("//*[contains(@class, 'ph-summary-entry-ctn')]/a/@href").extract()
        for p in products:
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_product)

    def parse_product(self, response):
        for info in response.css('div.ph-product-container'):
            yield {
                'product_name': info.css('h2.ph-product-name::text').extract_first(),
                'product_image': info.css('div.ph-product-img-ctn a').xpath('@href').extract(),
                'sku': info.css('span.ph-pid').xpath('@prod-sku').extract_first(),
                'short_description': info.css('div.ph-product-summary::text').extract_first(),
                'price': info.css('h2.ph-product-price > span.price::text').extract_first(),
                'long_description': info.css('div#product_tab_1').extract_first(),
                'specs': info.css('div#product_tab_2').extract_first(),
            }
