from django.urls import path
from .views import Home, LoginView, LogoutView

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    path('', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]
