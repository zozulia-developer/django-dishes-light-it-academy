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

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            return name

        if len(name) > 50:
            raise ValidationError('Ingredient name length should be less than 50 symbols!')

        if not name[0].isupper():
            raise ValidationError('Should start with an uppercase letter!')

        return name


class OrderIngredientsForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['dish']
        exclude = ()
        widgets = {
            'dish': forms.Select(attrs={
                'class': 'form-select',
                # 'disabled': True
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
        'ingredient': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control mb-4'}),
    },
    exclude=[],
    fk_name='order',
    # extra=1,
    can_delete=False
)
