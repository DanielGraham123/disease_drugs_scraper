from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Disease, Drug

admin.site.site_header = 'DCD Catalog'


class DiseaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'symptoms', 'causes', 'risks', 'preventions', 'link')
    list_filter = ('name', 'risks')

class DrugInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'generic_name', 'other_name', 'uses', 'precautions', 'interactions', 'storage', 'link')
    list_filter = ('name', 'generic_name', 'uses')

admin.site.register(Disease, DiseaseInfoAdmin)
admin.site.register(Drug, DrugInfoAdmin)
admin.site.unregister(Group)