from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import OrderIngredientsForm, DishIngredientsForm, DishIngredientFormset, IngredientForm, \
    OrderIngredientFormset
from .models import Dish, Ingredient, Order, DishIngredient


class SearchResultsView(ListView):
    model = Dish
    template_name = 'dishes/search_results.html'

    def get_queryset(self):
        query_q = self.request.GET.get('q')
        object_list = Dish.objects.filter(
            name__icontains=query_q
        )
        return object_list


class DishListView(ListView):
    model = Dish
    template_name = 'dishes/index.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        query_filter = self.request.GET.get('filter')
        query_from = self.request.GET.get('from')
        query_to = self.request.GET.get('to')
        if query_filter and query_filter == 'asc':
            dishes = Dish.objects.all().order_by('created_at')
        elif query_from:
            dishes = Dish.objects.filter(created_at__range=[query_from, query_to])
        else:
            dishes = Dish.objects.all().order_by('-created_at')
        return dishes


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/details.html'
    context_object_name = 'dish'


class DishIngredientCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    success_url = reverse_lazy('dishes:index')
    form_class = DishIngredientsForm

    def get_context_data(self, **kwargs):
        context = super(DishIngredientCreateView, self).get_context_data()
        if self.request.POST:
            context['di_formset'] = DishIngredientFormset(self.request.POST)
        else:
            context['di_formset'] = DishIngredientFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['di_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'dishes/ingredients.html'
    context_object_name = 'ingredients'


class IngredientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dishes/create_ingredient.html'
    form_class = IngredientForm


class OrderListView(ListView):
    model = Order
    template_name = 'dishes/orders.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'dishes/order_details.html'
    context_object_name = 'order'


class OrderIngredientCreateView(LoginRequiredMixin, CreateView):
    model = Order
    success_url = reverse_lazy('dishes:orders')
    form_class = OrderIngredientsForm

    def get_context_data(self, **kwargs):
        context = super(OrderIngredientCreateView, self).get_context_data()
        id = self.request.GET.get('id')
        if self.request.POST:
            context['oi_formset'] = OrderIngredientFormset(self.request.POST)
        else:
            dish_name = Dish.objects.filter(pk=id)
            ingredients_queryset = DishIngredient.objects.filter(dish=id)

            ingredients = [n.ingredient.id for n in ingredients_queryset.all()]
            amounts = [n.amount for n in ingredients_queryset.all()]
            data = dict(zip(ingredients, amounts))
            initial_data = [{'ingredient': i, 'amount': j} for i, j in data.items()]

            context['form'].fields['dish'].queryset = dish_name
            context['form'].fields['dish'].empty_label = None

            initial_formsets = OrderIngredientFormset(initial=initial_data)
            initial_formsets.extra = len(initial_data)

            context['oi_formset'] = initial_formsets
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['oi_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)
