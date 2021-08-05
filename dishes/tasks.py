import csv
from celery import shared_task

from datetime import datetime

from dish_order.settings import BASE_DIR


DATE_TIME_NOW = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')


@shared_task
def report_csv():
    title_row = [
        'ORDER_ID',
        'DISH_NAME',
        'INGREDIENTS',
        'CHANGED',
        'CHANGED_ITEMS_AND_AMOUNT'
    ]
    with open(BASE_DIR / 'reports/orders_report_'+DATE_TIME_NOW+'.csv', 'w', newline='') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',')
        file_writer.writerow(title_row)
