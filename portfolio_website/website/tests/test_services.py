import datetime

from django.test import SimpleTestCase, TestCase

from site_iuf_nails.services import parse_time_cell


class TestCase_parse_time_cell(TestCase):
    def test_parse_time_cell_without_time(self):
        assert parse_time_cell(time_cell_from_form="Label: 04.08", have_time=False) == datetime.datetime(datetime.datetime.today().year, 8, 4)

    def test_parse_time_cell_with_time(self):
        assert parse_time_cell(time_cell_from_form="Label 04.08 о 16:00", have_time=True) == datetime.datetime(datetime.datetime.today().year, 8, 4, 16)

    def test_parse_time_cell_empty_str_have_time_true(self):
        try:
            parse_time_cell(time_cell_from_form="", have_time=True)
            assert False
        except:
            assert True

    def test_parse_time_cell_empty_str_have_time_false(self):
        try:
            parse_time_cell(time_cell_from_form="", have_time=False)
            assert False
        except:
            assert True

    def test_parse_time_cell_empty_str_have_time_true(self):
        try:
            parse_time_cell(time_cell_from_form="04.08 о 16:00", have_time=True)
            assert False
        except:
            assert True

    def test(self):
        assert parse_time_cell(time_cell_from_form='Обране вікно: 19.08 о 16:00', have_time=False) == datetime.datetime(
            datetime.datetime.today().year, 8, 4)
