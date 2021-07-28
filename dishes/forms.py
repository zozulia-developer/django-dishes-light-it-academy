from django import forms
from django.forms import ValidationError, inlineformset_factory

from .models import Dish, OrderIngredient, DishIngredient, Ingredient, Order


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
        labels = {
            'name': 'Ingredient Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ingredient name'
            })
        }


class OrderIngredientsForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['dish']
        exclude = ()
        widgets = {
            'dish': forms.Select(attrs={
                'class': 'form-select',
                #'disabled': True
            }),
        }


class DishIngredientsForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name']
        exclude = ()
        labels = {
            'name': 'Dish Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter dish name',
                'readonly': 'readonly'
            })
        }


DishIngredientFormset = inlineformset_factory(
    Dish, DishIngredient,
    fields=['ingredient', 'amount'],
    labels={
        'ingredient': 'Ingredient name',
        'amount': 'Ingredient Amount'
    },
    widgets={
        'ingredient': forms.Select(attrs={'class': 'form-select'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
    },
    exclude=[],
    fk_name='dish',
    extra=1,
    can_delete=False
)

OrderIngredientFormset = inlineformset_factory(
    Order, OrderIngredient,
    fields=['ingredient', 'amount'],
    labels={
        'ingredient': 'Ingredient name',
        'amount': 'Ingredient Amount'
    },
    widgets={
        'ingredient': forms.Select(attrs={'class': 'form-select'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control mb-4'}),
    },
    exclude=[],
    fk_name='order',
    extra=1,
    can_delete=False
)
