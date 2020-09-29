from django.shortcuts import render
from django.conf import settings
import os
import json
from .models import Disease, Drug

# Create your views here.
def home(request):
    diseases_fil = Disease.objects.all().order_by('id')[:12]
    drugs_fil = Drug.objects.all().order_by('id')[:12]

    diseases = Disease.objects.all().values()
    drugs = Drug.objects.all().values()

    context = {
        'diseases_fil': diseases_fil,
        'drugs_fil': drugs_fil,
        'diseases': diseases,
        'drugs': drugs,
    }
    return render(request, 'diseaseInfo/main.html', context)

# DISEASE_FILE = os.path.join(settings.DATA_ROOT, 'mayo-diseases.json')

