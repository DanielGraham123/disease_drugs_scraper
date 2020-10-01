from django.urls import path
from .views import home, search

app_name = "diseaseInfo"

urlpatterns = [
    path('', home, name="home"),
    path('search_results', search, name="search")
]
