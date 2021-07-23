from django.core.validators import MinValueValidator
from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='DishIngredient',
        related_name='dishes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    dish = models.ForeignKey(
        'Dish',
        on_delete=models.CASCADE
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        through="OrderIngredient",
        related_name="orders",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]


class DishIngredient(models.Model):
    dish = models.ForeignKey(
        'Dish',
        on_delete=models.CASCADE,
        related_name='di'
    )
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='di'
    )
    amount = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )


class OrderIngredient(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='oi'
    )
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='oi'
    )
    amount = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
