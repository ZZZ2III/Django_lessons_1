from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=70)
    is_active = models.BooleanField()

    # def __str__(self):
    #     return self.name