# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from diseaseInfo.models import Drug

def clean_description(desc):
    return desc.strip()

def clean_list(elements):
    string = ''
    for element in elements:
        string += element + ', '

    return string.strip()


# class DiseasesPipeline:
#     def process_item(self, item, spider):
#         if isinstance(item, Disease):
#             name = item['name'] 
#             description = clean_description(item['description'])
#             causes = clean_list(item['causes'])
#             symptoms = clean_list(item['symptoms'])
#             preventions = clean_list(item['preventions'])
#             risks = clean_list(item['risks'])
#             complications = clean_list(item['complications'])
#             link = item['link']
            
#             Disease.objects.create(
#                 name = name,
#                 description = description,
#                 symptoms = symptoms,
#                 causes = causes,
#                 complications = complications,
#                 risks = risks,
#                 preventions = preventions,
#                 link = link
#             )
#         item.save()

#         return item

class DrugsPipeline:
    def process_item(self, item, spider):
        if isinstance(item, Drug):
            name = item['name'] 
            generic_name = item['generic_name']           
            # other_name = item['other_name']
            uses = clean_list(item['uses'])
            side_effects = clean_list(item['side_effects'])
            precautions = clean_list(item['precautions'])
            interactions = clean_list(item['interactions']) 
            overdose = clean_list(item['overdose'])
            link = item['link']

            Drug.objects.create(
                name = name,
                generic_name = generic_name,
                # other_name = other_name,
                uses = uses,
                side_effects = side_effects,
                precautions = precautions,
                interactions = interactions,
                overdose = overdose,
                link = link
            )
        print("***ITEM TO SAVE: ",item, " ******")
        item.save()

        return item

