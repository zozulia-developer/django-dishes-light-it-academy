from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import PostForm
from .models import Dish


class DishListView(ListView):
    model = Dish
    template_name = 'dishes/index.html'
    context_object_name = 'dishes'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/details.html'
    context_object_name = 'dish'


class DishCreateView(CreateView):
    pass
