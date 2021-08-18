from django.urls import path, include

from rest_framework import routers

from api.views import DishListView, DishDetailView, TopDishesListView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('dishes/', DishListView.as_view(), name='dishes'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('top3-dishes/', TopDishesListView.as_view(), name='top_dishes'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
