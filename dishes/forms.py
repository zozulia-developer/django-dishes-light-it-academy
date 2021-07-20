from django import forms
from django.forms import ValidationError

from .models import Dish


class PostForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['number']

        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'})
        }

