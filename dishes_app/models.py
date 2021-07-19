from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField(
        'Ingredient',
        through="DishIngredient",
        related_name="dishes"
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredients = models.ManyToManyField(
        'Ingredient',
        through="OrderIngredient",
        related_name="orders",
    )

    class Meta:
        ordering = ["-created_at"]


class DishIngredient(models.Model):
    dish_id = models.ForeignKey(
        'Dish',
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField(default=1)


class OrderIngredient(models.Model):
    order_id = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField(default=1)
