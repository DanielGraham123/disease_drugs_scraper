from django.shortcuts import render
from django.conf import settings
from .models import Disease, Drug

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain


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

def search(request):
    query = request.GET.get('q')

    if query:
        diseases_result = Disease.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(symptoms__icontains=query) | Q(risks__icontains=query) | Q(causes__icontains=query))

        drugs_result = Drug.objects.filter(Q(name__icontains=query) | Q(uses__icontains=query) | Q(generic_name__icontains=query) | Q(other_name__icontains=query) | Q(side_effects__icontains=query) | Q(precautions__icontains=query) | Q(interactions__icontains=query))
    else:
        diseases_result = Disease.objects.filter()
        drugs_result = Drug.objects.filter()
        

    page = request.GET.get('page', 1)

    result_set = chain(diseases_result, drugs_result)

    paginator = Paginator(list(result_set), 12)

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        'results': results,
        'query': query,
    }

    return render(request, 'diseaseInfo/search_results.html', context)

def details(request, name, description):
    disease_detail = Diseases.objects.get()

