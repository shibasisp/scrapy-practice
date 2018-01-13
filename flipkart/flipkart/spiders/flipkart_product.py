# -*- coding: utf-8 -*-
import scrapy
from flipkart.items import FlipkartItem


class FlipkartProductSpider(scrapy.Spider):
    name = 'flipkart_product'
    allowed_domains = ['https://www.flipkart.com/']
    start_urls = ['https://www.flipkart.com/moto-g5-plus-fine-gold-32-gb/p/itmes2zjvwfncxxr?pid=MOBEQHMGED7F9CZ2&srno=b_1_1&otracker=hp_omu_Top%20Selling%20Mobiles_5_4%20GB%20RAM%20%7C%2032%20GB%20ROM_75XUIC4Q6F_4&lid=LSTMOBEQHMGED7F9CZ2KTTROW&fm=neo/merchandising&iid=5deff33d-de63-4ac5-a2f2-df6a0ad96b87.MOBEQHMGED7F9CZ2.SEARCH&ppt=Store%20Browse&ppn=Search%20Page&ssid=4c6j5jbxeo0000001513961813566',
                  'https://www.flipkart.com/puma-kor-sneakers/p/itmez9myujjey2fb?pid=SHOEZ9MYPFNRFTP7&srno=b_1_6&otracker=nmenu_sub_Men_0_Casual%20Shoes&lid=LSTSHOEZ9MYPFNRFTP7YSGFBZ&fm=neo/merchandising&iid=3ee01f66-7daa-4ce0-bc4c-b0ac35acb410.SHOEZ9MYPFNRFTP7.SEARCH&ppt=Store%20Browse&ppn=Search%20Page&ssid=4c6j5jbxeo0000001513961813566']

    def parse(self, response):
        items = FlipkartItem()
        items['product_name'] = response.xpath('//div[contains(@class,"_33MqSN")]/div[contains(@class, "_2Cl4hZ")]/div[contains(@class,"_1MVZfW")]/div[contains(@class,"_2UDlNd")]/div/h1[contains(@class,"_3eAQiD")]/text()').extract()
        items['product_selling_price'] = response.xpath('//div[contains(@class,"_33MqSN")]/div[contains(@class,"_2Cl4hZ")]/div[contains(@class,"_1MVZfW")]/div[contains(@class,"_3ZYEWO")]/div[contains(@class,"_2MUtYG")]/div[contains(@class,"_1uv9Cb")]/div[contains(@class,"_1vC4OE _37U4_g")]/text()').extract()
        items['product_MRP'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="_3auQ3N _16fZeb"]/text()').extract()
        items['product_discount'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_1MVZfW"]/div[@class="_3ZYEWO"]/div[@class="_2MUtYG"]/div[@class="_1uv9Cb"]/div[@class="VGWI6T _3GXWnA"]/text()').extract()
        items['product_features'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_2KVF1P"]/div[@class="g2dDAR flex"]/div[@class="_3WHvuP"]/ul/li[@class="_2-riNZ"]/text()').extract()
        items['product_rating'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="col _39LH-M"]/div[@class="row _1Ahy2t _2aFisS"]/div[@class="ebepc-"]/div[@class="row"]/div[@class="col-4-12"]/div[@class="col"]/div[@class="row"]/div[@class="col-12-12 _11EBw0"]/div[@class="_1i0wk8"]/text()').extract_first()
        items['product_warranty'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_2Cl4hZ"]/div[@class="_2sVT0Y"]/div[@class="_3h7IGd"]/text()').extract()
        items['product_image'] = response.xpath('//div[@class="_33MqSN"]/div[@class="_3S6yHr"]/div[@class="_26KFgP"]/div[@class="_2wEmBu"]/div[@class="_1hMRnR"]/div[@class="_2SIJjY"]/img/@src').extract_first()
        yield items
