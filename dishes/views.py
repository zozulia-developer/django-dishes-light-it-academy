from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Dish, OrderIngredient, DishIngredient, Order


class DishListView(ListView):
    model = Dish
    template_name = 'dishes/index.html'
    context_object_name = 'dishes'


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/details.html'
    context_object_name = 'dish'


class DishCreateOrderView(CreateView):
    model = Order
    template_name = 'dishes/create_order.html'
    context_object_name = 'order'
    fields = ['ingredients', ]
