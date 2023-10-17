import calendar
import datetime

from .models import Day_of_week, Time_cell
from website.services import get_orders_list_where_time_cell_after_and_include_today

WEEKS = 3
DAY_IN_WEEK = 7


def get_working_dates_list_in_format(_format="%d.%m.%y") -> list:
    date = _get_start_date()
    working_dates = []
    orders = get_orders_list_where_time_cell_after_and_include_today()
    # print(get_orders_list_where_time_cell_after_and_include_today()[0])

    for i in range(WEEKS*DAY_IN_WEEK):
        working_dates.append({'date': date.strftime(_format), 'is_working': _is_working_date(date, orders)})
        date = _get_next_date(date)

    return working_dates


def _is_working_date(date: datetime, orders: list):
    Time_cell_count = len(Time_cell.objects.values())
    if not Time_cell_count:
        return False
    counter = 0
    for order in orders:

        if date == datetime.datetime(order['time_cell'].year, order['time_cell'].month, order['time_cell'].day) and order['status'] == 'confirmed':
            counter += 1
        if counter == Time_cell_count:
            return False

    work_days_of_week = [key.lower() for key, value in Day_of_week.objects.values()[0].items() if value][1::]
    today = datetime.datetime.today()
    if date.strftime('%A').lower() in work_days_of_week and today <= datetime.datetime(
            date.year, date.month, date.day):
        return True
    else:
        return False


def _get_start_date() -> datetime:
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    day = today.day - today.weekday()
    if day < 0:
        if today.month == 1:
            year = today.year - 1
            month = 12
        else:
            month -= 1
        day = calendar.monthrange(year, month)[1] - day
    return datetime.datetime(year, month, day)


def _get_next_date(start_date: datetime) -> datetime:
    last_day = int(calendar.monthrange(year=start_date.year, month=start_date.month)[1])
    day = start_date.day + 1
    year = start_date.year
    month = start_date.month

    if start_date.day == last_day:
        day = 1
        month = start_date.month + 1
        if month > 12:
            month = 1
            year = start_date.year + 1

    return datetime.datetime(year, month, day)


def get_working_time_cells_list_in_format(date: str, _format="%H:%M") -> list:

    time_cells = Time_cell.objects.values()
    orders = get_orders_list_where_time_cell_after_and_include_today()
    working_time_cells = []
    for time_cell in time_cells:
        working_time_cells.append(
            {'time': time_cell['time'].strftime(_format), 'is_working': _is_working_time_cell(time_cell=time_cell['time'], date=parsing_date(date), orders=orders)})
    return working_time_cells


def parsing_date(date: str) -> datetime:
    date = date.split('.')
    day = int(date[0])
    month = int(date[1])
    today = datetime.datetime.now()
    if today.month == 12 and month >= 1:
        year = today.year + 1
    else:
        year = today.year
    return datetime.datetime(year, month, day)


def _is_working_time_cell(time_cell: datetime, date: datetime, orders: list) -> bool:
    for order in orders:
        if order["time_cell"] == datetime.datetime(date.year, date.month, date.day, time_cell.hour) \
                and order['status'] == 'confirmed':
            return False
        # print(f'{order["time_cell"]} {order["status"]} {date} {time_cell}')
    return True
