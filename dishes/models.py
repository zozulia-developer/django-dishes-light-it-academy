from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


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

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dishes:index')


class Order(models.Model):
    dish = models.ForeignKey(
        'Dish',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='OrderIngredient',
        related_name='orders',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        blank=True,
        null=True
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

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse('dishes:index')

    def __str__(self):
        return str(self.pk)


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

    class Meta:
        pass

    def get_absolute_url(self):
        return reverse('dishes:index')

    def __str__(self):
        return str(self.pk)
