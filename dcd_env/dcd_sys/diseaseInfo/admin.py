from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Disease

admin.site.site_header = 'DCD Catalog'


class DiseaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'symptoms', 'causes', 'preventions', 'link')
    list_filter = ('name', 'symptoms')

admin.site.register(Disease, DiseaseInfoAdmin)
admin.site.unregister(Group)