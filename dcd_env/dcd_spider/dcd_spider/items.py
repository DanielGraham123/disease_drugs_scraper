# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from diseaseInfo.models import Disease, Drug

class DcdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DiseaseItem(DjangoItem):
    django_model = Disease
    name = scrapy.Field()
    description = scrapy.Field()
    symptoms = scrapy.Field()
    causes = scrapy.Field()
    complications = scrapy.Field()
    risks = scrapy.Field()
    preventions = scrapy.Field()
    link = scrapy.Field()

class DrugItem(DjangoItem):
    django_model = Drug
    name = scrapy.Field()
    generic_name = scrapy.Field()
    other_name = scrapy.Field()
    uses = scrapy.Field()
    side_effects = scrapy.Field()
    precautions = scrapy.Field()
    interactions = scrapy.Field()
    storage = scrapy.Field()
    link = scrapy.Field()
