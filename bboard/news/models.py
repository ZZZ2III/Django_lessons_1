from django.db import models

# Create your models here.

class NewsModel(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateField()
    date_redacted = models.DateField()
    flag_active = models.BooleanField()

    class Meta:
        db_table = 'newsmodel'
        ordering = ['date_created']


    def __str__(self):
        return self.title

class CommentsModel(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()
    news = models.ForeignKey('NewsModel', on_delete=models.CASCADE)
