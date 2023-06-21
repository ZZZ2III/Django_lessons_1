from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='Псевдоним')
    password = models.CharField(max_length=20, verbose_name='Пароль')
    firstname = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Отчество')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    birthday = models.DateField(verbose_name='День рождения')


class Advertisement(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.IntegerField()
