from rest_framework import serializers

from dishes.models import Dish, DishIngredient


class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = DishIngredient
        fields = ['ingredient_name', 'amount']


class DishSerializer(serializers.ModelSerializer):
    ingredients = DishIngredientSerializer(source='dish_ingredient', many=True)

    class Meta:
        model = Dish
        fields = ['name', 'ingredients']
