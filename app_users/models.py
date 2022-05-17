from cgitb import text
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AdvUser(AbstractUser):
    date_of_birth = models.DateField(null=True, verbose_name='Дата рождения', help_text='Дата рождения через "/"')
    avatar = models.ImageField(upload_to='user/', null=True, blank=True)
    info = models.TextField(null=True)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'