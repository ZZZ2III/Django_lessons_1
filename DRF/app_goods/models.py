from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    decription = models.TextField(blank=True, verbose_name='описание')
    weight = models.FloatField(verbose_name='вес')
