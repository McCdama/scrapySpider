import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapySpider.items import ScrapyspiderItem


class HindawiSpider(CrawlSpider):
    name = 'hindawi'
    allowed_domains = ['www.hindawi.org']
    start_urls = ['https://www.hindawi.org/books/categories/religions/']

    rules = (
        Rule(LinkExtractor(allow=r'/books/categories/religions/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for title in response.css('.bookCover'):
            file_url = response.urljoin(title.css('a').attrib['href'])
            file_url = file_url[:-1]  
            file_url = file_url + '.pdf'
            item = ScrapyspiderItem()
            item['file_urls'] = [file_url]
            yield item