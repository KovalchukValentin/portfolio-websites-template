import datetime
from typing import Union

from .models import Order, Gallery_image, Certificate_image, Offer

def parse_time_cell(time_cell_from_form: str, have_time=False) -> datetime:
    """Возвращает datetime дату с полученой строки, учитывая наличие времени have_time. Строка в формате %dd.mm%%HH:MM%.
    В случае ошибки возвращает None"""
    index = _get_index_char_from_in(time_cell_from_form, '0123')
    if not index:
        return None

    date = time_cell_from_form[index:index + 5:].split(".")
    day = int(date[0])
    month = int(date[1])
    time_cell_from_form = time_cell_from_form[index + 5::]
    hour = 0

    if have_time:
        index = _get_index_char_from_in(time_cell_from_form, '012')
        if not index:
            return None

        hour = int(time_cell_from_form[index:index + 5:].split(':')[0])
    try:
        return datetime.datetime(_get_year_for_parser(month=month), month, day, hour)
    except:
        return None


def _get_year_for_parser(month: int) -> int:
    '''Возвращает следующий год, если текущий месяц 12й, а полученый month меньше 12 и больше 0'''
    return datetime.datetime.today().year + 1 \
        if datetime.datetime.today().month == 12 and 12 > month > 0 \
        else datetime.datetime.today().year


def _get_index_char_from_in(string: str, found_chars: str) -> Union[int]:
    '''Возвращает индекс найденого символа в string из списка found_chars иначе возвращает None'''
    for num, char in enumerate(string):
        if char in found_chars:
            return num
    return None


def get_orders_list_where_time_cell_after_and_include_today() -> list:
    """Возвращает лист значений обьектов Order из базы даних в которых дата сегодня и позже"""
    orders = Order.objects.filter(time_cell__gte=datetime.datetime.today()-datetime.timedelta(days=1, hours=1)).values()
    return orders


def get_gallary_images_names() -> list:
    'Возвращает лист путей к изображениям из базы даних для галереи'
    return Gallery_image.objects.all()


def get_certificate_gallary_images_names() -> list:
    'Возвращает лист путей к изображениям из базы даних для галереи сертификатов'
    return Certificate_image.objects.all()


def get_offers_list() -> list:
    'Возвращает из базы даних лист словарей с 2я аргументами, где name - название услуги, а price - цена за услугу'
    return Offer.objects.all()

def is_good_name(name: str) -> bool:
    return len(name) > 1


def clear_telephone(telephone: str) -> str:
    return telephone.replace("+", '').replace(" ", '').replace("-", '').replace("(", '').replace(")", '')


def is_good_telephone(telephone: str) -> bool:
    if len(telephone) != 12 and len(telephone) != 10:
        return False
    for char in telephone:
        if not char in '0123456789':
            return False
    return True


def is_good_message(message:str):
    return not len(" ".join(message.split())) < 10


def clear_email(email: str):
    return " ".join(email.split())


def is_good_email(email: str):
    at_index = email.find('@')
    point_index = email.find('.')
    return not (at_index < 3 or point_index < at_index + 3 or len(email) < point_index + 3)

