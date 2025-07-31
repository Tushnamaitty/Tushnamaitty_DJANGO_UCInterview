import django.forms as forms
class CocktailForm(forms.Form):
    search_choices=forms.ChoiceField(choices=[('name','Name'),('ingredient','Ingredient')],
                                     widget=forms.RadioSelect,label='Search by')
    option=forms.CharField(label='Enter your search term', max_length=100,required=True)