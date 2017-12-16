# -*- coding: utf-8 -*-
import scrapy


class ScrollSpider(scrapy.Spider):
    name = 'scroll'
    # allowed_domains = ['toscrape.com/scroll']
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        import json
        data = json.loads(response.text)
        page = data["page"]
        for quote in data["quotes"]:
            yield{
                "author_name": quote["author"]["name"],
                "text": quote['text'],
                "tags": quote["tags"]
            }
        if data['has_next']:
            next_page = page + 1
            next_page_url = self.api_url.format(next_page)
            yield scrapy.Request(url = next_page_url, callback= self.parse)

