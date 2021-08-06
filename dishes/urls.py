from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'dishes'

urlpatterns = [
    path('', views.DishListView.as_view(), name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('details/<int:pk>',
         cache_page(60, cache='db_cache')(views.DishDetailView.as_view()),
         name='details'),
    path('create_dish/', views.DishIngredientCreateView.as_view(), name='create_dish'),
    path('ingredients/',
         cache_page(60, cache='db_cache')(views.IngredientListView.as_view()),
         name='ingredients'),
    path('create_ingredient/', views.IngredientCreateView.as_view(), name='create_ingredient'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order_details/<int:pk>',
         cache_page(60, cache='db_cache')(views.OrderDetailView.as_view()),
         name='order_details'),
    path('create_order', views.OrderIngredientCreateView.as_view(), name='create_order'),
]
