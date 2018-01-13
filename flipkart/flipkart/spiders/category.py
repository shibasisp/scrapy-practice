# -*- coding: utf-8 -*-
import scrapy
from flipkart.items import FlipkartItem


class CategorySpider(scrapy.Spider):
    def __init__(self, filename=None):
        if filename:
            import json
            datas = json.load(open('sitemaps.json'))
            for data in datas:
                self.start_urls.append(data['url'])
    name = 'category'
    # allowed_domains = ['https://www.flipkart.com/motorola-mobile-phones-store/']
    start_urls = ['https://www.flipkart.com/q/htc-mobiles']

    def parse(self, response):
        products = response.xpath('//a[contains(@class,"_2cLu-l") or contains(@class,"_1UoZlX")]/@href').extract()
        for product in products:
            yield response.follow(product, callback=self.parse_product)

        next_page_url = response.xpath('//div[contains(@class,"_2kUstJ")]/a/@href').extract_first()
        if next_page_url:
            yield response.follow(url= next_page_url, callback = self.parse)

    
    def parse_product(self, response):
        # items = FlipkartItem()
        # items['product_name'] = response.xpath('//div/h1[contains(@class,"_3eAQiD")]/text()').extract()
        # items['product_selling_price'] = response.xpath('//div[contains(@class,"_1vC4OE _37U4_g")]/text()').extract()
        # items['product_MRP'] = response.xpath('//div[contains(@class,"_3auQ3N _16fZeb")]/text()').extract()
        # items['product_discount'] = response.xpath('//div[contains(@class,"VGWI6T _3GXWnA")]/text()').extract()
        # items['product_features'] = response.xpath('//div[contains(@class,"_3WHvuP")]/ul/li[contains(@class, "_2-riNZ")]/text()').extract()
        # items['product_rating'] = response.xpath('//div[contains(@class,"_1i0wk8")]/text()').extract_first()
        # items['product_warranty'] = response.xpath('//div[contains(@class,"_3h7IGd")]/text()').extract()
        # items['product_image'] = response.xpath('//div[contains(@class,"_2SIJjY")]/img/@src').extract_first()
        # yield items
        for sel in response.xpath('//div[@class="_33MqSN"]'):
            items = FlipkartItem()
            items['product_name']          = sel.xpath('div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_2UDlNd"]/div/h1[@class="_3eAQiD"]/text()').extract()
            items['product_selling_price'] = sel.xpath('div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="_1vC4OE _37U4_g"]/text()').extract()
            items['product_MRP']           = sel.xpath('div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="_3auQ3N _16fZeb"]/text()').extract()
            items['product_discount']      = sel.xpath('div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="VGWI6T _3GXWnA"]/text()').extract()
            items['product_features']      = sel.xpath('div[@class="_2Cl4hZ"]/div[@class="_2KVF1P"]/div[@class="g2dDAR flex"]/div[@class="_3WHvuP"]/ul/li[@class="_2-riNZ"]/text()').extract()
            items['product_rating']        = sel.xpath('div[@class="_2Cl4hZ"]/div[@class="col _39LH-M"]/div[@class="row _1Ahy2t _2aFisS"]/div[@class="ebepc-"]/div[@class="row"]/div[@class="col-4-12"]/div[@class="col"]/div[@class="row"]/div[@class="col-12-12 _11EBw0"]/div[@class="_1i0wk8"]/text()').extract_first()
            items['product_warranty']      = sel.xpath('div[@class="_2Cl4hZ"]/div[@class="_2sVT0Y"]/div[@class="_3h7IGd"]/text()').extract()
            items['product_image']         = sel.xpath('div[@class="_3S6yHr"]/div[@class="_26KFgP"]/div[@class="_2wEmBu"]/div[@class="_1hMRnR"]/div[@class="_2SIJjY"]/img/@src').extract_first()
            yield items