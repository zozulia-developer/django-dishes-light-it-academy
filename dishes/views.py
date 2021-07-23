from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import OrderIngredientsForm, DishIngredientsForm
from .models import Dish


class SearchResultsView(ListView):
    model = Dish
    template_name = 'dishes/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Dish.objects.filter(
            name__icontains=query
        )
        return object_list


class DishListView(ListView):
    model = Dish
    template_name = 'dishes/index.html'
    context_object_name = 'dishes'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/details.html'
    context_object_name = 'dish'


class DishIngredientCreateView(CreateView):
    template_name = 'dishes/create_dish.html'
    form_class = DishIngredientsForm


class OrderIngredientsCreateView(CreateView):
    template_name = 'dishes/create_order.html'
    form_class = OrderIngredientsForm
