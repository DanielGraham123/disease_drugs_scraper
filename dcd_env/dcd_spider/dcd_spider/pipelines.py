# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from diseaseInfo.models import Disease

def clean_description(desc):
    return "" if desc != None else desc.strip()

def clean_symptoms(symptoms):
    string = ''
    for symptom in symptoms:
        string += symptom + ', '

    return string.strip()

def clean_causes(causes):
    string = ''
    for cause in causes:
        string += cause + ', '

    return string.strip()

def clean_complications(complications):
    string = ''
    for complication in complications:  
        string += complication + ', '

    return string.strip()

def clean_preventions(preventions):
    string = ''
    for prevention in preventions:
        string += prevention + ', '
    
    return string.strip()

def clean_risks(risks):
    string = ''
    for risk in risks:
        string += risk + ', '
    
    return string.strip()

class DcdSpiderPipeline:
    def process_item(self, item, spider):
        name = item['name'] 
        description = clean_description(item['description'])
        causes = clean_causes(item['causes'])
        symptoms = clean_symptoms(item['symptoms'])
        preventions = clean_preventions(item['preventions'])
        risks = clean_risks(item['risks'])
        complications = clean_complications(item['complications'])
        link = item['link']

        Disease.objects.create(
            name = name,
            description = description,
            symptoms = symptoms,
            causes = causes,
            complications = complications,
            risks = risks,
            preventions = preventions,
            link = link
        )

        item.save()
        return item

