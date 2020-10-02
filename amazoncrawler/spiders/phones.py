import scrapy
from ..items import AmazoncrawlerItem


class PhonesSpider(scrapy.Spider):
    name = 'phones'
    start_urls = ['https://www.amazon.in/Smartphones-%E2%82%B95-000-%E2%82%B910-Prime-Eligible/s?rh=n%3A1805560031%2Cp_36%3A1318505031%2Cp_85%3A10440599031&hidden-keywords=smartphone']

    def parse(self, response):

        item = AmazoncrawlerItem()
        all_divs = response.css(
            '.s-include-content-margin.s-border-bottom.s-latency-cf-section')

        for div in all_divs:
            title = div.css(
                '.a-color-base.a-text-normal').css('::text').extract_first()
            try:
                price = div.css(
                    '.a-price-whole::text').extract_first().replace(',', '')
            except:
                price = 'NA'

            try:
                reviews_count = div.css(
                    '.a-size-small .a-size-base').css('::text').extract_first().replace(',', '')
            except:
                reviews_count = 'NA'

            try:
                stars = div.css(
                    '.aok-align-bottom').css('::text').extract_first().split(' ')[0]
            except:
                stars = 'NA'

            link = div.css(
                '.a-link-normal.s-no-outline').css('::attr(href)').get()

            item['title'] = title
            item['price'] = price
            item['reviews_count'] = reviews_count
            item['stars'] = stars
            item['link'] = response.urljoin(link)

            yield item

        next_page = response.css('.a-last a').css('::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
