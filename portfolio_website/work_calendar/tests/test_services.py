import datetime

from django.test import SimpleTestCase, TestCase
from site_iuf_nails.models import Order
from work_calendar.models import Time_cell, Day_of_week

from work_calendar.services import get_working_dates_list_in_format, get_working_time_cells_list_in_format


class TestCase(TestCase):

    def setUp(self):
        Order.objects.create(name="1", telephone="1", time_cell=datetime.datetime(2022, 8, 8, 10), status='confirmed')
        Order.objects.create(name="1", telephone="1", time_cell=datetime.datetime(2022, 8, 8, 13), status='confirmed')
        Order.objects.create(name="1", telephone="1", time_cell=datetime.datetime(2022, 8, 8, 16), status='confirmed')
        Order.objects.create(name="1", telephone="1", time_cell=datetime.datetime(2022, 8, 8, 19), status='confirmed')

        Time_cell.objects.create(time=datetime.datetime(1, 1, 1, 10))
        Time_cell.objects.create(time=datetime.datetime(1, 1, 1, 13))
        Time_cell.objects.create(time=datetime.datetime(1, 1, 1, 16))
        Time_cell.objects.create(time=datetime.datetime(1, 1, 1, 19))
        Day_of_week.objects.create()

    def test_get_working_dates_list_in_format(self):
        test = False
        for date in get_working_dates_list_in_format():
            if date['date'] == '08.08.22' and date['is_working'] == False:
                test = True
        self.assertEqual(test, True)

    def test_get_working_time_cells_list_in_format(self):
        self.assertEqual(get_working_time_cells_list_in_format('8.8'), True)
