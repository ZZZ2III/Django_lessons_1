from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=70)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.id}. {self.name}, {self.country}, {self.city}'


class Authors(models.Model):
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(blank=True)
    biography = models.TextField(blank=True)
    second_name = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=16, blank=True)
    personal_page = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name}'


class Book(models.Model):
    STATUS_CHOISES = [
        ['d', 'Draft'],
        ['r', 'Review'],
        ['p', 'Published']

    ]

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Authors)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # , related_name='publisher')
    publication_date = models.DateField()
    status = models.CharField(max_length=1,choices=STATUS_CHOISES,default='d')
