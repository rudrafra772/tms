from django.contrib import admin
from .models import UserModel

# Register your models here.


admin.site.register(UserModel, list_display = ['id', 'username', 'email', 'is_superuser', 'is_staff', 'is_active', 'is_deleted'])