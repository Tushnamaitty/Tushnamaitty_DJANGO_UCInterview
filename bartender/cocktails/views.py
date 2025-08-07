from django.shortcuts import render

from .forms import CocktailForm,IngridentForm
import requests
# Create your views here.


def cocktail_list(request):
    data = None
    error_message = None
    print(request) 
    if(request.method == 'POST'):
        query = CocktailForm(request.POST)
        if query.is_valid():
            q = query.cleaned_data['name']
            api_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={q}"
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()
            except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"
    else:
        query = CocktailForm()
    print(query)
    context = {
        'form': query,
        'data': data,
        'error_message': error_message,
    }

    return render(request, 'cocktails/index.html', context)


def ing_list(request):
    data = None
    error_message = None
    if(request.method == 'POST'):
        query = IngridentForm(request.POST)
        if query.is_valid():
            q = query.cleaned_data['name']
            api_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={q}"
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()
            except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"
    else:
        query = IngridentForm()
    print(query)
    context = {
        'form': query,
        'data': data,
        'error_message': error_message,
    }

    return render(request, 'cocktails/ingredients.html', context)

def drink_view(request,drinkId):
    error_message = None
    data = None
    if(drinkId==None):
        error_message="Drink Id Not Present"
    else:
        api_url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drinkId}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"
    
    context = {
        'data': data,
        'error_message': error_message,
    }
    return render(request,'cocktails/drinks.html',context)



    
