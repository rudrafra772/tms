from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages
from .models import UserModel
from apps.user_mgmt.models import Attendance
from datetime import datetime

# Create your views here.

class LoginView(View): # pragma: no cover
    def get(self, request):
        if not self.request.user.is_authenticated:
            form = LoginForm()
            return render(request, 'home/index.html', {'form': form})  # Render the login form template
        else:
            return redirect('home')

    def post(self, request): 
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials")
                return redirect('login')
        else:
            messages.error(request, "Error")
            return redirect('login')

class LogoutView(View): # pragma: no cover
    def get(self, request):
        logout(request)
        return redirect('login')

class Home(View): # pragma: no cover
    def get(self, request):
        total_user = UserModel.objects.all().count()
        try:
            attendance = Attendance.objects.get(user = request.user, in_time__date = datetime.now().date())
        except Attendance.DoesNotExist:
            attendance = None
        return render(request, 'home/index.html', {"total_user":total_user, "attendance":attendance})