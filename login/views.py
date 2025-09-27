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
                saida = {'notificacao':{'tipo':'danger', 'message':'Credenciais Inválidas'}}
                return render(request, 'login/login.html', saida)
        except OperationalError:
                messages.error(request, 'Servidor Inativo.')
                saida = {'notificacao':{'tipo':'danger', 'message':'Server Inativo'}}
                return render(request, 'login/login.html', saida)
        
    return render(request, 'login/login.html')

@login_required
def logout_view(request):
    logout(request)
    saida = {'notificacao':{'tipo':'success', 'message':'Desconectado com sucesso'}}
    return render(request, 'login/login.html', saida)