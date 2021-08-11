from rest_framework import serializers

from dishes.models import Dish


class DishSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Dish
        fields = ['name', 'created_at', 'updated_at']
