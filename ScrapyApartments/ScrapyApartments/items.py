# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TayaraItem(scrapy.Item):
    _id= scrapy.Field()
    gouvernorat= scrapy.Field()
    delegation= scrapy.Field()
    superficie= scrapy.Field()
    salle_de_bains= scrapy.Field()
    chambres= scrapy.Field()
    prix= scrapy.Field()
    description= scrapy.Field()

class MubawabItem(scrapy.Item):
    _id= scrapy.Field()
    gouvernorat= scrapy.Field()
    delegation= scrapy.Field()
    superficie= scrapy.Field()
    salle_de_bains= scrapy.Field()
    chambres= scrapy.Field()
    nb_pieces= scrapy.Field()
    prix= scrapy.Field()
    etat= scrapy.Field()
    etage= scrapy.Field()
    standing= scrapy.Field()
    description= scrapy.Field()

