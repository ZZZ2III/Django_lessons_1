from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    firstname = forms.CharField()
    second_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birthday = forms.DateField()


class AdvertisementForm(forms.Form):
    title = forms.CharField()
    description = forms.Textarea()
    price = forms.IntegerField()