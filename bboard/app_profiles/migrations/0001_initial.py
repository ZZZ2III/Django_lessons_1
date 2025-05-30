# Generated by Django 4.2 on 2023-06-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='Псевдоним')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
                ('firstname', models.CharField(max_length=20, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=20, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('birthday', models.DateField(verbose_name='День рождения')),
            ],
        ),
    ]
