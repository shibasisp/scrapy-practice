# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log("I just visited " + response.url)
        # quote =  response.css("div.quote")
        # for i in quote:
        #     item = {
        #         "name": i.css("small.author::text").extract(),
        #         "tags": i.css("a.tag::text").extract(),
        #         "quotes": i.css("span.text::text").extract()
        #     }
        #     yield item
        urls = response.css("div.quote > span > a::attr(href)").extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url = url, callback = self.parse_author)

        next_page_url = response.css("ul.pager>li.next>a::attr(href)").extract_first()
        if next_page_url:    
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url= next_page_url, callback = self.parse)

    def parse_author(self,response):
        yield {
            "name": response.css("h3.author-title::text").extract(),
            "birth_date" :response.css("span.author-born-date::text").extract()
        } 
