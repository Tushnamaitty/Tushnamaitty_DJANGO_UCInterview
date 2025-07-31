from django.http import HttpResponse
from django.shortcuts import render
from .forms import CocktailForm
import requests
def home(request):
    return HttpResponse("Welcome")
def Cocktail_List(request):
    error_message=None
    data=None
    if request.method=='POST':
        query=CocktailForm(request.POST)
        if query.is_valid():
            search_type =query.cleaned_data['search_choices']
            search_input=query.cleaned_data['option']
            if search_type=='name':
                api_url=f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search_input}"
            else:
                api_url=f"https://www.thecocktaildb.com/api/json/v1/1/search.php?i={search_input}"    
            try:
                response=requests.get(api_url)
                response.raise_for_status()
                data=response.json()
            except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"
    else:
        query=CocktailForm()
    context = {
        'form': query,
        'data': data,
        'error_message': error_message,
    }
    return render(request, 'cocktails/index.html', context)
    

