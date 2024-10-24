from .views import UsersView, RolesAndPermissionView, AddPermissionView
from django.urls import path


urlpatterns = [
    path('users/', UsersView.as_view(), name="users"),
    path('roles_and_permissions/', RolesAndPermissionView.as_view(), name="r_and_p"),
    path('add_permission/', AddPermissionView.as_view(), name="add_permission"),
]
