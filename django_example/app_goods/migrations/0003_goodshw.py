# Generated by Django 4.2 on 2023-07-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0002_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsHw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('code', models.CharField(max_length=100, verbose_name='артикул')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('file', models.FileField(upload_to='files/homework')),
            ],
        ),
    ]
