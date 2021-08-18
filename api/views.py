from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView

from api.filters import DishDateTimeFilter
from api.permissions import IsActiveUser
from api.serializers import DishSerializer, TopDishesSerializer
from dishes.models import Dish, Order


class DishListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   GenericAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'name']
    filterset_class = DishDateTimeFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DishDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsActiveUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TopDishesListView(mixins.ListModelMixin, GenericAPIView):
    queryset = Order.objects\
                   .values('dish', 'user')\
                   .annotate(num_order=Count('dish'))\
                   .order_by('-num_order')[:3]
    serializer_class = TopDishesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
