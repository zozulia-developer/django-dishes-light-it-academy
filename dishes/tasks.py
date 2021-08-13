import csv
import os
from celery import shared_task
from django.utils.timezone import now

from dish_order.settings import BASE_DIR
from .models import Order

DATE_TIME_NOW = now().strftime('%d-%m-%Y_%H:%M:%S')
REPORT_DAY = now().strftime('%Y-%m-%d')


@shared_task
def report_csv():
    title_row = [
        'ORDER_ID',
        'DISH_NAME',
        'INGREDIENTS_AND_AMOUNT',
        'IS_CHANGED',
        'CHANGED_ITEMS_AND_AMOUNT'
    ]
    if not os.path.exists(BASE_DIR / 'reports'):
        os.mkdir(BASE_DIR / 'reports')

    filename = str(BASE_DIR) + '/reports/orders_report_' + DATE_TIME_NOW + '.csv'
    orders = Order.objects.filter(created_at__gt=REPORT_DAY)

    with open(filename, 'w', newline='') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',')
        file_writer.writerow(title_row)

        for order in orders:
            is_changed = False
            dish_ingredients = order.dish.di.filter(dish=order.dish.id)
            di_ingredients = "\n".join(
                f'{ingr.ingredient.name} - {ingr.amount}' for ingr in dish_ingredients
            )
            order_ingredients = order.oi.filter(order=order.id)
            oi_ingredients = "\n".join(
                f'{ingr.ingredient.name} - {ingr.amount}' for ingr in order_ingredients
            )

            for ingredient in oi_ingredients:
                if ingredient not in di_ingredients:
                    is_changed = True

            file_writer.writerow([
                order.id,
                order.dish.name,
                di_ingredients,
                is_changed,
                oi_ingredients if is_changed else ''
            ])
