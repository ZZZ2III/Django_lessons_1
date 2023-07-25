from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from app_users.models import TestUsers


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='name')
    last_name = forms.CharField(max_length=30, required=False, help_text='second name')
    date_of_birth = forms.DateField(required=True, help_text='дата рождения')
    city = forms.CharField(max_length=30, required=False, help_text='Город')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='name')
    last_name = forms.CharField(max_length=30, required=False, help_text='second name')
    date_of_birth = forms.DateField(required=True, help_text='дата рождения')
    city = forms.CharField(max_length=30, required=False, help_text='Город')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


class UserExtendedHomework(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='username')
    first_name = forms.CharField(max_length=30, required=False, help_text='name')
    last_name = forms.CharField(max_length=30, required=False, help_text='second name')
    email = forms.EmailField(required=False, help_text='enter your email here')
    date_of_birth = forms.DateField(required=True, help_text='дата рождения')
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    credit_card = forms.IntegerField(required=False, help_text='Введите номер скидочной карты')
    phone_number = forms.IntegerField(required=False, help_text='Введите номер телефона')

    # password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()
