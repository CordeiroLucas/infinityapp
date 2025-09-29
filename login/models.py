from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user_id : User = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    email: str = models.CharField(unique=True, blank=False, max_length=100)