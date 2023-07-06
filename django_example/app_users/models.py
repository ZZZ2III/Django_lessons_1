from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    date_of_birth = models.DateField()


class HomeworkModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True, default='0')
    date_of_birth = models.DateField(blank=True, default=0)
    credit_card = models.IntegerField(blank=True, default=0)
    phone_number = models.IntegerField(blank=True, default=0)
