from django_filters.rest_framework import FilterSet, CharFilter, DateTimeFilter

from dishes.models import Dish


class DishDateTimeFilter(FilterSet):
    class Meta:
        model = Dish
        fields = {
            'name': ['icontains'],
            'created_at': ['iexact', 'lte', 'gte']
        }