from datetime import datetime, date, time, timedelta
from django.conf import settings
import pytz

def current_date() -> date:
    """
    Returns the current date as a `datetime.date` object in the "YYYY-MM-DD" format.

    :return: The current date as a `datetime.date` object.
    :rtype: datetime.date

    :Example:
    
    >>> current_date()
    datetime.date(2024, 10, 21)

    The output format when printed will look like: "2024-10-21".
    """
    return datetime.now().date()

def current_time() -> time:
    """
    Returns the current time as a `datetime.time` object, including hours, minutes, seconds, and microseconds.

    :return: The current time as a `datetime.time` object.
    :rtype: datetime.time

    :Example:
    
    >>> current_time()
    datetime.time(14, 23, 7, 123456)

    The output format when printed will look like: "14:23:07.123456".
    """
    return datetime.now().time()

def str_to_date(date) -> date:
    """
    A function that converts a string in "YYYY-MM-DD" format to a Date object.

    :param date:
    :type date: str

    :return: The date as a `datetime.date` object.
    :rtype: datetime.date

    :Example:

    >>> str_to_date()
    datetime.date(2024, 10, 21)

    """
    return datetime.strptime(date, "%Y-%m-%d").date()

def datetime_in_timezone(date_and_time:datetime) -> datetime:

    time_zone = pytz.timezone(settings.TIME_ZONE)

    return date_and_time.astimezone(time_zone)

def formatted_time(time:timedelta) -> str:
    seconds = time.seconds
    sec = seconds % 60
    min = seconds // 60
    hr = min // 60
    return f"{hr:02}:{min:02}:{sec:02}"
