from django.shortcuts import render
from django.conf import settings
import os
import json
from .models import Disease

# Create your views here.
def home(request):
    diseases = Disease.objects.all().order_by('id')[:12]

    context = {
        'diseases': diseases
    }
    return render(request, 'diseaseInfo/main.html', context)

# DISEASE_FILE = os.path.join(settings.DATA_ROOT, 'mayo-diseases.json')
