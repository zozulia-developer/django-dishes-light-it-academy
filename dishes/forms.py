from django import forms
from django.forms import ValidationError

from .models import OrderIngredient, Order


class OrderPostForm(forms.Form):
    class Meta:
        model = Order
        fields = ['ingredients']
        # widgets = {
        #     'amount': forms.NumberInput(attrs={'class': 'form-control'})
        # }

