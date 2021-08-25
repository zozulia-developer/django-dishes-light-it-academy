from rest_framework import serializers

from api.validators import contain_numbers
from dishes.models import Dish, DishIngredient, Ingredient, Order


class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source="ingredient.name")

    class Meta:
        model = DishIngredient
        fields = ["ingredient_name", "amount"]


class DishListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[contain_numbers])
    ingredients = DishIngredientSerializer(
        source="dish_ingredient", many=True, read_only=True
    )

    class Meta:
        model = Dish
        fields = ["name", "ingredients", "created_at", "updated_at"]


class IngredientSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.name

    class Meta:
        model = Ingredient
        fields = ["name"]


class TopDishesSerializer(serializers.ModelSerializer):
    dish = serializers.ReadOnlyField()
    ingredients = IngredientSerializer(read_only=True, many=True)
    user = serializers.ReadOnlyField()
    num_order = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ["dish", "ingredients", "user", "num_order"]
