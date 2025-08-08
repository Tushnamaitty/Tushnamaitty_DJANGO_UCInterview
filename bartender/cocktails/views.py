from django.shortcuts import render
from .forms import CocktailForm,IngridentForm,MultiForm
import requests
from .models import CocktailSearch
def cocktail_list(request):
    cocktails = None
    error_message = None
    form = CocktailForm()
    if request.method == 'POST':
        form = CocktailForm(request.POST)
        if form.is_valid():
            cocktail_name = form.cleaned_data['name']
            cocktail_obj, created = CocktailSearch.objects.get_or_create(
                name=cocktail_name.lower()
            )
            cocktail_obj.search_count += 1
            cocktail_obj.save()
            api_url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_name}'
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = response.json()

                if data.get('drinks'):
                    cocktails = data['drinks']
                else:
                    error_message = f"No cocktail found with the name '{cocktail_name}'."

            except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"
    top_searches = CocktailSearch.objects.order_by('-search_count')
    context = {
        'form': form,
        'cocktails': cocktails,
        'error_message': error_message,
        'top_searches': top_searches
    }
    return render(request, "cocktails/index.html", context)
    
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

def multiple_ingredients(request):
    user_input = []
    cocktail_results = []
    
    if request.method == 'POST':
        query = MultiForm(request.POST)
        if query.is_valid():
            q = query.cleaned_data['name']
            ingredients = q.split(',')
            for ingredient in ingredients:
                user_input.append(ingredient.strip())
            for i in range(len(user_input)):
                ingredient = user_input[i]
                api_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}"
                response = requests.get(api_url)
                data = response.json()  
                if data.get('drinks'):
                    cocktail_results.extend(data['drinks'])
    context={
        'cocktails': cocktail_results
    }                
    
    return render(request, 'cocktails/multi.html',context)
    
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

