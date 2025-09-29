from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import OperationalError

from django.contrib.auth.models import User
from .models import Usuario

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("dashboard")
            else:
                out = {'popup':{'type':'danger', 'message':'Credenciais Inválidas'}}
                return render(request, 'login/login.html', out)
        except OperationalError:
                out = {'popup':{'type':'danger', 'message':'Server Inativo'}}
                return render(request, 'login/login.html', out)
        
    return render(request, 'login/login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        email_check = request.POST.get('email_check')
        password = request.POST.get('password')
        pass_check = request.POST.get('password_check')
        
        if password != pass_check:
            out = {'popup':{'type':'danger', 'message':'Insira senhas iguais!'}}
            return render(request, 'login/register.html', out)
        
        if email != email_check:
            out = {'popup':{'type':'danger', 'message':'Insira senhas iguais!'}}
            return render(request, 'login/register.html', out)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        
        if user is not None:
            user.save()
            auth_login(request, user)
            return redirect('dashboard')
        else:
            out = {'popup':{'type':'danger', 'message':'Credenciais Inválidas'}}
            return render(request, 'login/login.html', out)
        
    return render(request, 'login/register.html')

@login_required
def logout_view(request):
    logout(request)
    out = {'popup':{'type':'success', 'message':'Desconectado com sucesso'}}
    return render(request, 'login/login.html', out)