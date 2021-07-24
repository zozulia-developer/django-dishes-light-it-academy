from django import forms
from django.forms import ValidationError, inlineformset_factory

from .models import Dish, OrderIngredient, DishIngredient


# class DishIngredientsForm(forms.ModelForm):
#     class Meta:
#         # model = Dish
#         # fields = ['name', 'ingredients']
#         # widgets = {
#         #     'name': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'ingredients': forms.Select(attrs={'class': 'form-select'})
#         # }
#         model = DishIngredient
#         fields = ['dish', 'ingredient', 'amount']
#         # widgets = {
#         #     'dish': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'ingredient': forms.Select(attrs={'class': 'form-select'}),
#         #     'amount': forms.NumberInput()
#         # }


class OrderIngredientsForm(forms.ModelForm):
    class Meta:
        model = OrderIngredient
        fields = ['order', 'ingredient', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'})
        }


class DishIngredientsForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name']
        exclude = ()


DishIngredientFormset = inlineformset_factory(
    Dish, DishIngredient,
    fields=['ingredient', 'amount'],
    exclude=[],
    fk_name='dish',
    extra=1,
    can_delete=False
)
