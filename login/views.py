from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Bem-vindo, {username}')
            return redirect("dashboard")
        else:
            messages.error(request, 'Credenciais inválidas.')
            return redirect('login')
        
    return render(request, 'login/login.html')