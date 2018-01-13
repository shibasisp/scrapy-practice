# -*- coding: utf-8 -*-
import scrapy
from flipkart.items import FlipkartItem


class FlipkartProductListSpider(scrapy.Spider):
    name = 'flipkart_product_list'
    allowed_domains = ['https://www.flipkart.com/q/wrangler-trouser/']
    start_urls = ['https://www.flipkart.com/q/wrangler-trouser/']

    def parse(self, response):
        products = response.xpath('//div[@class="_3liAhj"]/a[@class="Zhf2z-"]/@href').extract()
        for product in products:
            url = response.urljoin(product)
            yield scrapy.Request(url, callback=self.parse_product)
    
    def parse_product(self, response):
        print("HI")
        # items = FlipkartItem()
        # items['product_name'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_2UDlNd"]/div/h1[@class="_3eAQiD"]/text()').extract()
        # items['product_selling_price'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="_1vC4OE _37U4_g"]/text()').extract()
        # items['product_MRP'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="_3auQ3N _16fZeb"]/text()').extract()
        # items['product_discount'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="VGWI6T _3GXWnA"]/text()').extract()
        # items['product_features'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_2KVF1P"]/div[@class="g2dDAR flex"]/div[@class="_3WHvuP"]/ul/li[@class="_2-riNZ"]/text()').extract()
        # items['product_rating'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="col _39LH-M"]/div[@class="row _1Ahy2t _2aFisS"]/div[@class="ebepc-"]/div[@class="row"]/div[@class="col-4-12"]/div[@class="col"]/div[@class="row"]/div[@class="col-12-12 _11EBw0"]/div[@class="_1i0wk8"]/text()').extract_first()
        # items['product_warranty'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_2sVT0Y"]/div[@class="_3h7IGd"]/text()').extract()
        # items['product_image'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_3S6yHr"]/div[@class="_26KFgP"]/div[@class="_2wEmBu"]/div[@class="_1hMRnR"]/div[@class="_2SIJjY"]/img/@src').extract_first()
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