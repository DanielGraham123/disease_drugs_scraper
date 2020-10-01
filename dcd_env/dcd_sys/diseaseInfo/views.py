from django.shortcuts import render
from django.conf import settings
from .models import Disease, Drug

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    query = request.GET['searchQuery']

    if query:
        result_set = Disease.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        result_set = Disease.objects.filter()

    page = request.GET.get('page', 1)

    paginator = Paginator(result_set, 10)

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

