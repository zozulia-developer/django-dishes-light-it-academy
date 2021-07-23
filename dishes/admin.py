from django.contrib import admin

from dishes.models import Ingredient, Dish, Order


class DishIngredientInline(admin.TabularInline):
    model = Dish.ingredients.through


class OrderIngredientInline(admin.TabularInline):
    model = Order.ingredients.through


class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    inlines = [DishIngredientInline]


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at",)
    inlines = [OrderIngredientInline]


admin.site.register(Ingredient)
admin.site.register(Dish, DishAdmin)
admin.site.register(Order, OrderAdmin)
