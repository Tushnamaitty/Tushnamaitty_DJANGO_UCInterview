from django.urls import path
from . import views
urlpatterns = [
    path('', views.Cocktail_List, name='cocktail_list'),
    path('cocktail/<str:drink_id>/', views.cocktail_detail, name='cocktail_detail'),
]
