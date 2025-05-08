from ScrapyApartments.items import TayaraItem
import scrapy

class TayaraSpider(scrapy.Spider):
    name = 'tayara'
    allowed_domains = ['tayara.tn']
    list_of_gouvernorats = ['Tunis', 'Ariana', 'Ben Arous', 'La Manouba']
    base_url = 'https://www.tayara.tn/ads/c/Immobilier/Appartements/l/{}/k/vendre/?page={}'
    
    def start_requests(self):
        for gouvernorat in self.list_of_gouvernorats:
            # request pages from 1 to 30
            for page in range(1, 30): 
                url = self.base_url.format(gouvernorat,page)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # all links in a single page
        all_links = response.css('article a::attr(href)').getall()

        for link in all_links:
            yield response.follow(link, self.parse_item)

        # next pages
        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_item(self, response):
        item = TayaraItem()

        item['gouvernorat'] = response.css('li.p-2.my-1.text-xs.text-gray-600 span::text')[1].get()
        item['delegation'] = response.css('li.p-2.my-1.text-xs.text-gray-600 span::text')[2].get()
        item['superficie'] = response.css('li:nth-child(2) span.font-semibold::text').get()
        item['salle_de_bains'] = response.css('li:nth-child(3) span.font-semibold::text').get()
        item['chambres'] = response.css('li:nth-child(4) span.font-semibold::text').get()
        item['prix'] = response.css('div.mt-4 > data::attr(value)').get()
        item['description'] = response.css('p.text-sm.text-start.text-gray-700.font-arabic.whitespace-pre-line.line-clamp-3 span::text').get()

        yield item
