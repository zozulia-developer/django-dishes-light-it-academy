from django.test import TestCase, Client

from dishes.forms import IngredientForm
from dishes.models import Dish, Ingredient


class DishTestCase(TestCase):
    dish_name = 'for test dish'
    fixtures = ['dish.json']

    def setUp(self):
        self.dish = Dish.objects.create(name=self.dish_name)

    def tearDown(self):
        self.dish.delete()

    def test_dish_list(self):
        self.assertEqual(self.dish.__str__(), self.dish_name)

    def test_success(self):
        c = Client(HTTP_ACCEPT='test')

        resp = c.get('/dishes/')
        self.assertEqual(resp.status_code, 200)

    def test_create_dish_throw_csrf(self):
        c = Client(enforce_csrf_checks=True)

        resp = c.post(
            '/dishes/create_dish/',
            follow=True,
            data={
                'name': 'name1',
            }
        )
        self.assertEqual(resp.status_code, 403)


class SearchDishTestCase(TestCase):
    search_phrase = 'Test Dish'

    def setUp(self):
        self.dish = Dish.objects.create(name='Test Dish')

    def tearDown(self) -> None:
        self.dish.delete()

    def test_query_search_filter(self):
        self.assertQuerysetEqual(Dish.objects.filter(name__icontains=self.search_phrase), ["<Dish: Test Dish>"])


class DishIngredientTestCase(TestCase):
    def setUp(self):
        self.dish = Dish.objects.create(name='First dish')
        self.ingredient = Ingredient.objects.create(name='First ingredient')

    def tearDown(self) -> None:
        self.dish.delete()
        self.ingredient.delete()

    def test_create_dish_ingredient(self):
        resp = self.client.post(
            '/dishes/create_dish/',
            follow=True,
            data={
                'dish': self.dish.pk,
                'ingredient': self.ingredient.pk,
                'amount': 3
            }
        )
        self.assertEqual(resp.status_code, 200)


class IngredientTestCase(TestCase):
    ingredient_name = 'Test ingredient 1'

    def setUp(self) -> None:
        self.ingredient = Ingredient.objects.create(name=self.ingredient_name)

    def tearDown(self) -> None:
        self.ingredient.delete()

    def test_ingredient_list(self):
        self.assertEqual(self.ingredient.__str__(), self.ingredient_name)

    def test_create_ingredient_throw_csrf(self):
        c = Client(enforce_csrf_checks=True)

        resp = c.post(
            '/dishes/create_ingredient/',
            follow=True,
            data={
                'name': 'test name',
            }
        )
        self.assertEqual(resp.status_code, 403)

    def test_get_absolute_url(self):
        c = Client(HTTP_ACCEPT='test')

        resp = c.get(self.ingredient.get_absolute_url())
        self.assertEqual(resp.status_code, 200)

    def test_create_ingredient_valid_form(self):
        form = IngredientForm(data={'name': 'Test valid name!'})
        self.assertTrue(form.is_valid())

    def test_create_ingredient_invalid_form(self):
        form = IngredientForm(data={'name': ''})
        self.assertFalse(form.is_valid())

    def test_name_starting_lowercase(self):
        form = IngredientForm(data={'name': 'invalid name'})
        self.assertEqual(form.errors['name'], ['Should start with an uppercase letter!'])

    def test_name_more_than_50(self):
        form = IngredientForm(data={'name': '123456789'*7})
        self.assertEqual(form.errors['name'], ['Ingredient name length should be less than 50 symbols!'])

    def test_get_create_ingredient_template(self):
        resp = self.client.get('/dishes/create_ingredient/')

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<h2>Create Ingredient</h2>', html=True)
