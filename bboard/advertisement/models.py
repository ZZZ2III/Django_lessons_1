from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=1500,verbose_name='Заголовок')
    name = models.CharField(max_length=15,verbose_name='Имя продавца')
    description = models.TextField(verbose_name='Описание товара')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    veiws_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisement',verbose_name='Статус')

    class Meta:
        db_table = 'advertisement'
        ordering = ['title']

    def __str__(self):
        return self.title

class My_testing_model(models.Model):
    title = models.CharField(max_length=1500)
    name = models.CharField(max_length=15)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    veiws_count = models.IntegerField(verbose_name='количество просмотров', default=0)

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Regions(models.Model):
    #name = models.CharField(max_length=15)
    name = models.ManyToManyField(Advertisement)

class Advertisement_type1(models.Model):
    name = models.CharField(max_length=20)
    conn = models.OneToOneField(Advertisement,on_delete=models.CASCADE)



