from django.urls import path
from .views import LoggerView


urlpatterns = [
    path('logs/', LoggerView.as_view(), name="db_logger")
]
