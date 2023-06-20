from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Заголовок')
    name = models.CharField(max_length=15, verbose_name='Имя исполнителя')
    description = models.TextField(verbose_name='Описание товара')
    created_at = models.DateTimeField(verbose_name='Дата создания публикации', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True,verbose_name='Дата окончания публикации')
    price = models.FloatField(verbose_name='Цена', default=0)
    veiws_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisement', verbose_name='Статус')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор', default=None, null=True,related_name='author')
    rubrik = models.ForeignKey('Rubrik', on_delete=models.CASCADE, verbose_name='Рубрика', default=None, null=True,related_name='rubrik')
    type = models.OneToOneField('Advertisement_type1',on_delete=models.CASCADE,verbose_name='Тип',default=None,null = True,related_name='type')
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
    # name = models.CharField(max_length=15)
    name = models.ManyToManyField(Advertisement)


class Advertisement_type1(models.Model):
    name = models.CharField(max_length=20)
    #conn = models.OneToOneField(Advertisement, on_delete=models.CASCADE, related_name='advertisement')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_nubmer = models.IntegerField(max_length=11)
    #con = models.One
    def __str__(self):
        return self.name

class Rubrik(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
