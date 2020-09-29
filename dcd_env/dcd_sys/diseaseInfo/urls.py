from django.urls import path
from .views import home

app_name = "diseaseInfo"

urlpatterns = [
    path('', home, name="home-view")
]
