from django.views import View
from apps.auth.models import UserModel
from django.shortcuts import render
from django.core.paginator import Paginator
from utils.helper.pagination import get_paginated_response
from utils.helper.search_and_filter import search, filter_by_staff, filter_by_user, filter_by_superuser
from django.db.models import Q
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.shortcuts import render, redirect
from django.contrib import messages
class UsersView(View):
    def get(self, request):
        # Get all users excluding the deleted ones

        search_query = request.GET.get('search', None)
        filter = request.GET.get('filter', None)

        search_fields = ['username', 'email']

        users = UserModel.objects.all().exclude(is_deleted=True).order_by("username")
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
    
class RolesAndPermissionView(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'user_mgmt/permission.html', {'groups':groups})
    

class AddPermissionView(View):
    def get(self, request):
        content_types = ContentType.objects.all()
        return render(request, 'user_mgmt/add_permission.html', {'content_types': content_types})



    
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Group, Permission, ContentType

# def add_permission_group(request):
#     if request.method == 'POST':
#         group_name = request.POST['group_name']
#         permission_name = request.POST['permission_name']
#         description = request.POST['description']
#         content_type_id = request.POST['content_type']
        
#         # Logic to create Group and Permission
#         group, created = Group.objects.get_or_create(name=group_name)
#         content_type = ContentType.objects.get(id=content_type_id)
#         permission = Permission.objects.create(
#             name=permission_name,
#             description=description,
#             content_type=content_type
#         )
        
#         # Associate the permission with the group
#         group.permissions.add(permission)

#         messages.success(request, 'Group and permission added successfully!')
#         return redirect('desired_redirect_url')  # Redirect as needed

#     content_types = ContentType.objects.all()
#     return render(request, 'add_permission_group.html', {'content_types': content_types})
