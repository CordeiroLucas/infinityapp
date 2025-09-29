from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import OperationalError

from django.contrib import messages

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo, {username}')
                return redirect("dashboard")
            else:
                messages.error(request, 'Credenciais inválidas.')
                out = {'popup':{'type':'danger', 'message':'Credenciais Inválidas'}}
                return render(request, 'login/login.html', out)
        except OperationalError:
                messages.error(request, 'Servidor Inativo.')
                out = {'popup':{'type':'danger', 'message':'Server Inativo'}}
                return render(request, 'login/login.html', out)
        
    return render(request, 'login/login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        pass_confirmation = request.POST['password_check']
        
        if password != pass_confirmation:
            out = {'popup':{'type':'danger', 'message':'Insira senhas iguais!'}}
            return render(request, 'login/register.html', out)
        
        out = {'popup':{'type':'success', 'message':'Registrado com sucesso'}}
        return render(request, 'login/register.html', out)
        
        
    return render(request, 'login/register.html')

@login_required
def logout_view(request):
    logout(request)
    out = {'popup':{'type':'success', 'message':'Desconectado com sucesso'}}
    return render(request, 'login/login.html', out)