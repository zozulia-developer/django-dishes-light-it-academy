from django.urls import path

from . import views


app_name = 'dishes'

urlpatterns = [
    path('', views.DishListView.as_view(), name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('details/<int:pk>', views.DishDetailView.as_view(), name='details'),
    path('create_dish/', views.DishIngredientCreateView.as_view(), name='create_dish'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredients'),
    path('create_ingredient/', views.IngredientCreateView.as_view(), name='create_ingredient'),
    path('create_order/', views.OrderIngredientsCreateView.as_view(), name='create_order'),
]
