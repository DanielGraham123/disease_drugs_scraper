from django.urls import path
from .views import home, search, details

app_name = "diseaseInfo"

urlpatterns = [
    path('', home, name="home"),
    path('search_results', search, name="search"),
    path('details/<int:id>', details, name="details"),
]
