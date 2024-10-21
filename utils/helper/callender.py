from calendar import Calendar
from typing import List
from datetime import date

def get_month_calender(year:int, month:int) -> List[List[date]]:
    """
    Returns a matrix representing the calendar for a specific month of a given year.

    Each week is represented as a list of `datetime.date` objects, with days outside
    the specified month represented as the last day of the previous month or the first 
    day of the next month (depending on their position).

    :param year: The year of the calendar (e.g., 2024).
    :type year: int
    :param month: The month of the calendar (1-12).
    :type month: int
    
    :return: A list of lists containing `datetime.date` objects representing the 
             weeks of the specified month.
    :rtype: List[List[datetime.date]]

    :Example:

    >>> get_month_calendar(2024, 10)
    [[datetime.date(2024, 9, 30), datetime.date(2024, 10, 1), 
      datetime.date(2024, 10, 2), datetime.date(2024, 10, 3), 
      datetime.date(2024, 10, 4), datetime.date(2024, 10, 5), 
      datetime.date(2024, 10, 6)],
     [datetime.date(2024, 10, 7), datetime.date(2024, 10, 8), 
      datetime.date(2024, 10, 9), datetime.date(2024, 10, 10), 
      datetime.date(2024, 10, 11), datetime.date(2024, 10, 12), 
      datetime.date(2024, 10, 13)],
     ...]
    """
    return Calendar().monthdatescalendar(year, month)
