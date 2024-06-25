from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages

# Create your views here.

class LoginView(View):
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

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class Home(View):
    def get(self, request):
        return render(request, 'home/index.html')