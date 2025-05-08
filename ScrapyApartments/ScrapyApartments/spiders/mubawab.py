from ScrapyApartments.items import MubawabItem
import scrapy
import re

class MubawatSpider(scrapy.Spider):
    name = 'mubawab'
    allowed_domains = ['mubawab.tn']
    list_of_gouvernorats = ['scrp/tunis/tunis-et-banlieue-nord', 'scrp/ariana/ariana', 'scrp/ben-arous/ben-arous', 'st/la-manouba']
    actual_gouvernorats = ['tunis', 'ariana', 'ben-arous', 'la-manouba']
    base_url = 'https://www.mubawab.tn/fr/{}/appartements-a-vendre:p:{}'

    def start_requests(self):
        for index, gouvernorat in enumerate(self.list_of_gouvernorats):  
            for page in range(1, 51):  # Request pages from 1 to 51
                url = self.base_url.format(gouvernorat, page)
                # Pass gouvernorat as a meta field to avoid scoping issues
                yield scrapy.Request(url=url, callback=self.parse, meta={'gouvernorat': self.actual_gouvernorats[index]})

    def parse(self, response):
        gouvernorat = response.meta['gouvernorat']  # Retrieve the gouvernorat passed in meta
        apartment_links = response.css('ul.ulListing li.listingBox.w100 a::attr(href)').getall()
        for link in apartment_links:
            # Pass gouvernorat to the next request via meta
            yield scrapy.Request(url=link, callback=self.parse_item, meta={'gouvernorat': gouvernorat})

        # Handle pagination (next page)
        next_page = response.css('a.paginationNext::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, meta={'gouvernorat': gouvernorat})

    def parse_item(self, response):
        item = MubawabItem()

        item['gouvernorat'] = response.meta['gouvernorat']

        value = response.css('h3.greyTit::text').get()
        item['delegation'] = ' '.join(value.split()) if value else None

        value = response.css('h3.orangeTit::text').get()
        item['prix'] = ''.join(re.findall(r'\d+', value)) if value else None

        value = response.css('div.disFlex.adDetails div:nth-of-type(1) span::text').get()
        item['superficie'] = re.search(r'\d+', value).group() if value else None

        value = response.css('div.disFlex.adDetails div:nth-of-type(2) span::text').get()
        item['nb_pieces'] = re.search(r'\d+', value).group() if value else None

        value = response.css('div.disFlex.adDetails div:nth-of-type(3) span::text').get()
        item['chambres'] = re.search(r'\d+', value).group() if value else None

        value = response.css('div.disFlex.adDetails div:nth-of-type(4) span::text').get()
        item['salle_de_bains'] = re.search(r'\d+', value).group() if value else None

        item['etat'] = None
        item['etage'] = None
        item['standing'] = None

        # Extract labeled features dynamically
        ad_features = response.css('div.adMainFeature.col-4')
        for feature in ad_features:
            label = feature.css('p.adMainFeatureContentLabel::text').get()
            value = feature.css('p.adMainFeatureContentValue::text').get()

            if label and value:
                label = label.strip().lower()
                if "etat" in label:  
                    item['etat'] = value.strip()
                elif "étage du bien" in label:
                    item['etage'] = value.strip()
                elif "standing" in label:
                    item['standing'] = value.strip()

        description = response.css('div.blockProp p::text').getall()
        item['description'] = ' '.join(description).strip() if description else None

        yield item
