from django.http import HttpResponse
from django.shortcuts import render
from .forms import CocktailForm
import requests
def home(request):
    return HttpResponse("Welcome")

#Task2
def Cocktail_List(request):
    error_message=None
    data=None
    template_name='cocktails/index.html'
    if request.method=='POST':
        query=CocktailForm(request.POST)
        if query.is_valid():
            search_type =query.cleaned_data['search_choices']
            search_input=query.cleaned_data['option']
            if search_type=='name':
                api_url=f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search_input}"
                template_name='cocktails/name.html'
            else:
                api_url=f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={search_input}"  
                template_name='cocktails/ingredient.html' 
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
    return render(request,template_name, context)


#Task 3
def cocktail_detail(request, drink_id):
    api_url=f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    try:
        response=requests.get(api_url)
        response.raise_for_status()
        data=response.json()
        if not data.get('drinks'): 
            raise ValueError("No cocktail found with this ID.")
        cocktail = data['drinks'][0]
        ingredient_with_measure=[]
        for i in range(1,4):
         ingredient_with_measure.append((cocktail.get(f'strIngredient{i}'),cocktail.get(f'strMeasure{i}')))
        context={
         'cocktail':cocktail,
         'ingredient_with_measure':ingredient_with_measure,
        }  
        return render(request,'detail.html',context)
    except requests.exceptions.RequestException as e:
                error_message = f"API Error: {e}"  
                return render(request,'detail.html',error_message)
                                        




