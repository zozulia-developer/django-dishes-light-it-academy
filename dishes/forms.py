from django import forms
from django.forms import ValidationError

from .models import Dish, OrderIngredient, DishIngredient


class DishIngredientsForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Select(attrs={'class': 'form-select'})
        }


class OrderIngredientsForm(forms.ModelForm):
    class Meta:
        model = OrderIngredient
        fields = ['order', 'ingredient', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }

