from rest_framework.routers import DefaultRouter
from .api import HealthCheck
from django.urls import path, include

router = DefaultRouter()
router.register('', HealthCheck, basename="health_check")

urlpatterns = [
    path('', include(router.urls))
]