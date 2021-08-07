import csv
from celery import shared_task
from django.utils.timezone import now

from dish_order.settings import BASE_DIR
from .models import Order, Dish


DATE_TIME_NOW = now().strftime('%d-%m-%Y_%H:%M:%S')
REPORT_DAY = now().strftime('%Y-%m-%d')


@shared_task
def report_csv():
    print('!!!START CELERY TASK!!!')

    title_row = [
        'ORDER_ID',
        'DISH_NAME',
        'INGREDIENTS_AND_AMOUNT',
        'IS_CHANGED',
        'CHANGED_ITEMS_AND_AMOUNT'
    ]
    filename = str(BASE_DIR) + '/reports/orders_report_' + DATE_TIME_NOW + '.csv'
    orders = Order.objects.filter(created_at__gt=REPORT_DAY)
    is_changed = False
    changed_ingredients = []

    with open(filename, 'w', newline='') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',')
        file_writer.writerow(title_row)

        for order in orders:
            dish_ingredients = order.dish.di.filter(dish=order.dish.id)
            ingredients = "\n".join(
                f'{i.ingredient.name} - {i.amount}' for i in dish_ingredients
            )

            file_writer.writerow([
                order.id,
                order.dish.name,
                ingredients,
            ])

    print('!!!END CELERY TASK!!!')
