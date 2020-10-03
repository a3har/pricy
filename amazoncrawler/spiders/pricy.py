import scrapy
from ..items import PricyItem

class PricySpider(scrapy.Spider):
    name = 'pricy'
    start_urls = ['https://www.amazon.in/dp/B07JD7QH4Q/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07JD7QH4Q&pd_rd_w=07gNl&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=1DMpV&pf_rd_r=KHWKJ0K9KQDJ1N405NV5&pd_rd_r=13e4e3a6-c6ac-49c8-bad6-daa77811302b&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTUFOWjZRREdTN1REJmVuY3J5cHRlZElkPUEwODg4MjI5MkJQNkJVTVI0MjM5QSZlbmNyeXB0ZWRBZElkPUEwODcwMTg2MklDUFMyTEI3Nlk4NSZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=']

    def parse(self, response):
        item = PricyItem()
        item['title'] = response.css('#productTitle').css('::text').extract_first().replace('\n','')
        p = response.css('#priceblock_ourprice')
        if(not p):
            p = response.css('#priceblock_dealprice')
        item['price'] = float(p.css('::text').extract_first().replace(',', '').replace('₹\xa0',''))
        yield item
