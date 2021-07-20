from django.urls import path

from . import views


app_name = 'dishes'

urlpatterns = [
    path('', views.DishListView.as_view(), name='index'),
    path('details/<int:pk>', views.DishDetailView.as_view(), name='details'),
    path('create_order/', views.DishCreateView.as_view(), name='create_order'),
]
