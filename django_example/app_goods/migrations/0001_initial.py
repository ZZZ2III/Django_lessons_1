# Generated by Django 4.2 on 2023-07-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='артикул товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
            ],
        ),
    ]
