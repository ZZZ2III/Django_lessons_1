from django.db import models


# Create your models here.
class Item(models.Model):
    code = models.CharField(max_length=100, verbose_name='артикул товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')


class Goods(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    code = models.CharField(max_length=100, verbose_name='артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')

