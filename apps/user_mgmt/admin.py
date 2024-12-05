from django.contrib import admin
from .models import Attendance
# Register your models here.


admin.site.register(Attendance, list_display = ['id', 'is_deleted'], readonly_fields = ['created_by', 'updated_by', 'is_deleted'])