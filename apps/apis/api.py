from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from .utils import response


class HealthCheck(viewsets.GenericViewSet):
    
    permission_classes = [AllowAny]

    @action(methods=['get'], detail=False)
    def health_check(self, request):
        return response()