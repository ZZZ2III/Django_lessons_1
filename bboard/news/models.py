from django.db import models

# Create your models here.

class NewsModel(models.Model):
    title = models.CharField(max_length=20,verbose_name='Заголовок')
    content = models.TextField(verbose_name="Содержимое новости")
    date_created = models.DateField(verbose_name="Дата создания")
    date_redacted = models.DateField(verbose_name='Дата редактирования')
    flag_active = models.BooleanField(verbose_name='Фейк?')

    class Meta:
        db_table = 'newsmodel'
        ordering = ['date_created']


    def __str__(self):
        return self.title

class CommentsModel(models.Model):
    name = models.CharField(max_length=20,verbose_name='Автор')
    text = models.TextField(verbose_name='Содержимое')
    news = models.ForeignKey('NewsModel', on_delete=models.CASCADE,related_name='comms')
    def __str__(self):
        return self.name
