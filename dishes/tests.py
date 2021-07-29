from django.test import TestCase, Client

from dishes.models import Dish, Ingredient


class DishTestCase(TestCase):
    dish_name = 'test dish'

    def setUp(self):
        pass

    def test_dish_list(self):
        dish = Dish.objects.create(name=self.dish_name)
        self.assertEqual(dish.__str__(), 'test dish')


class DishListCase(TestCase):
    fixtures = ['dish.json']

    def setUp(self):
        dish = Dish.objects.create(name='My dish')

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
                'name': 'name',
            }
        )
        self.assertEqual(resp.status_code, 403)
