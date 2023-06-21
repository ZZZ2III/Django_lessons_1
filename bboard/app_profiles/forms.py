from django import forms
import datetime
from django.core.exceptions import ValidationError

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    firstname = forms.CharField()
    second_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birthday = forms.DateField()

    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        #print(data,type(data))
        today = datetime.date.today()
        year_delta = (today-data) / 365
        if year_delta < 18 or year_delta<0:
            raise ValidationError('Регистрироваться на сайте могут только лица старше 18 лет')
        return data

    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        first_name = cleaned_data.get['firstname']
        last_name = cleaned_data.get['last_name']
        if first_name == 'Иван' and last_name == 'Иванов':
            msg = 'Запрещено регистрироваться Иванам Ивановым'
            self.add_error('firstname',msg)
            self.add_error('last_name',msg)
            #raise ValidationError()


class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=20,min_length=3)
    description = forms.CharField(max_length=200,min_length=10)
    price = forms.IntegerField(min_value=10,max_value=100000)