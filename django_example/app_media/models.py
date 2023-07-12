from django.db import models
from django.forms import ModelForm


# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class DocumentForm(ModelForm):
    class Meta:
        model = File
        fields = ('description', 'file')
