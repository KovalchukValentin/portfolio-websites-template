import datetime

from django.test import TestCase

from site_iuf_nails.models import Order
from site_iuf_nails.services import get_orders_list_where_time_cell_after_and_include_today


def print_return_from_func(func):
    print(f'FUNCTION: {func.__name__} RESULT: {func()}')
    for obj in func():
        print(obj['time_cell'])


class AnimalTestCase(TestCase):
    def setUp(self):
        Order.objects.create(name="before_today1", telephone="+380681111111", time_cell=datetime.datetime(2022, 7, 28, 12))
        Order.objects.create(name="before_today2", telephone="+380681111111", time_cell=datetime.datetime(2022, 7, 29, 10))
        Order.objects.create(name="today", telephone="+380680000000", time_cell=datetime.datetime.today())
        Order.objects.create(name="after_today1", telephone="+380680000000", time_cell=datetime.datetime.today() + datetime.timedelta(days=1))

    def test_get_orders_list_where_time_cell_after_and_include_today(self):
        # print_return_from_func(get_orders_list_where_time_cell_after_and_include_today)
        self.assertEqual(len(get_orders_list_where_time_cell_after_and_include_today()), 2)



