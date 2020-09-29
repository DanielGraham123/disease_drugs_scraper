from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from dcd_spider.dcd_spider import settings as my_settings

from scrapy.utils.project import get_project_settings
from dcd_spider.dcd_spider.spiders.spiderscript import DiseaseSpider


class Command(BaseCommand):
    help = 'Release the spiders'

    def handle(self, *args, **options):
        # crawler_settings = Settings()
        # crawler_settings.setmodule(my_settings)

        # process = CrawlerProcess(settings=crawler_settings)
        process = CrawlerProcess(get_project_settings())

        process.crawl(DiseaseSpider)
        process.start()