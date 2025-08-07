import django.forms as forms


class CocktailForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-slate-100 border-2 border-transparent rounded-lg focus:outline-none focus:ring-2 text-black focus:ring-sky-500 focus:border-transparent',
            'placeholder': 'e.g., Margarita'
        }))


class IngridentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-slate-100 border-2 border-transparent rounded-lg focus:outline-none focus:ring-2 text-black focus:ring-sky-500 focus:border-transparent',
            'placeholder': 'e.g., Gin'
        }))

class MultiForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 bg-slate-100 border-2 border-transparent rounded-lg focus:outline-none focus:ring-2 text-black focus:ring-sky-500 focus:border-transparent',
            'placeholder': 'e.g., Gin,Vodka'
        }))    