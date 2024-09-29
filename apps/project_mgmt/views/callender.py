from django.views import View
from django.shortcuts import render
from datetime import datetime, timedelta
from calendar import Calendar


class CalenderView(View):
    def get(self, request):
        current_date = datetime.now().date()
        calender = Calendar().monthdatescalendar(current_date.year, current_date.month)
        context = {
            'calender':calender,
            'month':current_date.month, 
            'year':current_date.year, 
            'current_date':current_date
        }
        return render(request, 'project_mgmt/calender.html', context)
    

class ChangeCalenderMonth(View):
    def get(self, request, date, next, prev):
        current_date = datetime.strptime(date, "%Y-%m-%d").date()
        first_date = current_date.replace(day=1)
        if prev == "1":
            previous_month = first_date - timedelta(days= 1)
            calender = Calendar().monthdatescalendar(previous_month.year, previous_month.month)
            context = {
                'calender':calender,
                'month':previous_month.month, 
                'year':previous_month.year, 
                'current_date':previous_month,
                'next': 0,
                'prev': 1,
                }
            return render(request, 'project_mgmt/calender.html', context)
        if next == "1":
            last_day_of_current_month = Calendar().monthdatescalendar(current_date.year, current_date.month)[-1]
            last_day_of_current_month = last_day_of_current_month[-1]
            next_month_date = last_day_of_current_month + timedelta(days=1)
            calender = Calendar().monthdatescalendar(next_month_date.year, next_month_date.month)
            context = {
                'calender':calender,
                'month':next_month_date.month, 
                'year':next_month_date.year, 
                'current_date':next_month_date,
                'next': 0,
                'prev': 1,
            }
            return render(request, 'project_mgmt/calender.html', context)
        return render(request, 'project_mgmt/calender.html')
        