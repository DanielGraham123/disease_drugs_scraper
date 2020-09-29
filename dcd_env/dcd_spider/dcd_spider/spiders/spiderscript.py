# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:48:44 2020
@author: daniel
"""

import scrapy
import logging
import json
# from tqdm import tqdm

from collections import OrderedDict
from scrapy.crawler import CrawlerProcess
from dcd_spider.items import DiseaseItem, DrugItem

# OUTPUT_FILE1 = 'mayo-diseases.json'
# OUTPUT_FILE2 = 'webmd-drugs.json'

diseases = []
drugs = []


class DiseaseSpider(scrapy.Spider):
    name = "dcd"
    
    allowed_domains = ['www.mayoclinic.org']
    start_urls = ['https://www.mayoclinic.org/diseases-conditions/']
    

    def __init__(self):
        self.diseases = []
        self.keys = []
    
    def parse(self, response):
        atoz_links = response.css('ol.acces-alpha a::attr(href)').getall()
        
       
        # with tqdm(total=len(atoz_links)) as progress:
        for link in atoz_links:
            key = link.split('/')[-1][-1]
            # progress.set_description("Processing {}".format(str(key)))
            # progress.update(1)
            
            letter_page = response.urljoin(link)
            print(str(letter_page))
            
            yield scrapy.Request(letter_page, callback=self.parse_letter)
             
    def parse_letter(self, response):
        diseases_links = response.css('div.content-within li a::attr(href)')
        for link in diseases_links:
            yield response.follow(link, self.parse_disease)
    
    def parse_disease(self, response):   
        item = DiseaseItem()     
        item['name'] = response.css('header h1 a::text').get(default='').strip()
                        
        item['description'] =  response.css('div.content').xpath('.//div[h2/text() = "Overview"]/p[1]/text()').get()
        
        item['symptoms'] = response.css('div.content').xpath('.//div[h2/text() = "Symptoms"]/ul[1]/li/text()').getall()
        
        item['causes'] =  response.css('div.content').xpath('.//h2[text() = "Causes"]/following-sibling::ul[1]/li/strong/text()').getall()
        
        item['risks'] = response.css('div.content').xpath('.//h2[text() = "Risk factors"]/following-sibling::ul[1]/li/strong/text()').getall()
        
        item['complications'] = response.css('div.content').xpath('.//h2[text() = "Complications"]/following-sibling::ul[1]/li/text()').getall()
        
        item['preventions'] = response.css('div.content').xpath('.//h2[text() = "Prevention"]/following-sibling::ul[1]/li/strong/text()').getall()
        
        item['link'] = response.url
        # diseases.append(
        #     OrderedDict([
                
        #         ('name', name),
        #         ('description', description),
        #         ('symptoms', symptoms),
        #         ('causes', causes),
        #         ('risks', risks),
        #         ('complications', complications),
        #         ('preventions', preventions),
        #         ('link', response.url),
        #         ])
        #     )
        
        # yield from diseases
        return item
        
       

class DrugsSpider(scrapy.Spider):
    name = 'drugs'
    
    allowed_domains = ['www.webmd.com']
    start_urls = ['https://www.webmd.com/drugs/2/index']
       
    def __init__(self):
        self.drugs = []
        self.keys = []
        
    def parse(self, response):
        atoz_links = response.css('div.drugs-browse-box ul li a::attr(href)').getall()
        
        # with tqdm(total=len(atoz_links)) as progress:
        for link in atoz_links:
            key = link.split('/')[-2]
            # progress.set_description("Processing {}".format(str(key)))
            # progress.update(1)
            
            letter_page = response.urljoin(link)
            print(str(letter_page))
            
            yield scrapy.Request(letter_page, callback=self.parse_letter)
             
    def parse_letter(self, response):
        drugs_links =  response.css('div.drug-list-container ul li a::attr(href)').getall()   
        for link in drugs_links:
            yield response.follow(link, self.parse_drug)
    
    def parse_drug(self, response):  
        item = DrugItem()
        item['name'] = response.css('div.drug-names h1::text').get()   
        item['generic_name'] = response.css('div.drug-names').xpath('.//p[1]/text()').get().split(':')[1].strip()
        item['other_name'] = response.css('div.drug-names').xpath('.//p[2]/text()').get().split(':')[1].strip()
        
        item['uses'] = self.convertToText(response.css('div.tab-content').xpath('.//div[h2/text() = "Uses"]/p'))
        
        item['side_effects'] = self.listify(
                            self.convertToText(response.css('div.tab-content').xpath('.//div[h2/text() = "Side Effects"]/p'))
                            )
         
        item['precautions'] = self.listify(
                            self.convertToText(response.css('div.tab-content').xpath('.//div[h2/text() = "Precautions"]/p'))
                            )
        
        item['interactions'] = self.listify(
                            self.convertToText(response.css('div.tab-content').xpath('.//div[h2/text() = "Interactions"]/p'))
                            )
        
        item['storage'] = self.listify(
                            self.convertToText(response.css('div#tab-5 div.inner-content').xpath('.//h3[text() = "Storage"]/following-sibling::p'))
                            )
        item['link'] = response.url
        
        # drugs.append(
        #     OrderedDict([
        #         ('name', name),
        #         ('generic_name', generic_name),
        #         ('other_name', other_name),
        #         ('uses', uses),
        #         ('side_effects', side_effects),
        #         ('precautions', precautions),
        #         ('interactions', interactions),
        #         ('storage', storage),
        #         ('link', response.url)
        #         ])
        #     )
        
        # yield from drugs    
        
    def convertToText(self, response):
        chunks = response.xpath('.//text()').getall()

        text = ''
        
        if chunks[0] == "See also Warning section.":
            del chunks[0]
        
        for chunk in chunks:
            text += chunk
            
        return text
    
    def listify(self, text):
        strings = text.split('.')
        
        effects = []
        
        for st in strings:
            effects.append(st.strip() + '.')
            
        return effects

            
# process = CrawlerProcess()
# process.crawl(DiseaseSpider)
# process.crawl(DrugsSpider)

# process.start()

# with open(OUTPUT_FILE1, 'wt') as out:
#     json.dump(diseases, out, indent=4)

# with open(OUTPUT_FILE2, 'wt') as out:
#     json.dump(drugs, out, indent=4)