import pytest

from pytest_django.fixtures import db

from unittest import mock

from dishes.models import Dish, Ingredient
from dishes.views import DishListView


@pytest.fixture
def dish(db):
    dish = Dish.objects.create(name='Dish 1')
    return dish


@pytest.fixture
def ingredient(db):
    ingredient = Ingredient.objects.create(name='Ingredient 1')
    return ingredient


@pytest.mark.django_db
def test_dish_list(dish):
    with mock.patch('dishes.models.Dish.__str__', return_value=['name']):
        assert dish.__str__() == ['name']


@pytest.mark.django_db
def test_ingredient_list(ingredient):
    with mock.patch('dishes.models.Ingredient.__str__', return_value=['name']):
        assert ingredient.__str__() == ['name']


@pytest.mark.django_db
def test_success(dish, client):
    resp = client.get('/', follow=True)

    assert resp.status_code == 200


@pytest.mark.django_db
def test_success_rf(rf, settings):
    request = rf.get('/')
    settings.LOGGING = {}
    response = DishListView.as_view()(request)

    assert response.status_code == 200
