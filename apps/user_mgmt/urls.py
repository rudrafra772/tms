from .views import UsersView
from django.urls import path


urlpatterns = [
    path('users/', UsersView.as_view(), name="users"),
]
