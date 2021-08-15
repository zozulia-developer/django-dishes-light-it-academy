from rest_framework import serializers

from api.validators import contain_numbers
from dishes.models import Dish, DishIngredient, Ingredient


class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = DishIngredient
        fields = ['ingredient_name', 'amount']


class DishSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100,
                                 validators=[contain_numbers])
    ingredients = DishIngredientSerializer(source='dish_ingredient',
                                           many=True,
                                           read_only=True)

    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'created_at', 'updated_at']

    # def create(self, validated_data):
    #     ingredients_data = validated_data.pop('dish_ingredient')
    #     ingredient_names = [i['ingredient'] for i in ingredients_data]
    #     ingredient_amount = [i['amount'] for i in ingredients_data]
    #     amount_index = 0
    #     dish = Dish.objects.create(**validated_data)
    #     dish_id = Dish.objects.filter(name=validated_data['name']).values_list('id', flat=True).last()
    #
    #     for ingredient in ingredient_names:
    #         Ingredient.objects.create(**ingredient)
    #     for ingredient in ingredient_names:
    #         ingredient_id = Ingredient.objects.filter(name=ingredient['name']).values_list('id', flat=True).last()
    #         DishIngredient.objects.create(dish=dish_id, ingredient=ingredient_id, amount=ingredient_amount[amount_index])
    #         amount_index += 1
    #     return dish
