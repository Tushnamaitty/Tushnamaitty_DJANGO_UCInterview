from django.urls import path
from .views import Cocktail_List

urlpatterns = [
    path('', Cocktail_List, name='cocktail_list')
]