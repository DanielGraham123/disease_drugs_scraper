from django.contrib import admin
from django.contrib.auth.models import Group

from diseaseInfo.models import Disease, Drug

admin.site.site_header = 'DCD Catalog'


class DiseaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'symptoms', 'causes', 'risks', 'preventions', 'link')
    list_filter = ('name', 'risks')
    search_fields = ('name', 'symptoms')

class DrugInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'generic_name', 'uses', 'precautions', 'interactions', 'overdose', 'link')
    list_filter = ('name', 'generic_name')
    search_fields = ('name', 'generic_name', 'uses', 'interactions')

admin.site.register(Disease, DiseaseInfoAdmin)
admin.site.register(Drug, DrugInfoAdmin)
admin.site.unregister(Group)