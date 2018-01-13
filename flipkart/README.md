# Flipkart Crawler

The crawler will crawl almost all the product page of [Flipkart](www.flipkart.com) and gather all the important informations in a CSV/JSON file.

### Dependencies

```
Python > 3
Scrapy 1.4.0 (tested)

```

## Running the crawler

1. ```bash
   cd flipkart/spiders/
   ```

2. Gather all the links of sitemap.xml in a file(say  `sitemaps.json`)

   ```bash
   scrapy runspider sitemaps.py -o sitemaps.json
   ```

3. Crawl all the links of `sitemaps.json`  and store it in another file ( say, `data.json`).

   ```bash
   scrapy runspider category.py -o data.json -a filename=sitemaps.json
   ```

   ​