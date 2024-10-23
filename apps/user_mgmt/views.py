from django.views import View
from apps.auth.models import UserModel
from django.shortcuts import render
from django.core.paginator import Paginator
from utils.helper.pagination import get_paginated_response
from utils.helper.search_and_filter import search, filter_by_staff, filter_by_user, filter_by_superuser
from django.db.models import Q

class UsersView(View):
    def get(self, request):
        # Get all users excluding the deleted ones

        search_query = request.GET.get('search', None)
        filter = request.GET.get('filter', None)

        search_fields = ['username', 'email']

        users = UserModel.objects.all().exclude(is_deleted=True)

        filter_map = {
            "is_staff": filter_by_staff,
            "is_superuser": filter_by_superuser,
            "is_active": filter_by_user
        }
        if filter in filter_map:
            users = filter_map[filter](users)

        if search_query:
            users = search(search_query, users, search_fields)
        

        count = request.GET.get('count', 5)
        page_number = request.GET.get('page', 1)
        page_obj = get_paginated_response(users, count, page_number)

        return render(request, 'user_mgmt/users.html', {'page_obj': page_obj})