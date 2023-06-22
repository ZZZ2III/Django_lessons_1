from django import forms
from news.models import NewsModel, CommentsModel

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = '__all__'


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = '__all__'
