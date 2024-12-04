from django.views import View
from django.shortcuts import render
from datetime import datetime, timedelta
from calendar import Calendar
from utils.helper.date_and_time import current_date, str_to_date
from utils.helper.callender import get_month_calender

class CalenderView(View):
    def get(self, request):
        date = current_date()
        calender = get_month_calender(date.year, date.month)
        context = {
            'calender':calender,
            'month':date.month, 
            'year':date.year, 
            'current_date':date,
            'calender_date':date
        }
        return render(request, 'project_mgmt/calender.html', context)
    

class ChangeCalenderMonth(View):
    def get(self, request, date, next, prev):
        calender_date = str_to_date(date)
        first_date = calender_date.replace(day=1)
        if prev == "1":
            previous_month = first_date - timedelta(days= 1)
            calender = get_month_calender(previous_month.year, previous_month.month)
            context = {
                'calender':calender,
                'month':previous_month.month, 
                'year':previous_month.year, 
                'calender_date':previous_month,
                'current_date':current_date(),
                'next': 0,
                'prev': 1,
                }
            return render(request, 'project_mgmt/calender.html', context)
        if next == "1":
            last_day_of_current_month = get_month_calender(calender_date.year, calender_date.month)[-1]
            last_day_of_current_month = last_day_of_current_month[-1]
            next_month_date = last_day_of_current_month + timedelta(days=1)
            calender = get_month_calender(next_month_date.year, next_month_date.month)
            context = {
                'calender':calender,
                'month':next_month_date.month, 
                'year':next_month_date.year, 
                'calender_date':next_month_date,
                'current_date':current_date(),
                'next': 0,
                'prev': 1,
            }
            return render(request, 'project_mgmt/calender.html', context)
        return render(request, 'project_mgmt/calender.html')
        