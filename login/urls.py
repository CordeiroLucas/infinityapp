from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name='inicio'),
    path("login/", views.login_view, name='login'),
]
