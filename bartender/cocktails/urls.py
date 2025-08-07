from django.urls import path
from .views import cocktail_list,ing_list,drink_view

urlpatterns = [
    path('name', cocktail_list, name='cocktail_list'),
    path('ingredients', ing_list, name='ing_list'),
    path('<str:drinkId>',drink_view,name='drinks_detail_view')
    
]