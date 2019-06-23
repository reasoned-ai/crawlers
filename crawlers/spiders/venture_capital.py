# -*- coding: utf-8 -*-
import scrapy


class VentureCapital(scrapy.Spider):
    name = 'venture_capital'
    start_url = 'https://golden.com/list-of-venture-capital-firms/'

    def start_requests(self):
        for i in range(1, 18):
            yield scrapy.Request(url=self.start_url + str(i), callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//div[@class="table-row__wrapper table-row__wrapper--highlight"]'):
            cells = row.xpath('./div/div[@class="table-cell-inner"]')
            yield {'firm': cells[0].xpath('./span/a/text()').extract_first(),
                   'description': cells[1].xpath('./div/text()').extract_first(),
                   'people_link': cells[2].xpath('./div/div/span/a/@href').extract_first(),
                   'people_name': cells[2].xpath('./div/div/span/a/text()').extract_first(),
                   'founded_at': cells[3].xpath('./div/div/text()').extract_first(),
                   'blog': cells[4].xpath('./div/span/a/@href').extract_first(),
                   'url': cells[5].xpath('./div/span/a/@href').extract_first(),
                   'twitter': cells[6].xpath('./div/span/a/@href').extract_first(),
                   'location': cells[7].xpath('./div/div/span/a/text()').extract_first()}

