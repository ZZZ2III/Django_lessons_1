from django.db import models


# Create your models here.
class Vacancy(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='Заголовок')
    publisher = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        permissions = (
            ('can_publish','Может опубликовать'),
        )

    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length=30,verbose_name='Заголовок')
    date_created = models.DateTimeField(verbose_name='Дата создания',auto_now_add=True)
    date_published = models.DateTimeField(verbose_name='Дата публикации')
    description = models.TextField()

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюмы'

    def __str__(self):
        return self.title