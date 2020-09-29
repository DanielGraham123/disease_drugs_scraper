# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from diseaseInfo.models import Disease

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
