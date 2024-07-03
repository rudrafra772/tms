from django.contrib import admin
from .models import Project, Board, Column, Task
# Register your models here.



#admin.site.register(Project)
admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Task)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at', 'is_deleted']
    readonly_fields = ['created_by', 'updated_by', 'is_deleted']